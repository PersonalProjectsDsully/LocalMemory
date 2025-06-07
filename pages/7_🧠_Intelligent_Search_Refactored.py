"""
Intelligent Search - Refactored Version

This is the refactored version of the Intelligent Search page, split into modular components
for better maintainability and organization.
"""

import streamlit as st
from datetime import datetime
from pathlib import Path

# Import refactored modules
from intelligent_search_modules import (
    # Core functionality
    is_report_incomplete,
    complete_incomplete_report,
    parse_qa_response_manually,
    extract_json_aggressively,
    safe_improvement_pipeline_call,
    
    # Session management
    update_improvement_session_state,
    get_unique_key,
    backup_session_state,
    restore_session_state,
    log_qa_operation,
    
    # UI components
    render_sidebar,
    display_search_history,
    format_search_results,
    render_result_item,
    
    # Workflow UI
    render_research_workflow,
    display_workflow_tracking,
    process_subtasks_ui,
    
    # Quick search UI
    render_quick_search,
    display_search_results,
    display_qa_improvements
)

# Import utilities
try:
    from utils.search.enhanced_search_thesaurus import EnhancedIntelligentSearchEngine as ThesaurusSearchEngine
    search_engine = ThesaurusSearchEngine(use_cache=True, cache_size=10000)
    print("Using thesaurus-enhanced search engine with synonym expansion")
except ImportError:
    try:
        from utils.search.intelligent_search_refined import get_refined_search_engine
        search_engine = get_refined_search_engine()
        print("Using refined search engine with improved scoring and intent handling")
    except ImportError:
        from utils.search.intelligent_search_enhanced import EnhancedIntelligentSearchEngine
        search_engine = EnhancedIntelligentSearchEngine()
        print("Using standard enhanced search engine")

try:
    from utils.research.workflow_orchestrator import WorkflowOrchestrator
except ImportError as e:
    st.error(f"Import error: {e}")
    st.error("Please restart the Streamlit app to reload the modules.")
    st.stop()

from utils.session.workflow_persistence import workflow_persistence
from utils.session.workflow_tracker import workflow_tracker
from utils.session.progress_reporter import ProgressReporter, set_progress_reporter
from utils.session.session_state_manager import initialize_session_state
from utils.session.settings_manager import settings_manager
from utils.content.batch_intelligence_processor import process_existing_content

# Page configuration
st.set_page_config(
    page_title="Intelligent Search - Personal Knowledge Base",
    page_icon="🧠",
    layout="wide"
)

def main():
    """Main application entry point"""
    # Page title and description
    st.title("🧠 Intelligent Search")
    st.markdown("Advanced AI-powered search with comprehensive research workflow")
    
    # Initialize components
    workflow_orchestrator = WorkflowOrchestrator()
    
    # Initialize session state
    initialize_session_state()
    
    # Initialize page-specific session state
    initialize_page_session_state()
    
    # Get settings
    settings = settings_manager.load_settings()
    
    # Render sidebar with options
    render_sidebar(search_engine, workflow_orchestrator, workflow_persistence, 
                  workflow_tracker, settings_manager)
    
    # Main content area
    if st.session_state.workflow_mode:
        # Research Workflow Mode
        render_research_workflow(workflow_orchestrator, workflow_persistence, workflow_tracker)
    else:
        # Quick Search Mode
        render_quick_search(search_engine, workflow_orchestrator)


def initialize_page_session_state():
    """Initialize page-specific session state variables"""
    defaults = {
        'search_history': [],
        'current_results': None,
        'show_analysis': False,
        'workflow_mode': False,
        'workflow_state': None,
        'clarification_responses': {},
        'prefill_task': None,
        'prefill_task_used': False,
        'qa_session_id': None
    }
    
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value


if __name__ == "__main__":
    main()