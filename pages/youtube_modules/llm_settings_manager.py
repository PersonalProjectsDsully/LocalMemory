"""
LLM Settings Manager Module

Handles LLM provider configuration and settings synchronization for the YouTube page.
"""

import streamlit as st
from utils.llm.llm_utils import (
    get_available_ollama_models, 
    get_available_openai_models, 
    get_available_lmstudio_models
)
from utils.session.session_state_manager import auto_save_settings


def render_llm_settings_sidebar():
    """Render the LLM settings sidebar"""
    with st.sidebar:
        render_llm_provider_settings()
        st.divider()
        render_youtube_api_settings()
        st.divider()
        render_auto_save_status()


def render_llm_provider_settings():
    """Render LLM provider selection and configuration"""
    st.subheader("⚙️ LLM Settings")
    st.info("💡 Settings are synced with global Settings page")
    
    # Get current provider from global settings
    current_provider = st.session_state.get('llm_provider', 'ollama')
    provider_display_map = {
        "ollama": "Ollama (Local)",
        "openai": "OpenAI",
        "lmstudio": "LM Studio (Local)"
    }
    current_display = provider_display_map.get(current_provider, "Ollama (Local)")
    
    # Provider selection
    provider_options = ["Ollama (Local)", "OpenAI", "LM Studio (Local)"]
    provider = st.selectbox(
        "LLM Provider",
        provider_options,
        index=provider_options.index(current_display),
        key="llm_provider_youtube",
        on_change=handle_provider_change,
        help="Synced with global settings - choose between local Ollama, cloud OpenAI, or local LM Studio"
    )
    
    # Provider-specific settings
    if provider == "OpenAI":
        render_openai_settings()
    elif provider == "LM Studio (Local)":
        render_lmstudio_settings()
    else:  # Ollama (Local)
        render_ollama_settings()


def handle_provider_change():
    """Handle LLM provider change and sync with global settings"""
    provider_map = {
        "Ollama (Local)": "ollama",
        "OpenAI": "openai", 
        "LM Studio (Local)": "lmstudio"
    }
    st.session_state.llm_provider = provider_map.get(st.session_state.llm_provider_youtube, "ollama")
    auto_save_settings()


def render_openai_settings():
    """Render OpenAI-specific settings"""
    def on_api_key_change():
        st.session_state.openai_api_key = st.session_state.openai_api_key_youtube
        auto_save_settings()
    
    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        value=st.session_state.get('openai_api_key', ''),
        key="openai_api_key_youtube",
        help="Enter your OpenAI API key",
        on_change=on_api_key_change
    )
    
    # Model selection
    model_options = get_available_openai_models(st.session_state.get('openai_api_key'))
    if model_options:
        current_model = st.session_state.get('openai_model', 'gpt-3.5-turbo')
        
        def on_openai_model_change():
            st.session_state.openai_model = st.session_state.openai_model_youtube
            auto_save_settings()
        
        selected_model = st.selectbox(
            "Model",
            model_options,
            index=model_options.index(current_model) if current_model in model_options else 0,
            key="openai_model_youtube",
            on_change=on_openai_model_change
        )


def render_lmstudio_settings():
    """Render LM Studio-specific settings"""
    def on_lmstudio_url_change():
        st.session_state.lmstudio_api_url = st.session_state.lmstudio_api_url_youtube
        auto_save_settings()
    
    api_url = st.text_input(
        "LM Studio API URL",
        value=st.session_state.get('lmstudio_api_url', 'http://localhost:1234'),
        key="lmstudio_api_url_youtube",
        help="URL for your local LM Studio instance (default: http://localhost:1234)",
        on_change=on_lmstudio_url_change
    )
    
    # Model selection
    models = get_available_lmstudio_models(api_url)
    if models:
        current_model = st.session_state.get('lmstudio_model', '')
        
        def on_lmstudio_model_change():
            st.session_state.lmstudio_model = st.session_state.lmstudio_model_youtube
            auto_save_settings()
        
        selected_model = st.selectbox(
            "Model",
            models,
            index=models.index(current_model) if current_model in models else 0,
            key="lmstudio_model_youtube",
            on_change=on_lmstudio_model_change
        )
    else:
        st.warning("No LM Studio models found. Is LM Studio server running? (lms server start)")


