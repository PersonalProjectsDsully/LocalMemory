"""
UI Components Module

Contains reusable UI components for the Intelligent Search page.
"""

import streamlit as st
from datetime import datetime
from pathlib import Path
import json


def render_sidebar(search_engine, workflow_orchestrator, workflow_persistence, workflow_tracker, settings_manager):
    """Render the sidebar with search options and settings"""
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
            render_quick_search_options(search_engine)
        else:
            # Research workflow options
            render_research_workflow_options(workflow_persistence, workflow_orchestrator, workflow_tracker)
        
        # Search history
        st.divider()
        display_search_history()


def render_quick_search_options(search_engine):
    """Render quick search specific options"""
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
    
    # QA and improvement settings
    st.subheader("Quality Assurance")
    
    enable_qa = st.checkbox(
        "Enable QA Improvement",
        value=st.session_state.get('enable_qa_improvement', True),
        help="Automatically analyze and improve generated reports"
    )
    st.session_state.enable_qa_improvement = enable_qa
    
    if enable_qa:
        qa_config = st.selectbox(
            "QA Configuration",
            options=["basic", "comprehensive", "trust_focused", "suggest_only"],
            index=1,  # Default to comprehensive
            help="Basic: Fast accuracy check\nComprehensive: Full analysis\nTrust-focused: Enhanced trust scoring\nSuggest only: No auto-fixes"
        )
        st.session_state.qa_config = qa_config
        
        # Configure the search engine's QA system
        search_engine.configure_qa_system(qa_config)
    
    st.divider()
    
    # Thesaurus settings
    st.subheader("🔤 Synonym Expansion")
    
    use_thesaurus = st.checkbox(
        "Enable Thesaurus Expansion",
        value=st.session_state.get('use_thesaurus', True),
        help="Automatically expand your search with synonyms from Moby Thesaurus"
    )
    st.session_state.use_thesaurus = use_thesaurus
    
    if use_thesaurus:
        col1, col2 = st.columns(2)
        with col1:
            expansion_weight = st.slider(
                "Expansion Weight",
                min_value=0.0,
                max_value=1.0,
                value=st.session_state.get('expansion_weight', 0.7),
                step=0.1,
                help="How much to weight synonym-based results (0=ignore, 1=equal weight)"
            )
            st.session_state.expansion_weight = expansion_weight
        
        with col2:
            max_synonyms = st.number_input(
                "Max Synonyms per Word",
                min_value=1,
                max_value=10,
                value=st.session_state.get('max_synonyms', 3),
                help="Maximum number of synonyms to use for each word"
            )
            st.session_state.max_synonyms = max_synonyms
        
        # Check thesaurus health
        if hasattr(search_engine, 'health_check'):
            health = search_engine.health_check()
            if health.get('thesaurus_health', {}).get('initialized'):
                st.success(f"✅ Thesaurus loaded: {health['thesaurus_health'].get('total_words', 0):,} words")
            else:
                st.warning("⚠️ Thesaurus not fully initialized - synonym expansion may be limited")
    
    st.divider()
    
    # Batch processing section
    st.header("Content Enhancement")
    if st.button("🚀 Process All Content", type="secondary"):
        with st.spinner("Processing all documents..."):
            from utils.content.batch_intelligence_processor import process_existing_content
            stats = process_existing_content()
            st.success(f"Processed {stats['processed']} documents!")
            st.json(stats)


def render_research_workflow_options(workflow_persistence, workflow_orchestrator, workflow_tracker):
    """Render research workflow specific options"""
    st.info("Research Workflow will guide you through a comprehensive research process")
    
    # Previous sessions
    st.divider()
    st.subheader("Previous Research Sessions")
    sessions = workflow_persistence.list_sessions()
    
    if sessions:
        session_names = [f"{s['created_at'][:10]} - {s['original_query'][:50]}..." for s in sessions[:5]]
        selected_session = st.selectbox("Load previous session:", ["Select a session..."] + session_names)
        
        if selected_session and selected_session != "Select a session..." and st.button("Load Session"):
            handle_session_load(selected_session, session_names, sessions, workflow_persistence, 
                              workflow_orchestrator, workflow_tracker)
    
    if st.session_state.workflow_state:
        display_workflow_progress(workflow_orchestrator, workflow_tracker, workflow_persistence)


def handle_session_load(selected_session, session_names, sessions, workflow_persistence, 
                       workflow_orchestrator, workflow_tracker):
    """Handle loading a previous research session"""
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
            restore_estimated_tracking(loaded_state, workflow_tracker)
        
        # Determine current stage and update session state
        determine_workflow_stage(loaded_state, workflow_orchestrator, session)
        
        st.success(f"Loaded session: {session['original_query'][:50]}...")
        st.rerun()


