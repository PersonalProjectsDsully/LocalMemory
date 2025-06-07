"""
Workflow UI Module

Handles the research workflow interface components.
"""

import streamlit as st
from datetime import datetime
import json
import copy
from pathlib import Path


def render_research_workflow(workflow_orchestrator, workflow_persistence, workflow_tracker):
    """Render the main research workflow interface"""
    st.header("🔬 Comprehensive Research Workflow")
    
    if not st.session_state.workflow_state:
        render_initial_query_input(workflow_orchestrator, workflow_persistence, workflow_tracker)
    else:
        handle_workflow_stages(workflow_orchestrator, workflow_persistence)


def render_initial_query_input(workflow_orchestrator, workflow_persistence, workflow_tracker):
    """Render the initial query input interface"""
    st.markdown("### Step 1: Describe Your Research Need")
    query = st.text_area(
        "What would you like to research?",
        placeholder="Enter a detailed description of what you want to learn or investigate...",
        height=100
    )
    
    if st.button("🚀 Start Research", type="primary", disabled=not query):
        with st.spinner("Analyzing your request..."):
            try:
                # Clear all workflow-related session state to start fresh
                workflow_keys_to_clear = [
                    'workflow_state',
                    'research_workflow',
                    'workflow_tracking',
                    'editable_decomposition',
                    'pending_tasks',
                    'completed_tasks'
                ]
                
                for key in workflow_keys_to_clear:
                    if key in st.session_state:
                        del st.session_state[key]
                
                # Reset workflow persistence to ensure new session
                workflow_persistence.current_session_dir = None
                
                # Clear workflow tracker state if available
                if hasattr(workflow_tracker, 'reset'):
                    workflow_tracker.reset()
                
                # Create a new workflow orchestrator instance to ensure clean state
                from utils.research.workflow_orchestrator import WorkflowOrchestrator
                new_workflow_orchestrator = WorkflowOrchestrator(query)
                
                # Execute the new workflow
                result = new_workflow_orchestrator.execute_workflow(query)
                st.session_state.workflow_state = result
                
                # Update the main workflow_orchestrator reference
                workflow_orchestrator = new_workflow_orchestrator
                
                st.rerun()
            except Exception as e:
                st.error(f"Failed to start research: {str(e)}")
                print(f"Workflow execution error: {e}")


def handle_workflow_stages(workflow_orchestrator, workflow_persistence):
    """Handle different workflow stages"""
    workflow_state = st.session_state.workflow_state
    stage = workflow_state['stage']
    
    if stage == 'inquiry_clarification':
        handle_inquiry_clarification(workflow_orchestrator, workflow_state)
    elif stage == 'task_decomposition':
        handle_task_decomposition(workflow_orchestrator, workflow_state, workflow_persistence)
    elif stage == 'document_research':
        handle_document_research(workflow_orchestrator, workflow_state, workflow_persistence)
    elif stage == 'report_generation' or stage == 'complete':
        handle_report_generation(workflow_orchestrator, workflow_state, workflow_persistence)


def handle_inquiry_clarification(workflow_orchestrator, workflow_state):
    """Handle the inquiry clarification stage"""
    st.markdown("### Step 1: Clarifying Your Research Request")
    
    data = workflow_state['data']
    
    # Handle parse errors - try to extract data from raw_response
    if data.get('parse_error') and 'raw_response' in data:
        try:
            raw_data = json.loads(data['raw_response'])
            data.update(raw_data)
        except:
            st.warning("There was an issue parsing the clarification questions. Proceeding with defaults.")
            data['clarifying_questions'] = []
            data['query_analysis'] = {
                'main_topic': 'AI Agents vs Other AI Systems',
                'implicit_needs': ['Comparison of approaches', 'Use cases', 'Implementation guidance']
            }
    
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
    clarifying_questions = data.get('clarifying_questions', [])
    
    if clarifying_questions:
        st.markdown("**Please answer these questions to help refine your research:**")
        
        for i, question_data in enumerate(clarifying_questions):
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
    else:
        st.info("No clarifying questions needed. Proceeding with the analysis of your request.")
    
    # Suggested refinement
    if 'suggested_refinement' in data:
        st.info(f"💡 Suggested refined request: {data['suggested_refinement']}")
    
    # Continue button
    all_answered = True  # Default to true if no questions
    if clarifying_questions:
        all_answered = all(
            st.session_state.clarification_responses.get(q['question']) 
            for q in clarifying_questions
        )
    
    if st.button("Continue to Task Planning →", type="primary", disabled=not all_answered):
        with st.spinner("Planning research tasks..."):
            handle_clarification_submission(workflow_orchestrator, clarifying_questions)


