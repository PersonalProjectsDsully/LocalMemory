"""
Research workflow steps - Inquiry clarification, task decomposition, etc.
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime

from ..llm.robust_json_parser import parse_llm_json
from .llm_provider import LLMProvider


class WorkflowSteps:
    """Handles individual steps of the research workflow"""
    
    def __init__(self, llm_provider: LLMProvider, persistence):
        self.llm_provider = llm_provider
        self.persistence = persistence
    
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
            "gaps": ["missing aspect 1", "missing aspect 2"],
            "redundancies": ["duplicate topic between task 2 and 3"],
            "suggestions": ["add subtask for X", "merge tasks Y and Z"],
            "approved": false
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
        
        return {
            'keywords': keywords,
            'subtask': subtask
        }