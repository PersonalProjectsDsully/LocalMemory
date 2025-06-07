"""
YouTube Page Utils Module

Contains utility functions and styling for the YouTube page.
"""

import streamlit as st
from datetime import datetime, timedelta
import re


def parse_youtube_date(published_str: str, reference_time: datetime) -> datetime:
    """
    Parse YouTube published date strings like '1 month ago', '2 weeks ago', etc.
    Returns a datetime object representing when the video was published.
    """
    if not published_str:
        return reference_time
    
    published_lower = published_str.lower().strip()
    
    # Handle ISO format dates first
    if not 'ago' in published_lower:
        try:
            # Try parsing ISO format
            return datetime.fromisoformat(published_str.replace('Z', '+00:00')).replace(tzinfo=None)
        except:
            return reference_time
    
    # Parse "X time ago" format
    # Extract number and time unit
    match = re.search(r'(\d+)\s*(second|minute|hour|day|week|month|year)s?\s+ago', published_lower)
    
    if not match:
        return reference_time
    
    number = int(match.group(1))
    unit = match.group(2)
    
    if unit == 'second':
        return reference_time - timedelta(seconds=number)
    elif unit == 'minute':
        return reference_time - timedelta(minutes=number)
    elif unit == 'hour':
        return reference_time - timedelta(hours=number)
    elif unit == 'day':
        return reference_time - timedelta(days=number)
    elif unit == 'week':
        return reference_time - timedelta(weeks=number)
    elif unit == 'month':
        # Approximate: 30 days per month
        return reference_time - timedelta(days=number * 30)
    elif unit == 'year':
        # Approximate: 365 days per year
        return reference_time - timedelta(days=number * 365)
    
    return reference_time


def setup_page_styling():
    """Setup custom CSS styling for the YouTube page"""
    st.markdown("""
    <style>
        /* Style all buttons with dark blue theme */
        .stButton>button {
            width: 100%;
            background-color: #1e3a5f !important;
            color: white !important;
            border: none !important;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #2c5282 !important;
            color: white !important;
        }
        .video-info {
            background-color: #1a1a1a;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
            border: 1px solid #333;
        }
        .video-info h3 {
            color: #ffffff;
            margin-bottom: 0.5rem;
        }
        .video-info p {
            color: #cccccc;
        }
        .channel-video-item {
            background-color: #1a1a1a;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 0.5rem;
            border: 1px solid #333;
            transition: border-color 0.3s ease;
        }
        .channel-video-item:hover {
            border-color: #2c5282;
        }
    </style>
    """, unsafe_allow_html=True)


def initialize_youtube_session_state():
    """Initialize YouTube-specific session state variables"""
    defaults = {
        'is_loading_transcript': False,
        'youtube_video_id': None,
        'youtube_video_title': None,
        'current_video_info': None,
        'channel_videos': [],
        'selected_videos': [],
        'channel_processing_complete': False
    }
    
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value


def format_video_duration(duration_seconds):
    """Format video duration from seconds to readable format"""
    if not duration_seconds:
        return "Unknown"
    
    try:
        duration = int(duration_seconds)
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60
        
        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes}:{seconds:02d}"
    except (ValueError, TypeError):
        return "Unknown"


def format_view_count(view_count):
    """Format view count to readable format"""
    if not view_count:
        return "Unknown"
    
    try:
        views = int(view_count)
        if views >= 1000000:
            return f"{views/1000000:.1f}M views"
        elif views >= 1000:
            return f"{views/1000:.1f}K views"
        else:
            return f"{views} views"
    except (ValueError, TypeError):
        return "Unknown"


def create_video_info_display(video_info):
    """Create a formatted video info display"""
    if not video_info:
        return
    
    st.markdown(f"""
    <div class="video-info">
        <h3>{video_info.get('title', 'Unknown Title')}</h3>
        <p><strong>Channel:</strong> {video_info.get('channel_title', 'Unknown Channel')}</p>
        <p><strong>Duration:</strong> {format_video_duration(video_info.get('duration'))}</p>
        <p><strong>Views:</strong> {format_view_count(video_info.get('view_count'))}</p>
        <p><strong>Published:</strong> {video_info.get('published_date', 'Unknown')}</p>
    </div>
    """, unsafe_allow_html=True)


def display_processing_status(status_message, is_processing=True):
    """Display a processing status message"""
    if is_processing:
        st.info(f"🔄 {status_message}")
    else:
        st.success(f"✅ {status_message}")


def handle_youtube_url_validation(url):
    """Validate and extract video ID from YouTube URL"""
    if not url:
        return None, "Please enter a YouTube URL"
    
    from utils.youtube.youtube_utils import extract_video_id
    
    video_id = extract_video_id(url)
    if not video_id:
        return None, "Invalid YouTube URL. Please enter a valid YouTube video URL."
    
    return video_id, None


def create_video_thumbnail_url(video_id):
    """Create YouTube thumbnail URL for a video ID"""
    if not video_id:
        return None
    return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"