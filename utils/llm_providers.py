"""
LLM Provider Base Classes and Provider-Specific Implementations
This module contains the base classes and provider-specific implementations
for different LLM providers (OpenAI, Ollama, LM Studio).
"""

import json
import requests
import streamlit as st
from typing import Any, Dict, List, Optional, Tuple
from abc import ABC, abstractmethod

# Import OpenAI client - make it conditional to handle environments without the package
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

from .llm_utils_common import strip_thinking_tags

# Default settings for providers
DEFAULT_OLLAMA_API_URL = "http://localhost:11434/api/generate"
DEFAULT_OLLAMA_MODEL = "llama3.1:8b"
DEFAULT_OPENAI_MODEL = "gpt-3.5-turbo"
DEFAULT_LMSTUDIO_API_URL = "http://localhost:1234"
DEFAULT_LMSTUDIO_MODEL = "granite-3.0-2b-instruct"


class LLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    @abstractmethod
    def call(self, prompt: str, operation_name: str = "LLM call") -> Optional[str]:
        """Call the LLM with the given prompt"""
        pass
    
    @abstractmethod
    def test_connection(self) -> Tuple[bool, str]:
        """Test the connection to the LLM provider"""
        pass
    
    @abstractmethod
    def get_available_models(self) -> List[str]:
        """Get list of available models for this provider"""
        pass


