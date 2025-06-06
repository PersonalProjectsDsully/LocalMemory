"""
Common utilities for LLM operations
This module contains shared utility functions used across different LLM providers.
"""

import re
from typing import Optional


def strip_thinking_tags(text: Optional[str]) -> Optional[str]:
    """
    Strips content between thinking-related tags from model responses.
    Handles None input gracefully and various tag formats including <think> and <thinking>.
    """
    if text is None:
        return None
    
    # Remove content between <thinking> and </thinking> tags (case-insensitive)
    cleaned_text = re.sub(r'<thinking>.*?</thinking>', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove content between <think> and </think> tags (case-insensitive)
    cleaned_text = re.sub(r'<think>.*?</think>', '', cleaned_text, flags=re.DOTALL | re.IGNORECASE)
    
    # Handle cases where tags might have attributes
    cleaned_text = re.sub(r'<thinking[^>]*>.*?</thinking>', '', cleaned_text, flags=re.DOTALL | re.IGNORECASE)
    cleaned_text = re.sub(r'<think[^>]*>.*?</think>', '', cleaned_text, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove any standalone tags that might be left
    cleaned_text = re.sub(r'</?thinking[^>]*>', '', cleaned_text, flags=re.IGNORECASE)
    cleaned_text = re.sub(r'</?think[^>]*>', '', cleaned_text, flags=re.IGNORECASE)
    
    # Also handle common variations like [thinking], {thinking}, [think], {think}
    cleaned_text = re.sub(r'\[thinking\].*?\[/thinking\]', '', cleaned_text, flags=re.DOTALL | re.IGNORECASE)
    cleaned_text = re.sub(r'\{thinking\}.*?\{/thinking\}', '', cleaned_text, flags=re.DOTALL | re.IGNORECASE)
    cleaned_text = re.sub(r'\[think\].*?\[/think\]', '', cleaned_text, flags=re.DOTALL | re.IGNORECASE)
    cleaned_text = re.sub(r'\{think\}.*?\{/think\}', '', cleaned_text, flags=re.DOTALL | re.IGNORECASE)
    
    # Trim any excessive whitespace that might result from removing sections
    cleaned_text = re.sub(r'\n{3,}', '\n\n', cleaned_text)
    
    # Clean up any leading/trailing whitespace
    cleaned_text = cleaned_text.strip()
    
    # If the entire response was just thinking tags, return a helpful message
    if not cleaned_text and text.strip():
        return "The model's response contained only internal reasoning. Please try rephrasing your question."
    
    return cleaned_text