def render_ollama_settings():
    """Render Ollama-specific settings"""
    def on_ollama_url_change():
        st.session_state.ollama_api_url = st.session_state.ollama_api_url_youtube
        auto_save_settings()
    
    api_url = st.text_input(
        "Ollama API URL",
        value=st.session_state.get('ollama_api_url', 'http://localhost:11434/api/generate'),
        key="ollama_api_url_youtube",
        on_change=on_ollama_url_change
    )
    
    # Model selection
    models, model_info = get_available_ollama_models(api_url)
    if models:
        current_model = st.session_state.get('ollama_model', 'llama3.1:8b')
        
        def on_ollama_model_change():
            st.session_state.ollama_model = st.session_state.ollama_model_youtube
            auto_save_settings()
        
        selected_model = st.selectbox(
            "Model",
            models,
            format_func=lambda x: f"{x} {model_info.get(x, '')}",
            index=models.index(current_model) if current_model in models else 0,
            key="ollama_model_youtube",
            on_change=on_ollama_model_change
        )
    else:
        st.warning("No Ollama models found. Is Ollama running?")


def render_youtube_api_settings():
    """Render YouTube Data API settings"""
    st.subheader("📺 YouTube Data API")
    st.caption("Optional: For fetching more than 15 videos per channel")
    
    def on_youtube_api_key_change():
        st.session_state.youtube_api_key = st.session_state.youtube_api_key_input
        auto_save_settings()
    
    youtube_api_key = st.text_input(
        "YouTube Data API Key",
        type="password",
        value=st.session_state.get('youtube_api_key', ''),
        key="youtube_api_key_input",
        help="Enter your YouTube Data API v3 key to fetch more videos",
        on_change=on_youtube_api_key_change
    )
    
    if youtube_api_key:
        st.success("✅ API key configured")
        st.caption("Can fetch up to 50 videos per channel")
    else:
        st.info("Using RSS feeds (limited to ~15 recent videos)")
        
    st.caption("Get API key at: [Google Cloud Console](https://console.cloud.google.com/apis/credentials)")


def render_auto_save_status():
    """Render auto-save status indicator"""
    if st.session_state.get('auto_save_enabled', True):
        st.caption("🔄 Settings auto-save is enabled")


def get_current_llm_config():
    """Get the current LLM configuration"""
    provider = st.session_state.get('llm_provider', 'ollama')
    
    config = {
        'provider': provider
    }
    
    if provider == 'openai':
        config.update({
            'api_key': st.session_state.get('openai_api_key', ''),
            'model': st.session_state.get('openai_model', 'gpt-3.5-turbo')
        })
    elif provider == 'lmstudio':
        config.update({
            'api_url': st.session_state.get('lmstudio_api_url', 'http://localhost:1234'),
            'model': st.session_state.get('lmstudio_model', '')
        })
    else:  # ollama
        config.update({
            'api_url': st.session_state.get('ollama_api_url', 'http://localhost:11434/api/generate'),
            'model': st.session_state.get('ollama_model', 'llama3.1:8b')
        })
    
    return config


def update_model_settings(provider, model):
    """Update model settings for the specified provider"""
    if provider == 'openai':
        st.session_state.openai_model = model
    elif provider == 'lmstudio':
        st.session_state.lmstudio_model = model
    elif provider == 'ollama':
        st.session_state.ollama_model = model
    
    auto_save_settings()


def validate_llm_configuration():
    """Validate the current LLM configuration"""
    provider = st.session_state.get('llm_provider', 'ollama')
    
    if provider == 'openai':
        api_key = st.session_state.get('openai_api_key', '')
        if not api_key:
            return False, "OpenAI API key is required"
        
        model = st.session_state.get('openai_model', '')
        if not model:
            return False, "OpenAI model selection is required"
            
    elif provider == 'lmstudio':
        api_url = st.session_state.get('lmstudio_api_url', '')
        if not api_url:
            return False, "LM Studio API URL is required"
        
        model = st.session_state.get('lmstudio_model', '')
        if not model:
            return False, "LM Studio model selection is required"
            
    elif provider == 'ollama':
        api_url = st.session_state.get('ollama_api_url', '')
        if not api_url:
            return False, "Ollama API URL is required"
        
        model = st.session_state.get('ollama_model', '')
        if not model:
            return False, "Ollama model selection is required"
    
    return True, "Configuration is valid"


def get_provider_status():
    """Get the status of the current LLM provider"""
    provider = st.session_state.get('llm_provider', 'ollama')
    
    if provider == 'openai':
        api_key = st.session_state.get('openai_api_key', '')
        return "configured" if api_key else "needs_configuration"
        
    elif provider == 'lmstudio':
        api_url = st.session_state.get('lmstudio_api_url', '')
        model = st.session_state.get('lmstudio_model', '')
        return "configured" if api_url and model else "needs_configuration"
        
    elif provider == 'ollama':
        api_url = st.session_state.get('ollama_api_url', '')
        model = st.session_state.get('ollama_model', '')
        return "configured" if api_url and model else "needs_configuration"
    
    return "unknown"