def handle_clarification_submission(workflow_orchestrator, clarifying_questions):
    """Handle submission of clarification responses"""
    # Build clarified request from user responses before proceeding
    original_query = workflow_orchestrator.workflow.workflow_state.get('original_query', '')
    clarified_request = ""
    
    if clarifying_questions and st.session_state.clarification_responses:
        responses = []
        for q in clarifying_questions:
            question = q['question']
            answer = st.session_state.clarification_responses.get(question, "")
            if answer and answer.strip():
                responses.append(f"Q: {question}\nA: {answer}")
        
        if responses:
            clarified_request = f"Original query: {original_query}\n\nClarifications:\n" + "\n\n".join(responses)
        else:
            clarified_request = f"Original query: {original_query}\n\n(No additional clarifications provided)"
    else:
        clarified_request = f"Original query: {original_query}\n\n(No additional clarifications provided)"
    
    # Set the clarified request in workflow state before changing stage
    if clarified_request and len(clarified_request.strip()) > 10:
        workflow_orchestrator.workflow.workflow_state['clarified_request'] = clarified_request
        workflow_orchestrator.workflow.workflow_state['current_stage'] = 'task_decomposition'
        workflow_orchestrator.current_stage = 'task_decomposition'
        
        # Save the updated workflow state with new stage
        from utils.session.workflow_persistence import workflow_persistence
        workflow_persistence.save_workflow_state(workflow_orchestrator.workflow.workflow_state)
        
        result = workflow_orchestrator.execute_workflow(
            "", 
            st.session_state.clarification_responses
        )
        st.session_state.workflow_state = result
        st.rerun()
    else:
        st.error("Please provide valid responses to all questions to continue.")


def handle_task_decomposition(workflow_orchestrator, workflow_state, workflow_persistence):
    """Handle the task decomposition stage"""
    st.markdown("### Step 2: Research Task Planning")
    
    data = workflow_state['data']
    decomposition = data['decomposition']
    verification = data['verification']
    
    # Initialize editable decomposition in session state if not exists
    if 'editable_decomposition' not in st.session_state:
        st.session_state.editable_decomposition = copy.deepcopy(decomposition)
        st.session_state.task_edits = {}
        
        # Ensure subtasks key exists
        if 'subtasks' not in st.session_state.editable_decomposition:
            st.session_state.editable_decomposition['subtasks'] = decomposition.get('subtasks', [])
    
    # Show verification status
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Completeness", f"{verification.get('completeness_score', 0)}%")
    with col2:
        st.metric("Tasks", len(st.session_state.editable_decomposition.get('subtasks', [])))
    with col3:
        status = "✅ Approved" if verification.get('approved') else "❌ Needs Review"
        st.metric("Status", status)
    
    # Display subtasks with edit capability
    st.markdown("**Research Tasks:**")
    
    subtasks = st.session_state.editable_decomposition.get('subtasks', [])
    for i, task in enumerate(subtasks):
        with st.container():
            col1, col2 = st.columns([4, 1])
            
            with col1:
                # Check if we're editing this task
                edit_key = f"edit_{task['id']}"
                if st.session_state.task_edits.get(edit_key, False):
                    # Edit mode
                    new_title = st.text_input("Title:", value=task['title'], key=f"title_{task['id']}")
                    new_desc = st.text_area("Description:", value=task['description'], key=f"desc_{task['id']}")
                    
                    col_save, col_cancel = st.columns(2)
                    with col_save:
                        if st.button("💾 Save", key=f"save_{task['id']}"):
                            task['title'] = new_title
                            task['description'] = new_desc
                            st.session_state.task_edits[edit_key] = False
                            st.rerun()
                    with col_cancel:
                        if st.button("❌ Cancel", key=f"cancel_{task['id']}"):
                            st.session_state.task_edits[edit_key] = False
                            st.rerun()
                else:
                    # View mode
                    st.markdown(f"**{i+1}. {task['title']}**")
                    st.write(task['description'])
                    st.caption(f"Priority: {task.get('priority', 'Normal')} | Estimated time: {task.get('estimated_time', 'Unknown')}")
            
            with col2:
                if not st.session_state.task_edits.get(edit_key, False):
                    if st.button("✏️ Edit", key=f"edit_btn_{task['id']}"):
                        st.session_state.task_edits[edit_key] = True
                        st.rerun()
                    
                    if st.button("🗑️ Delete", key=f"del_{task['id']}"):
                        subtasks.remove(task)
                        st.rerun()
    
    # Add new task button
    if st.button("➕ Add New Task"):
        new_task = {
            'id': f"task_{len(subtasks)+1}",
            'title': "New Research Task",
            'description': "Enter task description here",
            'priority': 'normal',
            'estimated_time': '30 minutes'
        }
        subtasks.append(new_task)
        st.session_state.task_edits[f"edit_{new_task['id']}"] = True
        st.rerun()
    
    # Gaps and suggestions
    if verification.get('gaps'):
        with st.expander("🔍 Identified Gaps", expanded=True):
            for gap in verification['gaps']:
                st.warning(f"- {gap}")
    
    if verification.get('suggestions'):
        with st.expander("💡 Suggestions", expanded=True):
            for suggestion in verification['suggestions']:
                st.info(f"- {suggestion}")
    
    # Continue button
    col1, col2 = st.columns(2)
    with col2:
        if st.button("Proceed to Research →", type="primary", disabled=len(subtasks) == 0):
            with st.spinner("Starting document research..."):
                # Update workflow state with edited tasks
                workflow_orchestrator.workflow.workflow_state['subtasks'] = subtasks
                workflow_orchestrator.current_stage = 'document_research'
                
                # Execute next stage
                result = workflow_orchestrator.execute_workflow("")
                st.session_state.workflow_state = result
                st.rerun()


