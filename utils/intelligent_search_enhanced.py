import json
import re
import math
from typing import Dict, List, Tuple, Any, Optional, Set
from pathlib import Path
import yaml
from datetime import datetime
from collections import defaultdict, Counter
import streamlit as st
from .llm_utils import _call_llm_api

class EnhancedIntelligentSearchEngine:
    """
    Enhanced search engine with query expansion and result clustering capabilities
    """
    
    def __init__(self, knowledgebase_path: str = "knowledgebase"):
        self.kb_path = Path(knowledgebase_path)
        self.content_index = {}
        self.entity_index = {}
        self.concept_index = {}
        self.relationship_map = {}
        
        # Initialize synonym mapping for common terms
        self.synonym_map = {
            # Programming/Tech synonyms
            'build': ['compile', 'construct', 'create', 'make'],
            'error': ['bug', 'issue', 'problem', 'fault', 'defect'],
            'fix': ['repair', 'resolve', 'correct', 'patch', 'debug'],
            'code': ['program', 'script', 'source'],
            'function': ['method', 'procedure', 'routine', 'operation'],
            'test': ['verify', 'validate', 'check', 'examine'],
            'deploy': ['release', 'launch', 'publish', 'rollout'],
            'api': ['interface', 'endpoint', 'service'],
            'database': ['db', 'datastore', 'storage'],
            'agent': ['bot', 'assistant', 'automation'],
            
            # AI/ML synonyms
            'ai': ['artificial intelligence', 'machine learning', 'ml'],
            'model': ['algorithm', 'network', 'system'],
            'train': ['teach', 'fit', 'learn'],
            'predict': ['forecast', 'estimate', 'infer'],
            'accuracy': ['precision', 'performance', 'quality'],
            
            # General synonyms
            'show': ['display', 'present', 'reveal', 'demonstrate'],
            'find': ['search', 'locate', 'discover', 'identify'],
            'use': ['utilize', 'employ', 'apply', 'implement'],
            'create': ['make', 'generate', 'produce', 'develop'],
            'improve': ['enhance', 'optimize', 'upgrade', 'refine'],
            'compare': ['contrast', 'versus', 'vs', 'difference'],
            'best': ['optimal', 'top', 'recommended', 'preferred'],
            'guide': ['tutorial', 'howto', 'walkthrough', 'instructions']
        }
        
        # Build reverse synonym map
        self.reverse_synonym_map = {}
        for primary, synonyms in self.synonym_map.items():
            for syn in synonyms:
                if syn not in self.reverse_synonym_map:
                    self.reverse_synonym_map[syn] = []
                self.reverse_synonym_map[syn].append(primary)
    
    def index_content(self) -> Dict[str, Any]:
        """
        Index all content in the knowledgebase with intelligent metadata
        """
        indexed_files = 0
        total_files = 0
        
        if not self.kb_path.exists():
            return {"indexed": 0, "total": 0, "status": "No knowledgebase directory found"}
        
        # Walk through all markdown files
        for md_file in self.kb_path.rglob("*.md"):
            total_files += 1
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Parse YAML frontmatter
                frontmatter, body = self._parse_frontmatter(content)
                
                file_key = str(md_file.relative_to(self.kb_path))
                
                # Store basic info with enhanced metadata
                try:
                    modified_time = datetime.fromtimestamp(md_file.stat().st_mtime)
                except:
                    modified_time = datetime.now()
                
                self.content_index[file_key] = {
                    'title': frontmatter.get('title', md_file.stem),
                    'author': frontmatter.get('author', 'Unknown'),
                    'category': frontmatter.get('category', 'General'),
                    'content_type': frontmatter.get('type', 'document'),
                    'date_added': frontmatter.get('date_added', datetime.now().isoformat()),
                    'full_path': str(md_file),
                    'body': body,
                    'frontmatter': frontmatter,
                    'word_count': len(body.split()) if body else 0,
                    'modified_time': modified_time
                }
                
                # Index entities if available
                entities = frontmatter.get('entities', [])
                for entity in entities:
                    if entity not in self.entity_index:
                        self.entity_index[entity] = []
                    self.entity_index[entity].append(file_key)
                
                # Index concepts if available
                concepts = frontmatter.get('concepts', [])
                for concept in concepts:
                    if concept not in self.concept_index:
                        self.concept_index[concept] = []
                    self.concept_index[concept].append(file_key)
                
                indexed_files += 1
                
            except Exception as e:
                print(f"Error indexing {md_file}: {e}")
                continue
        
        return {
            "indexed": indexed_files,
            "total": total_files,
            "status": f"Successfully indexed {indexed_files} of {total_files} files"
        }
    
    def _parse_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """Parse YAML frontmatter from markdown content"""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1]) or {}
                    body = parts[2].strip()
                    return frontmatter, body
                except yaml.YAMLError:
                    pass
        
        return {}, content
    
    def expand_query(self, query: str) -> Dict[str, Any]:
        """
        Expand query with synonyms, stemming, and n-grams
        """
        query_lower = query.lower()
        
        # Basic tokenization
        tokens = re.findall(r'\b\w+\b', query_lower)
        
        # Expand tokens with synonyms
        expanded_tokens = set(tokens)
        for token in tokens:
            # Add direct synonyms
            if token in self.synonym_map:
                expanded_tokens.update(self.synonym_map[token])
            # Add reverse synonyms
            if token in self.reverse_synonym_map:
                expanded_tokens.update(self.reverse_synonym_map[token])
        
        # Extract n-grams for phrase searching
        bigrams = []
        trigrams = []
        if len(tokens) >= 2:
            bigrams = [f"{tokens[i]} {tokens[i+1]}" for i in range(len(tokens)-1)]
        if len(tokens) >= 3:
            trigrams = [f"{tokens[i]} {tokens[i+1]} {tokens[i+2]}" for i in range(len(tokens)-2)]
        
        # Simple stemming (remove common suffixes)
        stemmed_tokens = set()
        # Order matters - try longer suffixes first
        suffixes = ['tion', 'ment', 'ing', 'est', 'er', 'ed', 'es', 'ly', 's']
        for token in expanded_tokens:
            stemmed = token
            for suffix in suffixes:
                if token.endswith(suffix) and len(token) > len(suffix) + 2:
                    candidate = token[:-len(suffix)]
                    # Add both the stemmed and original form
                    stemmed_tokens.add(candidate)
                    break
            stemmed_tokens.add(token)  # Always include original
        
        # Query decomposition for complex queries
        query_parts = []
        
        # Check for comparison queries
        comparison_match = re.search(r'(.+?)\s+(?:vs\.?|versus|compared to|or)\s+(.+)', query_lower)
        if comparison_match:
            query_parts.append({
                'type': 'comparison',
                'items': [comparison_match.group(1).strip(), comparison_match.group(2).strip()]
            })
        
        # Check for question words
        question_words = ['what', 'how', 'why', 'when', 'where', 'which', 'who']
        for qword in question_words:
            if query_lower.startswith(qword):
                query_parts.append({
                    'type': 'question',
                    'question_type': qword
                })
                break
        
        return {
            'original': query,
            'tokens': list(tokens),
            'expanded_tokens': list(expanded_tokens),
            'stemmed_tokens': list(stemmed_tokens),
            'bigrams': bigrams,
            'trigrams': trigrams,
            'query_parts': query_parts,
            'all_search_terms': list(expanded_tokens.union(stemmed_tokens))
        }
    
    def parse_query_intent(self, query: str) -> Dict[str, Any]:
        """
        Enhanced query intent parsing with query expansion
        """
        # First expand the query
        expanded_query = self.expand_query(query)
        
        prompt = f"""Analyze this user query and its expanded forms:

USER QUERY: "{query}"
EXPANDED TOKENS: {expanded_query['expanded_tokens']}
QUERY PARTS: {expanded_query['query_parts']}

Please determine:
1. INTENT TYPE: What is the user trying to do?
   - information_seeking: "What is...", "How does... work", "Explain..."
   - instruction_seeking: "How to...", "Best way to...", "Steps for..."
   - comparison_seeking: "X vs Y", "Which is better...", "Compare..."
   - troubleshooting: "Why isn't...", "What went wrong...", "Fix..."
   - discovery: "Find all...", "Show me...", "List..."

2. KEY ENTITIES: Extract specific people, places, tools, technologies, etc.

3. KEY CONCEPTS: Extract abstract ideas, methodologies, skills, topics

4. CONTEXT FILTERS: Any mentioned constraints like difficulty level, time period, categories

5. EXPECTED ANSWER TYPE: What type of response would best satisfy this query?
   - step_by_step_guide, conceptual_explanation, comparison_table, troubleshooting_guide, content_list, synthesized_answer

Respond in valid JSON format."""

        try:
            response = _call_llm_api(prompt, "query intent analysis")
            if response:
                # Clean and parse JSON
                if '```json' in response:
                    response = response.split('```json')[1].split('```')[0]
                elif '```' in response:
                    response = response.split('```')[1].split('```')[0]
                
                intent_data = json.loads(response)
                # Add expanded query data
                intent_data['expanded_query'] = expanded_query
                return intent_data
        except Exception as e:
            # Log the specific error but continue with fallback
            print(f"LLM API error in query intent analysis: {e}")
        
        # Fallback with expanded query info
        query_lower = query.lower()
        intent_type = "information_seeking"
        
        if any(phrase in query_lower for phrase in ["how to", "best way", "steps for"]):
            intent_type = "instruction_seeking"
        elif expanded_query['query_parts'] and any(p['type'] == 'comparison' for p in expanded_query['query_parts']):
            intent_type = "comparison_seeking"
        elif any(phrase in query_lower for phrase in ["why isn't", "what went wrong", "fix", "troubleshoot"]):
            intent_type = "troubleshooting"
        elif any(phrase in query_lower for phrase in ["find all", "show me", "list"]):
            intent_type = "discovery"
        
        return {
            "intent_type": intent_type,
            "key_entities": [],
            "key_concepts": [],
            "context_filters": {},
            "expected_answer_type": "synthesized_answer",
            "confidence": 0.5,
            "expanded_query": expanded_query
        }
    
    def calculate_search_score(self, query_data: Dict, content_data: Dict) -> float:
        """
        Calculate relevance score using multiple factors
        """
        score = 0.0
        
        # Safely get title and body with defaults
        title_lower = content_data.get('title', '').lower()
        body_lower = content_data.get('body', '').lower()
        
        # Score for exact phrase matches (highest weight)
        for trigram in query_data.get('trigrams', []):
            if trigram in title_lower:
                score += 10.0
            if trigram in body_lower:
                score += 2.0
        
        for bigram in query_data.get('bigrams', []):
            if bigram in title_lower:
                score += 5.0
            if bigram in body_lower:
                score += 1.0
        
        # Score for individual term matches
        all_terms = query_data.get('all_search_terms', [])
        if all_terms:
            # Title matches
            title_matches = sum(1 for term in all_terms if term in title_lower)
            score += (title_matches / len(all_terms)) * 3.0
            
            # Body matches (with diminishing returns)
            body_matches = sum(1 for term in all_terms if term in body_lower)
            score += min(body_matches * 0.1, 2.0)
        
        # Boost for entity/concept matches
        entities = set(content_data.get('frontmatter', {}).get('entities', []))
        concepts = set(content_data.get('frontmatter', {}).get('concepts', []))
        
        for term in all_terms:
            if any(term in entity.lower() for entity in entities):
                score += 2.0
            if any(term in concept.lower() for concept in concepts):
                score += 1.5
        
        return score
    
    def search_content(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """
        Enhanced search with query expansion and better scoring
        """
        query_intent = self.parse_query_intent(query)
        expanded_query = query_intent.get('expanded_query', self.expand_query(query))
        
        results = []
        
        # Search all content with enhanced scoring
        for file_key, content_data in self.content_index.items():
            score = self.calculate_search_score(expanded_query, content_data)
            
            if score > 0:
                results.append({
                    'file_key': file_key,
                    'match_type': 'enhanced',
                    'score': score,
                    'content': content_data,
                    'matched_terms': [t for t in expanded_query['all_search_terms'] 
                                    if t in content_data['body'].lower() or t in content_data['title'].lower()]
                })
        
        # Sort by score
        results.sort(key=lambda x: x['score'], reverse=True)
        
        # Apply clustering and ranking
        clustered_results = self.cluster_and_rank_results(results, query_intent)
        
        return clustered_results[:max_results]
    
    def cluster_and_rank_results(self, results: List[Dict[str, Any]], query_intent: Dict) -> List[Dict[str, Any]]:
        """
        Cluster similar results and apply advanced ranking
        """
        if not results:
            return results
        
        # Group results by similarity
        clusters = []
        clustered_files = set()
        
        for i, result in enumerate(results):
            if result['file_key'] in clustered_files:
                continue
            
            # Start new cluster
            cluster = {
                'primary': result,
                'members': [result],
                'cluster_score': result['score']
            }
            clustered_files.add(result['file_key'])
            
            # Find similar results for this cluster
            for j, other in enumerate(results[i+1:], i+1):
                if other['file_key'] in clustered_files:
                    continue
                
                # Calculate similarity based on shared matched terms
                result_terms = set(result.get('matched_terms', []))
                other_terms = set(other.get('matched_terms', []))
                shared_terms = result_terms & other_terms
                
                # Avoid division by zero
                max_terms = max(len(result_terms), len(other_terms))
                similarity = len(shared_terms) / max_terms if max_terms > 0 else 0
                
                # Also check category and author similarity
                if result['content']['category'] == other['content']['category']:
                    similarity += 0.2
                if result['content']['author'] == other['content']['author']:
                    similarity += 0.1
                
                # Add to cluster if similar enough
                if similarity > 0.5:
                    cluster['members'].append(other)
                    cluster['cluster_score'] += other['score'] * 0.5  # Diminishing returns
                    clustered_files.add(other['file_key'])
            
            clusters.append(cluster)
        
        # Rank clusters with various factors
        now = datetime.now()
        for cluster in clusters:
            primary = cluster['primary']
            
            # Base score from search relevance
            final_score = cluster['cluster_score']
            
            # Apply recency bias if needed
            if query_intent.get('intent_type') in ['troubleshooting', 'discovery']:
                # More weight to recent content for these query types
                content_date = primary['content'].get('modified_time', now)
                if isinstance(content_date, str):
                    try:
                        # Handle various date formats
                        if 'Z' in content_date:
                            content_date = datetime.fromisoformat(content_date.replace('Z', '+00:00'))
                        else:
                            content_date = datetime.fromisoformat(content_date)
                    except (ValueError, AttributeError):
                        content_date = now
                elif not isinstance(content_date, datetime):
                    content_date = now
                
                days_old = max(0, (now - content_date).days)
                recency_factor = math.exp(-days_old / 90)  # Decay over 90 days
                final_score *= (0.7 + 0.3 * recency_factor)
            
            # Diversity bonus (reduce score if too many from same category)
            category = primary['content']['category']
            category_count = sum(1 for c in clusters[:clusters.index(cluster)] 
                               if c['primary']['content']['category'] == category)
            diversity_penalty = 1.0 / (1.0 + category_count * 0.2)
            final_score *= diversity_penalty
            
            # Length preference (prefer comprehensive content for learning queries)
            if query_intent.get('intent_type') in ['information_seeking', 'instruction_seeking']:
                word_count = primary['content'].get('word_count', 100)
                length_factor = min(word_count / 500, 2.0)  # Optimal around 500+ words
                final_score *= (0.8 + 0.2 * length_factor)
            
            cluster['final_score'] = final_score
        
        # Sort clusters by final score
        clusters.sort(key=lambda x: x['final_score'], reverse=True)
        
        # Flatten back to results list with cluster information
        final_results = []
        for cluster in clusters:
            for i, member in enumerate(cluster['members']):
                result = member.copy()
                result['cluster_id'] = clusters.index(cluster)
                result['is_cluster_primary'] = (i == 0)
                result['cluster_size'] = len(cluster['members'])
                result['final_score'] = cluster['final_score'] if i == 0 else cluster['final_score'] * 0.8
                # Ensure we keep the original score as backup
                if 'score' not in result:
                    result['score'] = result.get('final_score', 0)
                final_results.append(result)
        
        return final_results
    
    def synthesize_answer(self, query: str, search_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Use LLM to synthesize an answer from clustered search results
        """
        if not search_results:
            return {
                "answer": "I couldn't find any relevant content for your query. Try rephrasing your question or checking if the content has been imported.",
                "confidence": 0.0,
                "sources": []
            }
        
        # Prepare context from search results, prioritizing primary cluster results
        context_pieces = []
        sources = []
        seen_clusters = set()
        
        for result in search_results[:7]:  # Slightly more results due to clustering
            # Skip non-primary cluster members for context
            if result.get('cluster_id') in seen_clusters and not result.get('is_cluster_primary'):
                continue
            
            seen_clusters.add(result.get('cluster_id'))
            content = result['content']
            
            cluster_info = ""
            if result.get('cluster_size', 1) > 1:
                cluster_info = f" (+ {result['cluster_size'] - 1} similar documents)"
            
            context_piece = f"""
Source {len(context_pieces) + 1}: {content.get('title', 'Untitled')} (by {content.get('author', 'Unknown')}){cluster_info}
Category: {content.get('category', 'General')}
Relevance: {result.get('final_score', result.get('score', 0)):.2f}
Matched terms: {', '.join(result.get('matched_terms', [])[:5])}

Content excerpt:
{content.get('body', '')[:1500]}...
"""
            context_pieces.append(context_piece)
            sources.append({
                'title': content.get('title', 'Untitled'),
                'author': content.get('author', 'Unknown'),
                'category': content.get('category', 'General'),
                'file_path': content.get('full_path', 'Unknown'),
                'score': result.get('final_score', result.get('score', 0)),
                'cluster_size': result.get('cluster_size', 1)
            })
        
        # Create synthesis prompt
        prompt = f"""Based on the following sources, please provide a comprehensive answer to the user's question.

USER QUESTION: "{query}"

AVAILABLE SOURCES:
{chr(10).join(context_pieces)}

Instructions:
1. Synthesize information from multiple sources when possible
2. Note when multiple similar documents support the same information
3. If sources contradict each other, mention the different perspectives
4. Include specific details and actionable information
5. If the answer requires multiple steps, organize them clearly
6. Always cite which sources you're drawing from
7. If the sources don't fully answer the question, say so

Please provide a clear, comprehensive answer based on the available sources."""

        try:
            response = _call_llm_api(prompt, "answer synthesis")
            if response and response.strip():
                # Calculate normalized confidence based on score distribution
                top_scores = [r.get('final_score', r.get('score', 0)) for r in search_results[:3]]
                if top_scores:
                    # Normalize scores - assume good match is score > 5
                    avg_top_score = sum(top_scores) / len(top_scores)
                    confidence = min(0.9, avg_top_score / 10.0)  # Normalize to 0-1 range
                else:
                    confidence = 0.5
                
                return {
                    "answer": response,
                    "confidence": confidence,
                    "sources": sources,
                    "total_results": len(search_results),
                    "clusters_found": len(seen_clusters)
                }
        except Exception as e:
            print(f"Error in answer synthesis: {e}")
        
        # Enhanced fallback response when LLM is unavailable
        fallback_answer = f"Found {len(search_results)} relevant documents"
        if len(seen_clusters) > 1:
            fallback_answer += f" organized in {len(seen_clusters)} topic clusters"
        fallback_answer += ".\n\n"
        
        # Add top results summary
        if search_results:
            fallback_answer += "**Top Results:**\n"
            for i, result in enumerate(search_results[:3]):
                content = result.get('content', {})
                title = content.get('title', 'Untitled')
                score = result.get('final_score', result.get('score', 0))
                matched = result.get('matched_terms', [])
                
                fallback_answer += f"\n{i+1}. **{title}**"
                if score > 0:
                    fallback_answer += f" (Relevance: {score:.1f})"
                if matched:
                    fallback_answer += f"\n   Matched: {', '.join(matched[:3])}"
                
                # Add brief excerpt
                body = content.get('body', '')
                if body:
                    excerpt = body[:200].strip()
                    if len(body) > 200:
                        excerpt += "..."
                    fallback_answer += f"\n   {excerpt}\n"
        
        return {
            "answer": fallback_answer,
            "confidence": 0.5,
            "sources": sources,
            "total_results": len(search_results),
            "clusters_found": len(seen_clusters)
        }
    
    def get_related_content(self, file_key: str, max_related: int = 5) -> List[Dict[str, Any]]:
        """
        Find content related to a specific file based on shared entities/concepts
        """
        if file_key not in self.content_index:
            return []
        
        current_content = self.content_index[file_key]
        current_entities = set(current_content.get('frontmatter', {}).get('entities', []))
        current_concepts = set(current_content.get('frontmatter', {}).get('concepts', []))
        
        # Also extract key terms from title
        title_terms = set(re.findall(r'\b\w+\b', current_content['title'].lower()))
        
        related_scores = {}
        
        for other_key, other_content in self.content_index.items():
            if other_key == file_key:
                continue
            
            other_frontmatter = other_content.get('frontmatter', {})
            other_entities = set(other_frontmatter.get('entities', []))
            other_concepts = set(other_frontmatter.get('concepts', []))
            other_title_terms = set(re.findall(r'\b\w+\b', other_content['title'].lower()))
            
            # Calculate various similarity scores
            entity_overlap = len(current_entities.intersection(other_entities))
            concept_overlap = len(current_concepts.intersection(other_concepts))
            title_overlap = len(title_terms.intersection(other_title_terms))
            
            # Category bonus
            category_match = 1.5 if current_content['category'] == other_content['category'] else 1.0
            
            score = (entity_overlap * 2 + concept_overlap * 1.5 + title_overlap * 0.5) * category_match
            
            if score > 0:
                related_scores[other_key] = {
                    'score': score,
                    'content': other_content,
                    'shared_entities': list(current_entities.intersection(other_entities)),
                    'shared_concepts': list(current_concepts.intersection(other_concepts)),
                    'shared_title_terms': list(title_terms.intersection(other_title_terms))
                }
        
        # Sort by score and return top results
        sorted_related = sorted(related_scores.items(), key=lambda x: x[1]['score'], reverse=True)
        
        return [
            {
                'file_key': key,
                'relationship_score': data['score'],
                'shared_entities': data['shared_entities'],
                'shared_concepts': data['shared_concepts'],
                'shared_title_terms': data['shared_title_terms'],
                'content': data['content']
            }
            for key, data in sorted_related[:max_related]
        ]

def get_enhanced_search_engine() -> EnhancedIntelligentSearchEngine:
    """Get or create the enhanced search engine instance"""
    if 'enhanced_search_engine' not in st.session_state:
        st.session_state.enhanced_search_engine = EnhancedIntelligentSearchEngine()
        # Index content on first load
        with st.spinner("Indexing knowledgebase content with enhanced features..."):
            result = st.session_state.enhanced_search_engine.index_content()
            if result['indexed'] > 0:
                st.success(f"✅ {result['status']}")
            else:
                st.info("📝 No content found to index. Import some content first!")
    
    return st.session_state.enhanced_search_engine