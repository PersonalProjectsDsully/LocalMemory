"""
LEGACY MODULE - DEPRECATED
This module is kept for backward compatibility only.
Please use the new modular structure instead:
- llm_client for main LLM operations
- video_analysis for YouTube video functions
- content_intelligence for content analysis
- openai_specialized for specialized OpenAI functions
"""

import json
from typing import Any, Dict, List, Optional, Tuple

# Import the new modular functions for backward compatibility
from .llm_client import (
    call_llm,
    test_llm_connection,
    get_available_openai_models,
    get_available_lmstudio_models,
    get_available_ollama_models
)
from .video_analysis import (
    classify_youtube_video,
    fallback_classification,
    recommend_category_and_tags,
    summarize_youtube_transcript
)
from .content_intelligence import extract_content_intelligence
from .openai_specialized import search_with_gpt4o_preview
from .llm_utils_common import strip_thinking_tags

# Legacy constants for backward compatibility
DEFAULT_LLM_API_URL = "http://localhost:11434/api/generate"
DEFAULT_LLM_MODEL = "llama3.1:8b"
DEFAULT_OPENAI_MODEL = "gpt-3.5-turbo"
DEFAULT_LMSTUDIO_API_URL = "http://localhost:1234"
DEFAULT_LMSTUDIO_MODEL = "granite-3.0-2b-instruct"

# Legacy wrapper functions for backward compatibility
def _call_llm_api(prompt: str, operation_name: str = "LLM call") -> Optional[str]:
    """DEPRECATED: Use call_llm from llm_client instead."""
    return call_llm(prompt, operation_name)

def _call_ollama_api(prompt: str, api_url: str, model_name: str, operation_name: str) -> Optional[str]:
    """DEPRECATED: Use OllamaProvider from llm_providers instead."""
    from .llm_providers import OllamaProvider
    provider = OllamaProvider(api_url, model_name)
    return provider.call(prompt, operation_name)

def _call_openai_api(prompt: str, api_key: str, model_name: str, operation_name: str) -> Optional[str]:
    """DEPRECATED: Use OpenAIProvider from llm_providers instead."""
    from .llm_providers import OpenAIProvider
    provider = OpenAIProvider(api_key, model_name)
    return provider.call(prompt, operation_name)

def _call_openai_api_direct(prompt: str, api_key: str, model_name: str, operation_name: str) -> Optional[str]:
    """DEPRECATED: Use OpenAIProvider from llm_providers instead."""
    from .llm_providers import OpenAIProvider
    provider = OpenAIProvider(api_key, model_name)
    return provider._call_direct(prompt, operation_name)

def _call_lmstudio_api(prompt: str, api_url: str, model_name: str, operation_name: str) -> Optional[str]:
    """DEPRECATED: Use LMStudioProvider from llm_providers instead."""
    from .llm_providers import LMStudioProvider
    provider = LMStudioProvider(api_url, model_name)
    return provider.call(prompt, operation_name)

def _call_gpt4o_search_direct(prompt: str, api_key: str) -> Optional[str]:
    """DEPRECATED: Use search_with_gpt4o_preview from openai_specialized instead."""
    return search_with_gpt4o_preview(prompt)

def _fallback_content_analysis(title: str, content_text: str) -> dict:
    """DEPRECATED: Use _fallback_content_analysis from content_intelligence instead."""
    from .content_intelligence import _fallback_content_analysis
    return _fallback_content_analysis(title, content_text)

def _parse_unstructured_response(response_text: str, title: str) -> dict:
    """DEPRECATED: Use _parse_unstructured_response from content_intelligence instead."""
    from .content_intelligence import _parse_unstructured_response
    return _parse_unstructured_response(response_text, title)

# All functions are now imported from their respective modules for backward compatibility
# Please update your imports to use the new modular structure