def handle_document_research(workflow_orchestrator, workflow_state, workflow_persistence):
    """Handle the document research stage"""
    st.markdown("### Step 3: Document Research & Analysis")
    
    research_results = workflow_state['data']
    
    # Progress overview
    total_tasks = len(research_results)
    completed_tasks = sum(1 for r in research_results if r['validation']['sufficient'])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Tasks", total_tasks)
    with col2:
        st.metric("Completed", completed_tasks)
    with col3:
        progress_pct = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        st.metric("Progress", f"{progress_pct:.0f}%")
    
    st.progress(completed_tasks / total_tasks if total_tasks > 0 else 0)
    
    # Display research results for each subtask
    for result in research_results:
        subtask = result['subtask']
        research = result['research']
        validation = result['validation']
        
        status_icon = "✅" if validation['sufficient'] else "🔄"
        
        with st.expander(f"{status_icon} {subtask['title']}", expanded=not validation['sufficient']):
            # Validation status
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.write(subtask['description'])
                
                # Research findings
                if research.get('analysis', {}).get('document_analyses'):
                    st.markdown("**Key Findings:**")
                    for doc in research['analysis']['document_analyses'][:3]:
                        st.markdown(f"- **{doc.get('document_title', 'Unknown')}**: {doc.get('relevance_assessment', 'No assessment')}")
                
                # Show insights if available
                if 'scratchpads' in workflow_state:
                    scratchpad = workflow_state['scratchpads'].get(subtask['id'], {})
                    if scratchpad.get('insights'):
                        st.markdown("**Insights:**")
                        for insight in scratchpad['insights'][:3]:
                            st.markdown(f"- {insight}")
            
            with col2:
                st.metric("Completeness", f"{validation.get('completeness_score', 0)}%")
                st.metric("Documents", research.get('documents_found', 0))
                
                if validation.get('missing_elements'):
                    st.warning("Missing elements:")
                    for element in validation['missing_elements']:
                        st.caption(f"- {element}")
            
            # Re-run research button for incomplete tasks
            if not validation['sufficient']:
                if st.button(f"🔄 Re-run Research", key=f"rerun_{subtask['id']}"):
                    with st.spinner(f"Re-researching: {subtask['title']}..."):
                        # Re-execute research for this specific task
                        st.info("Re-running research for this task...")
                        # Note: Implementation would trigger workflow to re-research this task
    
    # Continue to report generation
    if st.button("Generate Final Report →", type="primary"):
        with st.spinner("Generating comprehensive report..."):
            workflow_orchestrator.current_stage = 'report_generation'
            result = workflow_orchestrator.execute_workflow("")
            st.session_state.workflow_state = result
            st.rerun()


