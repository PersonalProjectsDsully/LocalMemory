"""
Progress Reporter for Real-time Workflow Updates
Provides callbacks for updating UI during long-running operations
"""

import streamlit as st
from typing import Optional, Callable
import time


class ProgressReporter:
    """Reports progress during workflow operations"""
    
    def __init__(self, status_container=None):
        self.status_container = status_container
        self.operation_count = 0
        self.current_task = None
        self.start_time = time.time()
    
    def update(self, message: str, task: Optional[str] = None):
        """Update progress with a message"""
        self.operation_count += 1
        if task:
            self.current_task = task
        
        # Format message with context
        elapsed = int(time.time() - self.start_time)
        formatted_message = f"[{elapsed}s] {message}"
        
        if self.current_task:
            formatted_message = f"📌 {self.current_task} - {formatted_message}"
        
        # Update status container if available
        if self.status_container:
            self.status_container.write(formatted_message)
        
        # Also print to console
        print(formatted_message)
    
    def update_metrics(self, operations: int, llm_calls: int):
        """Update metrics display"""
        if self.status_container:
            self.status_container.write(f"📊 Operations: {operations} | LLM Calls: {llm_calls} | Time: {int(time.time() - self.start_time)}s")
    
    def warning(self, message: str):
        """Show a warning message"""
        formatted_message = f"⚠️ {message}"
        if self.status_container:
            self.status_container.write(formatted_message)
        print(f"WARNING: {message}")
    
    def success(self, message: str):
        """Show a success message"""
        formatted_message = f"✅ {message}"
        if self.status_container:
            self.status_container.write(formatted_message)
        print(f"SUCCESS: {message}")
    
    def error(self, message: str):
        """Show an error message"""
        formatted_message = f"❌ {message}"
        if self.status_container:
            self.status_container.write(formatted_message)
        print(f"ERROR: {message}")


# Singleton instance for current progress
_current_progress_reporter: Optional[ProgressReporter] = None


def set_progress_reporter(reporter: ProgressReporter):
    """Set the current progress reporter"""
    global _current_progress_reporter
    _current_progress_reporter = reporter


def get_progress_reporter() -> Optional[ProgressReporter]:
    """Get the current progress reporter"""
    return _current_progress_reporter


def report_progress(message: str, task: Optional[str] = None):
    """Report progress if a reporter is available"""
    reporter = get_progress_reporter()
    if reporter:
        reporter.update(message, task)