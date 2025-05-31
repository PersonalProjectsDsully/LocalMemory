import json
import re
from typing import Dict, List, Tuple, Any, Optional
from pathlib import Path
import yaml
from datetime import datetime
import streamlit as st
from .llm_utils import _call_llm_api

class IntelligentSearchEngine:
    """
    Universal search engine that works across any domain using LLM-powered content analysis
    """
    
    def __init__(self, knowledgebase_path: str = "knowledgebase"):
        self.kb_path = Path(knowledgebase_path)
        self.content_index = {}
        self.entity_index = {}
        self.concept_index = {}
        self.relationship_map = {}
        
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
                
                # Store basic info
                self.content_index[file_key] = {
                    'title': frontmatter.get('title', md_file.stem),
                    'author': frontmatter.get('author', 'Unknown'),
                    'category': frontmatter.get('category', 'General'),
                    'content_type': frontmatter.get('type', 'document'),
                    'date_added': frontmatter.get('date_added', ''),
                    'full_path': str(md_file),
                    'body': body,
                    'frontmatter': frontmatter
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
    
    def parse_query_intent(self, query: str) -> Dict[str, Any]:
        """
        Use LLM to understand query intent and extract key information
        """
        prompt = f"""Analyze this user query and extract the following information:

USER QUERY: "{query}"

Please determine:
1. INTENT TYPE: What is the user trying to do?
   - information_seeking: "What is...", "How does... work", "Explain..."
   - instruction_seeking: "How to...", "Best way to...", "Steps for..."
   - comparison_seeking: "X vs Y", "Which is better...", "Compare..."
   - troubleshooting: "Why isn't...", "What went wrong...", "Fix..."
   - discovery: "Find all...", "Show me...", "List..."

2. KEY ENTITIES: Extract specific people, places, tools, technologies, movies, etc.

3. KEY CONCEPTS: Extract abstract ideas, methodologies, skills, topics

4. CONTEXT FILTERS: Any mentioned constraints like difficulty level, time period, specific categories

5. EXPECTED ANSWER TYPE: What type of response would best satisfy this query?
   - step_by_step_guide, conceptual_explanation, comparison_table, troubleshooting_guide, content_list, synthesized_answer

Respond in valid JSON format:
{{
  "intent_type": "information_seeking",
  "key_entities": ["entity1", "entity2"],
  "key_concepts": ["concept1", "concept2"],
  "context_filters": {{"difficulty": "beginner", "category": "technology"}},
  "expected_answer_type": "synthesized_answer",
  "confidence": 0.8
}}"""

        try:
            response = _call_llm_api(prompt, "query intent analysis")
            if response:
                # Clean and parse JSON
                if '```json' in response:
                    response = response.split('```json')[1].split('```')[0]
                elif '```' in response:
                    response = response.split('```')[1].split('```')[0]
                
                return json.loads(response)
        except:
            pass
        
        # Fallback intent parsing
        query_lower = query.lower()
        intent_type = "information_seeking"
        
        if any(phrase in query_lower for phrase in ["how to", "best way", "steps for"]):
            intent_type = "instruction_seeking"
        elif any(phrase in query_lower for phrase in ["vs", "versus", "compare", "which is better"]):
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
            "confidence": 0.5
        }
    
    def search_content(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """
        Search for relevant content based on query
        """
        query_intent = self.parse_query_intent(query)
        results = []
        
        # Search by entities
        for entity in query_intent.get('key_entities', []):
            if entity in self.entity_index:
                for file_key in self.entity_index[entity]:
                    if file_key in self.content_index:
                        results.append({
                            'file_key': file_key,
                            'match_type': 'entity',
                            'match_value': entity,
                            'score': 1.0,
                            'content': self.content_index[file_key]
                        })
        
        # Search by concepts
        for concept in query_intent.get('key_concepts', []):
            if concept in self.concept_index:
                for file_key in self.concept_index[concept]:
                    if file_key in self.content_index:
                        results.append({
                            'file_key': file_key,
                            'match_type': 'concept',
                            'match_value': concept,
                            'score': 0.8,
                            'content': self.content_index[file_key]
                        })
        
        # Keyword search in titles and content
        query_words = query.lower().split()
        for file_key, content_data in self.content_index.items():
            title_lower = content_data['title'].lower()
            body_lower = content_data['body'].lower()
            
            title_matches = sum(1 for word in query_words if word in title_lower)
            body_matches = sum(1 for word in query_words if word in body_lower)
            
            if title_matches > 0 or body_matches > 0:
                score = (title_matches * 2 + body_matches * 0.1) / len(query_words)
                results.append({
                    'file_key': file_key,
                    'match_type': 'keyword',
                    'match_value': f"{title_matches} title + {body_matches} body matches",
                    'score': score,
                    'content': content_data
                })
        
        # Remove duplicates and sort by score
        seen_files = set()
        unique_results = []
        for result in results:
            if result['file_key'] not in seen_files:
                seen_files.add(result['file_key'])
                unique_results.append(result)
        
        unique_results.sort(key=lambda x: x['score'], reverse=True)
        return unique_results[:max_results]
    
    def synthesize_answer(self, query: str, search_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Use LLM to synthesize an answer from multiple search results
        """
        if not search_results:
            return {
                "answer": "I couldn't find any relevant content for your query. Try rephrasing your question or checking if the content has been imported.",
                "confidence": 0.0,
                "sources": []
            }
        
        # Prepare context from search results
        context_pieces = []
        sources = []
        
        for i, result in enumerate(search_results[:5]):  # Limit to top 5 results
            content = result['content']
            context_piece = f"""
Source {i+1}: {content['title']} (by {content['author']})
Category: {content['category']}
Match: {result['match_type']} - {result['match_value']}

Content excerpt:
{content['body'][:1500]}...
"""
            context_pieces.append(context_piece)
            sources.append({
                'title': content['title'],
                'author': content['author'],
                'category': content['category'],
                'file_path': content['full_path'],
                'match_type': result['match_type'],
                'score': result['score']
            })
        
        # Create synthesis prompt
        prompt = f"""Based on the following sources, please provide a comprehensive answer to the user's question.

USER QUESTION: "{query}"

AVAILABLE SOURCES:
{chr(10).join(context_pieces)}

Instructions:
1. Synthesize information from multiple sources when possible
2. If sources contradict each other, mention the different perspectives
3. Include specific details and actionable information
4. If the answer requires multiple steps, organize them clearly
5. Always cite which sources you're drawing from (e.g., "According to Source 1...")
6. If the sources don't fully answer the question, say so and suggest what additional information might be needed

Please provide a clear, comprehensive answer based on the available sources."""

        try:
            response = _call_llm_api(prompt, "answer synthesis")
            if response:
                return {
                    "answer": response,
                    "confidence": min(0.9, sum(r['score'] for r in search_results[:3]) / 3),
                    "sources": sources
                }
        except Exception as e:
            print(f"Error in answer synthesis: {e}")
        
        # Fallback: simple concatenation
        fallback_answer = f"Found {len(search_results)} relevant sources:\n\n"
        for i, result in enumerate(search_results[:3]):
            content = result['content']
            fallback_answer += f"**{content['title']}** (by {content['author']})\n"
            fallback_answer += f"{content['body'][:500]}...\n\n"
        
        return {
            "answer": fallback_answer,
            "confidence": 0.5,
            "sources": sources
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
        
        related_scores = {}
        
        # Score other content based on shared entities and concepts
        for other_key, other_content in self.content_index.items():
            if other_key == file_key:
                continue
            
            other_frontmatter = other_content.get('frontmatter', {})
            other_entities = set(other_frontmatter.get('entities', []))
            other_concepts = set(other_frontmatter.get('concepts', []))
            
            entity_overlap = len(current_entities.intersection(other_entities))
            concept_overlap = len(current_concepts.intersection(other_concepts))
            
            score = entity_overlap * 2 + concept_overlap
            if score > 0:
                related_scores[other_key] = {
                    'score': score,
                    'content': other_content,
                    'shared_entities': list(current_entities.intersection(other_entities)),
                    'shared_concepts': list(current_concepts.intersection(other_concepts))
                }
        
        # Sort by score and return top results
        sorted_related = sorted(related_scores.items(), key=lambda x: x[1]['score'], reverse=True)
        
        return [
            {
                'file_key': key,
                'relationship_score': data['score'],
                'shared_entities': data['shared_entities'],
                'shared_concepts': data['shared_concepts'],
                'content': data['content']
            }
            for key, data in sorted_related[:max_related]
        ]

def get_search_engine() -> IntelligentSearchEngine:
    """Get or create the search engine instance"""
    if 'search_engine' not in st.session_state:
        st.session_state.search_engine = IntelligentSearchEngine()
        # Index content on first load
        with st.spinner("Indexing knowledgebase content..."):
            result = st.session_state.search_engine.index_content()
            if result['indexed'] > 0:
                st.success(f"✅ {result['status']}")
            else:
                st.info("📝 No content found to index. Import some content first!")
    
    return st.session_state.search_engine