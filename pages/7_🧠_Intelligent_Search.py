import streamlit as st
import json
from datetime import datetime
from pathlib import Path
import pandas as pd
from utils.intelligent_search_enhanced import EnhancedIntelligentSearchEngine
from utils.batch_intelligence_processor import process_existing_content
from utils.session_state_manager import initialize_session_state
from utils.settings_manager import settings_manager
from utils.research_workflow import ResearchWorkflow, WorkflowOrchestrator
from utils.workflow_persistence import workflow_persistence
from utils.workflow_tracker import workflow_tracker
from utils.progress_reporter import ProgressReporter, set_progress_reporter

st.set_page_config(
    page_title="Intelligent Search - Personal Knowledge Base",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Intelligent Search")
st.markdown("Advanced AI-powered search with comprehensive research workflow")

# Initialize components
search_engine = EnhancedIntelligentSearchEngine()
workflow_orchestrator = WorkflowOrchestrator()

# Initialize session state
initialize_session_state()

# Get settings
settings = settings_manager.load_settings()

# Initialize page-specific session state
if 'search_history' not in st.session_state:
    st.session_state.search_history = []
if 'current_results' not in st.session_state:
    st.session_state.current_results = None
if 'show_analysis' not in st.session_state:
    st.session_state.show_analysis = False
if 'workflow_mode' not in st.session_state:
    st.session_state.workflow_mode = False
if 'workflow_state' not in st.session_state:
    st.session_state.workflow_state = None
if 'clarification_responses' not in st.session_state:
    st.session_state.clarification_responses = {}
if 'prefill_task' not in st.session_state:
    st.session_state.prefill_task = None
if 'prefill_task_used' not in st.session_state:
    st.session_state.prefill_task_used = False

# Sidebar for options
with st.sidebar:
    st.header("Search Options")
    
    # Mode selection
    search_mode = st.radio(
        "Search Mode",
        ["Quick Search", "Research Workflow"],
        help="Quick Search: Fast results\nResearch Workflow: Comprehensive multi-step research"
    )
    
    st.session_state.workflow_mode = (search_mode == "Research Workflow")
    
    if not st.session_state.workflow_mode:
        # Quick search options
        search_depth = st.select_slider(
            "Search Depth",
            options=["Shallow", "Moderate", "Deep"],
            value="Moderate",
            help="Deeper searches analyze more content but take longer"
        )
        
        show_query_analysis = st.checkbox(
            "Show Query Analysis",
            value=st.session_state.show_analysis,
            help="Display how your query was interpreted"
        )
        st.session_state.show_analysis = show_query_analysis
        
        st.divider()
        
        # Batch processing section
        st.header("Content Enhancement")
        if st.button("🚀 Process All Content", type="secondary"):
            with st.spinner("Processing all documents..."):
                stats = process_existing_content()
                st.success(f"Processed {stats['processed']} documents!")
                st.json(stats)
    else:
        # Research workflow options
        st.info("Research Workflow will guide you through a comprehensive research process")
        
        # Previous sessions
        st.divider()
        st.subheader("Previous Research Sessions")
        sessions = workflow_persistence.list_sessions()
        if sessions:
            session_names = [f"{s['created_at'][:10]} - {s['original_query'][:50]}..." for s in sessions[:5]]
            selected_session = st.selectbox("Load previous session:", [""] + session_names)
            
            if selected_session and st.button("Load Session"):
                # Load the selected session
                session_idx = session_names.index(selected_session)
                session = sessions[session_idx]
                loaded_state = workflow_persistence.load_workflow_state(session['session_dir'])
                
                if loaded_state:
                    # Store session info for orchestrator restoration
                    st.session_state.research_workflow = {
                        'session_dir': session['session_dir'],
                        'loaded_state': loaded_state
                    }
                    # Restore workflow state
                    workflow_orchestrator.workflow.workflow_state = loaded_state
                    workflow_persistence.set_current_session(session['session_dir'])
                    
                    # Restore tracking data if available
                    if 'tracking_data' in loaded_state:
                        workflow_tracker.restore_tracking_data(loaded_state['tracking_data'])
                    else:
                        # Generate estimated tracking data from loaded state
                        scratchpads = loaded_state.get('scratchpads', {})
                        document_analysis = loaded_state.get('document_analysis', {})
                        
                        # Estimate operations based on content
                        estimated_llm_calls = sum(len(sp.get('high_value_findings', [])) + len(sp.get('insights', [])) for sp in scratchpads.values())
                        estimated_operations = len(scratchpads) + len(document_analysis)
                        
                        # Ensure workflow_tracking is initialized before restoring
                        workflow_tracker._ensure_initialized()
                        
                        # Restore basic tracking
                        st.session_state.workflow_tracking['operation_counts'] = {
                            'llm_generation': estimated_llm_calls // 2,
                            'llm_response': estimated_llm_calls // 2,
                            'document_search': len(document_analysis),
                            'validation_iteration': sum(sp.get('iteration_count', 1) for sp in scratchpads.values())
                        }
                        st.session_state.workflow_tracking['total_llm_calls'] = estimated_llm_calls
                    
                    # Determine current stage from loaded state
                    if loaded_state.get('final_report'):
                        workflow_orchestrator.current_stage = 'report_generation'
                        st.session_state.workflow_state = {
                            'stage': 'report_generation',
                            'data': {
                                'report': loaded_state['final_report'],
                                'metadata': {
                                    'generated_at': session.get('last_updated', datetime.now().isoformat()),
                                    'subtasks_completed': len(loaded_state.get('subtasks', [])),
                                    'documents_analyzed': len(loaded_state.get('document_analysis', {}))
                                }
                            }
                        }
                    elif loaded_state.get('document_analysis'):
                        workflow_orchestrator.current_stage = 'document_research'
                        # Reconstruct research results from loaded state
                        research_results = []
                        subtasks = loaded_state.get('subtasks', [])
                        scratchpads = loaded_state.get('scratchpads', {})
                        document_analysis = loaded_state.get('document_analysis', {})
                        
                        for subtask in subtasks:
                            subtask_id = subtask['id']
                            # Get the scratchpad for this subtask
                            scratchpad = scratchpads.get(subtask_id, {})
                            
                            # Create validation structure based on scratchpad contents
                            validation = {
                                'sufficient': len(scratchpad.get('high_value_findings', [])) > 0 or len(scratchpad.get('insights', [])) > 0,
                                'completeness_score': min(100, len(scratchpad.get('high_value_findings', [])) * 10 + len(scratchpad.get('insights', [])) * 5),
                                'total_findings': len(scratchpad.get('high_value_findings', [])) + len(scratchpad.get('insights', [])),
                                'missing_elements': []
                            }
                            
                            # Try to load saved task verification if it exists
                            # Construct proper path - session_dir already includes research_workspace
                            workspace_path = Path(session['session_dir'])
                            verification_file = workspace_path / '06_task_verifications' / f'{subtask_id}_verification.json'
                            
                            if verification_file.exists():
                                try:
                                    with open(verification_file, 'r', encoding='utf-8') as f:
                                        verification_data = json.load(f)
                                        if 'verification' in verification_data:
                                            validation['completion_verified'] = verification_data['verification'].get('verified', False)
                                            validation['completion_details'] = verification_data['verification']
                                except Exception as e:
                                    print(f"Error loading verification for {subtask_id}: {e}")
                            
                            # Create research structure
                            research = {
                                'documents_found': len(scratchpad.get('documents_analyzed', [])),
                                'analysis': document_analysis.get(subtask_id, {})
                            }
                            
                            research_results.append({
                                'subtask': subtask,
                                'research': research,
                                'validation': validation
                            })
                        
                        st.session_state.workflow_state = {
                            'stage': 'document_research',
                            'data': research_results,
                            'scratchpads': scratchpads,  # Include scratchpads in workflow state
                            'document_analysis': document_analysis,  # Include document analysis
                            'loaded_state': loaded_state  # Keep full loaded state for reference
                        }
                    elif loaded_state.get('subtasks'):
                        workflow_orchestrator.current_stage = 'task_decomposition'
                        # Reconstruct task decomposition state
                        decomposition = {
                            'subtasks': loaded_state.get('subtasks', [])
                        }
                        
                        # Create a basic verification structure
                        verification = {
                            'approved': True,  # Assume approved since we have subtasks
                            'completeness_score': 100,
                            'gaps': [],
                            'suggestions': []
                        }
                        
                        st.session_state.workflow_state = {
                            'stage': 'task_decomposition',
                            'data': {
                                'decomposition': decomposition,
                                'verification': verification
                            }
                        }
                    
                    st.success(f"Loaded session: {session['original_query'][:50]}...")
                    st.rerun()
        
        if st.session_state.workflow_state:
            st.divider()
            st.subheader("Workflow Progress")
            current_stage = st.session_state.workflow_state.get('stage', 'Not started')
            st.metric("Current Stage", current_stage.replace('_', ' ').title())
            
            # Add workflow tracking display
            with st.expander("📊 Workflow Tracking & Monitoring", expanded=True):
                workflow_tracker.display_status()
                
                # Export tracking data button
                col1, col2, col3 = st.columns([2, 1, 1])
                with col2:
                    if st.button("🔄 Reset Tracking"):
                        workflow_tracker.reset_tracking()
                        st.success("Tracking data reset")
                        st.rerun()
                with col3:
                    if st.button("📥 Export Tracking"):
                        tracking_data = workflow_tracker.export_tracking_data()
                        st.download_button(
                            "Download JSON",
                            tracking_data,
                            f"workflow_tracking_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                            mime="application/json"
                        )
            
            # Show progress
            stages = ['inquiry_clarification', 'task_decomposition', 'document_research', 'report_generation']
            current_idx = stages.index(workflow_orchestrator.current_stage) if workflow_orchestrator.current_stage in stages else 0
            progress = (current_idx + 1) / len(stages)
            st.progress(progress)
            
            # Show workspace location
            if workflow_persistence.current_session_dir:
                st.caption(f"📁 Workspace: {workflow_persistence.current_session_dir}")
    
    # Search history
    st.divider()
    st.header("Search History")
    if st.session_state.search_history:
        for i, item in enumerate(reversed(st.session_state.search_history[-5:])):
            if st.button(f"📝 {item['query'][:30]}...", key=f"history_{i}"):
                st.session_state.query_rerun = item['query']
                st.rerun()

# Main search interface
if st.session_state.workflow_mode:
    # Research Workflow Interface
    st.header("🔬 Comprehensive Research Workflow")
    
    if not st.session_state.workflow_state:
        # Initial query input
        st.markdown("### Step 1: Describe Your Research Need")
        query = st.text_area(
            "What would you like to research?",
            placeholder="Enter a detailed description of what you want to learn or investigate...",
            height=100
        )
        
        if st.button("🚀 Start Research", type="primary", disabled=not query):
            with st.spinner("Analyzing your request..."):
                try:
                    # Reset workflow persistence to ensure new session
                    workflow_persistence.current_session_dir = None
                    result = workflow_orchestrator.execute_workflow(query)
                    st.session_state.workflow_state = result
                    st.rerun()
                except Exception as e:
                    st.error(f"Failed to start research: {str(e)}")
                    print(f"Workflow execution error: {e}")
    
    else:
        # Handle workflow stages
        workflow_state = st.session_state.workflow_state
        stage = workflow_state['stage']
        
        if stage == 'inquiry_clarification':
            st.markdown("### Step 1: Clarifying Your Research Request")
            
            data = workflow_state['data']
            
            # Show analysis
            with st.expander("Query Analysis", expanded=True):
                if 'query_analysis' in data:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**Main Topic:**")
                        st.write(data['query_analysis'].get('main_topic', 'Not identified'))
                    with col2:
                        st.markdown("**Implicit Needs:**")
                        for need in data['query_analysis'].get('implicit_needs', []):
                            st.write(f"- {need}")
            
            # Clarifying questions
            st.markdown("**Please answer these questions to help refine your research:**")
            
            for i, question_data in enumerate(data.get('clarifying_questions', [])):
                question = question_data['question']
                purpose = question_data.get('purpose', '')
                options = question_data.get('options', [])
                
                st.markdown(f"**{i+1}. {question}**")
                if purpose:
                    st.caption(purpose)
                
                if options:
                    response = st.selectbox(
                        "Select an option or write your own:",
                        [""] + options + ["Other (specify below)"],
                        key=f"q_{i}"
                    )
                    if response == "Other (specify below)":
                        response = st.text_input("Your answer:", key=f"q_text_{i}")
                else:
                    response = st.text_area("Your answer:", key=f"q_area_{i}", height=70)
                
                st.session_state.clarification_responses[question] = response
            
            # Suggested refinement
            if 'suggested_refinement' in data:
                st.info(f"💡 Suggested refined request: {data['suggested_refinement']}")
            
            # Continue button
            all_answered = all(
                st.session_state.clarification_responses.get(q['question']) 
                for q in data.get('clarifying_questions', [])
            )
            
            if st.button("Continue to Task Planning →", type="primary", disabled=not all_answered):
                with st.spinner("Planning research tasks..."):
                    workflow_orchestrator.current_stage = 'task_decomposition'
                    result = workflow_orchestrator.execute_workflow(
                        "", 
                        st.session_state.clarification_responses
                    )
                    st.session_state.workflow_state = result
                    st.rerun()
        
        elif stage == 'task_decomposition':
            st.markdown("### Step 2: Research Task Planning")
            
            data = workflow_state['data']
            decomposition = data['decomposition']
            verification = data['verification']
            
            # Initialize editable decomposition in session state if not exists
            if 'editable_decomposition' not in st.session_state:
                # Deep copy the decomposition to avoid reference issues
                import copy
                st.session_state.editable_decomposition = copy.deepcopy(decomposition)
                st.session_state.task_edits = {}
                
                # Ensure subtasks key exists
                if 'subtasks' not in st.session_state.editable_decomposition:
                    st.session_state.editable_decomposition['subtasks'] = []
            
            # Show task breakdown with editing capability
            st.markdown("**Proposed Research Tasks:**")
            
            subtasks = st.session_state.editable_decomposition.get('subtasks', [])
            
            for i, task in enumerate(subtasks):
                with st.expander(f"📋 Task {i+1}: {task['title']}", expanded=True):
                    # Edit mode toggle
                    edit_key = f"edit_task_{i}"
                    if st.checkbox("Edit this task", key=edit_key):
                        # Editable fields
                        new_title = st.text_input("Title:", value=task['title'], key=f"title_{i}")
                        new_objective = st.text_area("Objective:", value=task['objective'], key=f"obj_{i}", height=70)
                        new_scope = st.text_area("Scope:", value=task['scope'], key=f"scope_{i}", height=70)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            new_complexity = st.selectbox("Complexity:", ["low", "medium", "high"], 
                                                        index=["low", "medium", "high"].index(task['complexity']), 
                                                        key=f"comp_{i}")
                        with col2:
                            new_est_docs = st.number_input("Est. Docs:", value=task['estimated_documents'], 
                                                         min_value=1, max_value=20, key=f"docs_{i}")
                        
                        # Store edits
                        st.session_state.task_edits[i] = {
                            'title': new_title,
                            'objective': new_objective,
                            'scope': new_scope,
                            'complexity': new_complexity,
                            'estimated_documents': new_est_docs
                        }
                    else:
                        # Display mode
                        col1, col2, col3 = st.columns([2, 1, 1])
                        with col1:
                            st.markdown(f"**Objective:** {task['objective']}")
                            st.markdown(f"**Scope:** {task['scope']}")
                        with col2:
                            st.metric("Complexity", task['complexity'])
                        with col3:
                            st.metric("Est. Docs", task['estimated_documents'])
                    
                    # Remove task button
                    if st.button(f"🗑️ Remove Task", key=f"remove_{i}"):
                        subtasks.pop(i)
                        st.session_state.editable_decomposition['subtasks'] = subtasks
                        st.rerun()
            
            # Add new task section
            with st.expander("➕ Add New Task", expanded=bool(st.session_state.get('prefill_task') and not st.session_state.get('prefill_task_used'))):
                # Check for pre-filled values
                prefill = st.session_state.get('prefill_task') if not st.session_state.get('prefill_task_used') else {}
                
                new_task_title = st.text_input("Task Title:", 
                                             value=prefill.get('title', ''),
                                             key="new_task_title")
                new_task_objective = st.text_area("Task Objective:", 
                                                value=prefill.get('objective', ''),
                                                key="new_task_obj", height=70)
                new_task_scope = st.text_area("Task Scope:", 
                                            value=prefill.get('scope', ''),
                                            key="new_task_scope", height=70)
                
                # Mark prefill as used after values are displayed
                if prefill and not st.session_state.get('prefill_task_used'):
                    st.session_state.prefill_task_used = True
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    new_task_complexity = st.selectbox("Complexity:", ["low", "medium", "high"], key="new_task_comp")
                with col2:
                    new_task_docs = st.number_input("Est. Docs:", value=5, min_value=1, max_value=20, key="new_task_docs")
                with col3:
                    col3a, col3b = st.columns(2)
                    with col3a:
                        if st.button("Add Task", type="primary"):
                            if new_task_title and new_task_objective:
                                # Get current tasks from session state to ensure accurate count
                                current_tasks = st.session_state.editable_decomposition.get('subtasks', [])
                                new_task = {
                                    'id': f"task_{len(current_tasks)+1}",
                                    'title': new_task_title,
                                    'objective': new_task_objective,
                                    'scope': new_task_scope,
                                    'complexity': new_task_complexity,
                                    'estimated_documents': new_task_docs,
                                    'dependencies': []
                                }
                                st.session_state.editable_decomposition['subtasks'].append(new_task)
                                
                                # Clear the prefill task and reset the used flag
                                st.session_state.prefill_task = None
                                st.session_state.prefill_task_used = False
                                
                                st.rerun()
                    
                    with col3b:
                        # Show cancel button only if there's a prefill task
                        if st.session_state.get('prefill_task'):
                            if st.button("Cancel", key="cancel_prefill"):
                                st.session_state.prefill_task = None
                                st.session_state.prefill_task_used = False
                                st.rerun()
            
            # Verification results
            if verification:
                st.divider()
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Completeness Score", f"{verification.get('completeness_score', 0)}%")
                with col2:
                    status = "✅ Approved" if verification.get('approved') else "⚠️ Needs Revision"
                    st.metric("Status", status)
                
                # Gaps with ability to address them
                if verification.get('gaps'):
                    st.warning("**Identified Gaps:**")
                    for i, gap in enumerate(verification['gaps']):
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.write(f"- {gap}")
                        with col2:
                            if st.button("Address", key=f"gap_{i}"):
                                # Create task based on the gap
                                if "theoretical" in gap.lower() or "framework" in gap.lower():
                                    # Special handling for theoretical framework gaps
                                    st.session_state.prefill_task = {
                                        'title': "Compare Theoretical Frameworks",
                                        'objective': "Analyze and compare theoretical models (e.g., control theory, decision theory, complexity theory) for AI agents vs prompts",
                                        'scope': "Focus on autonomy metrics, environmental dynamics, and decision-making frameworks"
                                    }
                                else:
                                    # General gap handling
                                    st.session_state.prefill_task = {
                                        'title': f"Address: {gap[:50]}...",
                                        'objective': f"Fill the identified gap: {gap}",
                                        'scope': gap
                                    }
                                st.rerun()
                
                # Suggestions with ability to implement them
                if verification.get('suggestions'):
                    st.info("**Suggestions:**")
                    for i, suggestion in enumerate(verification['suggestions']):
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.write(f"- {suggestion}")
                        with col2:
                            if st.button("Implement", key=f"sug_{i}"):
                                # Store the suggestion info for pre-filling
                                st.session_state.prefill_task = {
                                    'title': f"Implement: {suggestion[:50]}...",
                                    'objective': suggestion,
                                    'scope': 'As suggested by the verification process'
                                }
                                st.rerun()
            
            # Action buttons
            st.divider()
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("💾 Apply Edits", type="secondary"):
                    # Apply any task edits
                    for idx, edits in st.session_state.task_edits.items():
                        if idx < len(st.session_state.editable_decomposition['subtasks']):
                            st.session_state.editable_decomposition['subtasks'][idx].update(edits)
                    
                    # Update the workflow decomposition
                    workflow_orchestrator.workflow.workflow_state['subtasks'] = st.session_state.editable_decomposition['subtasks']
                    st.success("Tasks updated!")
                    st.session_state.task_edits = {}
                    st.rerun()
            
            with col2:
                if st.button("🔄 Re-verify Tasks", type="secondary"):
                    # Re-run verification with edited tasks
                    with st.spinner("Re-verifying tasks..."):
                        new_verification = workflow_orchestrator.workflow._verify_task_decomposition(
                            st.session_state.editable_decomposition,
                            workflow_orchestrator.workflow.workflow_state['clarified_request']
                        )
                        st.session_state.workflow_state['data']['verification'] = new_verification
                        st.rerun()
            
            with col3:
                # Allow proceeding even if not approved, with warning
                proceed_anyway = not verification.get('approved') and st.checkbox("Proceed anyway")
                if st.button("🔍 Begin Research →", type="primary", 
                           disabled=not (verification.get('approved') or proceed_anyway)):
                    with st.spinner("Starting document research..."):
                        # Apply any pending edits
                        for idx, edits in st.session_state.task_edits.items():
                            if idx < len(st.session_state.editable_decomposition['subtasks']):
                                st.session_state.editable_decomposition['subtasks'][idx].update(edits)
                        
                        # Update workflow with final tasks
                        workflow_orchestrator.workflow.workflow_state['subtasks'] = st.session_state.editable_decomposition['subtasks']
                        
                        workflow_orchestrator.current_stage = 'document_research'
                        result = workflow_orchestrator.execute_workflow("", {})
                        st.session_state.workflow_state = result
                        st.rerun()
        
        elif stage == 'document_research':
            st.markdown("### Step 3: Document Research & Analysis")
            
            data = workflow_state['data']
            
            # Progress overview
            total_tasks = len(data)
            completed_tasks = sum(1 for r in data if r.get('validation', {}).get('sufficient', False))
            
            st.progress(completed_tasks / total_tasks if total_tasks > 0 else 0)
            st.markdown(f"**Research Progress:** {completed_tasks}/{total_tasks} tasks completed")
            
            # Show research results for each subtask
            for result in data:
                subtask = result['subtask']
                research = result['research']
                validation = result['validation']
                
                with st.expander(f"📚 {subtask['title']}", expanded=not validation.get('sufficient', False)):
                    # Research summary
                    col1, col2, col3 = st.columns([2, 1, 1])
                    with col1:
                        st.markdown("**Documents Found:**")
                        st.write(f"{research['documents_found']} relevant documents")
                    with col2:
                        st.metric("Completeness", f"{validation['completeness_score']}%")
                    with col3:
                        status = "✅" if validation.get('sufficient', False) else "🔄"
                        st.metric("Status", status)
                    
                    # Key findings
                    if 'analysis' in research and 'document_analyses' in research['analysis']:
                        st.markdown("**Key Findings:**")
                        for doc_analysis in research['analysis']['document_analyses'][:3]:
                            if doc_analysis['relevance_score'] >= 7:
                                st.markdown(f"📄 **{doc_analysis['document_title']}** (Score: {doc_analysis['relevance_score']}/10)")
                                for insight in doc_analysis.get('insights', [])[:2]:
                                    st.write(f"  - {insight}")
                    
                    # Show completion verification if available
                    if validation.get('completion_verified') is not None:
                        st.divider()
                        completion = validation.get('completion_details', {})
                        
                        if validation['completion_verified']:
                            st.success("✅ Task Completion Verified")
                            if completion.get('completion_summary'):
                                st.write(f"**Summary:** {completion['completion_summary']}")
                            
                            # Show coverage metrics
                            if 'objective_coverage' in completion:
                                coverage = completion['objective_coverage']
                                col1, col2 = st.columns(2)
                                with col1:
                                    st.metric("Objective Coverage", f"{coverage.get('percentage', 0)}%")
                                with col2:
                                    if 'quality_assessment' in completion:
                                        quality = completion['quality_assessment']
                                        st.metric("Quality", quality.get('depth', 'unknown'))
                        else:
                            st.warning("⚠️ Task Not Yet Complete")
                            if completion.get('recommendation'):
                                st.info(f"**Recommendation:** {completion['recommendation'].replace('_', ' ').title()}")
                            if completion.get('missing_requirements'):
                                st.write("**Missing Requirements:**")
                                for req in completion['missing_requirements']:
                                    st.write(f"- {req}")
                    
                    # Missing information
                    if not validation.get('sufficient', False) and validation.get('missing_elements'):
                        st.warning("**Still need information about:**")
                        for element in validation['missing_elements']:
                            st.write(f"- {element}")
            
            # Action buttons
            col1, col2 = st.columns(2)
            with col1:
                if any(not r.get('validation', {}).get('sufficient', False) for r in data):
                    if st.button("🔄 Continue Research", type="secondary"):
                        # Create a status container for real-time updates
                        with st.status("Continuing research...", expanded=True) as status:
                            # Create and set progress reporter
                            progress_reporter = ProgressReporter(status)
                            set_progress_reporter(progress_reporter)
                            
                            # Show current tracking status
                            progress_reporter.update("🔍 Starting research iteration...")
                            
                            # Get initial status
                            initial_status = workflow_tracker.get_current_status()
                            progress_reporter.update_metrics(
                                initial_status['total_operations'], 
                                initial_status['total_llm_calls']
                            )
                            
                            # Execute workflow
                            result = workflow_orchestrator.execute_workflow("", {})
                            
                            # Show final status
                            final_status = workflow_tracker.get_current_status()
                            progress_reporter.success(
                                f"Completed - Operations: {final_status['total_operations']} | "
                                f"LLM Calls: {final_status['total_llm_calls']} | "
                                f"Time: {final_status['elapsed_minutes']:.1f} min"
                            )
                            
                            # Clear progress reporter
                            set_progress_reporter(None)
                            
                            st.session_state.workflow_state = result
                            status.update(label="Research iteration complete!", state="complete")
                            st.rerun()
            
            with col2:
                all_sufficient = all(r.get('validation', {}).get('sufficient', False) for r in data)
                completed_tasks = sum(1 for r in data if r.get('validation', {}).get('sufficient', False))
                total_tasks = len(data)
                
                # Allow report generation if at least some tasks have findings
                # Try multiple sources for scratchpads
                scratchpads = workflow_state.get('scratchpads', {})
                if not scratchpads and 'loaded_state' in workflow_state:
                    scratchpads = workflow_state['loaded_state'].get('scratchpads', {})
                if not scratchpads:
                    # Try to get from workflow orchestrator
                    scratchpads = workflow_orchestrator.workflow.workflow_state.get('scratchpads', {})
                
                has_findings = any(
                    scratchpad.get('high_value_findings') or scratchpad.get('insights') 
                    for scratchpad in scratchpads.values()
                )
                
                button_text = "📝 Generate Report →" if all_sufficient else f"📝 Generate Partial Report ({completed_tasks}/{total_tasks} complete)"
                
                if st.button(button_text, type="primary", disabled=not has_findings):
                    with st.spinner("Generating comprehensive report..."):
                        workflow_orchestrator.current_stage = 'report_generation'
                        result = workflow_orchestrator.execute_workflow("", {})
                        st.session_state.workflow_state = result
                        st.rerun()
        
        elif stage == 'report_generation':
            st.markdown("### Step 4: Research Report")
            
            data = workflow_state.get('data', {})
            report = data.get('report', 'No report generated')
            metadata = data.get('metadata', {})
            
            # Report metadata
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Subtasks Completed", metadata.get('subtasks_completed', 0))
            with col2:
                st.metric("Documents Analyzed", metadata.get('documents_analyzed', 0))
            with col3:
                generated_at = metadata.get('generated_at', datetime.now().isoformat())
                st.metric("Generated", datetime.fromisoformat(generated_at).strftime("%Y-%m-%d %H:%M"))
            
            # Report actions
            col1, col2, col3 = st.columns(3)
            with col1:
                # Download button
                st.download_button(
                    label="📥 Download Report (Markdown)",
                    data=report,
                    file_name=f"research_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )
            
            with col2:
                # Copy to clipboard functionality
                if st.button("📋 Copy to Clipboard"):
                    st.write("Report copied! (Use Ctrl+A, Ctrl+C on the report below)")
                    st.info("Select all text below and copy")
            
            with col3:
                # Start new research
                if st.button("🔄 New Research"):
                    st.session_state.workflow_state = None
                    st.session_state.clarification_responses = {}
                    workflow_orchestrator.current_stage = 'inquiry_clarification'
                    # Reset workflow persistence to force new session creation
                    workflow_persistence.current_session_dir = None
                    st.rerun()
            
            # Display report
            st.divider()
            st.markdown("## 📄 Research Report")
            
            # Show file location
            if workflow_persistence.current_session_dir:
                report_path = workflow_persistence.current_session_dir / "05_final_report.md"
                st.caption(f"📁 Report saved to: {report_path}")
            
            # Report container with custom styling
            st.markdown(
                """
                <style>
                .report-container {
                    background-color: #f8f9fa;
                    padding: 2rem;
                    border-radius: 10px;
                    margin: 1rem 0;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            
            with st.container():
                st.markdown(report)

else:
    # Quick Search Interface (existing functionality)
    query = st.text_input(
        "Enter your search query:",
        value=st.session_state.get('query_rerun', ''),
        placeholder="Search for concepts, topics, or ask questions..."
    )
    
    # Clear query_rerun after use
    if 'query_rerun' in st.session_state:
        del st.session_state.query_rerun
    
    col1, col2 = st.columns([1, 5])
    with col1:
        search_button = st.button("🔍 Search", type="primary")
    with col2:
        if st.session_state.current_results:
            if st.button("🔄 Clear Results"):
                st.session_state.current_results = None
                st.rerun()
    
    if search_button and query:
        with st.spinner("Searching intelligently..."):
            # Perform enhanced search
            results_list = search_engine.search_content(query)
            
            # Parse query intent for additional info
            query_intent = search_engine.parse_query_intent(query)
            
            # Generate synthesized answer if results found
            answer_data = None
            if results_list:
                answer_data = search_engine.synthesize_answer(query, results_list)
            
            # Format results in expected structure
            results = {
                'results': results_list,
                'query_analysis': {
                    'intent': query_intent.get('intent_type', 'information_seeking'),
                    'entities': query_intent.get('key_entities', []),
                    'search_type': query_intent.get('expected_answer_type', 'synthesized_answer'),
                    'expanded_terms': query_intent.get('expanded_query', {}).get('expanded_tokens', [])
                },
                'answer': answer_data.get('answer') if answer_data else None,
                'answer_confidence': answer_data.get('confidence', 0) if answer_data else 0,
                'total_clusters': answer_data.get('clusters_found', 0) if answer_data else 0,
                'related_queries': []  # Could be enhanced with query suggestions
            }
            
            # Store in session state
            st.session_state.current_results = results
            st.session_state.search_history.append({
                'query': query,
                'timestamp': datetime.now(),
                'results_count': len(results_list)
            })
    
    # Display results
    if st.session_state.current_results:
        results = st.session_state.current_results
        
        # Query analysis (if enabled)
        if st.session_state.show_analysis and 'query_analysis' in results:
            with st.expander("🔍 Query Analysis", expanded=True):
                analysis = results['query_analysis']
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.markdown("**Intent:**")
                    st.info(analysis.get('intent', 'General search'))
                
                with col2:
                    st.markdown("**Key Entities:**")
                    entities = analysis.get('entities', [])
                    if entities:
                        for entity in entities[:5]:
                            st.write(f"• {entity}")
                    else:
                        st.write("No specific entities")
                
                with col3:
                    st.markdown("**Expanded Terms:**")
                    expanded = analysis.get('expanded_terms', [])
                    if expanded:
                        for term in expanded[:5]:
                            st.write(f"• {term}")
                    else:
                        st.write("No expansions")
                
                with col4:
                    st.markdown("**Search Strategy:**")
                    st.success(analysis.get('search_type', 'Keyword search'))
        
        # Results summary with enhanced info
        total_results = len(results['results'])
        unique_clusters = len(set(r.get('cluster_id', i) for i, r in enumerate(results['results'])))
        st.markdown(f"### Found {total_results} relevant results in {unique_clusters} topic clusters")
        
        if results.get('answer'):
            st.markdown("#### 💡 AI-Generated Answer")
            col1, col2 = st.columns([5, 1])
            with col1:
                st.info(results['answer'])
            with col2:
                confidence = results.get('answer_confidence', 0) * 100
                st.metric("Confidence", f"{confidence:.0f}%")
            st.divider()
        
        # Display results
        if results['results']:
            st.markdown("#### 📄 Relevant Documents")
            
            for i, result in enumerate(results['results']):
                # Extract content data from nested structure
                content_data = result.get('content', {})
                title = content_data.get('title', 'Untitled')
                category = content_data.get('category', 'Uncategorized')
                
                # Show cluster indicator for non-primary results
                cluster_info = ""
                if result.get('cluster_size', 1) > 1 and not result.get('is_cluster_primary'):
                    cluster_info = " 🔗"
                
                with st.expander(f"**{title}**{cluster_info} - {category}", expanded=(i < 3)):
                    # Result metadata
                    col1, col2, col3 = st.columns([2, 1, 1])
                    with col1:
                        if content_data.get('author'):
                            st.write(f"**Author:** {content_data['author']}")
                        st.write(f"**Match Type:** {result.get('match_type', 'keyword')}")
                        
                        # Show matched terms
                        if result.get('matched_terms'):
                            matched = ", ".join(result['matched_terms'][:5])
                            st.write(f"**Matched:** {matched}")
                    with col2:
                        score = result.get('final_score', result.get('score', 0))
                        st.metric("Relevance", f"{score:.2f}")
                    with col3:
                        if result.get('cluster_size', 1) > 1:
                            st.metric("Similar Docs", result['cluster_size'] - 1)
                    
                    # Key concepts and entities
                    if content_data.get('entities') or content_data.get('concepts'):
                        col1, col2 = st.columns(2)
                        with col1:
                            if content_data.get('entities'):
                                st.markdown("**Key Entities:**")
                                for entity in content_data['entities'][:5]:
                                    st.write(f"• {entity}")
                        with col2:
                            if content_data.get('concepts'):
                                st.markdown("**Key Concepts:**")
                                for concept in content_data['concepts'][:5]:
                                    st.write(f"• {concept}")
                    
                    # Content preview
                    st.markdown("**Content Preview:**")
                    body = content_data.get('body', '')
                    preview_length = 500
                    if len(body) > preview_length:
                        st.write(body[:preview_length] + "...")
                        if st.button(f"Read more", key=f"more_{i}"):
                            st.write(body)
                    else:
                        st.write(body)
                    
                    # Related topics
                    if content_data.get('related_topics'):
                        st.markdown("**Related Topics:**")
                        related = ", ".join(content_data['related_topics'][:5])
                        st.write(related)
                    
                    # File path
                    st.caption(f"📁 {result.get('file_key', 'Unknown path')}")
        
        # Related searches
        if results.get('related_queries'):
            st.divider()
            st.markdown("#### 🔗 Related Searches")
            cols = st.columns(3)
            for i, related_query in enumerate(results['related_queries'][:6]):
                with cols[i % 3]:
                    if st.button(related_query, key=f"related_{i}"):
                        st.session_state.query_rerun = related_query
                        st.rerun()
        
        else:
            st.warning("No results found. Try rephrasing your query or using different keywords.")

# Footer
st.divider()
st.caption("Intelligent Search powered by AI - Continuously learning from your knowledge base")