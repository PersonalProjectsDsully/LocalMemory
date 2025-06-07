"""
Document analysis and search functionality for research workflow
"""

import hashlib
from typing import Dict, List, Any
from datetime import datetime

from ..llm.robust_json_parser import parse_llm_json
from .workflow_tracker import workflow_tracker
from ..session.progress_reporter import report_progress


class DocumentAnalyzer:
    """Handles document search and analysis for research workflow"""
    
    def __init__(self, search_engine, llm_provider):
        self.search_engine = search_engine
        self.llm_provider = llm_provider
    
    def search_documents(self, keywords: Dict) -> List[Dict]:
        """Search for documents using keywords"""
        # Track document search
        workflow_tracker.track_operation('document_search', {
            'primary_keywords': keywords.get('primary_keywords', []),
            'secondary_keywords': keywords.get('secondary_keywords', [])
        })
        
        # Report progress
        report_progress(f"Searching documents with {len(keywords.get('primary_keywords', []))} primary keywords")
        
        all_results = []
        
        # Search with primary keywords
        for i, keyword in enumerate(keywords.get('primary_keywords', [])):
            report_progress(f"Searching for: {keyword} ({i+1}/{len(keywords.get('primary_keywords', []))})")
            results_list = self.search_engine.search_content(keyword)
            all_results.extend(results_list)
        
        # Search with secondary keywords if not enough results
        if len(all_results) < 5:
            for keyword in keywords.get('secondary_keywords', []):
                results_list = self.search_engine.search_content(keyword)
                all_results.extend(results_list)
        
        # Search with keyword combinations
        for combination in keywords.get('keyword_combinations', []):
            query = ' '.join(combination)
            results_list = self.search_engine.search_content(query)
            all_results.extend(results_list)
        
        # Remove duplicates and filter
        unique_results = self._deduplicate_results(all_results, keywords.get('exclusion_keywords', []))
        
        return unique_results
    
    def _deduplicate_results(self, all_results: List[Dict], exclusion_keywords: List[str]) -> List[Dict]:
        """Remove duplicates and filter results"""
        # Pre-compile exclusion keywords for efficiency
        exclusion_keywords = [excl.lower() for excl in exclusion_keywords if excl]
        
        # Use content hashing for O(n) deduplication
        seen_hashes = set()
        seen_paths = set()
        unique_results = []
        
        for result in all_results:
            if not isinstance(result, dict):
                continue
            
            # Extract content efficiently
            content_text = ''
            if 'content' in result:
                if isinstance(result['content'], dict):
                    content_text = result['content'].get('body', '')
                else:
                    content_text = str(result.get('content', ''))
            
            # Create a content hash for deduplication
            file_path = result.get('file_path', '')
            content_hash = hashlib.md5(f"{file_path}:{content_text}".encode()).hexdigest()
            
            # Skip if we've seen this exact content before
            if content_hash in seen_hashes:
                continue
            
            # Skip if we've seen this file path (but different content)
            if file_path and file_path in seen_paths:
                continue
            
            # Check exclusion keywords (only on unique content)
            if exclusion_keywords and content_text:
                content_lower = content_text.lower()
                if any(keyword in content_lower for keyword in exclusion_keywords):
                    continue
            
            # Mark as seen
            seen_hashes.add(content_hash)
            if file_path:
                seen_paths.add(file_path)
            
            # Process and add the unique result
            result_data = self._process_result(result, content_text, file_path)
            unique_results.append(result_data)
        
        return unique_results
    
    def _process_result(self, result: Dict, content_text: str, file_path: str) -> Dict:
        """Process a search result into standard format"""
        if 'content' in result and isinstance(result['content'], dict):
            content_dict = result['content']
            result_data = {
                'file_path': result.get('file_key', result.get('file_path', file_path)),
                'title': content_dict.get('title', 'Unknown'),
                'category': content_dict.get('category', 'Unknown'),
                'content': content_text,
                'body': content_text,
                'score': result.get('score', 0)
            }
            # Safely merge other content fields
            for key, value in content_dict.items():
                if key not in result_data and value is not None:
                    result_data[key] = value
        else:
            # Fallback for simple content structure
            result_data = {
                'file_path': file_path,
                'title': result.get('title', 'Unknown'),
                'category': result.get('category', 'Unknown'),
                'content': content_text,
                'body': content_text,
                'score': result.get('score', 0)
            }
            # Merge any other fields
            for key, value in result.items():
                if key not in result_data and value is not None:
                    result_data[key] = value
        
        return result_data
    
    def analyze_documents(self, documents: List[Dict], subtask: Dict) -> Dict[str, Any]:
        """Deeply analyze documents for subtask relevance"""
        if not documents:
            # When no documents found, generate insights from general knowledge
            return self._generate_fallback_analysis(subtask)
        
        analysis_prompt = f"""
        Analyze the following documents for information relevant to this subtask:
        
        Subtask: {subtask['title']}
        Objective: {subtask['objective']}
        
        Documents:
        {self._format_documents_for_analysis(documents[:5])}  # Limit to top 5
        
        For each document:
        1. Extract key information relevant to the subtask
        2. Note important insights, examples, or data
        3. Identify connections between documents
        4. Rate relevance (1-10)
        
        Format as JSON:
        {{
            "document_analyses": [
                {{
                    "document_title": "...",
                    "relevance_score": 1-10,
                    "key_information": ["..."],
                    "insights": ["..."],
                    "quotes": ["..."],
                    "connections": ["..."]
                }}
            ],
            "synthesis": "...",
            "sufficiency": "sufficient|partial|insufficient",
            "missing_information": ["..."]
        }}
        """
        
        return parse_llm_json(self.llm_provider.generate(analysis_prompt), 'document_analysis')
    
    def _generate_fallback_analysis(self, subtask: Dict) -> Dict[str, Any]:
        """Generate analysis when no documents are found"""
        fallback_prompt = f"""
        No documents were found in the knowledge base for this research task:
        
        Task: {subtask['title']}
        Objective: {subtask['objective']}
        
        Based on general knowledge about this topic, provide:
        1. Key concepts and definitions
        2. General insights about the topic
        3. Common approaches or solutions
        4. What specific information would be valuable to find
        
        Format as JSON:
        {{
            "document_analyses": [
                {{
                    "document_title": "General Knowledge Synthesis",
                    "relevance_score": 5,
                    "key_information": ["..."],
                    "insights": ["..."],
                    "quotes": [],
                    "connections": []
                }}
            ],
            "synthesis": "...",
            "sufficiency": "partial",
            "missing_information": ["..."]
        }}
        """
        
        return parse_llm_json(self.llm_provider.generate(fallback_prompt), 'document_analysis')
    
    def _format_documents_for_analysis(self, documents: List[Dict]) -> str:
        """Format documents for LLM analysis with proper error handling"""
        if not documents:
            return "No documents to analyze"
        
        formatted = []
        for i, doc in enumerate(documents):
            if not isinstance(doc, dict):
                continue
            
            # Handle both direct content and nested content structure with safe access
            try:
                if 'content' in doc and isinstance(doc['content'], dict):
                    content = doc['content']
                    title = str(content.get('title', 'Unknown'))
                    category = str(content.get('category', 'Unknown'))
                    body = str(content.get('body', ''))[:500]
                else:
                    title = str(doc.get('title', 'Unknown'))
                    category = str(doc.get('category', 'Unknown'))
                    # Try multiple keys for body content
                    body = str(doc.get('body', doc.get('content', doc.get('text', ''))))[:500]
                
                # Ensure we have some content
                if not body and 'summary' in doc:
                    body = str(doc.get('summary', ''))[:500]
                
                formatted.append(f"""
            Document {i+1}:
            Title: {title}
            Category: {category}
            Excerpt: {body}...
            """)
            except Exception as e:
                print(f"Error formatting document {i}: {e}")
                formatted.append(f"Document {i+1}: Error formatting - {str(e)}")
        
        return '\n'.join(formatted) if formatted else "No valid documents to analyze"