def handle_report_generation(workflow_orchestrator, workflow_state, workflow_persistence):
    """Handle the report generation/completion stage"""
    st.markdown("### Step 4: Final Research Report")
    
    data = workflow_state['data']
    report = data.get('report', '')
    metadata = data.get('metadata', {})
    
    # Check if report is incomplete
    from .report_processing import is_report_incomplete, complete_incomplete_report
    
    is_incomplete = is_report_incomplete(report)
    is_completed = workflow_state.get('stage') == 'complete' or data.get('forced_complete', False)
    
    # Show metadata
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Generated", metadata.get('generated_at', 'Unknown')[:10])
    with col2:
        st.metric("Tasks Completed", metadata.get('subtasks_completed', 0))
    with col3:
        st.metric("Documents Analyzed", metadata.get('documents_analyzed', 0))
    
    # Report status and actions
    if is_incomplete and not is_completed:
        st.warning("⚠️ The report appears to be incomplete. You can:")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 Complete Report", type="primary"):
                with st.spinner("Completing report..."):
                    # Get workflow state for context
                    loaded_state = workflow_state.get('loaded_state')
                    if not loaded_state and hasattr(workflow_orchestrator, 'workflow'):
                        loaded_state = workflow_orchestrator.workflow.workflow_state
                    
                    completed_report = complete_incomplete_report(
                        report, 
                        workflow_orchestrator if hasattr(workflow_orchestrator, 'workflow') else None,
                        loaded_state
                    )
                    
                    if completed_report:
                        # Update the report in all relevant places
                        data['report'] = completed_report
                        workflow_state['data'] = data
                        
                        # Update workflow orchestrator state
                        if hasattr(workflow_orchestrator, 'workflow') and hasattr(workflow_orchestrator.workflow, 'workflow_state'):
                            workflow_orchestrator.workflow.workflow_state['final_report'] = completed_report
                            workflow_orchestrator.workflow.workflow_state['report_completed'] = True
                            
                            # Save the updated state
                            workflow_persistence.save_workflow_state(workflow_orchestrator.workflow.workflow_state)
                        
                        st.success("Report completed successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to complete the report. Please try regenerating.")
        
        with col2:
            if st.button("🔄 Regenerate Report"):
                with st.spinner("Regenerating report..."):
                    workflow_orchestrator.current_stage = 'report_generation'
                    result = workflow_orchestrator.execute_workflow("")
                    st.session_state.workflow_state = result
                    st.rerun()
        
        with col3:
            if st.button("✅ Mark as Complete"):
                # Force mark as complete
                workflow_state['stage'] = 'complete'
                data['forced_complete'] = True
                
                # Update workflow orchestrator state
                if hasattr(workflow_orchestrator, 'workflow') and hasattr(workflow_orchestrator.workflow, 'workflow_state'):
                    workflow_orchestrator.workflow.workflow_state['force_completed'] = True
                    workflow_orchestrator.workflow.workflow_state['report_completed'] = True
                    
                    # Save the updated state
                    workflow_persistence.save_workflow_state(workflow_orchestrator.workflow.workflow_state)
                
                st.rerun()
    
    # Display the report
    st.markdown("---")
    st.markdown(report)
    
    # Export options
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.download_button(
            label="📥 Download as Markdown",
            data=report,
            file_name=f"research_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown"
        )
    
    with col2:
        # Create a text version
        text_report = report.replace("#", "").replace("*", "").replace("-", "•")
        st.download_button(
            label="📥 Download as Text",
            data=text_report,
            file_name=f"research_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )
    
    with col3:
        if st.button("🔄 Run Manual QA Review"):
            # Trigger QA review
            st.session_state.run_manual_qa = True
            st.rerun()


def display_workflow_tracking(workflow_tracker):
    """Display workflow tracking information"""
    with st.expander("📊 Workflow Tracking", expanded=False):
        workflow_tracker.display_status()


def process_subtasks_ui(subtasks, workflow_orchestrator):
    """Process and display subtasks progress"""
    total = len(subtasks)
    completed = sum(1 for task in subtasks if task.get('completed', False))
    
    st.progress(completed / total if total > 0 else 0)
    st.metric("Progress", f"{completed}/{total} tasks completed")
    
    for task in subtasks:
        status = "✅" if task.get('completed', False) else "⏳"
        with st.expander(f"{status} {task['title']}", expanded=not task.get('completed', False)):
            st.write(task['description'])
            if task.get('results'):
                st.json(task['results'])