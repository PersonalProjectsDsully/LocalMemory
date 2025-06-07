"""
Comprehensive Research Workflow for Intelligent Search
This module now serves as a compatibility layer, delegating to the refactored components
"""

# Import all components from the refactored modules
from .research.workflow_orchestrator import ResearchWorkflow, WorkflowOrchestrator

# Export the main classes for backward compatibility
__all__ = ['ResearchWorkflow', 'WorkflowOrchestrator']