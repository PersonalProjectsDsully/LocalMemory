import streamlit as st
import re
from typing import Dict, Optional, Tuple
import requests
from pytube import YouTube

def extract_video_id(url: str) -> Optional[str]:
    """Extract video ID from YouTube URL"""
    video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    return video_id_match.group(1) if video_id_match else None

@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_video_info(video_id: str) -> Dict[str, str]:
    """Fetch video information with caching to prevent re-fetching"""
    video_title = "YouTube Video"
    video_author = "Unknown Channel"
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    
    # Method 1: Try noembed API (no API key required)
    try:
        noembed_url = f"https://noembed.com/embed?url=https://www.youtube.com/watch?v={video_id}"
        response = requests.get(noembed_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            video_title = data.get('title', 'YouTube Video')
            video_author = data.get('author_name', 'Unknown Channel')
            if 'thumbnail_url' in data:
                thumbnail_url = data['thumbnail_url']
                thumbnail_url = thumbnail_url.replace('hqdefault', 'maxresdefault')
    except:
        pass
    
    # Method 2: Try YouTube oEmbed API as backup
    if video_title == "YouTube Video":
        try:
            oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
            response = requests.get(oembed_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                video_title = data.get('title', 'YouTube Video')
                video_author = data.get('author_name', 'Unknown Channel')
                if 'thumbnail_url' in data:
                    thumbnail_url = data['thumbnail_url'].replace('hqdefault', 'maxresdefault')
        except:
            pass
    
    # Method 3: Try pytube as last resort
    if video_title == "YouTube Video":
        try:
            yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
            if hasattr(yt, 'title') and yt.title:
                video_title = yt.title
            if hasattr(yt, 'author') and yt.author:
                video_author = yt.author
            if hasattr(yt, 'thumbnail_url') and yt.thumbnail_url:
                thumbnail_url = yt.thumbnail_url
        except:
            pass
    
    return {
        'title': video_title,
        'author': video_author,
        'thumbnail_url': thumbnail_url,
        'video_id': video_id
    }