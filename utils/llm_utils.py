import json
from typing import Any, Dict, List, Optional, Tuple

import requests
import streamlit as st
import re
from datetime import datetime

# Import OpenAI client - make it conditional to handle environments without the package
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Default Ollama settings
DEFAULT_LLM_API_URL = "http://localhost:11434/api/generate"
DEFAULT_LLM_MODEL = "llama3.1:8b"

# Default OpenAI settings
DEFAULT_OPENAI_MODEL = "gpt-3.5-turbo"

# Default LM Studio settings
DEFAULT_LMSTUDIO_API_URL = "http://localhost:1234"
DEFAULT_LMSTUDIO_MODEL = "granite-3.0-2b-instruct"

def _call_llm_api(prompt: str, operation_name: str = "LLM call") -> Optional[str]:
    """
    Call the LLM API based on the selected provider (Ollama, OpenAI, or LM Studio)
    
    This function checks the session state for API configuration and uses the appropriate
    provider. Falls back to Ollama as the default provider.
    """
    provider = st.session_state.get("llm_provider", "ollama")
    
    if provider == "openai":
        api_key = st.session_state.get("openai_api_key", "")
        model_name = st.session_state.get("openai_model", DEFAULT_OPENAI_MODEL)
        
        if not api_key:
            st.warning("OpenAI API key is not set. Please enter your API key in the sidebar.")
            return None
            
        if not OPENAI_AVAILABLE:
            st.error("OpenAI Python package is not installed. Please install it with 'pip install openai'")
            return None
            
        return _call_openai_api(prompt, api_key, model_name, operation_name)
    elif provider == "lmstudio":
        api_url = st.session_state.get("lmstudio_api_url", DEFAULT_LMSTUDIO_API_URL)
        model_name = st.session_state.get("lmstudio_model", DEFAULT_LMSTUDIO_MODEL)
        
        # Debug logging
        print(f"LM Studio session state model: {st.session_state.get('lmstudio_model', 'NOT SET')}")
        print(f"Using LM Studio model: {model_name}")
        
        return _call_lmstudio_api(prompt, api_url, model_name, operation_name)
    else:  # Default to Ollama
        api_url = st.session_state.get("ollama_api_url", DEFAULT_LLM_API_URL)
        model_name = st.session_state.get("ollama_model", DEFAULT_LLM_MODEL)
        
        return _call_ollama_api(prompt, api_url, model_name, operation_name)

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

def _call_ollama_api(prompt: str, api_url: str, model_name: str, operation_name: str) -> Optional[str]:
    """Call the Ollama API with the given prompt and model."""
    # Truncate very long prompts to avoid timeouts
    max_prompt_length = 8000
    if len(prompt) > max_prompt_length:
        print(f"Warning: Truncating long prompt from {len(prompt)} to {max_prompt_length} characters")
        prompt = prompt[:max_prompt_length] + "\n\n[Truncated due to length]"
    
    payload = {"model": model_name, "prompt": prompt, "stream": False}
    try:
        print(f"Sending request to Ollama LLM ({model_name}) for {operation_name}...")
        # Increase timeout for complex operations
        timeout = 120 if operation_name == "research workflow" else 60
        response = requests.post(api_url, json=payload, timeout=timeout)
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