class OllamaProvider(LLMProvider):
    """Ollama LLM provider implementation"""
    
    def __init__(self, api_url: str = None, model_name: str = None):
        self.api_url = api_url or st.session_state.get("ollama_api_url", DEFAULT_OLLAMA_API_URL)
        self.model_name = model_name or st.session_state.get("ollama_model", DEFAULT_OLLAMA_MODEL)
    
    def call(self, prompt: str, operation_name: str = "LLM call") -> Optional[str]:
        """Call the Ollama API with the given prompt and model."""
        # Truncate very long prompts to avoid timeouts
        max_prompt_length = 8000
        if len(prompt) > max_prompt_length:
            print(f"Warning: Truncating long prompt from {len(prompt)} to {max_prompt_length} characters")
            prompt = prompt[:max_prompt_length] + "\n\n[Truncated due to length]"
        
        payload = {"model": self.model_name, "prompt": prompt, "stream": False}
        try:
            print(f"Sending request to Ollama LLM ({self.model_name}) for {operation_name}...")
            # Increase timeout for complex operations
            timeout = 120 if operation_name == "research workflow" else 60
            response = requests.post(self.api_url, json=payload, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            llm_response_text = data.get("response", "").strip()
            
            # Strip thinking tags from the response
            llm_response_text = strip_thinking_tags(llm_response_text)
            
            if not llm_response_text and prompt:  # Check if prompt was non-empty
                print(f"Ollama LLM returned an empty response for {operation_name} with a non-empty prompt.")
            elif llm_response_text:  # Only log success if we got a response
                print(f"Ollama LLM {operation_name} successful.")
            return llm_response_text
        except requests.exceptions.Timeout:
            print(f"Ollama LLM API request timed out during {operation_name}.")
            st.error(f"LLM request timed out. ({operation_name})")
        except requests.exceptions.RequestException as e:
            print(f"Ollama LLM API communication error during {operation_name}: {e}")
            st.error(f"LLM API error: {e} ({operation_name})")
        except Exception as e:
            print(f"An unexpected error occurred during Ollama LLM {operation_name}: {e}")
            st.error(f"Unexpected LLM error: {e} ({operation_name})")
        return None
    
    def test_connection(self) -> Tuple[bool, str]:
        """Test the connection to Ollama"""
        test_prompt = "Please respond with just the word 'connected'."
        try:
            response = self.call(test_prompt, "connection test")
            if response and "connect" in response.lower():
                return True, f"Connected to Ollama ({self.model_name})"
            else:
                return False, f"Failed to get a valid response from Ollama ({self.model_name})"
        except Exception as e:
            return False, f"Ollama API error: {str(e)[:100]}"
    
    def get_available_models(self) -> Tuple[List[str], Dict[str, str]]:
        """
        Fetch available models from Ollama API with detailed information.
        
        Returns:
            tuple: (model_names, model_display_info)
        """
        model_names: List[str] = []
        model_display_info: Dict[str, str] = {}
        
        # Extract base URL
        base_url = self.api_url.split('/api/')[0] if '/api/' in self.api_url else self.api_url
        tags_url = f"{base_url}/api/tags"
        
        try:
            response = requests.get(tags_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                models_data = data.get("models", [])
                
                for model_spec in models_data:
                    name = model_spec.get("name")
                    if not name: continue
                    
                    # Skip embedding models
                    if "embed" in name.lower() or "embedding" in name.lower():
                        continue
                        
                    details = model_spec.get("details", {})
                    parameter_size = details.get("parameter_size", "")
                    family = details.get("family", "")
                    
                    model_names.append(name)
                    
                    display_parts = []
                    if parameter_size: display_parts.append(parameter_size)
                    if family and family.lower() not in name.lower():
                        display_parts.append(f"({family.capitalize()})")
                    
                    if display_parts:
                        model_display_info[name] = " ".join(display_parts)
                
                # Sort models by family and size
                import re
                
                def get_sort_key(model_name_full: str):
                    size_val = float('inf')
                    match_name = re.search(r'(\d+\.?\d*)[bB]', model_name_full)
                    if match_name:
                        size_val = float(match_name.group(1))
                    
                    family_prio = 3
                    if "llama" in model_name_full.lower(): family_prio = 0
                    elif "mistral" in model_name_full.lower(): family_prio = 1
                    elif "gemma" in model_name_full.lower(): family_prio = 2
                    
                    return (family_prio, size_val, model_name_full)

                model_names.sort(key=get_sort_key)
                
                if not model_names:
                    default_models = ["llama3.1:8b", "mistral:7b", "gemma:7b"]
                    return (default_models, {m: "" for m in default_models})
                    
                return model_names, model_display_info
        except Exception as e:
            print(f"Error connecting to Ollama API: {e}")
            
        # Fallback
        default_models = ["llama3.1:8b", "mistral:7b"]
        return (default_models, {m: "" for m in default_models})


class OpenAIProvider(LLMProvider):
    """OpenAI LLM provider implementation"""
    
    def __init__(self, api_key: str = None, model_name: str = None):
        self.api_key = api_key or st.session_state.get("openai_api_key", "")
        self.model_name = model_name or st.session_state.get("openai_model", DEFAULT_OPENAI_MODEL)
    
    def call(self, prompt: str, operation_name: str = "LLM call") -> Optional[str]:
        """Call the OpenAI API with the given prompt and model."""
        if not self.api_key:
            st.warning("OpenAI API key is not set. Please enter your API key in the sidebar.")
            return None
            
        if not OPENAI_AVAILABLE:
            st.error("OpenAI Python package is not installed. Please install it with 'pip install openai'")
            return None
        
        try:
            print(f"Sending request to OpenAI ({self.model_name}) for {operation_name}...")
            
            # Create OpenAI client with explicit parameters to avoid environment issues
            try:
                # Try creating client with minimal parameters
                client = OpenAI(api_key=self.api_key)
            except TypeError as e:
                if "proxies" in str(e):
                    # If there's a proxies error, try to work around it
                    print("Working around proxies parameter issue...")
                    # Clear any environment variables that might be causing issues
                    import os
                    for key in list(os.environ.keys()):
                        if 'PROXY' in key.upper():
                            print(f"Removing environment variable: {key}")
                            del os.environ[key]
                    
                    # Try again without proxy environment variables
                    try:
                        client = OpenAI(api_key=self.api_key)
                    except:
                        # Last resort - use requests directly
                        print("Using direct API calls as fallback...")
                        return self._call_direct(prompt, operation_name)
                else:
                    raise e
            
            # Check if this is a reasoning model (o1, o3)
            if self.model_name.startswith(('o1', 'o3')):
                # Use responses API for reasoning models
                response = client.responses.create(
                    model=self.model_name,
                    input=prompt,
                    reasoning={"effort": "medium"}  # Can be made configurable
                )
                llm_response_text = response.choices[0].text.strip() if hasattr(response.choices[0], 'text') else str(response)
            else:
                # Use chat completions API for regular models
                response = client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that provides concise, accurate summaries and follows formatting instructions precisely."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,  # Consider making this configurable
                    max_tokens=1000   # Consider making this configurable
                )
                llm_response_text = response.choices[0].message.content.strip()
            
            llm_response_text = strip_thinking_tags(llm_response_text)  # Strip thinking tags
            
            if not llm_response_text and prompt:
                print(f"OpenAI returned an empty response for {operation_name} with a non-empty prompt.")
            elif llm_response_text:
                print(f"OpenAI {operation_name} successful.")
            
            return llm_response_text
        except Exception as e:
            print(f"An error occurred during OpenAI {operation_name}: {e}")
            # More specific error messages
            if "api_key" in str(e).lower():
                st.error(f"OpenAI API key error: Please check your API key is valid ({operation_name})")
            elif "model" in str(e).lower():
                st.error(f"OpenAI model error: Model '{self.model_name}' may not be available ({operation_name})")
            elif "rate" in str(e).lower():
                st.error(f"OpenAI rate limit error: Please wait and try again ({operation_name})")
            else:
                st.error(f"OpenAI API error: {e} ({operation_name})")
            return None
    
    def _call_direct(self, prompt: str, operation_name: str) -> Optional[str]:
        """Direct API call to OpenAI using requests library as a fallback."""
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Determine which API to use based on model
            if self.model_name.startswith(('o1', 'o3')):
                # Use responses endpoint for reasoning models
                url = "https://api.openai.com/v1/responses"
                payload = {
                    "model": self.model_name,
                    "input": prompt,
                    "reasoning": {"effort": "medium"}
                }
            else:
                # Use chat completions endpoint for regular models
                url = "https://api.openai.com/v1/chat/completions"
                payload = {
                    "model": self.model_name,
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant that provides concise, accurate summaries and follows formatting instructions precisely."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 1000
                }
            
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract text based on response type
            if self.model_name.startswith(('o1', 'o3')):
                llm_response_text = data.get("choices", [{}])[0].get("text", "").strip()
            else:
                llm_response_text = data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
            
            llm_response_text = strip_thinking_tags(llm_response_text)
            
            if llm_response_text:
                print(f"OpenAI {operation_name} successful (direct API).")
            
            return llm_response_text
            
        except Exception as e:
            print(f"Direct OpenAI API call failed: {e}")
            st.error(f"Direct OpenAI API error: {e}")
            return None
    
    def test_connection(self) -> Tuple[bool, str]:
        """Test the connection to OpenAI"""
        test_prompt = "Please respond with just the word 'connected'."
        try:
            response = self.call(test_prompt, "connection test")
            if response and "connect" in response.lower():
                return True, f"Connected to OpenAI ({self.model_name})"
            else:
                return False, f"Failed to get a valid response from OpenAI"
        except Exception as e:
            return False, f"OpenAI API error: {str(e)[:100]}"
    
    def get_available_models(self) -> List[str]:
        """Fetch available OpenAI models dynamically from the API."""
        if not self.api_key:
            # Return default list if no API key
            return [
                "gpt-4o",
                "gpt-4-turbo",
                "gpt-4",
                "gpt-3.5-turbo",
                "o1-preview",
                "o1-mini",
            ]
        
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Call the models endpoint directly
            response = requests.get("https://api.openai.com/v1/models", headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            model_ids = []
            
            # Extract model IDs from the response
            for model in data.get('data', []):
                model_id = model.get('id', '')
                # Filter for models we can use for chat/completions
                if any(prefix in model_id for prefix in ['gpt', 'o1', 'o3', 'davinci', 'curie', 'babbage', 'ada']):
                    # Skip embedding models and other non-chat models
                    if not any(skip in model_id for skip in ['embedding', 'whisper', 'tts', 'dall-e', 'search', 'similarity', 'edit', 'insert']):
                        model_ids.append(model_id)
            
            # Sort models with preferred ones first
            preferred_order = ['gpt-4o', 'gpt-4-turbo', 'gpt-4', 'gpt-3.5-turbo', 'o1', 'o3']
            
            def sort_key(model_id):
                for i, prefix in enumerate(preferred_order):
                    if model_id.startswith(prefix):
                        return (i, model_id)
                return (len(preferred_order), model_id)
            
            model_ids.sort(key=sort_key)
            
            # If no models found, return defaults
            if not model_ids:
                return [
                    "gpt-4o",
                    "gpt-4-turbo",
                    "gpt-4",
                    "gpt-3.5-turbo",
                ]
            
            print(f"Successfully fetched {len(model_ids)} OpenAI models")
            return model_ids
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                print("Invalid OpenAI API key")
                st.error("Invalid OpenAI API key. Please check your key.")
            else:
                print(f"HTTP error fetching OpenAI models: {e}")
        except Exception as e:
            print(f"Error fetching OpenAI models: {e}")
        
        # Return default list on error
        return [
            "gpt-4o",
            "gpt-4-turbo",
            "gpt-4",
            "gpt-3.5-turbo",
        ]


class LMStudioProvider(LLMProvider):
    """LM Studio LLM provider implementation"""
    
    def __init__(self, api_url: str = None, model_name: str = None):
        self.api_url = api_url or st.session_state.get("lmstudio_api_url", DEFAULT_LMSTUDIO_API_URL)
        self.model_name = model_name or st.session_state.get("lmstudio_model", DEFAULT_LMSTUDIO_MODEL)
    
    def call(self, prompt: str, operation_name: str = "LLM call") -> Optional[str]:
        """Call the LM Studio API with the given prompt and model."""
        try:
            print(f"Sending request to LM Studio ({self.model_name}) for {operation_name}...")
            
            # LM Studio uses OpenAI-compatible endpoint for chat completions
            chat_url = f"{self.api_url}/v1/chat/completions"
            
            headers = {
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model_name,
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant that provides concise, accurate summaries and follows formatting instructions precisely."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": -1,  # LM Studio uses -1 for no limit
                "stream": False
            }
            
            # Increase timeout for complex operations
            timeout = 120 if operation_name == "research workflow" else 60
            response = requests.post(chat_url, json=payload, headers=headers, timeout=timeout)
            response.raise_for_status()
            
            data = response.json()
            llm_response_text = data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
            
            # Strip thinking tags from the response
            llm_response_text = strip_thinking_tags(llm_response_text)
            
            if not llm_response_text and prompt:
                print(f"LM Studio returned an empty response for {operation_name} with a non-empty prompt.")
            elif llm_response_text:
                print(f"LM Studio {operation_name} successful.")
                # Log performance stats if available
                if "stats" in data:
                    stats = data["stats"]
                    print(f"  - Tokens/second: {stats.get('tokens_per_second', 'N/A')}")
                    print(f"  - Time to first token: {stats.get('time_to_first_token', 'N/A')}s")
                    
            return llm_response_text
        except requests.exceptions.Timeout:
            print(f"LM Studio API request timed out during {operation_name}.")
            st.error(f"LM Studio request timed out. ({operation_name})")
        except requests.exceptions.RequestException as e:
            print(f"LM Studio API communication error during {operation_name}: {e}")
            st.error(f"LM Studio API error: {e} ({operation_name})")
        except Exception as e:
            print(f"An unexpected error occurred during LM Studio {operation_name}: {e}")
            st.error(f"Unexpected LM Studio error: {e} ({operation_name})")
        return None
    
    def test_connection(self) -> Tuple[bool, str]:
        """Test the connection to LM Studio"""
        test_prompt = "Please respond with just the word 'connected'."
        try:
            response = self.call(test_prompt, "connection test")
            if response and "connect" in response.lower():
                return True, f"Connected to LM Studio ({self.model_name})"
            else:
                return False, f"Failed to get a valid response from LM Studio ({self.model_name})"
        except Exception as e:
            return False, f"LM Studio API error: {str(e)[:100]}"
    
    def get_available_models(self) -> List[str]:
        """
        Fetch available models from LM Studio API.
        
        Returns:
            List of model names
        """
        model_names: List[str] = []
        
        models_url = f"{self.api_url}/v1/models"
        
        try:
            response = requests.get(models_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                
                # Handle different response formats from LM Studio
                if "data" in data:
                    # Standard OpenAI-compatible format
                    models_data = data["data"]
                    for model in models_data:
                        model_id = model.get("id")
                        if model_id:
                            # Skip embedding models
                            model_type = model.get("type", "")
                            if model_type != "embeddings" and "embed" not in model_id.lower():
                                model_names.append(model_id)
                elif isinstance(data, list):
                    # Direct array format (what LM Studio is returning)
                    for model in data:
                        if isinstance(model, str):
                            # Simple string array
                            if "embed" not in model.lower():  # Skip embedding models
                                model_names.append(model)
                        elif isinstance(model, dict) and "id" in model:
                            # Array of model objects
                            model_id = model["id"]
                            model_type = model.get("type", "")
                            if model_type != "embeddings" and "embed" not in model_id.lower():
                                model_names.append(model_id)
                
                # Remove duplicates and sort
                model_names = list(set(model_names))
                model_names.sort()
                
                if not model_names:
                    # Return default if no models found
                    default_models = ["granite-3.0-2b-instruct", "meta-llama-3.1-8b-instruct"]
                    return default_models
                    
                return model_names
        except Exception as e:
            print(f"Error connecting to LM Studio API: {e}")
        
        # Fallback models
        default_models = ["granite-3.0-2b-instruct", "meta-llama-3.1-8b-instruct"]
        return default_models