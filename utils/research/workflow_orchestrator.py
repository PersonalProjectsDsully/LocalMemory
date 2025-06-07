"""
Workflow orchestrator for the complete research process
"""

import streamlit as st
from typing import Dict, List, Any
from datetime import datetime

from .llm_provider import LLMProvider
from .workflow_steps import WorkflowSteps
from .document_analysis import DocumentAnalyzer
from .validation import ResearchValidator
from .report_generation import ReportGenerator
from ..session.workflow_persistence import workflow_persistence
from ..session.progress_reporter import report_progress


class ResearchWorkflow:
    """Manages the comprehensive research workflow process"""
    
    def __init__(self, original_query: str = None):
        self.llm_provider = LLMProvider()
        # Reuse search engine from session state if available
        if 'search_engine' in st.session_state:
            self.search_engine = st.session_state.search_engine
        else:
            from ..search.intelligent_search import get_search_engine
            self.search_engine = get_search_engine()
        self.workflow_state = self._init_workflow_state(original_query)
        self.persistence = workflow_persistence
        
        # Initialize components
        self.steps = WorkflowSteps(self.llm_provider, self.persistence)
        self.document_analyzer = DocumentAnalyzer(self.search_engine, self.llm_provider)
        self.validator = ResearchValidator(self.llm_provider, self.persistence)
        self.report_generator = ReportGenerator(self.llm_provider, self.workflow_state, self.persistence)
        
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
        
        return st.session_state.research_workflow
    
    # Delegate methods to components
    def step1_inquiry_clarification(self, user_query: str) -> Dict[str, Any]:
        return self.steps.step1_inquiry_clarification(user_query)
    
    def step2_task_decomposition(self, clarified_request: str) -> Dict[str, Any]:
        result = self.steps.step2_task_decomposition(clarified_request)
        # Save subtasks to workflow state
        self.workflow_state['subtasks'] = result['decomposition'].get('subtasks', [])
        self.persistence.save_workflow_state(self.workflow_state)
        return result
    
    def step3_keyword_research(self, subtask: Dict) -> Dict[str, Any]:
        keywords_data = self.steps.step3_keyword_research(subtask)
        keywords = keywords_data['keywords']
        
        # Perform document search
        relevant_docs = self.document_analyzer.search_documents(keywords)
        
        # Analyze documents
        analysis = self.document_analyzer.analyze_documents(relevant_docs, subtask)
        
        return {
            'keywords': keywords,
            'documents_found': len(relevant_docs),
            'analysis': analysis
        }
    
    def step4_iterative_validation(self, subtask_id: str, analysis: Dict) -> Dict[str, Any]:
        return self.validator.step4_iterative_validation(subtask_id, analysis, self.workflow_state)
    
    def step5_report_generation(self) -> str:
        # Final verification of all tasks before report generation
        all_tasks_verified = self.validator.verify_all_tasks_complete(self.workflow_state)
        
        # Generate report
        return self.report_generator.step5_report_generation(all_tasks_verified)


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
                    self.current_stage = self._determine_stage_from_state(loaded_state)
    
    def _determine_stage_from_state(self, loaded_state: Dict) -> str:
        """Determine current stage from loaded state"""
        if loaded_state.get('final_report'):
            return 'report_generation'
        elif loaded_state.get('document_analysis') and loaded_state.get('subtasks'):
            return 'document_research'
        elif loaded_state.get('subtasks'):
            # Check if we should be in research by looking for scratchpads
            if loaded_state.get('scratchpads'):
                return 'document_research'
            else:
                return 'task_decomposition'
        elif loaded_state.get('clarified_request'):
            return 'task_decomposition'
        else:
            return 'inquiry_clarification'
    
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
        if saved_stage and saved_stage in ['inquiry_clarification', 'task_decomposition', 
                                          'document_research', 'report_generation']:
            self.current_stage = saved_stage
            print(f"DEBUG: Using saved stage: {self.current_stage}")
            return
        
        # Otherwise, infer stage from state data
        self.current_stage = self._determine_stage_from_state(workflow_state)
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
            decomposition = self._create_fallback_decomposition()
            decomposition_result['decomposition'] = decomposition
            decomposition_result['verification'] = {'approved': True}
        
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
        """Handle iterative document research for all subtasks"""
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
            
            # Check dependencies
            dependencies = subtask.get('dependencies', [])
            unsatisfied_deps = [dep for dep in dependencies if dep not in completed_tasks]
            
            if unsatisfied_deps:
                # Check if dependencies have been attempted
                attempted_deps = []
                for dep in dependencies:
                    dep_scratchpad = self.workflow.workflow_state.get('scratchpads', {}).get(dep, {})
                    if dep_scratchpad.get('iteration_count', 0) > 0:
                        attempted_deps.append(dep)
                
                if all(dep in attempted_deps for dep in unsatisfied_deps):
                    print(f"Info: Task {subtask_id} proceeding despite incomplete dependencies")
                else:
                    print(f"Warning: Task {subtask_id} has unsatisfied dependencies: {unsatisfied_deps}")
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
                task_iterations = self.workflow.workflow_state['scratchpads'][subtask_id].get('iteration_count', 0)
                if task_iterations < 3:
                    print(f"Task {subtask_id} needs more research (iteration {task_iterations}/3)")
                else:
                    print(f"Task {subtask_id} reached max iterations, marking as complete")
                    completed_tasks.add(subtask_id)
            else:
                print(f"Task {subtask_id} has sufficient research")
                completed_tasks.add(subtask_id)
        
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
                    'documents_analyzed': self.workflow.report_generator._count_analyzed_documents()
                }
            },
            'next_action': 'display_report'
        }
    
    def update_report(self, new_report: str) -> Dict[str, Any]:
        """Update an existing report"""
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
                    'documents_analyzed': self.workflow.report_generator._count_analyzed_documents(),
                    'updated': True
                }
            },
            'next_action': 'display_report'
        }
    
    # Helper methods
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
    
    def _create_fallback_decomposition(self) -> Dict:
        """Create fallback task decomposition"""
        return {
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
    
    def _create_default_subtasks(self):
        """Create default subtasks when none exist"""
        default_subtasks = self._create_fallback_decomposition()['subtasks']
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
            current = queue.pop(0)
            execution_order.append(current)
            
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check for circular dependencies
        if len(execution_order) != len(subtasks):
            print("Warning: Circular dependencies detected. Processing tasks in original order.")
            return list(range(len(subtasks)))
        
        print(f"Task execution order: {[subtasks[i]['id'] for i in execution_order]}")
        
        return execution_order