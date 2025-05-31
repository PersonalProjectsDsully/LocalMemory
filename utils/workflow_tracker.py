"""
Workflow Tracking and Monitoring
Provides detailed tracking of research workflow operations
"""

from datetime import datetime
from typing import Dict, List, Any, Optional
import streamlit as st
from collections import defaultdict
import json
from pathlib import Path


class WorkflowTracker:
    """Tracks and monitors workflow operations to prevent loops and provide visibility"""
    
    def __init__(self):
        # Initialize tracking in session state if not exists
        self._ensure_initialized()
    
    def _ensure_initialized(self):
        """Ensure tracking is initialized in session state"""
        if 'workflow_tracking' not in st.session_state:
            st.session_state.workflow_tracking = {
                'operations': [],
                'task_iterations': defaultdict(int),
                'operation_counts': defaultdict(int),
                'start_time': datetime.now(),
                'warnings': [],
                'current_task': None,
                'total_llm_calls': 0,
                'operation_count_limit': 50  # Track only top 50 operation types
            }
    
    def track_operation(self, operation_type: str, details: Dict[str, Any]) -> None:
        """Track a workflow operation"""
        self._ensure_initialized()
        tracking = st.session_state.workflow_tracking
        
        # Create operation record
        operation = {
            'timestamp': datetime.now().isoformat(),
            'type': operation_type,
            'details': details,
            'task': tracking.get('current_task', 'unknown')
        }
        
        # Add to operations list with size limit
        tracking['operations'].append(operation)
        # Keep only last 1000 operations to prevent memory issues
        if len(tracking['operations']) > 1000:
            tracking['operations'] = tracking['operations'][-1000:]
        
        # Ensure operation_counts is a defaultdict
        if not isinstance(tracking['operation_counts'], defaultdict):
            tracking['operation_counts'] = defaultdict(int, tracking['operation_counts'])
        tracking['operation_counts'][operation_type] += 1
        
        # Cleanup operation_counts to prevent unbounded growth
        limit = tracking.get('operation_count_limit', 50)
        if len(tracking['operation_counts']) > limit:
            # Keep only the top N most frequent operations
            sorted_ops = sorted(tracking['operation_counts'].items(), 
                              key=lambda x: x[1], reverse=True)
            tracking['operation_counts'] = defaultdict(int, dict(sorted_ops[:limit]))
        
        # Track LLM calls
        if 'llm' in operation_type.lower():
            tracking['total_llm_calls'] += 1
        
        # Check for potential issues
        self._check_for_issues(operation_type, details)
        
        # Keep only last 100 operations to prevent memory issues
        if len(tracking['operations']) > 100:
            tracking['operations'] = tracking['operations'][-100:]
    
    def track_task_iteration(self, task_id: str, iteration: int) -> None:
        """Track task iterations"""
        self._ensure_initialized()
        tracking = st.session_state.workflow_tracking
        tracking['task_iterations'][task_id] = iteration
        tracking['current_task'] = task_id
        
        # Cleanup old task iterations to prevent unbounded growth
        # Keep only the last 50 task iterations
        if len(tracking['task_iterations']) > 50:
            # Sort by value (iteration count) and keep the most recent/active tasks
            items = list(tracking['task_iterations'].items())
            # Keep the current task and the 49 most recent others
            if task_id in tracking['task_iterations']:
                current_value = tracking['task_iterations'][task_id]
                other_items = [(k, v) for k, v in items if k != task_id]
                other_items = other_items[-49:]  # Keep last 49
                tracking['task_iterations'] = defaultdict(int, {task_id: current_value})
                tracking['task_iterations'].update(dict(other_items))
            else:
                tracking['task_iterations'] = defaultdict(int, dict(items[-50:]))
        
        # Warn if too many iterations
        if iteration > 5:
            warning = f"Task {task_id} has {iteration} iterations - may be stuck"
            self._add_warning(warning)
            print(f"WARNING: {warning}")
    
    def _check_for_issues(self, operation_type: str, details: Dict[str, Any]) -> None:
        """Check for potential workflow issues"""
        self._ensure_initialized()
        tracking = st.session_state.workflow_tracking
        
        # Check for rapid repeated operations
        recent_ops = tracking['operations'][-10:]
        same_type_count = sum(1 for op in recent_ops if op['type'] == operation_type)
        
        if same_type_count > 7:
            self._add_warning(f"Repeated operation detected: {operation_type} ({same_type_count} times in last 10 ops)")
        
        # Check for high LLM call rate
        if tracking['total_llm_calls'] > 50:
            elapsed = (datetime.now() - tracking['start_time']).total_seconds() / 60
            rate = tracking['total_llm_calls'] / max(elapsed, 1)
            if rate > 10:  # More than 10 calls per minute
                self._add_warning(f"High LLM call rate: {rate:.1f} calls/minute")
    
    def _add_warning(self, warning: str) -> None:
        """Add a warning to the tracking"""
        self._ensure_initialized()
        tracking = st.session_state.workflow_tracking
        warning_entry = {
            'timestamp': datetime.now().isoformat(),
            'message': warning
        }
        tracking['warnings'].append(warning_entry)
        
        # Keep only last 20 warnings
        if len(tracking['warnings']) > 20:
            tracking['warnings'] = tracking['warnings'][-20:]
    
    def get_current_status(self) -> Dict[str, Any]:
        """Get current workflow status"""
        self._ensure_initialized()
        tracking = st.session_state.workflow_tracking
        
        elapsed_minutes = (datetime.now() - tracking['start_time']).total_seconds() / 60
        
        return {
            'current_task': tracking.get('current_task', 'None'),
            'total_operations': len(tracking['operations']),
            'operation_counts': dict(tracking['operation_counts']),
            'task_iterations': dict(tracking['task_iterations']),
            'total_llm_calls': tracking['total_llm_calls'],
            'elapsed_minutes': round(elapsed_minutes, 1),
            'warnings': tracking['warnings'][-5:],  # Last 5 warnings
            'recent_operations': tracking['operations'][-10:]  # Last 10 operations
        }
    
    def display_status(self) -> None:
        """Display current tracking status in Streamlit"""
        status = self.get_current_status()
        
        # Create columns for metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Current Task", status['current_task'])
        with col2:
            st.metric("Total Operations", status['total_operations'])
        with col3:
            st.metric("LLM Calls", status['total_llm_calls'])
        with col4:
            st.metric("Time (min)", status['elapsed_minutes'])
        
        # Show warnings if any
        if status['warnings']:
            st.markdown("### ⚠️ Warnings")
            for warning in status['warnings']:
                st.warning(f"{warning['message']} ({warning['timestamp']})")
        
        # Create tabs for different tracking views
        tab1, tab2, tab3 = st.tabs(["📊 Operations", "🔄 Iterations", "📋 Activity Log"])
        
        with tab1:
            # Show operation breakdown
            st.markdown("**Operation Counts:**")
            if status['operation_counts']:
                for op_type, count in status['operation_counts'].items():
                    st.write(f"• {op_type}: {count}")
            else:
                st.write("No operations recorded yet")
        
        with tab2:
            # Show task iterations
            st.markdown("**Task Iterations:**")
            if status['task_iterations']:
                for task_id, iterations in status['task_iterations'].items():
                    color = "🔴" if iterations >= 5 else "🟡" if iterations >= 3 else "🟢"
                    st.write(f"{color} {task_id}: {iterations} iterations")
            else:
                st.write("No task iterations recorded yet")
        
        with tab3:
            # Show recent operations
            st.markdown("**Recent Operations:**")
            if status['recent_operations']:
                for op in reversed(status['recent_operations'][-10:]):
                    st.text(f"{op['timestamp']} - {op['type']} ({op['task']})")
            else:
                st.write("No operations recorded yet")
    
    def export_tracking_data(self) -> str:
        """Export tracking data as JSON"""
        self._ensure_initialized()
        tracking = st.session_state.workflow_tracking
        
        export_data = {
            'export_time': datetime.now().isoformat(),
            'session_start': tracking['start_time'].isoformat(),
            'summary': self.get_current_status(),
            'all_operations': tracking['operations'],
            'all_warnings': tracking['warnings']
        }
        
        return json.dumps(export_data, indent=2)
    
    def reset_tracking(self) -> None:
        """Reset tracking data"""
        st.session_state.workflow_tracking = {
            'operations': [],
            'task_iterations': defaultdict(int),
            'operation_counts': defaultdict(int),
            'start_time': datetime.now(),
            'warnings': [],
            'current_task': None,
            'total_llm_calls': 0,
            'operation_count_limit': 50
        }
    
    def restore_tracking_data(self, tracking_data: Dict[str, Any]) -> None:
        """Restore tracking data from exported state"""
        self._ensure_initialized()
        
        # Restore from exported tracking data
        if 'summary' in tracking_data:
            summary = tracking_data['summary']
            st.session_state.workflow_tracking.update({
                'operation_counts': defaultdict(int, summary.get('operation_counts', {})),
                'task_iterations': defaultdict(int, summary.get('task_iterations', {})),
                'total_llm_calls': summary.get('total_llm_calls', 0),
                'warnings': tracking_data.get('all_warnings', []),
                'operations': tracking_data.get('all_operations', [])
            })
            
            # Try to parse start time if available
            if 'session_start' in tracking_data:
                try:
                    st.session_state.workflow_tracking['start_time'] = datetime.fromisoformat(tracking_data['session_start'])
                except:
                    pass  # Keep current start time if parsing fails


# Global tracker instance
workflow_tracker = WorkflowTracker()