"""
LLM Provider wrapper for research workflow
"""

from typing import Optional
from ..llm.llm_utils import _call_llm_api, strip_thinking_tags
from .workflow_tracker import workflow_tracker


class LLMProvider:
    """Simple wrapper for LLM functionality"""
    
    def generate(self, prompt: str) -> str:
        """Generate a response from the LLM"""
        # Track LLM call
        workflow_tracker.track_operation('llm_generation', {
            'prompt_length': len(prompt),
            'prompt_preview': prompt[:100] + '...' if len(prompt) > 100 else prompt
        })
        
        response = _call_llm_api(prompt, "research workflow")
        
        # Track response
        workflow_tracker.track_operation('llm_response', {
            'response_length': len(response) if response else 0,
            'success': response is not None
        })
        
        if response:
            return strip_thinking_tags(response)
        return ""