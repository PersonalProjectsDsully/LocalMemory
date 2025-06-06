"""
Specialized OpenAI Functions
This module contains specialized functions that only work with specific OpenAI models,
such as the GPT-4o Search Preview model.
"""

import streamlit as st
from typing import Optional

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


def search_with_gpt4o_preview(prompt: str) -> Optional[str]:
    """
    Call GPT-4o Search Preview model specifically for web search functionality.
    This function uses the chat completions endpoint with the search preview model.
    """
    api_key = st.session_state.get("openai_api_key", "")
    
    if not api_key:
        st.warning("OpenAI API key is not set. Please enter your API key in the sidebar.")
        return None
        
    if not OPENAI_AVAILABLE:
        st.error("OpenAI Python package is not installed. Please install it with 'pip install openai'")
        return None
    
    try:
        client = OpenAI(api_key=api_key)
        
        # Use the search preview model with appropriate parameters
        response = client.chat.completions.create(
            model="gpt-4o-search-preview",
            messages=[
                {"role": "user", "content": prompt}
            ],
            response_format={
                "type": "text"
            }
        )
        
        # Extract the content from the response
        if response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content
            return content.strip() if content else None
        
        return None
        
    except Exception as e:
        print(f"GPT-4o Search Preview error: {e}")
        # Try direct API call as fallback
        return _call_gpt4o_search_direct(prompt, api_key)


def _call_gpt4o_search_direct(prompt: str, api_key: str) -> Optional[str]:
    """Direct API call to GPT-4o Search Preview using requests library."""
    try:
        import requests
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        url = "https://api.openai.com/v1/chat/completions"
        payload = {
            "model": "gpt-4o-search-preview",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "response_format": {
                "type": "text"
            }
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        
        data = response.json()
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        
        return content.strip() if content else None
        
    except Exception as e:
        print(f"Direct GPT-4o Search Preview API call failed: {e}")
        st.error(f"GPT-4o Search Preview error: {e}")
        return None