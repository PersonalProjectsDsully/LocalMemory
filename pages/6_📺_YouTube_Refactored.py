"""
YouTube Content Manager - Refactored Version

This is the refactored version of the YouTube page, split into modular components
for better maintainability and organization.
"""

import streamlit as st
import os
import sys

# Add path for utils imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import refactored modules
from youtube_modules import (
    # Utils
    setup_page_styling,
    initialize_youtube_session_state,
    
    # Single video
    render_single_video_tab,
    
    # Channel explorer
    render_channel_explorer_tab,
    
    # LLM settings
    render_llm_settings_sidebar
)

# Import utilities
from utils.session.session_state_manager import initialize_session_state

# Page configuration
st.set_page_config(
    page_title="YouTube - Local Knowledgebase",
    page_icon="📺",
    layout="wide"
)


def main():
    """Main application entry point"""
    # Initialize session state from saved settings
    initialize_session_state()
    
    # Initialize YouTube-specific session state
    initialize_youtube_session_state()
    
    # Setup custom styling
    setup_page_styling()
    
    # Page title and description
    st.title("📺 YouTube Content Manager")
    st.write("Extract transcripts from videos and explore entire YouTube channels")
    
    # Render LLM settings sidebar
    render_llm_settings_sidebar()
    
    # Main content tabs
    render_main_tabs()


def render_main_tabs():
    """Render the main content tabs"""
    tab1, tab2 = st.tabs(["🎥 Single Video", "📡 Channel Explorer"])
    
    with tab1:
        render_single_video_tab()
    
    with tab2:
        render_channel_explorer_tab()


if __name__ == "__main__":
    main()