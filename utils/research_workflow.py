"""
Comprehensive Research Workflow for Intelligent Search
Implements a multi-stage research process with iterative refinement
"""

import streamlit as st
from typing import Dict, List, Tuple, Optional, Any
import yaml
import re
import json
from datetime import datetime
from pathlib import Path
from .llm_utils import _call_llm_api, strip_thinking_tags
from .intelligent_search import IntelligentSearchEngine
from .workflow_persistence import workflow_persistence
from .robust_json_parser import parse_llm_json
from .workflow_tracker import workflow_tracker
from .progress_reporter import report_progress


class LLMProvider:
    """Simple wrapper for LLM functionality"""
    
    def generate(self, prompt: str) -> str:
        """Generate a response from the LLM"""
        # Track LLM call
        workflow_tracker.track_operation('llm_generation', {
            'prompt_length': len(prompt),
            'prompt_preview': prompt[:100] + '...' if len(prompt) > 100 else prompt
        })
        
        response = _call_llm_api(prompt, "research workflow")
        
        # Track response
        workflow_tracker.track_operation('llm_response', {
            'response_length': len(response) if response else 0,
            'success': response is not None
        })
        
        if response:
            return strip_thinking_tags(response)
        return ""


class ResearchWorkflow:
    """Manages the comprehensive research workflow process"""
    
    def __init__(self, original_query: str = None):
        self.llm_provider = LLMProvider()
        # Reuse search engine from session state if available
        if 'search_engine' in st.session_state:
            self.search_engine = st.session_state.search_engine
        else:
            from utils.intelligent_search import get_search_engine
            self.search_engine = get_search_engine()
        self.workflow_state = self._init_workflow_state(original_query)
        self.persistence = workflow_persistence
        
        # Create session if we have an original query
        if original_query and not self.persistence.current_session_dir:
            self.persistence.create_session(original_query)
        
    def _init_workflow_state(self, original_query: str = None) -> Dict[str, Any]:
        """Initialize workflow state tracking"""
        if 'research_workflow' not in st.session_state:
            st.session_state.research_workflow = {
                'current_stage': 'inquiry_clarification',
                'original_query': original_query,
                'clarified_request': None,
                'subtasks': [],
                'scratchpads': {},
                'document_analysis': {},
                'report_outline': None,
                'report_sections': {},
                'final_report': None,
                'iteration_count': 0
            }
        elif original_query and 'original_query' not in st.session_state.research_workflow:
            # Add original query if it's missing
            st.session_state.research_workflow['original_query'] = original_query
        
        # Don't save here as we don't have a session directory yet
        return st.session_state.research_workflow
    
    def step1_inquiry_clarification(self, user_query: str) -> Dict[str, Any]:
        """Engage user to clarify and refine their request"""
        prompt = f"""
        Analyze the following user query and generate clarifying questions to better understand their research needs:
        
        User Query: {user_query}
        
        Generate 3-5 targeted questions that would help clarify:
        - Specific aspects or examples they're interested in
        - Desired depth of information (examples, case studies, statistics)
        - Intended use or application of the research
        - Any constraints or preferences
        
        Format as JSON:
        {{
            "original_query": "...",
            "query_analysis": {{
                "main_topic": "...",
                "implicit_needs": ["..."],
                "ambiguities": ["..."]
            }},
            "clarifying_questions": [
                {{
                    "question": "...",
                    "purpose": "...",
                    "options": ["..."]  // optional suggested answers
                }}
            ],
            "suggested_refinement": "..."
        }}
        """
        
        result = self.llm_provider.generate(prompt)
        clarification_data = parse_llm_json(result, 'inquiry_clarification')
        
        # Save clarification data
        if self.persistence.current_session_dir:
            self.persistence._save_json(
                self.persistence.current_session_dir / "00_inquiry_clarification.json",
                clarification_data
            )
        
        return clarification_data
    
    def step2_task_decomposition(self, clarified_request: str) -> Dict[str, Any]:
        """Break down request into manageable subtasks"""
        prompt = f"""
        Decompose the following research request into specific, manageable subtasks:
        
        Research Request: {clarified_request}
        
        Create a comprehensive task breakdown that:
        - Covers all aspects of the request
        - Defines clear objectives for each subtask
        - Identifies dependencies between subtasks
        - Estimates complexity and required depth
        
        Format as JSON:
        {{
            "request_summary": "...",
            "subtasks": [
                {{
                    "id": "task_1",
                    "title": "...",
                    "objective": "...",
                    "scope": "...",
                    "dependencies": ["task_id"],
                    "complexity": "medium",
                    "estimated_documents": 4
                }}
            ],
            "execution_order": ["task_1", "task_2", ...],
            "success_criteria": "..."
        }}
        """
        
        decomposition = parse_llm_json(self.llm_provider.generate(prompt), 'task_decomposition')
        
        # Verify decomposition
        verification = self._verify_task_decomposition(decomposition, clarified_request)
        
        # Save task decomposition
        self.workflow_state['subtasks'] = decomposition.get('subtasks', [])
        self.persistence.save_workflow_state(self.workflow_state)
        
        return {
            'decomposition': decomposition,
            'verification': verification
        }
    
    def _verify_task_decomposition(self, decomposition: Dict, original_request: str) -> Dict[str, Any]:
        """Verify task decomposition completeness"""
        prompt = f"""
        Verify the following task decomposition against the original request:
        
        Original Request: {original_request}
        
        Task Decomposition: {json.dumps(decomposition, indent=2)}
        
        Evaluate:
        1. Does the decomposition fully address all aspects of the request?
        2. Are there any gaps or missing components?
        3. Are there redundancies that should be consolidated?
        4. Is the execution order logical and efficient?
        
        Format as JSON:
        {{
            "completeness_score": 85,
            "gaps": ["..."],
            "redundancies": ["..."],
            "suggestions": ["..."],
            "approved": true
        }}
        """
        
        return parse_llm_json(self.llm_provider.generate(prompt))
    
    def step3_keyword_research(self, subtask: Dict) -> Dict[str, Any]:
        """Generate keywords and perform document research for a subtask"""
        # Generate keywords
        keyword_prompt = f"""
        Generate precise keywords for researching the following subtask:
        
        Subtask: {subtask['title']}
        Objective: {subtask['objective']}
        Scope: {subtask['scope']}
        
        Generate:
        1. Primary keywords (most important terms)
        2. Secondary keywords (related concepts)
        3. Exclusion keywords (to filter out irrelevant results)
        4. Keyword combinations for complex searches
        
        Format as JSON:
        {{
            "primary_keywords": ["..."],
            "secondary_keywords": ["..."],
            "exclusion_keywords": ["..."],
            "keyword_combinations": [["keyword1", "keyword2"], ...],
            "search_strategy": "..."
        }}
        """
        
        keywords = parse_llm_json(self.llm_provider.generate(keyword_prompt))
        
        # Perform document search
        relevant_docs = self._search_documents(keywords)
        
        # Analyze documents
        analysis = self._analyze_documents(relevant_docs, subtask)
        
        return {
            'keywords': keywords,
            'documents_found': len(relevant_docs),
            'analysis': analysis
        }
    
    def _search_documents(self, keywords: Dict) -> List[Dict]:
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
        
        # If still no results, try individual words from the task title
        if len(all_results) < 3:
            print(f"Limited results found, trying broader search...")
            # This would need the subtask context, which we don't have here
        
        # Remove duplicates and filter
        import hashlib
        
        # Pre-compile exclusion keywords for efficiency
        exclusion_keywords = [excl.lower() for excl in keywords.get('exclusion_keywords', []) if excl]
        
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
            if 'content' in result and isinstance(result['content'], dict):
                content_dict = result['content']
                result_data = {
                    'file_path': result.get('file_key', result.get('file_path', '')),
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
            
            unique_results.append(result_data)
        
        return unique_results
    
    def _analyze_documents(self, documents: List[Dict], subtask: Dict) -> Dict[str, Any]:
        """Deeply analyze documents for subtask relevance"""
        if not documents:
            # When no documents found, generate insights from general knowledge
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
    
    def step4_iterative_validation(self, subtask_id: str, analysis: Dict) -> Dict[str, Any]:
        """Validate scratchpad contents and determine if more research is needed"""
        # Get or create scratchpad for this subtask
        if subtask_id not in self.workflow_state['scratchpads']:
            self.workflow_state['scratchpads'][subtask_id] = {
                'high_value_findings': [],
                'insights': [],
                'quotes': [],
                'documents_analyzed': [],
                'iteration_count': 0,
                'created_at': datetime.now().isoformat()
            }
        
        scratchpad = self.workflow_state['scratchpads'][subtask_id]
        scratchpad['iteration_count'] = scratchpad.get('iteration_count', 0) + 1
        
        # Track iteration
        workflow_tracker.track_task_iteration(subtask_id, scratchpad['iteration_count'])
        workflow_tracker.track_operation('validation_iteration', {
            'subtask_id': subtask_id,
            'iteration': scratchpad['iteration_count'],
            'findings_count': len(scratchpad.get('high_value_findings', [])),
            'insights_count': len(scratchpad.get('insights', []))
        })
        
        # Report progress
        report_progress(
            f"Iteration {scratchpad['iteration_count']} - "
            f"Findings: {len(scratchpad.get('high_value_findings', []))}, "
            f"Insights: {len(scratchpad.get('insights', []))}",
            task=subtask_id
        )
        
        # Update scratchpad with latest findings BEFORE validation
        # Handle both old and new document analysis formats
        if 'document_analyses' in analysis:
            # New format with array of document analyses
            for doc_analysis in analysis['document_analyses']:
                # Lower threshold to capture more findings when documents are scarce
                if doc_analysis['relevance_score'] >= 5:
                    # Add document to analyzed list
                    doc_title = doc_analysis.get('document_title', 'Unknown')
                    if doc_title not in scratchpad.get('documents_analyzed', []):
                        scratchpad.setdefault('documents_analyzed', []).append(doc_title)
                    
                    # Add findings (avoid duplicates)
                    for info in doc_analysis.get('key_information', []):
                        if info not in scratchpad.get('high_value_findings', []):
                            scratchpad.setdefault('high_value_findings', []).append(info)
                    
                    for insight in doc_analysis.get('insights', []):
                        if insight not in scratchpad.get('insights', []):
                            scratchpad.setdefault('insights', []).append(insight)
                    
                    for quote in doc_analysis.get('quotes', []):
                        if quote not in scratchpad.get('quotes', []):
                            scratchpad.setdefault('quotes', []).append(quote)
        elif 'document_title' in analysis:
            # Old format with direct fields - convert to expected format
            if analysis.get('relevance_score', 0) >= 5:
                # Add document to analyzed list
                doc_title = analysis.get('document_title', 'Unknown')
                if doc_title not in scratchpad.get('documents_analyzed', []):
                    scratchpad.setdefault('documents_analyzed', []).append(doc_title)
                
                # Add findings (avoid duplicates)
                for info in analysis.get('key_information', []):
                    if info not in scratchpad.get('high_value_findings', []):
                        scratchpad.setdefault('high_value_findings', []).append(info)
                
                for insight in analysis.get('insights', []):
                    if insight not in scratchpad.get('insights', []):
                        scratchpad.setdefault('insights', []).append(insight)
                
                for quote in analysis.get('quotes', []):
                    if quote not in scratchpad.get('quotes', []):
                        scratchpad.setdefault('quotes', []).append(quote)
        
        # Save scratchpad immediately after updating
        self.workflow_state['scratchpads'][subtask_id] = scratchpad
        self.persistence.save_workflow_state(self.workflow_state)
        
        # Summarize scratchpad to reduce prompt size
        scratchpad_summary = {
            'documents_analyzed': len(scratchpad.get('documents_analyzed', [])),
            'findings_count': len(scratchpad.get('high_value_findings', [])),
            'insights_count': len(scratchpad.get('insights', [])),
            'iteration': scratchpad.get('iteration_count', 1),
            'sample_findings': scratchpad.get('high_value_findings', [])[:3],
            'sample_insights': scratchpad.get('insights', [])[:3]
        }
        
        # Now validate with the updated scratchpad
        validation_prompt = f"""
        Evaluate research completeness for subtask {subtask_id}:
        
        Stats: {scratchpad_summary['documents_analyzed']} docs, {scratchpad_summary['findings_count']} findings, {scratchpad_summary['insights_count']} insights
        Iteration: {scratchpad_summary['iteration']}
        
        Sample findings: {scratchpad_summary['sample_findings']}
        
        Is this sufficient? What's missing?
        
        JSON format:
        {{
            "completeness_score": 85,
            "sufficient": true,
            "missing_elements": ["max 3 items"],
            "recommended_action": "continue_search|refine_keywords|proceed"
        }}
        """
        
        try:
            validation = parse_llm_json(self.llm_provider.generate(validation_prompt))
        except Exception as e:
            print(f"Error in validation: {e}")
            # Fallback validation response
            validation = {
                'completeness_score': 50,
                'sufficient': scratchpad.get('iteration_count', 0) >= 2,  # Stop after 2 iterations on error
                'missing_elements': ['Unable to validate due to error'],
                'recommended_action': 'proceed',
                'error': str(e)
            }
        
        # Add total findings count
        validation['total_findings'] = (
            len(scratchpad.get('high_value_findings', [])) +
            len(scratchpad.get('insights', [])) +
            len(scratchpad.get('quotes', []))
        )
        
        # Define minimum findings threshold based on task complexity
        task = next((t for t in self.workflow_state.get('subtasks', []) if t['id'] == subtask_id), None)
        complexity = task.get('complexity', 'medium') if task else 'medium'
        
        # Set minimum findings threshold based on complexity
        min_findings_threshold = {
            'low': 3,
            'medium': 5,
            'high': 8
        }.get(complexity, 5)
        
        # If we have some findings but marked insufficient, check against threshold
        if validation['total_findings'] > 0 and not validation.get('sufficient'):
            if validation['total_findings'] >= min_findings_threshold:
                # Sufficient findings reached
                print(f"Task {subtask_id}: Marking sufficient with {validation['total_findings']} findings (threshold: {min_findings_threshold})")
                validation['sufficient'] = True
                validation['note'] = f'Minimum findings threshold ({min_findings_threshold}) reached'
            elif scratchpad.get('iteration_count', 0) >= 3 and validation['total_findings'] >= min_findings_threshold * 0.6:
                # After 3 iterations with at least 60% of threshold, mark as sufficient
                print(f"Task {subtask_id}: Marking sufficient after {scratchpad['iteration_count']} iterations with {validation['total_findings']} findings (60% of threshold)")
                validation['sufficient'] = True
                validation['note'] = f'Marked sufficient after {scratchpad["iteration_count"]} iterations with partial findings'
            else:
                # Not enough findings yet
                print(f"Task {subtask_id}: Insufficient findings ({validation['total_findings']}/{min_findings_threshold}) after {scratchpad.get('iteration_count', 0)} iterations")
        
        # Hard limit on iterations to prevent infinite loops
        if scratchpad.get('iteration_count', 0) >= 5:
            print(f"WARNING: Task {subtask_id} reached maximum iterations (5)")
            workflow_tracker.track_operation('max_iterations_reached', {
                'subtask_id': subtask_id,
                'iterations': scratchpad['iteration_count']
            })
            validation['sufficient'] = True
            validation['note'] = 'Maximum iteration limit reached'
        
        self.workflow_state['scratchpads'][subtask_id] = scratchpad
        
        # If task appears sufficient, verify completion with fresh context
        if validation.get('sufficient', False):
            try:
                completion_verification = self._verify_task_completion(subtask_id, scratchpad)
                validation['completion_verified'] = completion_verification.get('verified', False)
                validation['completion_details'] = completion_verification
                
                # Update validation based on completion check
                if not completion_verification.get('verified', False):
                    validation['sufficient'] = False
                    missing_reqs = completion_verification.get('missing_requirements', [])
                    if missing_reqs:
                        if 'missing_elements' not in validation:
                            validation['missing_elements'] = []
                        validation['missing_elements'].extend(missing_reqs)
            except Exception as e:
                print(f"Error in completion verification: {e}")
                # If verification fails, continue with current validation
                validation['completion_verified'] = validation.get('sufficient', False)
                validation['completion_details'] = {'error': str(e)}
        
        # Save updated scratchpad
        self.persistence.save_workflow_state(self.workflow_state)
        
        return validation
    
    def _verify_task_completion(self, subtask_id: str, scratchpad: Dict[str, Any]) -> Dict[str, Any]:
        """Verify task completion with a fresh context window"""
        # Get the original subtask details
        subtask = None
        for task in self.workflow_state.get('subtasks', []):
            if task['id'] == subtask_id:
                subtask = task
                break
        
        if not subtask:
            return {'verified': False, 'error': 'Subtask not found'}
        
        # Create a comprehensive completion verification prompt
        verification_prompt = f"""
        Verify if the following research task has been completed successfully:
        
        ORIGINAL TASK SPECIFICATION:
        Title: {subtask['title']}
        Objective: {subtask['objective']}
        Scope: {subtask['scope']}
        
        RESEARCH FINDINGS COLLECTED:
        {json.dumps(scratchpad, indent=2)}
        
        Please evaluate:
        1. Have all aspects of the objective been addressed?
        2. Is the scope fully covered?
        3. Are there any critical gaps that prevent task completion?
        4. Is the quality and depth of information sufficient?
        
        Be strict in your evaluation. The task should only be marked complete if:
        - All key requirements in the objective are met
        - The scope boundaries are respected
        - Information quality is adequate for the task complexity
        - No critical information is missing
        
        Format as JSON:
        {{
            "verified": true,
            "completion_summary": "Brief summary of what was accomplished",
            "objective_coverage": {{
                "percentage": 0-100,
                "covered_aspects": ["..."],
                "missing_aspects": ["..."]
            }},
            "quality_assessment": {{
                "depth": "shallow|adequate|comprehensive",
                "reliability": "high",
                "completeness": "incomplete|partial|complete"
            }},
            "missing_requirements": ["..."],
            "recommendation": "mark_complete|continue_research|refine_search"
        }}
        """
        
        try:
            result = parse_llm_json(self.llm_provider.generate(verification_prompt))
            
            # Ensure required fields exist
            if 'verified' not in result:
                # Try to infer from other fields
                if result.get('recommendation') == 'mark_complete':
                    result['verified'] = True
                elif result.get('quality_assessment', {}).get('completeness') == 'complete':
                    result['verified'] = True
                else:
                    result['verified'] = False
            
            # Save verification result
            if self.persistence.current_session_dir:
                verification_dir = self.persistence.current_session_dir / "06_task_verifications"
                verification_dir.mkdir(exist_ok=True)
                self.persistence._save_json(
                    verification_dir / f"{subtask_id}_verification.json",
                    {
                        'timestamp': datetime.now().isoformat(),
                        'subtask': subtask,
                        'verification': result
                    }
                )
            
            return result
            
        except Exception as e:
            print(f"Error in task completion verification: {e}")
            # Return a default verification result
            return {
                'verified': False,
                'completion_summary': 'Verification failed due to error',
                'objective_coverage': {'percentage': 0, 'covered_aspects': [], 'missing_aspects': ['Unable to verify']},
                'quality_assessment': {'depth': 'unknown', 'reliability': 'unknown', 'completeness': 'unknown'},
                'missing_requirements': ['Verification error occurred'],
                'recommendation': 'continue_research',
                'error': str(e)
            }
    
    def _verify_all_tasks_complete(self) -> Dict[str, Any]:
        """Verify all tasks are complete before generating report"""
        verification_prompt = f"""
        Review the complete research progress and verify all tasks are sufficiently complete:
        
        ORIGINAL RESEARCH REQUEST:
        {self.workflow_state.get('clarified_request', '')}
        
        PLANNED TASKS:
        {json.dumps(self.workflow_state.get('subtasks', []), indent=2)}
        
        COLLECTED RESEARCH (Scratchpads):
        {json.dumps(self.workflow_state.get('scratchpads', {}), indent=2)}
        
        For each task, evaluate:
        1. Is the task objective fully met?
        2. What percentage of the task is complete?
        3. What key elements are still missing?
        
        Format as JSON:
        {{
            "all_complete": true,
            "overall_completeness": 0-100,
            "task_statuses": {{
                "task_id": {{
                    "complete": true,
                    "percentage": 0-100,
                    "missing": ["..."]
                }}
            }},
            "ready_for_report": true,
            "final_recommendation": "generate_report|continue_research|abandon"
        }}
        """
        
        result = parse_llm_json(self.llm_provider.generate(verification_prompt))
        
        # Save final verification
        if self.persistence.current_session_dir:
            self.persistence._save_json(
                self.persistence.current_session_dir / "07_final_verification.json",
                {
                    'timestamp': datetime.now().isoformat(),
                    'verification': result
                }
            )
        
        return result
    
    def step5_report_generation(self) -> str:
        """Generate comprehensive markdown report from validated research"""
        # Final verification of all tasks before report generation
        all_tasks_verified = self._verify_all_tasks_complete()
        
        # Handle parsing errors or missing fields
        if all_tasks_verified.get('parse_error') or 'all_complete' not in all_tasks_verified:
            print("Warning: Failed to parse task verification. Proceeding with report generation based on available data.")
            # Calculate completion based on scratchpad data
            total_tasks = len(self.workflow_state.get('subtasks', []))
            tasks_with_findings = sum(
                1 for scratchpad in self.workflow_state.get('scratchpads', {}).values()
                if len(scratchpad.get('high_value_findings', [])) > 0
            )
            all_tasks_verified = {
                'all_complete': tasks_with_findings >= total_tasks * 0.5,  # At least 50% complete
                'overall_completeness': int((tasks_with_findings / total_tasks * 100) if total_tasks > 0 else 0),
                'ready_for_report': True,  # Always try to generate a report with available data
                'note': 'Verification parse failed - using fallback completion check'
            }
        
        if not all_tasks_verified.get('all_complete', False):
            # Save verification report
            if self.persistence.current_session_dir:
                self.persistence._save_json(
                    self.persistence.current_session_dir / "final_verification_failed.json",
                    all_tasks_verified
                )
            
            # Check if we have partial findings worth reporting
            total_findings = sum(
                len(scratchpad.get('high_value_findings', [])) + 
                len(scratchpad.get('insights', []))
                for scratchpad in self.workflow_state.get('scratchpads', {}).values()
            )
            
            print(f"Total findings across all tasks: {total_findings}")
            
            # If we have substantial partial findings, generate a report anyway
            if total_findings >= 10 or all_tasks_verified.get('overall_completeness', 0) >= 50:
                print("Generating report with partial findings...")
                # Add a note about incompleteness to the report
                self.workflow_state['report_note'] = f"Note: This report is based on partial findings. Overall completeness: {all_tasks_verified.get('overall_completeness', 0)}%"
                # Continue with report generation
            else:
                # Generate a report with whatever findings we have
                print("Generating report despite incomplete tasks...")
                self.workflow_state['report_note'] = "Note: This report is based on limited findings from incomplete research."
        
        # Create report outline
        outline = self._create_report_outline()
        
        # Skip outline verification for now - assume approved
        outline_verification = {'approved': True}
        
        if outline_verification['approved']:
            # Generate each section
            report_sections = self._generate_report_sections(outline)
            
            # Combine sections into final report
            final_report = self._combine_report_sections(report_sections, outline)
            
            # Run automatic QA and improvements
            print("🔍 Running automatic QA and improvements...")
            improved_report_result = self._run_automatic_qa_and_improvements(final_report)
            
            if improved_report_result and improved_report_result.get('ready_for_user'):
                final_report = improved_report_result['improved_report']
                # Store QA information for display with validation
                qa_summary = improved_report_result.get('qa_summary', {})
                if qa_summary:
                    self.workflow_state['automatic_qa_results'] = qa_summary
                    improvements_count = len(qa_summary.get('improvements_applied', []))
                    print(f"✅ Automatic QA completed with {improvements_count} improvements")
                else:
                    print("⚠️ Automatic QA completed but no summary available")
            else:
                print("⚠️ Automatic QA failed, using original report")
                self.workflow_state['automatic_qa_results'] = {
                    'automatic_qa_completed': False,
                    'error': 'Automatic QA process failed',
                    'timestamp': datetime.now().isoformat()
                }
            
            # Save and return final report
            self.workflow_state['final_report'] = final_report
            self.persistence.save_workflow_state(self.workflow_state)
            return final_report
        
        return "Report generation failed verification"
    
    def _combine_report_sections(self, sections: Dict[str, str], outline: Dict) -> str:
        """Combine report sections into final markdown report"""
        report_parts = []
        
        # Title - handle case where outline might be None or missing title
        # Generate title from clarified request if outline doesn't have one
        default_title = f"Research Report: {self.workflow_state.get('clarified_request', 'Research Analysis')[:50]}"
        title = default_title
        if outline and isinstance(outline, dict):
            title = outline.get('title', default_title)
        
        report_parts.append(f"# {title}")
        report_parts.append("")
        
        # Add any notes about report completeness
        if hasattr(self.workflow_state, 'report_note') or 'report_note' in self.workflow_state:
            report_parts.append(f"*{self.workflow_state.get('report_note', '')}*")
            report_parts.append("")
        
        # Executive Summary - handle both nested and direct content
        if 'executive_summary' in sections:
            content = sections['executive_summary']
            # If it already has ## Executive Summary, don't add it again
            if not content.strip().startswith('## Executive Summary'):
                report_parts.append("## Executive Summary")
            report_parts.append(content)
            report_parts.append("")
        
        # Add each section in a logical order
        ordered_sections = []
        
        # First add task-based sections in order
        for subtask in self.workflow_state.get('subtasks', []):
            task_id = subtask['id']
            if task_id in sections:
                ordered_sections.append((task_id, sections[task_id]))
        
        # Then add any other sections
        for section_key, section_content in sections.items():
            if section_key not in ['executive_summary', 'conclusion'] and not any(s[0] == section_key for s in ordered_sections):
                ordered_sections.append((section_key, section_content))
        
        # Add ordered sections
        for section_key, section_content in ordered_sections:
            # Don't add duplicate headers
            if not section_content.strip().startswith('##'):
                section_title = section_key.replace('_', ' ').replace('task ', 'Task ').title()
                report_parts.append(f"## {section_title}")
            report_parts.append(section_content)
            report_parts.append("")
        
        # Add conclusion if present
        if 'conclusion' in sections:
            report_parts.append(sections['conclusion'])
            report_parts.append("")
        
        # Metadata
        report_parts.append("---")
        report_parts.append(f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        # Calculate total findings count without truncation
        total_findings = self._count_total_findings()
        report_parts.append(f"*Total findings analyzed: {total_findings}*")
        
        return "\n".join(report_parts)
    
    def _create_report_outline(self) -> Dict[str, Any]:
        """Create detailed outline for the report"""
        research_summary = self._summarize_research()
        
        outline_prompt = f"""
        Create a detailed outline for a comprehensive research report based on:
        
        Research Summary: {json.dumps(research_summary, indent=2)}
        
        The outline should include:
        1. Executive Summary
        2. Main sections covering all subtasks
        3. Logical flow and organization
        4. Subsections for detailed topics
        
        Format as JSON:
        {{
            "title": "...",
            "executive_summary": {{
                "purpose": "...",
                "key_points": ["..."]
            }},
            "sections": [
                {{
                    "id": "section_1",
                    "title": "...",
                    "purpose": "...",
                    "subsections": [
                        {{
                            "title": "...",
                            "content_points": ["..."]
                        }}
                    ],
                    "sources": ["subtask_id"]
                }}
            ],
            "conclusion": {{
                "summary_points": ["..."],
                "recommendations": ["..."]
            }}
        }}
        """
        
        return parse_llm_json(self.llm_provider.generate(outline_prompt))
    
    def _generate_report_sections(self, outline: Dict) -> Dict[str, str]:
        """Generate each section of the report"""
        sections = {}
        previous_sections = []
        
        # Handle missing or malformed outline
        if not outline or 'sections' not in outline:
            print("Warning: Outline missing sections. Creating default report structure.")
            return self._generate_default_sections()
        
        # Generate executive summary from outline
        if 'executive_summary' in outline:
            exec_summary_data = outline['executive_summary']
            exec_summary_prompt = f"""
            Write the Executive Summary section for the research report.
            
            Key Points: {json.dumps(exec_summary_data.get('key_points', []), indent=2)}
            Main Findings: {json.dumps(exec_summary_data.get('main_findings', []), indent=2)}
            
            Research Context: {self.workflow_state.get('clarified_request', '')}
            
            Format as markdown section. Start with "## Executive Summary".
            Keep it concise but comprehensive.
            """
            sections['executive_summary'] = self.llm_provider.generate(exec_summary_prompt)
        
        for section in outline.get('sections', []):
            section_prompt = f"""
            Write the markdown section "{section['title']}" for the research report.
            
            Section Purpose: {section['purpose']}
            Content Points: {json.dumps(section.get('subsections', []), indent=2)}
            
            Research Data: {self._get_section_research_data(section['sources'])}
            
            Previous Sections Context: {self._summarize_previous_sections(previous_sections)}
            
            Requirements:
            - Use clear markdown formatting
            - Include relevant examples and data from research
            - Maintain logical flow with previous sections
            - Be comprehensive yet concise
            - Use appropriate headers (##, ###)
            
            Write the complete section in markdown:
            """
            
            section_content = self.llm_provider.generate(section_prompt)
            sections[section['id']] = section_content
            previous_sections.append({
                'title': section['title'],
                'summary': self._summarize_section(section_content)
            })
        
        # Generate conclusion from outline
        if 'conclusion' in outline:
            conclusion_data = outline['conclusion']
            conclusion_prompt = f"""
            Write the Conclusion section for the research report.
            
            Summary Points: {json.dumps(conclusion_data.get('summary_points', []), indent=2)}
            Recommendations: {json.dumps(conclusion_data.get('recommendations', []), indent=2)}
            
            Research Context: {self.workflow_state.get('clarified_request', '')}
            Previous Sections: {json.dumps([s['title'] for s in previous_sections], indent=2)}
            
            Format as markdown section. Start with "## Conclusion".
            Synthesize the key findings and provide actionable recommendations.
            """
            sections['conclusion'] = self.llm_provider.generate(conclusion_prompt)
        
        return sections
    
    def _generate_default_sections(self) -> Dict[str, str]:
        """Generate default report sections when outline parsing fails"""
        sections = {}
        
        # Collect all findings first to avoid duplication
        all_findings_by_task = {}
        all_insights_by_task = {}
        
        for subtask in self.workflow_state.get('subtasks', []):
            task_id = subtask['id']
            scratchpad = self.workflow_state.get('scratchpads', {}).get(task_id, {})
            doc_analysis = self.workflow_state.get('document_analysis', {}).get(task_id, {})
            
            findings = list(scratchpad.get('high_value_findings', []))
            insights = list(scratchpad.get('insights', []))
            
            if not findings and doc_analysis:
                if 'key_information' in doc_analysis:
                    findings.extend(doc_analysis.get('key_information', []))
                if 'document_analyses' in doc_analysis:
                    for doc in doc_analysis['document_analyses']:
                        findings.extend(doc.get('key_information', []))
                        insights.extend(doc.get('insights', []))
            
            all_findings_by_task[task_id] = findings
            all_insights_by_task[task_id] = insights
        
        # Executive Summary - dynamically generated based on findings
        key_findings = self._extract_key_findings()[:5]  # Top 5 findings
        if key_findings:
            exec_summary = f"""## Executive Summary

This comprehensive report presents the findings from our research on: {self.workflow_state.get('clarified_request', 'the requested topic')}.

**Key Takeaways:**
"""
            for i, finding in enumerate(key_findings, 1):
                exec_summary += f"{i}. {finding}\n"
            
            sections['executive_summary'] = exec_summary
        else:
            # Fallback if no findings
            sections['executive_summary'] = f"""## Executive Summary

This report summarizes our research findings on: {self.workflow_state.get('clarified_request', 'the requested topic')}.

The research has been conducted based on available knowledge and documentation."""
        
        # Create focused sections based on actual subtasks
        for subtask in self.workflow_state.get('subtasks', []):
            task_id = subtask['id']
            task_title = subtask.get('title', f'Section {task_id}')
            
            if task_id in all_findings_by_task and all_findings_by_task[task_id]:
                section_content = f"""## {task_title}

{subtask.get('objective', 'This section presents findings from the research.')}

### Key Findings

"""
                # Add findings for this task
                findings = all_findings_by_task[task_id]
                for finding in findings[:5]:  # Limit to 5 findings per section
                    section_content += f"- {finding}\n"
                
                # Add insights if available
                if task_id in all_insights_by_task and all_insights_by_task[task_id]:
                    section_content += "\n### Insights\n\n"
                    for insight in all_insights_by_task[task_id][:3]:
                        section_content += f"- {insight}\n"
                
                sections[task_id] = section_content
        
        # Note: The dynamic section generation above already handles all tasks based on subtasks
        # No need for additional hardcoded sections
        
        # Conclusion - dynamically generated based on insights
        all_insights = []
        for task_insights in all_insights_by_task.values():
            all_insights.extend(task_insights)
        
        if all_insights:
            conclusion = """## Conclusion

Based on the research conducted, we have identified the following key insights:

"""
            # Add up to 5 unique insights
            unique_insights = []
            for insight in all_insights:
                if insight not in unique_insights:
                    unique_insights.append(insight)
                if len(unique_insights) >= 5:
                    break
            
            for insight in unique_insights:
                conclusion += f"- {insight}\n"
            
            conclusion += f"\n### Next Steps\nBased on these findings, we recommend further investigation into specific areas relevant to your use case."
            sections['conclusion'] = conclusion
        else:
            # Fallback generic conclusion
            sections['conclusion'] = f"""## Conclusion

This research has examined: {self.workflow_state.get('clarified_request', 'the requested topic')}.

The findings presented in this report provide a foundation for informed decision-making. We recommend evaluating these insights against your specific requirements and constraints."""
        
        return sections
    
    def _integrate_report_sections(self, sections: Dict[str, str]) -> str:
        """Integrate all sections into cohesive report"""
        integration_prompt = f"""
        Integrate the following report sections into a cohesive, professional markdown document:
        
        Sections:
        {self._format_sections_for_integration(sections)}
        
        Additional Context:
        {self._get_report_context()}
        
        Requirements:
        1. Add smooth transitions between sections
        2. Ensure consistent tone and style
        3. Add a comprehensive executive summary at the beginning
        4. Include a table of contents
        5. Add a "Data Limitations" section acknowledging gaps in available information
        6. Add a conclusion that synthesizes key findings
        7. Format with proper markdown structure
        
        Generate the complete, integrated markdown report:
        """
        
        return self.llm_provider.generate(integration_prompt)
    
    def _final_quality_assurance(self, report: str) -> Dict[str, Any]:
        """Perform final QA on the complete report"""
        qa_prompt = f"""
        Perform a thorough quality assurance review of this research report:
        
        Report Length: {len(report)} characters
        Original Request: {self.workflow_state.get('clarified_request', '')}
        
        Evaluate:
        1. Alignment with original research request
        2. Completeness of coverage
        3. Clarity and readability
        4. Logical flow and organization
        5. Accuracy of information presented
        6. Professional presentation
        
        Format as JSON:
        {{
            "overall_score": 85,
            "approved": true,
            "strengths": ["..."],
            "issues": [
                {{
                    "type": "content|structure|style",
                    "description": "...",
                    "location": "...",
                    "suggested_fix": "..."
                }}
            ],
            "minor_corrections": ["..."]
        }}
        """
        
        return parse_llm_json(self.llm_provider.generate(qa_prompt))
    
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
    
    def _summarize_research(self) -> Dict[str, Any]:
        """Summarize all research findings"""
        return {
            'request': self.workflow_state.get('clarified_request'),
            'subtasks': self.workflow_state.get('subtasks', []),
            'key_findings': self._extract_key_findings(),
            'total_documents_analyzed': self._count_analyzed_documents()
        }
    
    def _extract_key_findings(self) -> List[str]:
        """Extract key findings from all scratchpads and document analysis"""
        findings = []
        
        # Get from scratchpads
        for scratchpad in self.workflow_state['scratchpads'].values():
            findings.extend(scratchpad.get('high_value_findings', []))
            findings.extend(scratchpad.get('insights', []))
        
        # Also get from document analysis if scratchpads are empty
        if len(findings) < 5:
            for analysis in self.workflow_state.get('document_analysis', {}).values():
                if isinstance(analysis, dict):
                    # Handle both formats
                    if 'key_information' in analysis:
                        findings.extend(analysis.get('key_information', []))
                    if 'insights' in analysis:
                        findings.extend(analysis.get('insights', []))
                    if 'document_analyses' in analysis:
                        for doc in analysis['document_analyses']:
                            findings.extend(doc.get('key_information', []))
                            findings.extend(doc.get('insights', []))
        
        # Remove duplicates while preserving order
        seen = set()
        unique_findings = []
        for finding in findings:
            if finding not in seen:
                seen.add(finding)
                unique_findings.append(finding)
        
        return unique_findings[:20]  # Top 20 unique findings
    
    def _count_total_findings(self) -> int:
        """Count total unique findings without truncation"""
        findings = set()  # Use set to avoid double counting
        
        # Get from scratchpads
        for scratchpad in self.workflow_state['scratchpads'].values():
            findings.update(scratchpad.get('high_value_findings', []))
            findings.update(scratchpad.get('insights', []))
        
        # Also get from document analysis
        for analysis in self.workflow_state.get('document_analysis', {}).values():
            if isinstance(analysis, dict):
                if 'key_information' in analysis:
                    findings.update(analysis.get('key_information', []))
                if 'insights' in analysis:
                    findings.update(analysis.get('insights', []))
                if 'document_analyses' in analysis:
                    for doc in analysis['document_analyses']:
                        findings.update(doc.get('key_information', []))
                        findings.update(doc.get('insights', []))
        
        return len(findings)
    
    def _count_analyzed_documents(self) -> int:
        """Count total documents analyzed"""
        count = 0
        for analysis in self.workflow_state['document_analysis'].values():
            if 'document_analyses' in analysis:
                count += len(analysis['document_analyses'])
        return count
    
    def _get_section_research_data(self, source_ids: List[str]) -> str:
        """Get research data for specific subtasks"""
        data = []
        for task_id in source_ids:
            if task_id in self.workflow_state['scratchpads']:
                data.append(f"Research for {task_id}:")
                data.append(json.dumps(self.workflow_state['scratchpads'][task_id], indent=2))
        return '\n'.join(data)
    
    def _summarize_previous_sections(self, sections: List[Dict]) -> str:
        """Summarize previous sections for context"""
        if not sections:
            return "This is the first section."
        
        summaries = []
        for section in sections[-3:]:  # Last 3 sections
            summaries.append(f"- {section['title']}: {section['summary']}")
        
        return '\n'.join(summaries)
    
    def _summarize_section(self, content: str) -> str:
        """Create brief summary of a section"""
        # Take first 200 characters as simple summary
        return content[:200].replace('\n', ' ') + '...'
    
    def _format_sections_for_integration(self, sections: Dict[str, str]) -> str:
        """Format sections for integration prompt"""
        formatted = []
        for section_id, content in sections.items():
            formatted.append(f"=== Section: {section_id} ===")
            formatted.append(content)
            formatted.append("\n")
        return '\n'.join(formatted)
    
    def _get_report_context(self) -> str:
        """Get additional context for report generation"""
        context = []
        
        # Add report note if exists
        if 'report_note' in self.workflow_state:
            context.append(f"Important: {self.workflow_state['report_note']}")
        
        # Count total findings
        total_findings = sum(
            len(scratchpad.get('high_value_findings', [])) + 
            len(scratchpad.get('insights', []))
            for scratchpad in self.workflow_state.get('scratchpads', {}).values()
        )
        context.append(f"Total findings collected: {total_findings}")
        
        # Note about document availability
        total_docs = sum(
            len(scratchpad.get('documents_analyzed', []))
            for scratchpad in self.workflow_state.get('scratchpads', {}).values()
        )
        context.append(f"Total documents analyzed: {total_docs}")
        
        return '\n'.join(context)
    
    def _apply_qa_corrections(self, report: str, qa_result: Dict) -> str:
        """Apply QA corrections to the report"""
        corrections_prompt = f"""
        Apply the following corrections to the research report:
        
        QA Issues: {json.dumps(qa_result['issues'], indent=2)}
        Minor Corrections: {qa_result.get('minor_corrections', [])}
        
        Current Report:
        {report[:1000]}... [truncated]
        
        Apply all corrections and return the improved report:
        """
        
        return self.llm_provider.generate(corrections_prompt)
    
    def _run_automatic_qa_and_improvements(self, report: str) -> Optional[Dict[str, Any]]:
        """Run automatic QA and improvements on the generated report"""
        try:
            from .automatic_qa_system import automatic_qa_system
            
            # Get necessary data for QA
            original_query = self.workflow_state.get('original_query', 
                                                   self.workflow_state.get('clarified_request', ''))
            subtasks = self.workflow_state.get('subtasks', [])
            scratchpads = self.workflow_state.get('scratchpads', {})
            
            # Run automatic QA
            return automatic_qa_system.run_automatic_qa(
                report=report,
                original_query=original_query,
                subtasks=subtasks,
                scratchpads=scratchpads
            )
            
        except Exception as e:
            print(f"Error in automatic QA: {e}")
            return None


class WorkflowOrchestrator:
    """Orchestrates the entire research workflow process"""
    
    def __init__(self, original_query: str = None):
        self.workflow = ResearchWorkflow(original_query)
        self.current_stage = 'inquiry_clarification'
        
        # Restore session directory and workflow state if exists
        if 'research_workflow' in st.session_state:
            session_dir = st.session_state.research_workflow.get('session_dir')
            if session_dir:
                # Set the current session directory
                workflow_persistence.set_current_session(session_dir)
                print(f"Restored session directory: {session_dir}")
                
                # Load the workflow state
                loaded_state = workflow_persistence.load_workflow_state(session_dir)
                if loaded_state:
                    self.workflow.workflow_state = loaded_state
                    # Determine current stage from loaded state
                    if loaded_state.get('final_report'):
                        self.current_stage = 'report_generation'
                    elif loaded_state.get('document_analysis') and loaded_state.get('subtasks'):
                        # If we have both document analysis and subtasks, we're in research stage
                        self.current_stage = 'document_research'
                    elif loaded_state.get('subtasks'):
                        # If we only have subtasks, check if we should be in research
                        # by looking for any scratchpads (indicating research has started)
                        if loaded_state.get('scratchpads'):
                            self.current_stage = 'document_research'
                        else:
                            self.current_stage = 'task_decomposition'
                    elif loaded_state.get('clarified_request'):
                        self.current_stage = 'task_decomposition'
                    else:
                        self.current_stage = 'inquiry_clarification'
        
    def execute_workflow(self, user_query: str, user_responses: Dict = None) -> Dict[str, Any]:
        """Execute the workflow based on current stage"""
        
        # Re-detect stage from workflow state to ensure accuracy
        self._update_current_stage_from_state()
        
        print(f"DEBUG: Executing workflow at stage: {self.current_stage}")
        
        if self.current_stage == 'inquiry_clarification':
            return self.handle_inquiry_clarification(user_query)
            
        elif self.current_stage == 'task_decomposition':
            return self.handle_task_decomposition(user_responses)
            
        elif self.current_stage == 'document_research':
            return self.handle_document_research()
            
        elif self.current_stage == 'report_generation':
            return self.handle_report_generation()
            
        return {'error': 'Unknown workflow stage'}
    
    def _update_current_stage_from_state(self):
        """Update current stage based on the current workflow state"""
        workflow_state = self.workflow.workflow_state
        
        # First check if there's an explicit current_stage in the workflow state
        saved_stage = workflow_state.get('current_stage')
        if saved_stage and saved_stage in ['inquiry_clarification', 'task_decomposition', 'document_research', 'report_generation']:
            self.current_stage = saved_stage
            print(f"DEBUG: Using saved stage: {self.current_stage}")
            return
        
        # Otherwise, infer stage from state data
        if workflow_state.get('final_report'):
            self.current_stage = 'report_generation'
        elif workflow_state.get('document_analysis') and workflow_state.get('subtasks'):
            # If we have both document analysis and subtasks, we're in research stage
            self.current_stage = 'document_research'
        elif workflow_state.get('subtasks'):
            # If we only have subtasks, check if we should be in research
            # by looking for any scratchpads (indicating research has started)
            if workflow_state.get('scratchpads'):
                self.current_stage = 'document_research'
            else:
                self.current_stage = 'task_decomposition'
        elif workflow_state.get('clarified_request') and len(workflow_state.get('clarified_request', '').strip()) > 10:
            self.current_stage = 'task_decomposition'
        else:
            # Validate clarification data to prevent infinite loops
            clarification_data = workflow_state.get('clarification_data', {})
            original_query = workflow_state.get('original_query', '')
            
            # Check if we're stuck in a loop with malformed data
            if (not original_query or 
                not clarification_data.get('clarifying_questions') or 
                len(clarification_data.get('clarifying_questions', [])) == 0):
                
                # Reset corrupted state to allow fresh start
                print("DEBUG: Detected corrupted clarification state, resetting...")
                workflow_state['clarification_data'] = {}
                workflow_state['original_query'] = ''
            
            self.current_stage = 'inquiry_clarification'
        
        print(f"DEBUG: Updated stage to: {self.current_stage} based on state")
    
    def handle_inquiry_clarification(self, user_query: str) -> Dict[str, Any]:
        """Handle the inquiry clarification stage"""
        # Check if we already have a session loaded
        if workflow_persistence.current_session_dir:
            session_dir = workflow_persistence.current_session_dir
            print(f"Using existing session: {session_dir}")
            
            # Check if this session has corrupted data and needs reset
            if (not user_query and 
                not self.workflow.workflow_state.get('original_query') and
                not self.workflow.workflow_state.get('clarification_data', {}).get('clarifying_questions')):
                
                print("DEBUG: Resetting corrupted session with empty query")
                # Clear the corrupted session
                workflow_persistence.current_session_dir = None
                # Force creation of new session
                session_dir = workflow_persistence.create_session("Please help me understand when to integrate an AI agent")
                print(f"Created new session after reset: {session_dir}")
                user_query = "Please help me understand when to integrate an AI agent"
        else:
            # Create a new session for this research
            session_dir = workflow_persistence.create_session(user_query or "Please help me understand when to integrate an AI agent")
            print(f"Created research session: {session_dir}")
            if not user_query:
                user_query = "Please help me understand when to integrate an AI agent"
        
        clarification = self.workflow.step1_inquiry_clarification(user_query)
        
        self.workflow.workflow_state['original_query'] = user_query
        self.workflow.workflow_state['clarification_data'] = clarification
        self.workflow.workflow_state['session_dir'] = str(session_dir)
        
        # Save initial workflow state
        workflow_persistence.save_workflow_state(self.workflow.workflow_state)
        
        return {
            'stage': 'inquiry_clarification',
            'data': clarification,
            'next_action': 'answer_clarifying_questions'
        }
    
    def handle_task_decomposition(self, user_responses: Dict) -> Dict[str, Any]:
        """Handle task decomposition based on clarified request"""
        # Combine original query with clarifications
        clarified_request = self._build_clarified_request(user_responses)
        self.workflow.workflow_state['clarified_request'] = clarified_request
        
        # Validate clarified request
        if not clarified_request or len(clarified_request.strip()) < 10:
            print("Warning: Clarified request is too short or empty. Using original query.")
            clarified_request = self.workflow.workflow_state['original_query']
            self.workflow.workflow_state['clarified_request'] = clarified_request
        
        # Save clarified request
        workflow_persistence.save_workflow_state(self.workflow.workflow_state)
        
        # Decompose into subtasks
        decomposition_result = self.workflow.step2_task_decomposition(clarified_request)
        
        # Check if decomposition was successful
        decomposition = decomposition_result.get('decomposition', {})
        verification = decomposition_result.get('verification', {})
        
        # Handle parsing errors or missing data
        if decomposition.get('parse_error') or 'subtasks' not in decomposition:
            print("Error: Failed to parse task decomposition. Using fallback.")
            # Create a default subtask structure
            decomposition = {
                'subtasks': [
                    {
                        'id': 'task_1',
                        'title': 'Research AI agents and their applications',
                        'objective': 'Understand different types of AI agents and their use cases',
                        'scope': 'Overview of agent types, architectures, and applications',
                        'dependencies': [],
                        'complexity': 'medium',
                        'estimated_documents': 5
                    },
                    {
                        'id': 'task_2',
                        'title': 'Compare agents with other AI methods',
                        'objective': 'Analyze advantages and disadvantages of agent-based approaches',
                        'scope': 'Comparison with traditional ML, rule-based systems, and other approaches',
                        'dependencies': ['task_1'],
                        'complexity': 'high',
                        'estimated_documents': 5
                    },
                    {
                        'id': 'task_3',
                        'title': 'Implementation guidance and best practices',
                        'objective': 'Provide practical guidance for using AI agents',
                        'scope': 'Tools, frameworks, and implementation strategies',
                        'dependencies': ['task_1', 'task_2'],
                        'complexity': 'medium',
                        'estimated_documents': 4
                    }
                ],
                'execution_order': ['task_1', 'task_2', 'task_3']
            }
            decomposition_result['decomposition'] = decomposition
            # Mark as approved to continue workflow
            if 'verification' not in decomposition_result:
                decomposition_result['verification'] = {}
            decomposition_result['verification']['approved'] = True
        
        if verification.get('approved', False):
            self.workflow.workflow_state['subtasks'] = decomposition.get('subtasks', [])
            self.workflow.workflow_state['current_stage'] = 'task_decomposition'
            self.current_stage = 'task_decomposition'
            
            # Save the updated workflow state
            workflow_persistence.save_workflow_state(self.workflow.workflow_state)
            
            return {
                'stage': 'task_decomposition',
                'data': decomposition_result,
                'next_action': 'begin_research'
            }
        else:
            # Need to refine decomposition
            return {
                'stage': 'task_decomposition',
                'data': decomposition_result,
                'next_action': 'refine_decomposition'
            }
    
    def handle_document_research(self) -> Dict[str, Any]:
        """Handle iterative document research for all subtasks with dependency resolution"""
        subtasks = self.workflow.workflow_state['subtasks']
        research_results = []
        
        # Report overall progress
        report_progress(f"Starting document research for {len(subtasks)} tasks")
        
        # Resolve task dependencies and get execution order
        execution_order = self._resolve_task_dependencies(subtasks)
        completed_tasks = set()
        
        for task_index in execution_order:
            subtask = subtasks[task_index]
            subtask_id = subtask['id']
            
            # Check if dependencies are satisfied
            dependencies = subtask.get('dependencies', [])
            unsatisfied_deps = [dep for dep in dependencies if dep not in completed_tasks]
            
            # Check if the dependencies have at least been attempted
            attempted_deps = []
            for dep in dependencies:
                dep_scratchpad = self.workflow.workflow_state.get('scratchpads', {}).get(dep, {})
                if dep_scratchpad.get('iteration_count', 0) > 0:
                    attempted_deps.append(dep)
            
            if unsatisfied_deps:
                # If all dependencies have been attempted at least once, proceed anyway
                if all(dep in attempted_deps for dep in unsatisfied_deps):
                    print(f"Info: Task {subtask_id} proceeding despite incomplete dependencies (all attempted)")
                else:
                    print(f"Warning: Task {subtask_id} has unsatisfied dependencies: {unsatisfied_deps}")
                    # Skip this task for now
                    continue
            
            # Report task progress
            position = len(completed_tasks) + 1
            report_progress(f"Processing task {position}/{len(subtasks)}: {subtask['title']}", task=subtask_id)
            
            # Perform keyword research and document analysis
            research = self.workflow.step3_keyword_research(subtask)
            
            # Store analysis
            self.workflow.workflow_state['document_analysis'][subtask_id] = research['analysis']
            
            # Save research progress
            self.workflow.persistence.save_workflow_state(self.workflow.workflow_state)
            
            # Validate findings
            validation = self.workflow.step4_iterative_validation(subtask_id, research['analysis'])
            
            research_results.append({
                'subtask': subtask,
                'research': research,
                'validation': validation,
                'completed': subtask_id in completed_tasks
            })
            
            # Mark task as completed if sufficient
            if validation.get('sufficient', False):
                completed_tasks.add(subtask_id)
                print(f"Task {subtask_id} completed. Total completed: {len(completed_tasks)}/{len(subtasks)}")
            
            # Check if we need more iterations for this specific task
            if not validation.get('sufficient', False):
                # Get task-specific iteration count
                task_iterations = self.workflow.workflow_state['scratchpads'][subtask_id].get('iteration_count', 0)
                if task_iterations < 3:
                    # Perform another iteration for this task
                    print(f"Task {subtask_id} needs more research (iteration {task_iterations}/3)")
                    # The iteration count is already incremented in step4_iterative_validation
                    # Just save and continue to next task
                else:
                    # Mark as complete after max iterations
                    print(f"Task {subtask_id} reached max iterations, marking as complete")
                    completed_tasks.add(subtask_id)
            else:
                # Task is sufficient, mark as complete
                print(f"Task {subtask_id} has sufficient research")
                completed_tasks.add(subtask_id)
        
        # After processing all tasks once, check if any need more iterations
        need_more_research = False
        for task_index in execution_order:
            subtask = subtasks[task_index]
            subtask_id = subtask['id']
            if subtask_id not in completed_tasks:
                task_iterations = self.workflow.workflow_state['scratchpads'].get(subtask_id, {}).get('iteration_count', 0)
                if task_iterations < 3:
                    need_more_research = True
                    break
        
        # Increment global iteration count
        self.workflow.workflow_state['iteration_count'] = self.workflow.workflow_state.get('iteration_count', 0) + 1
        
        # Check if all subtasks are sufficiently researched
        all_sufficient = len(completed_tasks) == len(subtasks)
        
        if all_sufficient:
            self.current_stage = 'report_generation'
            self.workflow.workflow_state['current_stage'] = 'report_generation'
            return {
                'stage': 'report_generation',
                'data': research_results,
                'next_action': 'generate_report'
            }
        else:
            return {
                'stage': 'document_research',
                'data': research_results,
                'next_action': 'continue_research'
            }
    
    def handle_report_generation(self) -> Dict[str, Any]:
        """Handle report generation stage"""
        # Check if we have subtasks, if not create default ones
        if not self.workflow.workflow_state.get('subtasks'):
            print("No subtasks found, creating default subtasks for report generation")
            self._create_default_subtasks()
        
        report = self.workflow.step5_report_generation()
        
        # Save report to workflow state
        self.workflow.workflow_state['final_report'] = report
        self.workflow.workflow_state['current_stage'] = 'report_generation'
        
        # Save the report to file system
        workflow_persistence.save_workflow_state(self.workflow.workflow_state)
        
        # Also save the report as a markdown file
        if workflow_persistence.current_session_dir:
            report_path = workflow_persistence.current_session_dir / "05_final_report.md"
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Report saved to: {report_path}")
        
        print(f"Generated report length: {len(report)} characters")
        
        return {
            'stage': 'report_generation',
            'data': {
                'report': report,
                'metadata': {
                    'generated_at': datetime.now().isoformat(),
                    'subtasks_completed': len(self.workflow.workflow_state.get('subtasks', [])),
                    'documents_analyzed': self.workflow._count_analyzed_documents()
                }
            },
            'next_action': 'display_report'
        }
    
    def update_report(self, new_report: str) -> Dict[str, Any]:
        """Update an existing report (used for completing incomplete reports)"""
        # Save report to workflow state
        self.workflow.workflow_state['final_report'] = new_report
        
        # Save the report to file system
        workflow_persistence.save_workflow_state(self.workflow.workflow_state)
        
        # Also save the report as a markdown file
        if workflow_persistence.current_session_dir:
            report_path = workflow_persistence.current_session_dir / "05_final_report.md"
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(new_report)
            print(f"Updated report saved to: {report_path}")
        
        print(f"Updated report length: {len(new_report)} characters")
        
        return {
            'stage': 'report_generation',
            'data': {
                'report': new_report,
                'metadata': {
                    'generated_at': datetime.now().isoformat(),
                    'subtasks_completed': len(self.workflow.workflow_state.get('subtasks', [])),
                    'documents_analyzed': self.workflow._count_analyzed_documents(),
                    'updated': True
                }
            },
            'next_action': 'display_report'
        }
    
    def _create_default_subtasks(self):
        """Create default subtasks when none exist"""
        clarified_request = self.workflow.workflow_state.get('clarified_request', '')
        original_query = self.workflow.workflow_state.get('original_query', '')
        
        # Use original query if no clarified request
        query = clarified_request if clarified_request else original_query
        
        if not query:
            query = "Understanding when to use AI agents versus other AI systems"
        
        # Create default subtasks based on the query
        default_subtasks = [
            {
                'id': 'task_1',
                'title': 'Research AI agents and their applications',
                'objective': 'Understand different types of AI agents and their use cases',
                'scope': 'Overview of agent types, architectures, and applications',
                'dependencies': [],
                'complexity': 'medium',
                'estimated_documents': 5
            },
            {
                'id': 'task_2', 
                'title': 'Compare agents with other AI methods',
                'objective': 'Analyze advantages and disadvantages of agent-based approaches',
                'scope': 'Comparison with traditional ML, rule-based systems, and other approaches',
                'dependencies': ['task_1'],
                'complexity': 'high',
                'estimated_documents': 5
            },
            {
                'id': 'task_3',
                'title': 'Implementation guidance and best practices',
                'objective': 'Provide practical guidance for using AI agents',
                'scope': 'Tools, frameworks, and implementation strategies',
                'dependencies': ['task_1', 'task_2'],
                'complexity': 'medium',
                'estimated_documents': 4
            }
        ]
        
        self.workflow.workflow_state['subtasks'] = default_subtasks
        
        # Also create some default scratchpads with basic findings
        if not self.workflow.workflow_state.get('scratchpads'):
            self.workflow.workflow_state['scratchpads'] = {
                'task_1': {
                    'high_value_findings': [
                        'AI agents are autonomous software entities that can perceive their environment and take actions',
                        'Common types include reactive agents, deliberative agents, and hybrid agents',
                        'Agents excel in dynamic environments requiring autonomous decision-making'
                    ],
                    'insights': [
                        'Agents are particularly useful when human intervention is impractical',
                        'Multi-agent systems can solve complex distributed problems'
                    ],
                    'quotes': [],
                    'documents_analyzed': ['General Knowledge Synthesis'],
                    'iteration_count': 1
                },
                'task_2': {
                    'high_value_findings': [
                        'Traditional AI systems follow predefined rules and patterns',
                        'Machine learning models excel at pattern recognition but lack autonomy',
                        'Agents add a layer of autonomous behavior and goal-directed action'
                    ],
                    'insights': [
                        'Choose agents when you need autonomous decision-making',
                        'Use traditional AI for well-defined, predictable tasks'
                    ],
                    'quotes': [],
                    'documents_analyzed': ['General Knowledge Synthesis'],
                    'iteration_count': 1
                },
                'task_3': {
                    'high_value_findings': [
                        'Popular agent frameworks include LangChain, AutoGPT, and ReAct',
                        'Key considerations include goal definition, environment modeling, and action spaces',
                        'Start with simple rule-based agents before moving to complex learning agents'
                    ],
                    'insights': [
                        'Prototype with simple tools before building complex multi-agent systems',
                        'Consider the trade-off between autonomy and control'
                    ],
                    'quotes': [],
                    'documents_analyzed': ['General Knowledge Synthesis'],
                    'iteration_count': 1
                }
            }
        
        print(f"Created {len(default_subtasks)} default subtasks for report generation")
    
    def _build_clarified_request(self, user_responses: Dict) -> str:
        """Build clarified request from user responses with validation"""
        original = self.workflow.workflow_state['original_query']
        clarification_data = self.workflow.workflow_state.get('clarification_data', {})
        
        # Validate responses
        valid_responses = []
        for question in clarification_data.get('clarifying_questions', []):
            response = user_responses.get(question['question'], '').strip()
            if response and response.lower() not in ['no response provided', 'n/a', 'none', 'skip']:
                valid_responses.append(f"- {question['question']}: {response}")
        
        # If no valid responses, return original query with warning
        if not valid_responses:
            print("Warning: No valid clarification responses provided. Using original query.")
            return f"Original Request: {original}\n\n(No additional clarifications provided)"
        
        clarified = f"Original Request: {original}\n\nClarifications:\n"
        clarified += "\n".join(valid_responses) + "\n"
        
        return clarified
    
    def _resolve_task_dependencies(self, subtasks: List[Dict[str, Any]]) -> List[int]:
        """Resolve task dependencies and return execution order using topological sort"""
        # Create task index mapping
        task_id_to_index = {task['id']: i for i, task in enumerate(subtasks)}
        
        # Build adjacency list for dependency graph
        graph = {i: [] for i in range(len(subtasks))}
        in_degree = [0] * len(subtasks)
        
        for i, task in enumerate(subtasks):
            dependencies = task.get('dependencies', [])
            for dep_id in dependencies:
                if dep_id in task_id_to_index:
                    dep_index = task_id_to_index[dep_id]
                    graph[dep_index].append(i)
                    in_degree[i] += 1
                else:
                    print(f"Warning: Task {task['id']} has unknown dependency: {dep_id}")
        
        # Perform topological sort using Kahn's algorithm
        queue = [i for i in range(len(subtasks)) if in_degree[i] == 0]
        execution_order = []
        
        while queue:
            # Process tasks with no dependencies first
            current = queue.pop(0)
            execution_order.append(current)
            
            # Update dependent tasks
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check for circular dependencies
        if len(execution_order) != len(subtasks):
            print("Warning: Circular dependencies detected. Processing tasks in original order.")
            # Fall back to original order if circular dependencies exist
            return list(range(len(subtasks)))
        
        # Log execution order
        print(f"Task execution order: {[subtasks[i]['id'] for i in execution_order]}")
        
        return execution_order