"""
LLM Client Module
This module provides the main interface for calling LLMs and specialized functions.
It handles provider selection and routing.
"""

import streamlit as st
from typing import Optional, Tuple, List

from .llm_providers import OllamaProvider, OpenAIProvider, LMStudioProvider
from .openai_specialized import search_with_gpt4o_preview


def call_llm(prompt: str, operation_name: str = "LLM call") -> Optional[str]:
    """
    Public wrapper for calling the LLM API.
    This is the main function that should be imported and used by other modules.
    
    Args:
        prompt: The prompt to send to the LLM
        operation_name: Description of the operation for logging
        
    Returns:
        The LLM response text, or None if failed
    """
    provider = st.session_state.get("llm_provider", "ollama")
    
    if provider == "openai":
        api_key = st.session_state.get("openai_api_key", "")
        model_name = st.session_state.get("openai_model", "gpt-3.5-turbo")
        
        if not api_key:
            st.warning("OpenAI API key is not set. Please enter your API key in the sidebar.")
            return None
        
        llm_provider = OpenAIProvider(api_key, model_name)
        return llm_provider.call(prompt, operation_name)
        
    elif provider == "lmstudio":
        api_url = st.session_state.get("lmstudio_api_url", "http://localhost:1234")
        model_name = st.session_state.get("lmstudio_model", "granite-3.0-2b-instruct")
        
        llm_provider = LMStudioProvider(api_url, model_name)
        return llm_provider.call(prompt, operation_name)
        
    else:  # Default to Ollama
        api_url = st.session_state.get("ollama_api_url", "http://localhost:11434/api/generate")
        model_name = st.session_state.get("ollama_model", "llama3.1:8b")
        
        llm_provider = OllamaProvider(api_url, model_name)
        return llm_provider.call(prompt, operation_name)


def test_llm_connection() -> Tuple[bool, str]:
    """Test the connection to the currently selected LLM provider"""
    provider = st.session_state.get("llm_provider", "ollama")
    
    if provider == "openai":
        api_key = st.session_state.get("openai_api_key", "")
        model_name = st.session_state.get("openai_model", "gpt-3.5-turbo")
        
        if not api_key:
            return False, "OpenAI API key is not set"
        
        llm_provider = OpenAIProvider(api_key, model_name)
        return llm_provider.test_connection()
        
    elif provider == "lmstudio":
        api_url = st.session_state.get("lmstudio_api_url", "http://localhost:1234")
        model_name = st.session_state.get("lmstudio_model", "granite-3.0-2b-instruct")
        
        llm_provider = LMStudioProvider(api_url, model_name)
        return llm_provider.test_connection()
        
    else:  # Ollama
        api_url = st.session_state.get("ollama_api_url", "http://localhost:11434/api/generate")
        model_name = st.session_state.get("ollama_model", "llama3.1:8b")
        
        llm_provider = OllamaProvider(api_url, model_name)
        return llm_provider.test_connection()


def get_available_models():
    """Get available models for the currently selected provider"""
    provider = st.session_state.get("llm_provider", "ollama")
    
    if provider == "openai":
        api_key = st.session_state.get("openai_api_key", "")
        llm_provider = OpenAIProvider(api_key)
        return llm_provider.get_available_models()
        
    elif provider == "lmstudio":
        api_url = st.session_state.get("lmstudio_api_url", "http://localhost:1234")
        llm_provider = LMStudioProvider(api_url)
        return llm_provider.get_available_models()
        
    else:  # Ollama
        api_url = st.session_state.get("ollama_api_url", "http://localhost:11434/api/generate")
        llm_provider = OllamaProvider(api_url)
        return llm_provider.get_available_models()


# Convenience functions for backward compatibility
def get_available_openai_models(api_key: Optional[str] = None) -> List[str]:
    """Fetch available OpenAI models dynamically from the API."""
    llm_provider = OpenAIProvider(api_key)
    return llm_provider.get_available_models()


def get_available_lmstudio_models(api_url: str = "http://localhost:1234") -> List[str]:
    """Fetch available models from LM Studio API."""
    llm_provider = LMStudioProvider(api_url)
    return llm_provider.get_available_models()


def get_available_ollama_models(api_url: str = "http://localhost:11434/api/generate"):
    """Fetch available models from Ollama API with detailed information."""
    llm_provider = OllamaProvider(api_url)
    return llm_provider.get_available_models()