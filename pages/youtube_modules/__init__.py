# YouTube Module Components
"""
This package contains the refactored components of the YouTube page.
The original monolithic file has been split into logical modules for better
maintainability and organization.
"""

from .youtube_page_utils import (
    parse_youtube_date,
    setup_page_styling,
    initialize_youtube_session_state
)

from .single_video_handler import (
    render_single_video_tab,
    process_video_url,
    extract_video_transcript,
    generate_video_summary,
    save_video_to_knowledgebase
)

from .channel_explorer_handler import (
    render_channel_explorer_tab,
    process_channel_url,
    fetch_channel_videos,
    handle_bulk_processing,
    process_duplicate_detection
)

from .llm_settings_manager import (
    render_llm_settings_sidebar,
    handle_provider_change,
    update_model_settings,
    get_current_llm_config
)

__all__ = [
    # Utils
    'parse_youtube_date',
    'setup_page_styling',
    'initialize_youtube_session_state',
    
    # Single video
    'render_single_video_tab',
    'process_video_url',
    'extract_video_transcript',
    'generate_video_summary',
    'save_video_to_knowledgebase',
    
    # Channel explorer
    'render_channel_explorer_tab',
    'process_channel_url',
    'fetch_channel_videos',
    'handle_bulk_processing',
    'process_duplicate_detection',
    
    # LLM settings
    'render_llm_settings_sidebar',
    'handle_provider_change',
    'update_model_settings',
    'get_current_llm_config'
]