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
from .qa_improvement_system import ReportQASystem, ReportImprovementPipeline, QA_CONFIGS

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
        
        # Inverted index for fast search
        self.inverted_index = {}  # {term: {doc_id: frequency}}
        self.document_lengths = {}  # {doc_id: word_count}
        self.total_documents = 0
        
        # QA and improvement system
        self.qa_system = ReportQASystem(QA_CONFIGS.get("comprehensive"))
        self.improvement_pipeline = ReportImprovementPipeline(self.qa_system)
        
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
                
                # Build inverted index for this document
                self._update_inverted_index(file_key, body, frontmatter.get('title', ''))
                
            except Exception as e:
                print(f"Error indexing {md_file}: {e}")
                continue
        
        # Update total document count
        self.total_documents = len(self.content_index)
        
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
    
    def _parse_markdown_structure(self, content: str) -> Dict[str, Any]:
        """
        Parse markdown content to identify structural elements like headers, summary, key points
        """
        structure = {
            'headers': [],
            'summary': '',
            'key_points': [],
            'sections': {}
        }
        
        # Handle null or empty content
        if not content:
            return structure
            
        lines = content.split('\n')
        current_section = None
        section_content = []
        in_summary = False
        in_key_points = False
        
        for line in lines:
            # Check for headers
            if line.startswith('#'):
                # Save previous section if exists
                if current_section and section_content:
                    structure['sections'][current_section] = '\n'.join(section_content).strip()
                    section_content = []
                
                # Extract header level and text
                header_match = re.match(r'^(#+)\s+(.+)$', line)
                if header_match:
                    level = len(header_match.group(1))
                    header_text = header_match.group(2).strip()
                    structure['headers'].append({
                        'level': level,
                        'text': header_text
                    })
                    current_section = header_text
                    
                    # Check for special sections
                    header_lower = header_text.lower()
                    in_summary = 'summary' in header_lower or 'abstract' in header_lower
                    in_key_points = 'key point' in header_lower or 'takeaway' in header_lower
            else:
                # Collect content for current section
                if current_section:
                    section_content.append(line)
                
                # Extract summary content
                if in_summary and line.strip():
                    structure['summary'] += line + ' '
                
                # Extract key points (look for bullet points)
                if in_key_points and line.strip().startswith(('-', '*', '•')):
                    key_point = line.strip().lstrip('-*•').strip()
                    if key_point:
                        structure['key_points'].append(key_point)
        
        # Save last section
        if current_section and section_content:
            structure['sections'][current_section] = '\n'.join(section_content).strip()
        
        # Clean up summary
        structure['summary'] = structure['summary'].strip()
        
        return structure
    
    def _update_inverted_index(self, doc_id: str, body: str, title: str = "") -> None:
        """
        Update inverted index with terms from a document
        """
        # Tokenize content (body + title)
        full_text = f"{title} {body}".lower()
        tokens = re.findall(r'\b\w+\b', full_text)
        
        # Count term frequencies
        term_freq = Counter(tokens)
        
        # Update document length
        self.document_lengths[doc_id] = len(tokens)
        
        # Update inverted index
        for term, freq in term_freq.items():
            # Skip very short terms and common stopwords
            if len(term) < 2 or term in {'a', 'an', 'the', 'is', 'are', 'was', 'were', 'be', 'been', 'being'}:
                continue
                
            if term not in self.inverted_index:
                self.inverted_index[term] = {}
            
            self.inverted_index[term][doc_id] = freq
    
    def _search_with_index(self, query_terms: List[str]) -> Set[str]:
        """
        Use inverted index to quickly find candidate documents
        """
        candidate_docs = set()
        
        for term in query_terms:
            term_lower = term.lower()
            
            # Direct term lookup
            if term_lower in self.inverted_index:
                candidate_docs.update(self.inverted_index[term_lower].keys())
            
            # Also check stemmed versions
            # Simple stemming by removing common suffixes
            suffixes = ['ing', 'ed', 'es', 's', 'er', 'est', 'ly']
            for suffix in suffixes:
                if term_lower.endswith(suffix) and len(term_lower) > len(suffix) + 2:
                    stem = term_lower[:-len(suffix)]
                    if stem in self.inverted_index:
                        candidate_docs.update(self.inverted_index[stem].keys())
                        break
        
        return candidate_docs
    
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
    
    def _generate_report_outline(self, query: str, search_results: List[Dict[str, Any]], query_intent: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a structured outline for the report based on query and results
        """
        # Group results by theme/cluster
        clusters = {}
        for result in search_results:
            cluster_id = result.get('cluster_id', result['file_key'])
            if cluster_id not in clusters:
                clusters[cluster_id] = []
            clusters[cluster_id].append(result)
        
        # Determine report structure based on query type
        answer_type = query_intent.get('expected_answer_type', 'detailed_explanation')
        
        outline = {
            'title': f"Report: {query}",
            'executive_summary': {
                'purpose': f"Comprehensive answer to: {query}",
                'key_findings': []
            },
            'sections': [],
            'conclusion': {
                'summary_points': [],
                'recommendations': []
            }
        }
        
        # Build sections based on answer type
        if answer_type == 'step_by_step_guide':
            # Organize as sequential steps
            outline['sections'].append({
                'title': 'Prerequisites',
                'content_type': 'list',
                'sources': []
            })
            outline['sections'].append({
                'title': 'Step-by-Step Instructions',
                'content_type': 'numbered_list',
                'sources': []
            })
            outline['sections'].append({
                'title': 'Common Issues and Solutions',
                'content_type': 'subsections',
                'sources': []
            })
        
        elif answer_type == 'comparison_table':
            # Organize as comparison
            items = query_intent.get('comparison_items', ['Option A', 'Option B'])
            outline['sections'].append({
                'title': 'Overview',
                'content_type': 'paragraph',
                'sources': []
            })
            outline['sections'].append({
                'title': f'{items[0] if len(items) > 0 else "First Option"} Details',
                'content_type': 'subsections',
                'sources': []
            })
            if len(items) > 1:
                outline['sections'].append({
                    'title': f'{items[1]} Details',
                    'content_type': 'subsections',
                    'sources': []
                })
            outline['sections'].append({
                'title': 'Comparison Summary',
                'content_type': 'table',
                'sources': []
            })
        
        else:
            # Default structure - organize by theme/cluster
            for i, (cluster_id, cluster_results) in enumerate(clusters.items()):
                if i >= 4:  # Limit to 4 main sections
                    break
                
                # Get primary result for cluster theme
                primary = next((r for r in cluster_results if r.get('is_cluster_primary')), cluster_results[0])
                theme = primary['content'].get('category', f'Topic {i+1}')
                
                outline['sections'].append({
                    'title': theme,
                    'content_type': 'mixed',
                    'sources': [r['file_key'] for r in cluster_results]
                })
        
        return outline
    
    def _generate_structured_report(self, query: str, search_results: List[Dict[str, Any]], outline: Dict[str, Any], context_pieces: List[str]) -> Optional[Dict[str, Any]]:
        """
        Generate a structured report based on the outline
        """
        try:
            # Generate executive summary
            exec_summary_prompt = f"""Create an executive summary for this research query:
            
Query: "{query}"
Number of sources: {len(search_results)}

Based on these sources:
{chr(10).join(context_pieces[:3])}

Create a brief executive summary (2-3 sentences) that directly answers the question."""

            exec_summary = _call_llm_api(exec_summary_prompt, "executive summary")
            if not exec_summary:
                return None
            
            # Start building the report
            report_parts = [f"# {outline['title']}\n"]
            report_parts.append("## Executive Summary\n")
            report_parts.append(exec_summary + "\n")
            
            # Add table of contents if multiple sections
            if len(outline['sections']) > 1:
                report_parts.append("\n## Table of Contents\n")
                for i, section in enumerate(outline['sections']):
                    report_parts.append(f"{i+1}. [{section['title']}](#{section['title'].lower().replace(' ', '-')})\n")
                report_parts.append("\n")
            
            # Track citations for footnotes
            citation_map = {}  # source_key -> citation_number
            citation_counter = 1
            
            # Generate content for each section
            for section in outline['sections']:
                report_parts.append(f"\n## {section['title']}\n")
                
                # Get relevant sources for this section
                section_sources = []
                section_citations = []
                for result in search_results:
                    if result['file_key'] in section.get('sources', []) or not section.get('sources'):
                        section_sources.append(result)
                        # Track citation
                        if result['file_key'] not in citation_map:
                            citation_map[result['file_key']] = citation_counter
                            citation_counter += 1
                        section_citations.append(citation_map[result['file_key']])
                        if len(section_sources) >= 3:
                            break
                
                # Generate section content based on type
                if section['content_type'] == 'numbered_list':
                    section_prompt = f"""Create a numbered list of steps for: {section['title']}
Query context: {query}

Use these sources:
{self._format_sources_for_section_with_citations(section_sources, section_citations)}

Format as a clear numbered list with detailed steps.
Include inline citations using [1], [2], etc. when referencing specific information from sources."""
                
                elif section['content_type'] == 'table':
                    section_prompt = f"""Create a comparison table for: {section['title']}
Query context: {query}

Use these sources:
{self._format_sources_for_section_with_citations(section_sources, section_citations)}

Format as a markdown table comparing key features.
Include citations in table cells using [1], [2], etc."""
                
                else:
                    section_prompt = f"""Write a section about: {section['title']}
Query context: {query}

Use these sources:
{self._format_sources_for_section_with_citations(section_sources, section_citations)}

Include key points and specific details from the sources.
Add inline citations using [1], [2], etc. when making claims based on specific sources."""
                
                section_content = _call_llm_api(section_prompt, f"section: {section['title']}")
                if section_content:
                    report_parts.append(section_content + "\n")
            
            # Add conclusion
            report_parts.append("\n## Conclusion\n")
            conclusion_prompt = f"""Write a brief conclusion for this report on: {query}

Summarize the key findings and provide any recommendations.
Keep it to 2-3 sentences."""
            
            conclusion = _call_llm_api(conclusion_prompt, "conclusion")
            if conclusion:
                report_parts.append(conclusion + "\n")
            
            # Add sources section with proper citations
            report_parts.append("\n## References\n")
            # Sort citation map by citation number
            sorted_citations = sorted(citation_map.items(), key=lambda x: x[1])
            for file_key, citation_num in sorted_citations:
                # Find the source in search results
                source_result = next((r for r in search_results if r['file_key'] == file_key), None)
                if source_result:
                    content = source_result['content']
                    file_path = content.get('full_path', 'Unknown')
                    file_name = Path(file_path).name if file_path != 'Unknown' else 'Unknown'
                    report_parts.append(f"[{citation_num}] **{content.get('title', 'Untitled')}** by {content.get('author', 'Unknown')} - {file_name} (Category: {content.get('category', 'General')})\n")
            
            # Calculate confidence
            top_scores = [r.get('final_score', r.get('score', 0)) for r in search_results[:3]]
            confidence = min(0.9, sum(top_scores) / len(top_scores) / 10.0) if top_scores else 0.5
            
            return {
                "answer": ''.join(report_parts),
                "confidence": confidence,
                "sources": [
                    {
                        'title': r['content'].get('title', 'Untitled'),
                        'author': r['content'].get('author', 'Unknown'),
                        'category': r['content'].get('category', 'General'),
                        'file_path': r['content'].get('full_path', 'Unknown'),
                        'score': r.get('final_score', r.get('score', 0))
                    }
                    for r in search_results[:10]
                ],
                "total_results": len(search_results),
                "report_type": "structured"
            }
            
        except Exception as e:
            print(f"Error generating structured report: {e}")
            return None
    
    def _format_sources_for_section(self, sources: List[Dict[str, Any]]) -> str:
        """Format sources for section generation"""
        formatted = []
        for i, source in enumerate(sources[:3]):
            content = source['content']
            formatted.append(f"""
Source {i+1}: {content.get('title', 'Untitled')}
{content.get('body', '')[:500]}...
""")
        return '\n'.join(formatted)
    
    def _format_sources_for_section_with_citations(self, sources: List[Dict[str, Any]], citations: List[int]) -> str:
        """Format sources with citation numbers for section generation"""
        formatted = []
        for i, (source, citation_num) in enumerate(zip(sources[:3], citations[:3])):
            content = source['content']
            formatted.append(f"""
Source [{citation_num}]: {content.get('title', 'Untitled')} by {content.get('author', 'Unknown')}
{content.get('body', '')[:500]}...
""")
        return '\n'.join(formatted)
    
    def configure_qa_system(self, config_name: str = "comprehensive") -> None:
        """Configure the QA system with a preset or custom configuration"""
        if config_name in QA_CONFIGS:
            self.qa_system = ReportQASystem(QA_CONFIGS[config_name])
            self.improvement_pipeline = ReportImprovementPipeline(self.qa_system)
        else:
            print(f"Unknown QA config: {config_name}. Available: {list(QA_CONFIGS.keys())}")
    
    def synthesize_answer_with_qa(self, query: str, search_results: List[Dict[str, Any]], 
                                 use_structured_report: bool = True, 
                                 enable_qa_improvement: bool = True) -> Dict[str, Any]:
        """
        Generate answer with optional QA improvement pipeline
        """
        # Generate initial answer
        initial_result = self.synthesize_answer(query, search_results, use_structured_report)
        
        if not enable_qa_improvement or not self.qa_system.config.get("enabled", True):
            return initial_result
        
        # Run improvement pipeline
        try:
            improvement_result = self.improvement_pipeline.improve_report(
                initial_result["answer"],
                initial_result.get("sources", []),
                query
            )
            
            # Add QA information to result
            result = initial_result.copy()
            result.update({
                "qa_enabled": True,
                "qa_status": improvement_result["status"],
                "original_answer": improvement_result["original_report"],
                "answer": improvement_result["improved_report"],
                "qa_results": improvement_result.get("final_qa", improvement_result.get("qa_results")),
                "improvements_made": improvement_result.get("improvements_made", []),
                "score_improvement": improvement_result.get("score_improvement", 0.0)
            })
            
            return result
            
        except Exception as e:
            print(f"Error in QA improvement pipeline: {e}")
            # Return original result if QA fails
            initial_result["qa_enabled"] = False
            initial_result["qa_error"] = str(e)
            return initial_result
    
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
        expected_answer_type = "synthesized_answer"
        comparison_items = []
        
        if any(phrase in query_lower for phrase in ["how to", "best way", "steps for"]):
            intent_type = "instruction_seeking"
            expected_answer_type = "step_by_step_guide"
        elif expanded_query['query_parts'] and any(p['type'] == 'comparison' for p in expanded_query['query_parts']):
            intent_type = "comparison_seeking"
            expected_answer_type = "comparison_table"
            # Extract comparison items from query parts
            for part in expanded_query['query_parts']:
                if part['type'] == 'comparison' and 'items' in part:
                    comparison_items = part['items']
                    break
        elif any(phrase in query_lower for phrase in ["why isn't", "what went wrong", "fix", "troubleshoot"]):
            intent_type = "troubleshooting"
            expected_answer_type = "troubleshooting_guide"
        elif any(phrase in query_lower for phrase in ["find all", "show me", "list"]):
            intent_type = "discovery"
            expected_answer_type = "content_list"
        
        result = {
            "intent_type": intent_type,
            "key_entities": [],
            "key_concepts": [],
            "context_filters": {},
            "expected_answer_type": expected_answer_type,
            "confidence": 0.5,
            "expanded_query": expanded_query
        }
        
        # Add comparison items if found
        if comparison_items:
            result["comparison_items"] = comparison_items
            
        return result
    
    def calculate_search_score(self, query_data: Dict, content_data: Dict) -> float:
        """
        Calculate relevance score using multiple factors including phrase proximity and structure
        """
        score = 0.0
        
        # Safely get title and body with defaults
        title_lower = content_data.get('title', '').lower()
        body_lower = content_data.get('body', '').lower()
        
        # Parse markdown structure if not already done
        if 'structure' not in content_data:
            content_data['structure'] = self._parse_markdown_structure(content_data.get('body', ''))
        
        structure = content_data.get('structure', {})
        if not structure:
            structure = {'headers': [], 'summary': '', 'key_points': [], 'sections': {}}
        
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
            
            # NEW: Structure-aware scoring
            # Summary matches (high value)
            if structure.get('summary'):
                summary_lower = structure['summary'].lower()
                summary_matches = sum(1 for term in all_terms if term in summary_lower)
                if summary_matches:
                    score += (summary_matches / len(all_terms)) * 4.0  # 2x multiplier
            
            # Header matches (medium-high value)
            for header in structure.get('headers', []):
                header_lower = header['text'].lower()
                header_matches = sum(1 for term in all_terms if term in header_lower)
                if header_matches:
                    # Higher level headers get more weight
                    header_weight = 3.0 / header['level']  # H1=3.0, H2=1.5, H3=1.0
                    score += (header_matches / len(all_terms)) * header_weight
            
            # Key points matches (high value)
            for key_point in structure.get('key_points', []):
                key_point_lower = key_point.lower()
                kp_matches = sum(1 for term in all_terms if term in key_point_lower)
                if kp_matches:
                    score += (kp_matches / len(all_terms)) * 3.6  # 1.8x multiplier
        
        # NEW: Phrase proximity scoring
        proximity_score = self._calculate_proximity_score(query_data.get('tokens', []), body_lower)
        score += proximity_score
        
        # Boost for entity/concept matches
        entities = set(content_data.get('frontmatter', {}).get('entities', []))
        concepts = set(content_data.get('frontmatter', {}).get('concepts', []))
        
        for term in all_terms:
            if any(term in entity.lower() for entity in entities):
                score += 2.0
            if any(term in concept.lower() for concept in concepts):
                score += 1.5
        
        return score
    
    def _calculate_proximity_score(self, query_tokens: List[str], text: str) -> float:
        """
        Calculate proximity bonus based on how close query terms appear to each other
        Using efficient sliding window approach instead of exponential combinations
        """
        if len(query_tokens) < 2 or not text:
            return 0.0
        
        # Find all positions of query tokens in text
        token_positions = {}
        for token in query_tokens:
            positions = []
            start = 0
            while True:
                pos = text.find(token, start)
                if pos == -1:
                    break
                positions.append(pos)
                start = pos + 1
            if positions:
                token_positions[token] = positions
        
        # If not all tokens found, no proximity bonus
        if len(token_positions) < len(query_tokens):
            return 0.0
        
        # Use a more efficient approach: find the minimum window containing all terms
        # Instead of checking all combinations, use a sliding window approach
        
        # Create a list of all positions with their token
        all_positions = []
        for token in query_tokens:
            for pos in token_positions.get(token, []):
                all_positions.append((pos, token))
        
        # Sort by position
        all_positions.sort()
        
        # Find minimum window containing all unique tokens
        min_span = float('inf')
        left = 0
        token_count = {}
        unique_tokens_in_window = 0
        
        for right in range(len(all_positions)):
            pos, token = all_positions[right]
            
            # Add token to window
            if token not in token_count:
                token_count[token] = 0
            token_count[token] += 1
            if token_count[token] == 1:
                unique_tokens_in_window += 1
            
            # Try to shrink window from left
            while unique_tokens_in_window == len(query_tokens):
                # Calculate span
                span = all_positions[right][0] - all_positions[left][0]
                min_span = min(min_span, span)
                
                # Remove leftmost token
                left_pos, left_token = all_positions[left]
                token_count[left_token] -= 1
                if token_count[left_token] == 0:
                    unique_tokens_in_window -= 1
                left += 1
        
        # Calculate proximity bonus
        # Closer terms get higher bonus (normalized by 100 chars)
        if min_span < float('inf'):
            proximity_bonus = 2.0 / (1 + min_span / 100)
            return proximity_bonus
        
        return 0.0
    
    def search_content(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """
        Enhanced search with query expansion and better scoring using inverted index
        """
        query_intent = self.parse_query_intent(query)
        expanded_query = query_intent.get('expanded_query', self.expand_query(query))
        
        results = []
        
        # Use inverted index to get candidate documents
        candidate_docs = self._search_with_index(expanded_query['all_search_terms'])
        
        # If no candidates from index, fall back to full search
        if not candidate_docs:
            candidate_docs = set(self.content_index.keys())
        
        # Score only candidate documents
        for file_key in candidate_docs:
            if file_key not in self.content_index:
                continue
                
            content_data = self.content_index[file_key]
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
    
    def synthesize_answer(self, query: str, search_results: List[Dict[str, Any]], use_structured_report: bool = True) -> Dict[str, Any]:
        """
        Use LLM to synthesize an answer from clustered search results with optional structured report
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

        # If structured report is requested, generate it
        if use_structured_report:
            query_intent = self.parse_query_intent(query)
            outline = self._generate_report_outline(query, search_results, query_intent)
            
            # Generate structured report
            structured_answer = self._generate_structured_report(query, search_results, outline, context_pieces)
            if structured_answer:
                return structured_answer

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