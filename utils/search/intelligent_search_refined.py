"""
Refined Intelligent Search Engine
Addresses scoring heuristics and query intent handling issues
"""

import json
import re
import math
from typing import Dict, List, Tuple, Any, Optional, Set
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False
    class MockStreamlit:
        class session_state:
            enhanced_search_engine = None
        def spinner(self, text): 
            from contextlib import contextmanager
            @contextmanager
            def mock_spinner():
                yield None
            return mock_spinner()
        def success(self, text): pass
        def info(self, text): pass
    st = MockStreamlit()

from .llm_utils import _call_llm_api
from .intelligent_search_enhanced import EnhancedIntelligentSearchEngine
from .search_config import (
    get_scoring_config, get_intent_patterns, get_recency_config,
    get_length_config, get_clustering_config, get_llm_intent_config
)


class RefinedIntelligentSearchEngine(EnhancedIntelligentSearchEngine):
    """
    Refined search engine with improved scoring heuristics and query intent handling
    """
    
    def __init__(self, knowledgebase_path: str = "knowledgebase"):
        super().__init__(knowledgebase_path)
        
        # Load configuration from centralized config
        self.scoring_config = get_scoring_config()
        self.intent_patterns = get_intent_patterns()
        self.recency_config = get_recency_config()
        self.length_config = get_length_config()
        self.clustering_config = get_clustering_config()
        self.llm_intent_config = get_llm_intent_config()
    
    def analyze_query_intent(self, query: str) -> Dict[str, Any]:
        """
        Enhanced query intent analysis with better fallback and context awareness
        """
        expanded_query = self.expand_query(query)
        
        # First try LLM analysis with improved prompt
        prompt = f"""Analyze this user query for search intent:

USER QUERY: "{query}"
EXPANDED TOKENS: {expanded_query['expanded_tokens']}

Determine the PRIMARY intent and provide confidence:

1. INTENT TYPE (choose ONE primary intent):
   - information_seeking: General knowledge questions ("What is...", "How does X work")
   - instruction_seeking: Step-by-step guidance ("How to...", "Steps for...")
   - comparison_seeking: Comparing options ("X vs Y", "Which is better")
   - troubleshooting: Problem solving ("Why isn't...", "Fix...", "Error...")
   - discovery: Finding/listing content ("Find all...", "Show me...")

2. CONFIDENCE: How certain are you about this classification? (0.0-1.0)

3. RECENCY_IMPORTANT: Does this query need recent/updated information? (true/false)
   - Consider: troubleshooting, version-specific questions, "latest" info
   - NOT for: general concepts, how-to guides, basic explanations

4. KEY_ENTITIES: Specific tools, technologies, names, etc.
5. KEY_CONCEPTS: Abstract topics, methodologies, skills

Respond in valid JSON format with these exact field names."""

        # Try LLM analysis first
        llm_result = self._try_llm_intent_analysis(prompt)
        if llm_result:
            # Validate and enhance LLM result
            return self._validate_and_enhance_intent(llm_result, query, expanded_query)
        
        # Enhanced fallback with pattern matching
        return self._fallback_intent_analysis(query, expanded_query)
    
    def _try_llm_intent_analysis(self, prompt: str) -> Optional[Dict]:
        """Try LLM analysis with better error handling"""
        try:
            response = _call_llm_api(prompt, "query intent analysis")
            if not response:
                return None
                
            # Clean JSON from response
            json_text = response
            if '```json' in response:
                json_text = response.split('```json')[1].split('```')[0]
            elif '```' in response:
                json_text = response.split('```')[1].split('```')[0]
            
            # Parse and validate structure
            intent_data = json.loads(json_text.strip())
            
            # Ensure required fields exist
            required_fields = ['intent_type', 'confidence']
            if all(field in intent_data for field in required_fields):
                return intent_data
            else:
                print(f"LLM intent analysis missing required fields: {required_fields}")
                return None
                
        except json.JSONDecodeError as e:
            print(f"JSON parsing error in intent analysis: {e}")
            return None
        except Exception as e:
            print(f"LLM intent analysis error: {e}")
            return None
    
    def _validate_and_enhance_intent(self, llm_result: Dict, query: str, expanded_query: Dict) -> Dict:
        """Validate LLM result and enhance with fallback logic"""
        
        # Validate intent type
        valid_intents = ['information_seeking', 'instruction_seeking', 'comparison_seeking', 
                        'troubleshooting', 'discovery']
        
        if llm_result.get('intent_type') not in valid_intents:
            print(f"Invalid intent type from LLM: {llm_result.get('intent_type')}, falling back")
            return self._fallback_intent_analysis(query, expanded_query)
        
        # Validate confidence
        confidence = llm_result.get('confidence', 0.5)
        if not isinstance(confidence, (int, float)) or not (0 <= confidence <= 1):
            confidence = 0.5
        
        # Double-check recency importance with pattern matching
        recency_important = llm_result.get('recency_important', False)
        query_lower = query.lower()
        
        # Override recency for certain patterns
        if any(pattern in query_lower for pattern in ['latest', 'recent', 'new', 'updated', '2024', '2025']):
            recency_important = True
        elif any(pattern in query_lower for pattern in ['what is', 'how does', 'explain', 'concept']):
            recency_important = False
        
        # Build validated result
        result = {
            'intent_type': llm_result['intent_type'],
            'confidence': confidence,
            'recency_important': recency_important,
            'key_entities': llm_result.get('key_entities', []),
            'key_concepts': llm_result.get('key_concepts', []),
            'context_filters': llm_result.get('context_filters', {}),
            'expected_answer_type': self._get_expected_answer_type(llm_result['intent_type']),
            'expanded_query': expanded_query
        }
        
        # Add comparison items if detected
        if llm_result['intent_type'] == 'comparison_seeking':
            comparison_items = self._extract_comparison_items(query, expanded_query)
            if comparison_items:
                result['comparison_items'] = comparison_items
        
        return result
    
    def _fallback_intent_analysis(self, query: str, expanded_query: Dict) -> Dict:
        """Enhanced fallback intent analysis using pattern matching"""
        query_lower = query.lower()
        
        # Pattern-based intent detection with confidence scoring
        intent_scores = {}
        
        for intent_type, patterns in self.intent_patterns.items():
            score = 0
            for pattern in patterns:
                if re.search(pattern, query_lower, re.IGNORECASE):
                    score += 1
            
            if score > 0:
                intent_scores[intent_type] = score
        
        # Determine primary intent
        if intent_scores:
            primary_intent = max(intent_scores, key=intent_scores.get)
            max_score = intent_scores[primary_intent]
            confidence = min(0.8, 0.4 + (max_score * 0.2))  # Cap at 0.8 for fallback
        else:
            primary_intent = 'information_seeking'
            confidence = 0.3  # Low confidence for default
        
        # Determine recency importance
        recency_important = False
        if primary_intent in ['troubleshooting', 'discovery']:
            recency_important = True
        elif any(re.search(pattern, query_lower) for pattern in self.intent_patterns.get('version_specific', [])):
            recency_important = True
        
        return {
            'intent_type': primary_intent,
            'confidence': confidence,
            'recency_important': recency_important,
            'key_entities': [],
            'key_concepts': [],
            'context_filters': {},
            'expected_answer_type': self._get_expected_answer_type(primary_intent),
            'expanded_query': expanded_query,
            'fallback_used': True
        }
    
    def calculate_search_score(self, query_data: Dict, content_data: Dict) -> float:
        """
        Refined scoring with reduced double-counting and better balance
        """
        score = 0.0
        
        # Get basic content
        title_lower = content_data.get('title', '').lower()
        body_lower = content_data.get('body', '').lower()
        
        # Parse structure
        if 'structure' not in content_data:
            content_data['structure'] = self._parse_markdown_structure(content_data.get('body', ''))
        structure = content_data.get('structure', {})
        
        # Track which terms have been matched to avoid double-counting
        matched_terms = set()
        
        # 1. PHRASE MATCHING (highest priority)
        phrase_score = 0.0
        
        # Trigrams (highest value)
        for trigram in query_data.get('trigrams', []):
            if trigram in title_lower:
                phrase_score += self.scoring_config['trigram_title_bonus']
                # Mark component bigrams and terms as matched
                words = trigram.split()
                for i in range(len(words) - 1):
                    matched_terms.add(f"{words[i]} {words[i+1]}")
                matched_terms.update(words)
            elif trigram in body_lower:
                phrase_score += self.scoring_config['trigram_body_bonus']
                # Mark component terms as partially matched
                words = trigram.split()
                for word in words:
                    matched_terms.add(word)
        
        # Bigrams (only if not already counted in trigrams)
        for bigram in query_data.get('bigrams', []):
            if bigram not in matched_terms:
                if bigram in title_lower:
                    phrase_score += self.SCORING_CONFIG['bigram_title_bonus']
                    matched_terms.add(bigram)
                    matched_terms.update(bigram.split())
                elif bigram in body_lower:
                    phrase_score += self.SCORING_CONFIG['bigram_body_bonus']
                    matched_terms.update(bigram.split())
        
        score += phrase_score
        
        # 2. INDIVIDUAL TERM MATCHING (only for unmatched terms)
        all_terms = query_data.get('all_search_terms', [])
        unmatched_terms = [term for term in all_terms if term not in matched_terms]
        
        if unmatched_terms:
            # Title matches
            title_matches = sum(1 for term in unmatched_terms if term in title_lower)
            title_fraction = title_matches / len(all_terms) if all_terms else 0
            score += title_fraction * self.SCORING_CONFIG['title_fraction_multiplier']
            
            # Body matches (with cap)
            body_matches = sum(1 for term in unmatched_terms if term in body_lower)
            body_score = min(
                body_matches * self.SCORING_CONFIG['body_term_base'], 
                self.SCORING_CONFIG['body_term_max']
            )
            score += body_score
        
        # 3. STRUCTURE-BASED SCORING (with caps to prevent dominance)
        structure_score = 0.0
        
        if all_terms:
            # Summary matches (capped)
            if structure.get('summary'):
                summary_lower = structure['summary'].lower()
                summary_matches = sum(1 for term in all_terms if term in summary_lower)
                if summary_matches:
                    summary_contribution = min(
                        (summary_matches / len(all_terms)) * self.SCORING_CONFIG['summary_multiplier'],
                        self.SCORING_CONFIG['summary_max_contribution']
                    )
                    structure_score += summary_contribution
            
            # Header matches (capped and level-weighted)
            header_contribution = 0.0
            for header in structure.get('headers', []):
                header_lower = header['text'].lower()
                header_matches = sum(1 for term in all_terms if term in header_lower)
                if header_matches:
                    level_weight = self.SCORING_CONFIG['header_base_weight'] / header['level']
                    header_contribution += (header_matches / len(all_terms)) * level_weight
            
            structure_score += min(header_contribution, self.SCORING_CONFIG['header_max_contribution'])
            
            # Key points matches (capped)
            key_points_contribution = 0.0
            for key_point in structure.get('key_points', []):
                key_point_lower = key_point.lower()
                kp_matches = sum(1 for term in all_terms if term in key_point_lower)
                if kp_matches:
                    key_points_contribution += (kp_matches / len(all_terms)) * self.SCORING_CONFIG['key_points_multiplier']
            
            structure_score += min(key_points_contribution, self.SCORING_CONFIG['key_points_max_contribution'])
        
        score += structure_score
        
        # 4. PROXIMITY SCORING (capped)
        proximity_score = self._calculate_proximity_score(query_data.get('tokens', []), body_lower)
        score += min(proximity_score, self.SCORING_CONFIG['proximity_max_contribution'])
        
        # 5. ENTITY/CONCEPT BONUSES (reduced)
        entities = set(content_data.get('frontmatter', {}).get('entities', []))
        concepts = set(content_data.get('frontmatter', {}).get('concepts', []))
        
        for term in all_terms:
            if any(term in entity.lower() for entity in entities):
                score += self.SCORING_CONFIG['entity_bonus']
            elif any(term in concept.lower() for concept in concepts):
                score += self.SCORING_CONFIG['concept_bonus']
        
        return score
    
    def rank_and_cluster_results(self, search_results: List[Dict[str, Any]], 
                                query_intent: Dict[str, Any], max_results: int = 20) -> List[Dict[str, Any]]:
        """
        Enhanced ranking with smarter recency bias and better intent handling
        """
        if not search_results:
            return []
        
        # Sort by search score first
        search_results.sort(key=lambda x: x.get('score', 0), reverse=True)
        search_results = search_results[:max_results]
        
        # Cluster similar results
        clusters = []
        clustered_files = set()
        
        for result in search_results:
            if result['file_key'] in clustered_files:
                continue
            
            cluster = {
                'primary': result,
                'members': [result],
                'cluster_score': result['score']
            }
            clustered_files.add(result['file_key'])
            
            # Find similar results for clustering
            for other in search_results:
                if other['file_key'] in clustered_files:
                    continue
                
                similarity = self._calculate_content_similarity(result, other)
                if similarity > 0.5:
                    cluster['members'].append(other)
                    cluster['cluster_score'] += other['score'] * 0.5
                    clustered_files.add(other['file_key'])
            
            clusters.append(cluster)
        
        # Apply intent-aware ranking adjustments
        now = datetime.now()
        for cluster in clusters:
            primary = cluster['primary']
            final_score = cluster['cluster_score']
            
            # Smart recency bias based on intent and query patterns
            if self._should_apply_recency_bias(query_intent):
                recency_factor = self._calculate_recency_factor(primary, now)
                final_score *= recency_factor
            
            # Content length preference based on intent
            if query_intent.get('intent_type') in ['information_seeking', 'instruction_seeking']:
                length_factor = self._calculate_length_factor(primary)
                final_score *= length_factor
            
            # Diversity penalty (reduce clustering dominance)
            category = primary['content']['category']
            category_count = sum(1 for c in clusters[:clusters.index(cluster)] 
                               if c['primary']['content']['category'] == category)
            diversity_penalty = 1.0 / (1.0 + category_count * 0.15)  # Reduced penalty
            final_score *= diversity_penalty
            
            cluster['final_score'] = final_score
        
        # Sort by final score
        clusters.sort(key=lambda x: x['final_score'], reverse=True)
        
        # Flatten results
        final_results = []
        for cluster in clusters:
            for i, member in enumerate(cluster['members']):
                result = member.copy()
                result['cluster_id'] = clusters.index(cluster)
                result['is_cluster_primary'] = (i == 0)
                result['cluster_size'] = len(cluster['members'])
                result['final_score'] = cluster['final_score'] if i == 0 else cluster['final_score'] * 0.8
                final_results.append(result)
        
        return final_results
    
    def _should_apply_recency_bias(self, query_intent: Dict) -> bool:
        """Determine if recency bias should be applied based on intent analysis"""
        
        # Use explicit recency_important flag if available
        if 'recency_important' in query_intent:
            return query_intent['recency_important']
        
        # Fallback to intent type
        intent_type = query_intent.get('intent_type', '')
        
        # Apply recency for troubleshooting and discovery
        if intent_type in ['troubleshooting', 'discovery']:
            return True
        
        # Check for version-specific terms
        if query_intent.get('key_entities'):
            for entity in query_intent['key_entities']:
                if re.search(r'\b20\d{2}\b|\bv\d+\.\d+\b|\blatest\b|\brecent\b', entity.lower()):
                    return True
        
        return False
    
    def _calculate_recency_factor(self, content: Dict, now: datetime) -> float:
        """Calculate recency factor with improved logic"""
        content_date = content['content'].get('modified_time', now)
        
        if isinstance(content_date, str):
            try:
                if 'Z' in content_date:
                    content_date = datetime.fromisoformat(content_date.replace('Z', '+00:00'))
                else:
                    content_date = datetime.fromisoformat(content_date)
            except (ValueError, AttributeError):
                content_date = now
        elif not isinstance(content_date, datetime):
            content_date = now
        
        days_old = max(0, (now - content_date).days)
        
        # More gradual decay: content loses 50% relevance after 180 days
        recency_factor = math.exp(-days_old / 180)
        
        # Apply milder bias: 0.8 to 1.2 range instead of 0.7 to 1.0
        return 0.8 + 0.4 * recency_factor
    
    def _calculate_length_factor(self, content: Dict) -> float:
        """Calculate content length factor for comprehensive queries"""
        word_count = content['content'].get('word_count', 100)
        
        # Prefer moderate length content (300-1000 words optimal)
        if word_count < 100:
            return 0.7  # Very short content penalty
        elif word_count < 300:
            return 0.85 + (word_count - 100) / 200 * 0.15  # Gradual increase
        elif word_count <= 1000:
            return 1.0  # Optimal range
        else:
            # Gentle penalty for very long content
            return max(0.9, 1.0 - (word_count - 1000) / 10000 * 0.1)
    
    def _get_expected_answer_type(self, intent_type: str) -> str:
        """Map intent type to expected answer type"""
        mapping = {
            'instruction_seeking': 'step_by_step_guide',
            'comparison_seeking': 'comparison_table',
            'troubleshooting': 'troubleshooting_guide',
            'discovery': 'content_list',
            'information_seeking': 'synthesized_answer'
        }
        return mapping.get(intent_type, 'synthesized_answer')
    
    def _extract_comparison_items(self, query: str, expanded_query: Dict) -> List[str]:
        """Extract comparison items from query"""
        # Check expanded query parts first
        for part in expanded_query.get('query_parts', []):
            if part.get('type') == 'comparison' and 'items' in part:
                return part['items']
        
        # Fallback pattern matching
        vs_pattern = r'(.+?)\s+(?:vs?|versus)\s+(.+?)(?:\s|$)'
        match = re.search(vs_pattern, query, re.IGNORECASE)
        if match:
            return [match.group(1).strip(), match.group(2).strip()]
        
        return []


def get_refined_search_engine():
    """Get or create the refined search engine instance"""
    if STREAMLIT_AVAILABLE and hasattr(st.session_state, 'refined_search_engine'):
        return st.session_state.refined_search_engine
    
    engine = RefinedIntelligentSearchEngine()
    
    if STREAMLIT_AVAILABLE:
        st.session_state.refined_search_engine = engine
    
    return engine