def _call_openai_api(prompt: str, api_key: str, model_name: str, operation_name: str) -> Optional[str]:
    """Call the OpenAI API with the given prompt and model."""
    try:
        print(f"Sending request to OpenAI ({model_name}) for {operation_name}...")
        
        # Create OpenAI client with explicit parameters to avoid environment issues
        try:
            # Try creating client with minimal parameters
            client = OpenAI(api_key=api_key)
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
                    client = OpenAI(api_key=api_key)
                except:
                    # Last resort - use requests directly
                    print("Using direct API calls as fallback...")
                    return _call_openai_api_direct(prompt, api_key, model_name, operation_name)
            else:
                raise e
        
        # Check if this is a reasoning model (o1, o3)
        if model_name.startswith(('o1', 'o3')):
            # Use responses API for reasoning models
            response = client.responses.create(
                model=model_name,
                input=prompt,
                reasoning={"effort": "medium"}  # Can be made configurable
            )
            llm_response_text = response.choices[0].text.strip() if hasattr(response.choices[0], 'text') else str(response)
        else:
            # Use chat completions API for regular models
            response = client.chat.completions.create(
                model=model_name,
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
            st.error(f"OpenAI model error: Model '{model_name}' may not be available ({operation_name})")
        elif "rate" in str(e).lower():
            st.error(f"OpenAI rate limit error: Please wait and try again ({operation_name})")
        else:
            st.error(f"OpenAI API error: {e} ({operation_name})")
        return None

def _call_openai_api_direct(prompt: str, api_key: str, model_name: str, operation_name: str) -> Optional[str]:
    """Direct API call to OpenAI using requests library as a fallback."""
    try:
        import requests
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Determine which API to use based on model
        if model_name.startswith(('o1', 'o3')):
            # Use responses endpoint for reasoning models
            url = "https://api.openai.com/v1/responses"
            payload = {
                "model": model_name,
                "input": prompt,
                "reasoning": {"effort": "medium"}
            }
        else:
            # Use chat completions endpoint for regular models
            url = "https://api.openai.com/v1/chat/completions"
            payload = {
                "model": model_name,
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
        if model_name.startswith(('o1', 'o3')):
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

def _call_lmstudio_api(prompt: str, api_url: str, model_name: str, operation_name: str) -> Optional[str]:
    """Call the LM Studio API with the given prompt and model."""
    try:
        print(f"Sending request to LM Studio ({model_name}) for {operation_name}...")
        
        # LM Studio uses OpenAI-compatible endpoint for chat completions
        chat_url = f"{api_url}/v1/chat/completions"
        
        headers = {
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model_name,
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

def extract_content_intelligence(content_text: str, title: str, author: str = "Unknown", content_type: str = "general") -> dict:
    """
    Universal content analysis using LLM to extract entities, concepts, relationships, and metadata
    Works across any domain - Azure, movies, cooking, survival, etc.
    """
    if not content_text or not content_text.strip():
        return {
            'entities': [],
            'concepts': [],
            'content_structure': 'unknown',
            'difficulty_level': 'unknown',
            'prerequisites': [],
            'related_topics': [],
            'authority_signals': [],
            'category': 'General',
            'tags': [],
            'confidence_score': 0.1
        }
    
    # Create universal content analysis prompt
    prompt = f"""Analyze this content and extract structured information. Be domain-agnostic and work for any topic (tech, entertainment, cooking, survival, etc.).

CONTENT TITLE: {title}
AUTHOR/CREATOR: {author}
CONTENT TYPE: {content_type}

CONTENT TEXT:
{content_text[:8000]}

Please extract the following information in a structured format:

1. ENTITIES (specific people, places, tools, technologies, movies, etc.):
   - List 5-10 most important specific entities mentioned

2. CONCEPTS (abstract ideas, methodologies, genres, skills, etc.):
   - List 5-10 key concepts or topics covered

3. CONTENT STRUCTURE (what type of content this is):
   - tutorial/how-to, overview/explanation, comparison/review, troubleshooting/problem-solving, list/compilation, or discussion/opinion

4. DIFFICULTY LEVEL:
   - beginner, intermediate, advanced, or expert

5. PREREQUISITES (what someone should know/have before this content):
   - List 3-5 prerequisites if any are mentioned or implied

6. RELATED TOPICS (what naturally connects to this content):
   - List 5-8 related topics someone might want to learn about

7. AUTHORITY SIGNALS (indicators of expertise or confidence):
   - Quote specific phrases that show authority/experience
   - Rate confidence: high/medium/low

8. CATEGORY RECOMMENDATION:
   - Suggest the best high-level category for this content

9. DESCRIPTIVE TAGS:
   - List 8-12 descriptive tags that would help find this content

Please format your response as a valid JSON object with these exact keys:
{{
  "entities": ["entity1", "entity2"],
  "concepts": ["concept1", "concept2"],
  "content_structure": "tutorial",
  "difficulty_level": "intermediate",
  "prerequisites": ["prereq1", "prereq2"],
  "related_topics": ["topic1", "topic2"],
  "authority_signals": ["quote1", "quote2"],
  "category": "Category Name",
  "tags": ["tag1", "tag2"],
  "confidence_score": 0.8
}}"""

    try:
        response = _call_llm_api(prompt, "content intelligence extraction")
        
        if not response:
            return _fallback_content_analysis(title, content_text)
        
        # Parse JSON response
        try:
            # Clean up response to extract JSON
            if '```json' in response:
                response = response.split('```json')[1].split('```')[0]
            elif '```' in response:
                response = response.split('```')[1].split('```')[0]
            
            result = json.loads(response)
            
            # Validate required fields
            required_fields = ['entities', 'concepts', 'content_structure', 'difficulty_level', 
                             'prerequisites', 'related_topics', 'authority_signals', 'category', 'tags']
            
            for field in required_fields:
                if field not in result:
                    result[field] = []
            
            # Ensure confidence score exists
            if 'confidence_score' not in result:
                result['confidence_score'] = 0.7
            
            return result
            
        except json.JSONDecodeError:
            # If JSON parsing fails, try to extract information manually
            return _parse_unstructured_response(response, title)
            
    except Exception as e:
        print(f"Error in content intelligence extraction: {str(e)}")
        return _fallback_content_analysis(title, content_text)

def _fallback_content_analysis(title: str, content_text: str) -> dict:
    """Fallback analysis when LLM is unavailable"""
    # Simple keyword-based analysis
    words = content_text.lower().split()
    
    # Detect some basic patterns
    has_steps = any(word in content_text.lower() for word in ['step', 'first', 'second', 'then', 'next', 'finally'])
    has_comparison = any(word in content_text.lower() for word in ['versus', 'vs', 'better', 'worse', 'compare'])
    has_tutorial = any(word in content_text.lower() for word in ['how to', 'tutorial', 'guide', 'instruction'])
    
    if has_tutorial or has_steps:
        structure = 'tutorial'
    elif has_comparison:
        structure = 'comparison'
    else:
        structure = 'overview'
    
    # Basic category detection
    category = "General"
    if any(word in title.lower() for word in ['azure', 'cloud', 'microsoft', 'aws', 'tech']):
        category = "Technology"
    elif any(word in title.lower() for word in ['movie', 'film', 'actor', 'director']):
        category = "Entertainment"
    elif any(word in title.lower() for word in ['cook', 'recipe', 'food', 'kitchen']):
        category = "Cooking"
    elif any(word in title.lower() for word in ['survival', 'outdoor', 'camping', 'wilderness']):
        category = "Outdoor"
    
    return {
        'entities': [title],
        'concepts': [],
        'content_structure': structure,
        'difficulty_level': 'intermediate',
        'prerequisites': [],
        'related_topics': [],
        'authority_signals': [],
        'category': category,
        'tags': [structure, category.lower()],
        'confidence_score': 0.3
    }

def _parse_unstructured_response(response_text: str, title: str) -> dict:
    """Parse LLM response when JSON parsing fails"""
    # Try to extract information from unstructured text
    lines = response_text.split('\n')
    
    result = {
        'entities': [],
        'concepts': [],
        'content_structure': 'unknown',
        'difficulty_level': 'unknown',
        'prerequisites': [],
        'related_topics': [],
        'authority_signals': [],
        'category': 'General',
        'tags': [],
        'confidence_score': 0.5
    }
    
    current_section = None
    for line in lines:
        line = line.strip()
        if 'entities' in line.lower():
            current_section = 'entities'
        elif 'concepts' in line.lower():
            current_section = 'concepts'
        elif 'tags' in line.lower():
            current_section = 'tags'
        elif 'category' in line.lower() and ':' in line:
            result['category'] = line.split(':')[1].strip()
        elif current_section and line.startswith('-'):
            item = line[1:].strip()
            if current_section in result and isinstance(result[current_section], list):
                result[current_section].append(item)
    
    return result

def recommend_category_and_tags(transcript: str, video_title: str, video_author: str) -> Dict[str, Any]:
    """
    Recommend a category and suggest tags for a YouTube video.
    
    Args:
        transcript: The full transcript text
        video_title: Title of the video
        video_author: Channel/author name
        
    Returns:
        Dict with 'category' and 'tags' keys, or None if failed
    """
    prompt = f"""Based on the following YouTube video information, please recommend a category and suggest relevant tags.

Video Title: {video_title}
Channel/Author: {video_author}

Transcript excerpt:
{transcript[:3000]}...

Available categories:
- Programming: Software development, coding tutorials, programming languages
- AI/ML: Artificial intelligence, machine learning, deep learning, neural networks
- DevOps: CI/CD, cloud computing, infrastructure, deployment, containers
- Web Development: Frontend, backend, web frameworks, HTML/CSS/JavaScript
- Database: SQL, NoSQL, database design, data modeling
- Security: Cybersecurity, encryption, security best practices

Please respond in the following JSON format ONLY (no additional text):
{{
    "category": "One of the categories listed above",
    "tags": ["tag1", "tag2", "tag3", "tag4", "tag5"],
    "category_reasoning": "Brief explanation of why this category was chosen"
}}

Provide 5-7 relevant tags that describe the content. Tags should be lowercase and concise."""

    response = _call_llm_api(prompt, "category and tag recommendation")
    if not response:
        return {"category": "Programming", "tags": [], "category_reasoning": "Failed to get recommendation"}
    
    try:
        # Try to parse as JSON
        import json
        result = json.loads(response)
        
        # Validate category
        valid_categories = ["Programming", "AI/ML", "DevOps", "Web Development", "Database", "Security"]
        if result.get("category") not in valid_categories:
            result["category"] = "Programming"  # Default
            
        # Ensure tags is a list
        if not isinstance(result.get("tags"), list):
            result["tags"] = []
            
        return result
    except json.JSONDecodeError:
        # If JSON parsing fails, try to extract information manually
        category = "Programming"  # Default
        tags = []
        
        # Simple pattern matching for category
        response_lower = response.lower()
        if "ai/ml" in response_lower or "artificial intelligence" in response_lower or "machine learning" in response_lower:
            category = "AI/ML"
        elif "devops" in response_lower or "deployment" in response_lower or "cloud" in response_lower:
            category = "DevOps"
        elif "web development" in response_lower or "frontend" in response_lower or "backend" in response_lower:
            category = "Web Development"
        elif "database" in response_lower or "sql" in response_lower:
            category = "Database"
        elif "security" in response_lower or "cybersecurity" in response_lower:
            category = "Security"
            
        return {"category": category, "tags": tags, "category_reasoning": "Extracted from response"}

def summarize_youtube_transcript(transcript: str, video_title: str, video_author: str) -> Optional[str]:
    """
    Summarize a YouTube video transcript using the configured LLM.
    
    Args:
        transcript: The full transcript text
        video_title: Title of the video
        video_author: Channel/author name
        
    Returns:
        A summary with key points, or None if failed
    """
    prompt = f"""Please provide a comprehensive summary of the following YouTube video transcript.

Video Title: {video_title}
Channel/Author: {video_author}

Instructions:
1. Start with a brief overview (2-3 sentences)
2. List the main key points or topics covered (use bullet points)
3. Include any important quotes or insights
4. If there are actionable items or recommendations, list them separately
5. Keep the summary concise but informative

Transcript:
{transcript[:8000]}...  # Limiting to avoid token limits

Please format your response in markdown."""

    return _call_llm_api(prompt, "YouTube video summarization")

def get_available_openai_models(api_key: Optional[str] = None) -> List[str]:
    """Fetch available OpenAI models dynamically from the API."""
    # If no API key provided, try to get from session state
    if not api_key:
        api_key = st.session_state.get('openai_api_key', '')
    
    if not api_key:
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
        # Use requests to directly call the API and bypass the proxy issue
        import requests
        
        headers = {
            "Authorization": f"Bearer {api_key}",
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

def get_available_lmstudio_models(api_url: str = DEFAULT_LMSTUDIO_API_URL) -> List[str]:
    """
    Fetch available models from LM Studio API.
    
    Returns:
        List of model names
    """
    model_names: List[str] = []
    
    models_url = f"{api_url}/v1/models"
    
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

def get_available_ollama_models(api_url: str = DEFAULT_LLM_API_URL) -> Tuple[List[str], Dict[str, str]]:
    """
    Fetch available models from Ollama API with detailed information.
    
    Returns:
        tuple: (model_names, model_display_info)
    """
    model_names: List[str] = []
    model_display_info: Dict[str, str] = {}
    
    # Extract base URL
    base_url = api_url.split('/api/')[0] if '/api/' in api_url else api_url
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
            
            # Sort models
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

def test_llm_connection() -> Tuple[bool, str]:
    """Test the connection to the currently selected LLM provider"""
    provider = st.session_state.get("llm_provider", "ollama")
    test_prompt = "Please respond with just the word 'connected'."
    
    if provider == "openai":
        api_key = st.session_state.get("openai_api_key", "")
        model_name = st.session_state.get("openai_model", DEFAULT_OPENAI_MODEL)
        
        if not api_key: return False, "OpenAI API key is not set"
        if not OPENAI_AVAILABLE: return False, "OpenAI package not installed"
        
        try:
            response = _call_openai_api(test_prompt, api_key, model_name, "connection test")
            if response and "connect" in response.lower():
                return True, f"Connected to OpenAI ({model_name})"
            else:
                return False, f"Failed to get a valid response from OpenAI"
        except Exception as e:
            return False, f"OpenAI API error: {str(e)[:100]}"
    elif provider == "lmstudio":
        api_url = st.session_state.get("lmstudio_api_url", DEFAULT_LMSTUDIO_API_URL)
        model_name = st.session_state.get("lmstudio_model", DEFAULT_LMSTUDIO_MODEL)
        
        try:
            response = _call_lmstudio_api(test_prompt, api_url, model_name, "connection test")
            if response and "connect" in response.lower():
                return True, f"Connected to LM Studio ({model_name})"
            else:
                return False, f"Failed to get a valid response from LM Studio ({model_name})"
        except Exception as e:
            return False, f"LM Studio API error: {str(e)[:100]}"
    else:  # Ollama
        api_url = st.session_state.get("ollama_api_url", DEFAULT_LLM_API_URL)
        model_name = st.session_state.get("ollama_model", DEFAULT_LLM_MODEL)
        
        try:
            response = _call_ollama_api(test_prompt, api_url, model_name, "connection test")
            if response and "connect" in response.lower():
                return True, f"Connected to Ollama ({model_name})"
            else:
                return False, f"Failed to get a valid response from Ollama ({model_name})"
        except Exception as e:
            return False, f"Ollama API error: {str(e)[:100]}"