def restore_estimated_tracking(loaded_state, workflow_tracker):
    """Restore estimated tracking data from loaded state"""
    scratchpads = loaded_state.get('scratchpads', {})
    document_analysis = loaded_state.get('document_analysis', {})
    
    # Estimate operations based on content
    estimated_llm_calls = sum(len(sp.get('high_value_findings', [])) + len(sp.get('insights', [])) 
                            for sp in scratchpads.values())
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


def determine_workflow_stage(loaded_state, workflow_orchestrator, session):
    """Determine the current workflow stage from loaded state"""
    if loaded_state.get('final_report'):
        # Check if workflow is marked as completed
        is_completed = loaded_state.get('report_completed', False) or loaded_state.get('force_completed', False)
        stage = 'complete' if is_completed else 'report_generation'
        
        workflow_orchestrator.current_stage = 'report_generation' if not is_completed else 'complete'
        
        # Ensure workflow_orchestrator has the loaded state for QA access
        if hasattr(workflow_orchestrator, 'workflow') and hasattr(workflow_orchestrator.workflow, 'workflow_state'):
            workflow_orchestrator.workflow.workflow_state.update(loaded_state)
        
        st.session_state.workflow_state = {
            'stage': stage,
            'data': {
                'report': loaded_state['final_report'],
                'metadata': {
                    'generated_at': session.get('last_updated', datetime.now().isoformat()),
                    'subtasks_completed': len(loaded_state.get('subtasks', [])),
                    'documents_analyzed': len(loaded_state.get('document_analysis', {}))
                },
                'forced_complete': loaded_state.get('force_completed', False)
            },
            'loaded_state': loaded_state
        }
    elif loaded_state.get('document_analysis'):
        handle_document_research_stage(loaded_state, workflow_orchestrator, session)
    elif loaded_state.get('subtasks'):
        handle_task_decomposition_stage(loaded_state, workflow_orchestrator)


def handle_document_research_stage(loaded_state, workflow_orchestrator, session):
    """Handle document research stage restoration"""
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
        'scratchpads': scratchpads,
        'document_analysis': document_analysis,
        'loaded_state': loaded_state
    }


def handle_task_decomposition_stage(loaded_state, workflow_orchestrator):
    """Handle task decomposition stage restoration"""
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


def display_workflow_progress(workflow_orchestrator, workflow_tracker, workflow_persistence):
    """Display workflow progress and tracking"""
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


def display_search_history():
    """Display search history in the sidebar"""
    st.header("Search History")
    if st.session_state.search_history:
        for i, search in enumerate(st.session_state.search_history[-5:][::-1]):
            with st.expander(f"{search['query'][:30]}...", expanded=False):
                st.caption(f"Time: {search['timestamp']}")
                st.caption(f"Results: {search['num_results']}")
                if st.button(f"Load", key=f"load_{i}"):
                    st.session_state.current_results = search['results']
                    st.rerun()


def format_search_results(results, query):
    """Format search results for display"""
    if not results:
        return None
    
    # Add to search history
    st.session_state.search_history.append({
        'query': query,
        'results': results,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'num_results': len(results.get('results', []))
    })
    
    return results


def render_result_item(result, idx):
    """Render a single search result item"""
    with st.expander(f"{idx+1}. {result['title']}", expanded=(idx < 3)):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**Category:** {result.get('category', 'Unknown')}")
            if result.get('author'):
                st.caption(f"Author: {result['author']}")
            if result.get('created_at'):
                st.caption(f"Created: {result['created_at']}")
        
        with col2:
            score = result.get('similarity_score', 0)
            st.metric("Relevance", f"{score:.1%}")
            
            # Show reasoning if available
            if result.get('reasoning'):
                with st.popover("📊 Scoring Details"):
                    st.json(result['reasoning'])
        
        # Content preview
        st.divider()
        content = result.get('content', {})
        if isinstance(content, dict) and 'body' in content:
            preview = content['body'][:500] + "..." if len(content['body']) > 500 else content['body']
            st.markdown(preview)
        
        # Highlights
        if result.get('highlights'):
            st.markdown("**Key Highlights:**")
            for highlight in result['highlights'][:3]:
                st.markdown(f"- {highlight}")
        
        # Show intelligent features if available
        if result.get('ai_summary'):
            with st.expander("🤖 AI Summary"):
                st.markdown(result['ai_summary'])
        
        if result.get('key_topics'):
            st.markdown("**Key Topics:** " + ", ".join(result['key_topics']))