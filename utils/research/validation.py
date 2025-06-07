"""
Research validation and scratchpad management
"""

import json
from typing import Dict, List, Any
from datetime import datetime

from ..llm.robust_json_parser import parse_llm_json
from .workflow_tracker import workflow_tracker
from ..session.progress_reporter import report_progress


class ResearchValidator:
    """Handles validation of research findings and scratchpad management"""
    
    def __init__(self, llm_provider, persistence):
        self.llm_provider = llm_provider
        self.persistence = persistence
    
    def step4_iterative_validation(self, subtask_id: str, analysis: Dict, 
                                  workflow_state: Dict) -> Dict[str, Any]:
        """Validate scratchpad contents and determine if more research is needed"""
        # Get or create scratchpad for this subtask
        if subtask_id not in workflow_state['scratchpads']:
            workflow_state['scratchpads'][subtask_id] = {
                'high_value_findings': [],
                'insights': [],
                'quotes': [],
                'documents_analyzed': [],
                'iteration_count': 0,
                'created_at': datetime.now().isoformat()
            }
        
        scratchpad = workflow_state['scratchpads'][subtask_id]
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
        
        # Update scratchpad with latest findings
        self._update_scratchpad(scratchpad, analysis)
        
        # Save scratchpad immediately after updating
        workflow_state['scratchpads'][subtask_id] = scratchpad
        self.persistence.save_workflow_state(workflow_state)
        
        # Validate with the updated scratchpad
        validation = self._validate_research(subtask_id, scratchpad, workflow_state)
        
        # Check if we need more iterations
        validation = self._check_completion_criteria(
            validation, scratchpad, subtask_id, workflow_state
        )
        
        # Save updated scratchpad
        self.persistence.save_workflow_state(workflow_state)
        
        return validation
    
    def _update_scratchpad(self, scratchpad: Dict, analysis: Dict):
        """Update scratchpad with latest findings from analysis"""
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
    
    def _validate_research(self, subtask_id: str, scratchpad: Dict, 
                          workflow_state: Dict) -> Dict[str, Any]:
        """Validate research completeness"""
        # Summarize scratchpad to reduce prompt size
        scratchpad_summary = {
            'documents_analyzed': len(scratchpad.get('documents_analyzed', [])),
            'findings_count': len(scratchpad.get('high_value_findings', [])),
            'insights_count': len(scratchpad.get('insights', [])),
            'iteration': scratchpad.get('iteration_count', 1),
            'sample_findings': scratchpad.get('high_value_findings', [])[:3],
            'sample_insights': scratchpad.get('insights', [])[:3]
        }
        
        validation_prompt = f"""
        Evaluate research completeness for subtask {subtask_id}:
        
        Stats: {scratchpad_summary['documents_analyzed']} docs, {scratchpad_summary['findings_count']} findings, {scratchpad_summary['insights_count']} insights
        Iteration: {scratchpad_summary['iteration']}
        
        Sample findings: {scratchpad_summary['sample_findings']}
        
        Is this sufficient? What's missing?
        
        JSON format:
        {{
            "completeness_score": 85,
            "sufficient": false,
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
                'sufficient': scratchpad.get('iteration_count', 0) >= 2,
                'missing_elements': ['Unable to validate due to error'],
                'recommended_action': 'proceed',
                'error': str(e)
            }
        
        return validation
    
    def _check_completion_criteria(self, validation: Dict, scratchpad: Dict, 
                                  subtask_id: str, workflow_state: Dict) -> Dict:
        """Check if research meets completion criteria"""
        # Ensure consistency between sufficient and recommended_action
        if 'sufficient' in validation and 'recommended_action' in validation:
            if validation['sufficient'] and validation['recommended_action'] != 'proceed':
                validation['recommended_action'] = 'proceed'
            elif not validation['sufficient'] and validation['recommended_action'] == 'proceed':
                validation['recommended_action'] = 'continue_search'
        
        # Add total findings count
        validation['total_findings'] = (
            len(scratchpad.get('high_value_findings', [])) +
            len(scratchpad.get('insights', [])) +
            len(scratchpad.get('quotes', []))
        )
        
        # Define minimum findings threshold based on task complexity
        task = next((t for t in workflow_state.get('subtasks', []) 
                    if t['id'] == subtask_id), None)
        complexity = task.get('complexity', 'medium') if task else 'medium'
        
        # Set minimum findings threshold based on complexity
        min_findings_threshold = {
            'low': 3,
            'medium': 5,
            'high': 8
        }.get(complexity, 5)
        
        # Check if we have sufficient findings
        if validation['total_findings'] > 0 and not validation.get('sufficient'):
            if validation['total_findings'] >= min_findings_threshold:
                print(f"Task {subtask_id}: Marking sufficient with {validation['total_findings']} findings")
                validation['sufficient'] = True
                validation['note'] = f'Minimum findings threshold ({min_findings_threshold}) reached'
            elif scratchpad.get('iteration_count', 0) >= 3 and validation['total_findings'] >= min_findings_threshold * 0.6:
                print(f"Task {subtask_id}: Marking sufficient after {scratchpad['iteration_count']} iterations")
                validation['sufficient'] = True
                validation['note'] = f'Marked sufficient after {scratchpad["iteration_count"]} iterations'
        
        # Hard limit on iterations
        if scratchpad.get('iteration_count', 0) >= 5:
            print(f"WARNING: Task {subtask_id} reached maximum iterations (5)")
            workflow_tracker.track_operation('max_iterations_reached', {
                'subtask_id': subtask_id,
                'iterations': scratchpad['iteration_count']
            })
            validation['sufficient'] = True
            validation['note'] = 'Maximum iteration limit reached'
        
        # Verify completion if marked sufficient
        if validation.get('sufficient', False):
            try:
                completion_verification = self._verify_task_completion(
                    subtask_id, scratchpad, workflow_state
                )
                validation['completion_verified'] = completion_verification.get('verified', False)
                validation['completion_details'] = completion_verification
                
                if not completion_verification.get('verified', False):
                    validation['sufficient'] = False
                    missing_reqs = completion_verification.get('missing_requirements', [])
                    if missing_reqs:
                        if 'missing_elements' not in validation:
                            validation['missing_elements'] = []
                        validation['missing_elements'].extend(missing_reqs)
            except Exception as e:
                print(f"Error in completion verification: {e}")
                validation['completion_verified'] = validation.get('sufficient', False)
                validation['completion_details'] = {'error': str(e)}
        
        return validation
    
    def _verify_task_completion(self, subtask_id: str, scratchpad: Dict, 
                               workflow_state: Dict) -> Dict[str, Any]:
        """Verify task completion with a fresh context window"""
        # Get the original subtask details
        subtask = None
        for task in workflow_state.get('subtasks', []):
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
            "verified": false,
            "completion_summary": "Brief summary of what was accomplished",
            "objective_coverage": {{
                "percentage": 75,
                "covered_aspects": ["aspect1", "aspect2"],
                "missing_aspects": ["aspect3"]
            }},
            "quality_assessment": {{
                "depth": "adequate",
                "reliability": "high",
                "completeness": "partial"
            }},
            "missing_requirements": ["requirement1", "requirement2"],
            "recommendation": "continue_research"
        }}
        
        Note: Set "verified" to true ONLY if the task is genuinely complete with high quality.
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
            return {
                'verified': False,
                'completion_summary': 'Verification failed due to error',
                'objective_coverage': {'percentage': 0, 'covered_aspects': [], 'missing_aspects': ['Unable to verify']},
                'quality_assessment': {'depth': 'unknown', 'reliability': 'unknown', 'completeness': 'unknown'},
                'missing_requirements': ['Verification error occurred'],
                'recommendation': 'continue_research',
                'error': str(e)
            }
    
    def verify_all_tasks_complete(self, workflow_state: Dict) -> Dict[str, Any]:
        """Verify all tasks are complete before generating report"""
        verification_prompt = f"""
        Review the complete research progress and verify all tasks are sufficiently complete:
        
        ORIGINAL RESEARCH REQUEST:
        {workflow_state.get('clarified_request', '')}
        
        PLANNED TASKS:
        {json.dumps(workflow_state.get('subtasks', []), indent=2)}
        
        COLLECTED RESEARCH (Scratchpads):
        {json.dumps(workflow_state.get('scratchpads', {}), indent=2)}
        
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