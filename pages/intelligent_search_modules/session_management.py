"""
Session Management Module

Handles session state management, backups, and unique key generation for the Intelligent Search page.
"""

import streamlit as st
from datetime import datetime


def update_improvement_session_state(original_report, improved_report, improvements_made, fix_type='general', fix_details=None):
    """
    Helper function to safely update improvement session state
    """
    if 'manual_improvement_applied' not in st.session_state:
        # First improvement - initialize with truly original report
        st.session_state.manual_improvement_applied = {
            'original_report': original_report,
            'improved_report': improved_report,
            'improvements_made': improvements_made,
            'individual_fixes': [],
            'layer_fixes': [],
            'timestamp': datetime.now()
        }
    else:
        # Subsequent improvements - preserve original report, update improved version
        st.session_state.manual_improvement_applied['improved_report'] = improved_report
        st.session_state.manual_improvement_applied['improvements_made'].extend(improvements_made)
        
        # Ensure arrays exist
        if 'individual_fixes' not in st.session_state.manual_improvement_applied:
            st.session_state.manual_improvement_applied['individual_fixes'] = []
        if 'layer_fixes' not in st.session_state.manual_improvement_applied:
            st.session_state.manual_improvement_applied['layer_fixes'] = []
    
    # Add specific fix details based on type
    if fix_type == 'individual' and fix_details:
        st.session_state.manual_improvement_applied['individual_fixes'].append(fix_details)
    elif fix_type == 'layer' and fix_details:
        st.session_state.manual_improvement_applied['layer_fixes'].append(fix_details)


def get_unique_key(base_key):
    """Generate unique widget key using QA session ID"""
    session_id = st.session_state.get('qa_session_id', 'default')
    return f"{base_key}_{session_id}"


def backup_session_state():
    """Create a backup of current session state for error recovery"""
    try:
        if 'manual_improvement_applied' in st.session_state:
            st.session_state._qa_backup = st.session_state.manual_improvement_applied.copy()
        return True
    except Exception as e:
        print(f"Warning: Failed to backup session state: {e}")
        return False


def restore_session_state():
    """Restore session state from backup"""
    try:
        if '_qa_backup' in st.session_state and st.session_state._qa_backup:
            st.session_state.manual_improvement_applied = st.session_state._qa_backup.copy()
            return True
        return False
    except Exception as e:
        print(f"Warning: Failed to restore session state: {e}")
        return False


def log_qa_operation(operation, details=None, error=None):
    """Log QA operations for debugging"""
    try:
        import time
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] QA Operation: {operation}"
        if details:
            log_entry += f" | Details: {details}"
        if error:
            log_entry += f" | Error: {error}"
        
        # Initialize log if it doesn't exist
        if 'qa_operation_log' not in st.session_state:
            st.session_state.qa_operation_log = []
        
        # Keep only last 50 entries
        st.session_state.qa_operation_log.append(log_entry)
        if len(st.session_state.qa_operation_log) > 50:
            st.session_state.qa_operation_log = st.session_state.qa_operation_log[-50:]
            
        print(log_entry)  # Also print to console
    except Exception as e:
        print(f"Warning: Failed to log QA operation: {e}")


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