"""
Legacy QA improvement system - minimal compatibility layer
This file provides minimal compatibility for the old QA system
while we transition to the new structured approach.
"""

import json
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional

# Make LLM utils import optional for testing environments
try:
    from .llm_utils import _call_llm_api
    LLM_AVAILABLE = True
except ImportError:
    LLM_AVAILABLE = False
    def _call_llm_api(*args, **kwargs):
        return "Mock LLM response for testing"

# QA Configurations
QA_CONFIGS = {
    "comprehensive": {
        "name": "Comprehensive QA",
        "description": "Thorough analysis covering all aspects",
        "checks": [
            "technical_accuracy",
            "clarity_and_readability", 
            "completeness",
            "structure_and_organization",
            "practical_applicability"
        ]
    }
}

class ReportQASystem:
    """Legacy QA system - compatibility layer"""
    
    def __init__(self, config):
        self.config = config
    
    def analyze_report(self, report_content: str, context: str = "") -> Dict[str, Any]:
        """Minimal QA analysis for compatibility"""
        return {
            "inaccurate_or_confusing_sections": [],
            "overall_score": 0.8,
            "suggestions": []
        }
    
    def run_report_qa(self, report_content: str, sources: List[str], query_description: str) -> Dict[str, Any]:
        """Run QA analysis on a report - compatibility method"""
        print("Warning: Using legacy run_report_qa method.")
        print("For full QA functionality, please use the new structured QA system.")
        
        # Return a basic QA result structure
        return {
            "inaccurate_or_confusing_sections": [
                {
                    "section_title": "Structure", 
                    "issue": "Legacy QA system in use - limited functionality",
                    "suggested_fix": "Please migrate to the new structured QA system for full functionality",
                    "confidence": 0.9
                }
            ],
            "overall_score": 0.7,
            "suggestions": [
                "Consider upgrading to the new structured QA system for better analysis"
            ],
            "timestamp": datetime.now().isoformat(),
            "query_description": query_description,
            "sources_count": len(sources)
        }

class ReportImprovementPipeline:
    """Legacy improvement pipeline - compatibility layer"""
    
    def __init__(self, qa_system):
        self.qa_system = qa_system
    
    def _apply_fixes(self, report_content: str, issues: List[Dict], sources: List[str], query_description: str) -> Tuple[str, bool]:
        """Legacy apply fixes method - returns original content unchanged"""
        print("Warning: Using legacy _apply_fixes method. No changes will be made.")
        print("Please use the new structured QA system instead.")
        return report_content, False