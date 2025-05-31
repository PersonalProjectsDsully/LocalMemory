import streamlit as st
from typing import Dict, Any
from .settings_manager import settings_manager

# Flag to track if settings have been modified
_settings_modified = False

def initialize_session_state():
    """Initialize session state from saved settings"""
    # Load saved settings
    saved_settings = settings_manager.load_settings()
    
    # Initialize session state with saved values if not already set
    for key, value in saved_settings.items():
        if key not in st.session_state:
            st.session_state[key] = value
    
    # Initialize other session state variables that aren't in settings
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []
    
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    
    if 'settings' not in st.session_state:
        st.session_state.settings = saved_settings.copy()

def sync_settings_to_session_state(settings: Dict[str, Any]):
    """Sync settings dict to session state"""
    for key, value in settings.items():
        st.session_state[key] = value
    st.session_state.settings = settings.copy()

def sync_session_state_to_settings() -> Dict[str, Any]:
    """Sync session state back to settings dict"""
    settings = st.session_state.get('settings', {}).copy()
    
    # Update settings with current session state values
    settings_keys = [
        'theme', 'items_per_page', 'show_previews', 'auto_save',
        'default_category', 'youtube_language', 'export_format',
        'enable_analytics', 'llm_provider', 'ollama_api_url',
        'ollama_model', 'openai_api_key', 'openai_model',
        'lmstudio_api_url', 'lmstudio_model',
        'chat_use_knowledge_base', 'chat_selected_categories',
        'chat_max_context_docs', 'sidebar_state', 'default_view'
    ]
    
    for key in settings_keys:
        if key in st.session_state:
            settings[key] = st.session_state[key]
    
    return settings

def auto_save_settings():
    """Automatically save settings when they change"""
    if st.session_state.get('auto_save_enabled', True):
        current_settings = sync_session_state_to_settings()
        settings_manager.save_settings(current_settings)
        return True
    return False

def mark_settings_modified():
    """Mark that settings have been modified"""
    global _settings_modified
    _settings_modified = True
    # Auto-save if enabled
    auto_save_settings()