# Intelligent Search Module Components
"""
This package contains the refactored components of the Intelligent Search page.
The original monolithic file has been split into logical modules for better
maintainability and organization.
"""

from .report_processing import (
    is_report_incomplete,
    complete_incomplete_report
)

from .qa_quality import (
    parse_qa_response_manually,
    extract_json_aggressively,
    safe_improvement_pipeline_call
)

from .session_management import (
    update_improvement_session_state,
    get_unique_key,
    backup_session_state,
    restore_session_state,
    log_qa_operation
)

from .ui_components import (
    render_sidebar,
    display_search_history,
    format_search_results,
    render_result_item
)

from .workflow_ui import (
    render_research_workflow,
    display_workflow_tracking,
    process_subtasks_ui
)

from .quick_search_ui import (
    render_quick_search,
    display_search_results,
    display_qa_improvements
)

__all__ = [
    # Report processing
    'is_report_incomplete',
    'complete_incomplete_report',
    
    # QA quality
    'parse_qa_response_manually',
    'extract_json_aggressively',
    'safe_improvement_pipeline_call',
    
    # Session management
    'update_improvement_session_state',
    'get_unique_key',
    'backup_session_state',
    'restore_session_state',
    'log_qa_operation',
    
    # UI components
    'render_sidebar',
    'display_search_history',
    'format_search_results',
    'render_result_item',
    
    # Workflow UI
    'render_research_workflow',
    'display_workflow_tracking',
    'process_subtasks_ui',
    
    # Quick search UI
    'render_quick_search',
    'display_search_results',
    'display_qa_improvements'
]