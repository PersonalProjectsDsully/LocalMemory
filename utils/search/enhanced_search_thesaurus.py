"""
Enhanced Intelligent Search Engine with Moby Thesaurus Integration

This module enhances the existing intelligent search functionality
by adding synonym expansion capabilities using the Moby Thesaurus.
"""

from typing import List, Dict, Optional, Tuple
import logging
from .moby_thesaurus import RobustMobyThesaurus, CachedMobyThesaurus
from .intelligent_search_enhanced import EnhancedIntelligentSearchEngine as BaseIntelligentSearchEngine

logger = logging.getLogger(__name__)


class EnhancedIntelligentSearchEngine:
    """Enhanced search engine with Moby Thesaurus integration"""
    
    def __init__(self, base_engine: Optional[BaseIntelligentSearchEngine] = None, 
                 use_cache: bool = True, cache_size: int = 10000):
        """
        Initialize enhanced search engine
        
        Args:
            base_engine: Existing search engine instance
            use_cache: Whether to use cached thesaurus lookups
            cache_size: Size of the synonym cache
        """
        self.base_engine = base_engine or BaseIntelligentSearchEngine()
        
        if use_cache:
            self.thesaurus = CachedMobyThesaurus(cache_size=cache_size)
        else:
            self.thesaurus = RobustMobyThesaurus(
                fallback_file="data/thesaurus/emergency_fallback.json"
            )
        
        # Initialize thesaurus
        try:
            if hasattr(self.thesaurus, 'initialize'):
                self.thesaurus.initialize()
            elif hasattr(self.thesaurus, 'thesaurus') and hasattr(self.thesaurus.thesaurus, 'initialize'):
                self.thesaurus.thesaurus.initialize()
            logger.info("Thesaurus initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize thesaurus: {e}")
            # Continue with limited functionality
        
        # Preload common search terms if using cache
        if use_cache and hasattr(self.thesaurus, 'preload_common_words'):
            common_terms = [
                'search', 'find', 'create', 'delete', 'update', 'modify',
                'code', 'debug', 'error', 'function', 'variable', 'class',
                'method', 'algorithm', 'data', 'structure', 'system', 'process',
                'file', 'document', 'text', 'image', 'video', 'audio',
                'user', 'admin', 'setting', 'configuration', 'option'
            ]
            self.thesaurus.preload_common_words(common_terms)
    
    def search_with_expansion(self, query: str, use_synonyms: bool = True, 
                            expansion_weight: float = 0.7,
                            max_synonyms_per_word: int = 3) -> List[Dict]:
        """
        Search with optional synonym expansion
        
        Args:
            query: Search query string
            use_synonyms: Whether to use synonym expansion
            expansion_weight: Weight factor for expanded results (0-1)
            max_synonyms_per_word: Maximum synonyms to use per word
        
        Returns:
            List of search results with scores
        """
        
        # Get base results
        base_results = self.base_engine.search(query)
        
        if not use_synonyms:
            return base_results
        
        # Get query expansions
        if hasattr(self.thesaurus, 'thesaurus') and hasattr(self.thesaurus.thesaurus, 'expand_query'):
            expansions = self.thesaurus.thesaurus.expand_query(
                query, 
                max_per_word=max_synonyms_per_word
            )
        else:
            expansions = self._get_query_expansions(query, max_synonyms_per_word)
        
        if not expansions:
            return base_results
        
        # Log expansions for debugging
        logger.info(f"Query expansions: {expansions}")
        
        # Create expanded queries and search
        expanded_results = []
        
        for original_word, synonyms in expansions.items():
            for synonym in synonyms:
                # Create modified query
                expanded_query = query.replace(original_word, synonym)
                
                # Skip if expanded query is same as original
                if expanded_query == query:
                    continue
                
                # Search with expanded query
                syn_results = self.base_engine.search(expanded_query)
                
                # Adjust scores based on expansion
                for result in syn_results:
                    result['score'] = result.get('score', 1.0) * expansion_weight
                    result['expansion_source'] = f"{original_word} → {synonym}"
                    result['expanded_query'] = expanded_query
                
                expanded_results.extend(syn_results)
        
        # Merge and deduplicate results
        merged_results = self._merge_results(base_results, expanded_results)
        
        return merged_results
    
    def _get_query_expansions(self, query: str, max_per_word: int) -> Dict[str, List[str]]:
        """Get expansions for query words"""
        words = query.lower().split()
        expansions = {}
        
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        
        for word in words:
            if word in stop_words:
                continue
            
            if hasattr(self.thesaurus, 'get_synonyms_cached'):
                synonyms = self.thesaurus.get_synonyms_cached(word, max_per_word)
            else:
                synonyms = self.thesaurus.get_synonyms(word, max_per_word)
            
            if synonyms:
                expansions[word] = synonyms
        
        return expansions
    
    def _merge_results(self, base_results: List[Dict], 
                      expanded_results: List[Dict]) -> List[Dict]:
        """Merge base and expanded results, removing duplicates"""
        
        # Create a map of document IDs to results
        result_map = {}
        
        # Add base results first (higher priority)
        for result in base_results:
            doc_id = result.get('id', result.get('path', result.get('title', '')))
            if doc_id:
                result_map[doc_id] = result
                result['is_base_result'] = True
        
        # Add expanded results, updating scores if already present
        for result in expanded_results:
            doc_id = result.get('id', result.get('path', result.get('title', '')))
            
            if not doc_id:
                continue
            
            if doc_id in result_map:
                # Combine scores using maximum
                existing_score = result_map[doc_id].get('score', 0)
                new_score = result.get('score', 0)
                result_map[doc_id]['score'] = max(existing_score, new_score)
                
                # Track expansion sources
                if 'expansion_sources' not in result_map[doc_id]:
                    result_map[doc_id]['expansion_sources'] = []
                
                if 'expansion_source' in result:
                    result_map[doc_id]['expansion_sources'].append(
                        result['expansion_source']
                    )
            else:
                result['is_expanded_result'] = True
                result_map[doc_id] = result
        
        # Sort by score
        sorted_results = sorted(
            result_map.values(),
            key=lambda x: x.get('score', 0),
            reverse=True
        )
        
        return sorted_results
    
    def get_synonym_suggestions(self, word: str, max_suggestions: int = 5) -> List[str]:
        """
        Get synonym suggestions for a single word
        
        Args:
            word: Word to get synonyms for
            max_suggestions: Maximum number of suggestions
        
        Returns:
            List of synonym suggestions
        """
        if hasattr(self.thesaurus, 'get_synonyms_cached'):
            return self.thesaurus.get_synonyms_cached(word, max_suggestions)
        else:
            return self.thesaurus.get_synonyms(word, max_suggestions)
    
    def explain_expansions(self, query: str) -> Dict[str, any]:
        """
        Explain how a query would be expanded
        
        Args:
            query: Query to explain
        
        Returns:
            Dictionary with expansion details
        """
        expansions = self._get_query_expansions(query, max_per_word=5)
        
        explanation = {
            'original_query': query,
            'words_analyzed': query.lower().split(),
            'expansions': expansions,
            'expanded_queries': []
        }
        
        # Generate all possible expanded queries
        for word, synonyms in expansions.items():
            for synonym in synonyms:
                expanded_query = query.replace(word, synonym)
                if expanded_query != query:
                    explanation['expanded_queries'].append({
                        'query': expanded_query,
                        'substitution': f"{word} → {synonym}"
                    })
        
        return explanation
    
    def health_check(self) -> Dict[str, any]:
        """Check health of the enhanced search system"""
        health = {
            'base_engine_healthy': hasattr(self.base_engine, 'search'),
            'thesaurus_health': {}
        }
        
        # Check thesaurus health
        if hasattr(self.thesaurus, 'health_check'):
            health['thesaurus_health'] = self.thesaurus.health_check()
        elif hasattr(self.thesaurus, 'thesaurus') and hasattr(self.thesaurus.thesaurus, 'health_check'):
            health['thesaurus_health'] = self.thesaurus.thesaurus.health_check()
        else:
            health['thesaurus_health'] = {
                'initialized': hasattr(self.thesaurus, 'initialized') and self.thesaurus.initialized,
                'type': type(self.thesaurus).__name__
            }
        
        return health
    
    def configure_qa_system(self, qa_config: str):
        """Configure QA system - delegate to base engine if available"""
        if hasattr(self.base_engine, 'configure_qa_system'):
            return self.base_engine.configure_qa_system(qa_config)
        else:
            # Store config for future use
            self.qa_config = qa_config
            logger.info(f"QA config set to: {qa_config} (base engine doesn't support QA)")
    
    def search_content(self, query: str):
        """Basic search method - delegate to base engine"""
        if hasattr(self.base_engine, 'search_content'):
            return self.base_engine.search_content(query)
        elif hasattr(self.base_engine, 'search'):
            return self.base_engine.search(query)
        else:
            logger.warning("Base engine has no search method available")
            return []
    
    def parse_query_intent(self, query: str):
        """Parse query intent - delegate to base engine"""
        if hasattr(self.base_engine, 'parse_query_intent'):
            return self.base_engine.parse_query_intent(query)
        else:
            # Return basic intent structure
            return {
                'intent_type': 'information_seeking',
                'key_entities': query.split(),
                'expected_answer_type': 'synthesized_answer',
                'expanded_query': {'expanded_tokens': []}
            }
    
    def synthesize_answer_with_qa(self, query, results, **kwargs):
        """Synthesize answer - delegate to base engine"""
        if hasattr(self.base_engine, 'synthesize_answer_with_qa'):
            return self.base_engine.synthesize_answer_with_qa(query, results, **kwargs)
        else:
            # Return basic answer structure
            return {
                'answer': f"Found {len(results)} results for: {query}",
                'confidence': 0.5,
                'clusters_found': 1
            }
    
    def explain_expansions(self, query: str) -> Dict[str, any]:
        """
        Explain how a query would be expanded with synonyms
        
        Args:
            query: Query to explain
        
        Returns:
            Dictionary with expansion details
        """
        try:
            # Get expansions from thesaurus
            if hasattr(self.thesaurus, 'expand_query'):
                expansions = self.thesaurus.expand_query(query, max_per_word=5)
            else:
                expansions = self._get_query_expansions(query, max_per_word=5)
            
            explanation = {
                'original_query': query,
                'words_analyzed': query.lower().split(),
                'expansions': expansions,
                'expanded_queries': []
            }
            
            # Generate sample expanded queries
            for word, synonyms in expansions.items():
                for synonym in synonyms[:3]:  # Limit to top 3 for readability
                    expanded_query = query.replace(word, synonym)
                    if expanded_query != query:
                        explanation['expanded_queries'].append({
                            'query': expanded_query,
                            'substitution': f"{word} → {synonym}"
                        })
            
            return explanation
        
        except Exception as e:
            logger.error(f"Error explaining expansions: {e}")
            return {
                'original_query': query,
                'words_analyzed': query.lower().split(),
                'expansions': {},
                'expanded_queries': [],
                'error': str(e)
            }


# Convenience function for quick setup
def create_enhanced_search_engine(use_cache: bool = True, 
                                cache_size: int = 10000) -> EnhancedIntelligentSearchEngine:
    """
    Create an enhanced search engine with thesaurus support
    
    Args:
        use_cache: Whether to use cached thesaurus lookups
        cache_size: Size of the synonym cache
    
    Returns:
        Configured EnhancedIntelligentSearchEngine instance
    """
    return EnhancedIntelligentSearchEngine(
        use_cache=use_cache,
        cache_size=cache_size
    )