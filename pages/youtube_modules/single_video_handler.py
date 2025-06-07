"""
Single Video Handler Module

Handles single YouTube video processing, transcript extraction, and AI summarization.
"""

import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import time
from datetime import datetime
from pathlib import Path
import json

from utils.youtube.youtube_utils import extract_video_id, fetch_video_info
from utils.llm.llm_utils import (
    summarize_youtube_transcript, 
    recommend_category_and_tags, 
    test_llm_connection,
    extract_content_intelligence,
    classify_youtube_video
)
from utils.content.duplicate_detection import find_existing_video, get_duplicate_handling_choice, update_existing_video_metadata


def render_single_video_tab():
    """Render the single video processing tab"""
    # YouTube URL input
    youtube_url = st.text_input(
        "Enter YouTube URL:", 
        placeholder="https://youtube.com/watch?v=... or https://youtu.be/...",
        help="Paste any YouTube video URL here",
        key="youtube_url_input"
    )
    
    if youtube_url:
        video_id, error = process_video_url(youtube_url)
        
        if video_id:
            display_video_interface(video_id)
        else:
            st.error(error or "Invalid YouTube URL. Please enter a valid YouTube video URL.")
    
    # Display transcript and summary if available
    if 'youtube_transcript' in st.session_state and 'youtube_video_id' in st.session_state:
        display_transcript_interface()


def process_video_url(youtube_url):
    """Process the YouTube URL and extract video information"""
    video_id = extract_video_id(youtube_url)
    
    if not video_id:
        return None, "Invalid YouTube URL. Please enter a valid YouTube video URL."
    
    # Fetch video info using cached function
    with st.spinner("Loading video information..."):
        video_info = fetch_video_info(video_id)
    
    # Store in session state
    st.session_state['youtube_video_id'] = video_id
    st.session_state['youtube_video_title'] = video_info['title']
    st.session_state['youtube_video_author'] = video_info['author']
    st.session_state['youtube_thumbnail_url'] = video_info['thumbnail_url']
    st.session_state['youtube_url'] = youtube_url
    st.session_state['current_video_info'] = video_info
    
    return video_id, None


def display_video_interface(video_id):
    """Display the video information and control interface"""
    video_info = st.session_state.get('current_video_info', {})
    
    # Display video info
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(video_info.get('thumbnail_url', ''), use_container_width=True)
    
    with col2:
        st.markdown('<div class="video-info">', unsafe_allow_html=True)
        if video_info.get('title') != "YouTube Video":
            st.subheader(video_info.get('title', 'Unknown Title'))
        st.caption(f"Channel: {video_info.get('author', 'Unknown Channel')}")
        st.caption(f"Video ID: {video_id}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Control buttons
        render_video_control_buttons(video_id)


def render_video_control_buttons(video_id):
    """Render the control buttons for video operations"""
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    
    with col_btn1:
        render_transcript_button(video_id)
    
    with col_btn2:
        render_language_check_button(video_id)
    
    with col_btn3:
        render_llm_test_button()


def render_transcript_button(video_id):
    """Render the transcript extraction button"""
    # Only show Get Transcript if we don't have it yet
    if 'youtube_transcript' not in st.session_state or st.session_state.get('youtube_video_id') != video_id:
        if st.button("Get Transcript", type="primary", use_container_width=True):
            extract_video_transcript(video_id)
    else:
        # Transcript already loaded
        st.success("✓ Transcript loaded")


def render_language_check_button(video_id):
    """Render the language check button"""
    if st.button("Check Languages", use_container_width=True):
        check_available_languages(video_id)


def render_llm_test_button():
    """Render the LLM test button"""
    if st.button("Test LLM", use_container_width=True):
        with st.spinner("Testing LLM connection..."):
            success, message = test_llm_connection()
            if success:
                st.success(message)
            else:
                st.error(message)


def extract_video_transcript(video_id):
    """Extract transcript from YouTube video with retry logic"""
    st.session_state.is_loading_transcript = True
    
    # Create progress indicators for retry attempts
    status_container = st.empty()
    progress_container = st.empty()
    
    # Intelligent retry logic with progressive delays
    transcript = None
    transcript_error = None
    max_retries = 3
    retry_delays = [0, 3, 6]  # 0 seconds (immediate), 3 seconds, 6 seconds
    
    for attempt in range(max_retries):
        try:
            if attempt == 0:
                status_container.info("🔄 Fetching transcript...")
            else:
                status_container.warning(f"🔄 Retry attempt {attempt}/{max_retries-1} - Fetching transcript...")
                progress_container.info(f"⏳ Waiting {retry_delays[attempt]} seconds before retry...")
                time.sleep(retry_delays[attempt])
            
            # Try to get transcript
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            break  # Success! Exit retry loop
            
        except Exception as transcript_exc:
            transcript_error = str(transcript_exc)
            
            # If this is not the last attempt, check if we should retry
            if attempt < max_retries - 1:
                # Check if this is a retryable error
                if any(retryable in transcript_error.lower() for retryable in [
                    'timeout', 'connection', 'network', 'temporary', 'too many requests'
                ]):
                    status_container.warning(f"⚠️ Attempt {attempt + 1} failed: {transcript_error[:50]}... Retrying...")
                    continue  # Retry for network/rate limit issues
                else:
                    # For non-retryable errors (no captions, private video), break immediately
                    status_container.error(f"❌ Attempt {attempt + 1} failed: {transcript_error[:50]}...")
                    break
            
            # Last attempt failed, try alternative transcript sources
            if attempt == max_retries - 1:
                try:
                    status_container.info("🔍 Trying alternative transcript sources...")
                    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                    available_transcripts = list(transcript_list)
                    if available_transcripts:
                        # Try the first available transcript
                        transcript = available_transcripts[0].fetch()
                        status_container.success("✅ Found transcript using alternative source!")
                        break
                except:
                    pass
    
    # Clear progress indicators
    progress_container.empty()
    
    if transcript:
        # Success! Process the transcript
        process_transcript_success(transcript, status_container)
    else:
        # All attempts failed
        handle_transcript_failure(transcript_error, status_container)


def process_transcript_success(transcript, status_container):
    """Process successful transcript extraction"""
    status_container.success("✅ Transcript loaded successfully!")
    
    # Combine transcript text with timestamps
    full_transcript = ""
    full_transcript_text_only = ""
    
    for entry in transcript:
        timestamp = f"[{int(entry['start']//60):02d}:{int(entry['start']%60):02d}]"
        full_transcript += f"{timestamp} {entry['text']}\n"
        full_transcript_text_only += f"{entry['text']} "
    
    # Store transcript in session state
    st.session_state['youtube_transcript'] = full_transcript
    st.session_state['youtube_transcript_text_only'] = full_transcript_text_only
    st.session_state.is_loading_transcript = False
    
    # Clear status and rerun to show transcript
    status_container.empty()
    st.rerun()


def handle_transcript_failure(transcript_error, status_container):
    """Handle transcript extraction failure"""
    st.session_state.is_loading_transcript = False
    status_container.empty()
    
    # Determine the reason for failure and show appropriate message
    if "no element found" in transcript_error:
        st.error("❌ This video does not have captions available after 3 attempts.")
        st.info("💡 **Possible reasons:**")
        st.info("• Video has no captions or auto-generated captions")
        st.info("• Captions are disabled by the creator")
        st.info("• Video is too new (captions still processing)")
    elif "Video unavailable" in transcript_error:
        st.error("❌ Video is unavailable or private after 3 attempts.")
    elif "Too Many Requests" in transcript_error:
        st.error("❌ Rate limited after 3 attempts. Please wait a few minutes and try again.")
    else:
        st.error(f"❌ Failed to get transcript after 3 attempts: {transcript_error}")
    
    st.info("💡 **Try these videos with known captions:**")
    st.code("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    st.code("https://www.youtube.com/watch?v=jNQXAC9IVRw")


def check_available_languages(video_id):
    """Check available transcript languages for the video"""
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        available_langs = []
        for transcript in transcript_list:
            lang_info = f"{transcript.language} ({transcript.language_code})"
            if transcript.is_generated:
                lang_info += " [Auto-generated]"
            available_langs.append(lang_info)
        
        if available_langs:
            st.success(f"Available transcripts: {', '.join(available_langs)}")
        else:
            st.warning("No transcripts found for this video.")
    except Exception as e:
        st.error("No captions available for this video.")


def display_transcript_interface():
    """Display the transcript and AI summary interface"""
    st.divider()
    
    # Create tabs for transcript and summary
    tab1_1, tab1_2 = st.tabs(["📝 Transcript", "🤖 AI Summary"])
    
    with tab1_1:
        display_transcript_tab()
    
    with tab1_2:
        display_ai_summary_tab()


def display_transcript_tab():
    """Display the transcript viewing tab"""
    # Options for transcript display
    col1, col2 = st.columns([1, 1])
    with col1:
        show_timestamps = st.checkbox("Show timestamps", value=True)
    with col2:
        # Category selector for saving
        categories = ["Programming", "AI/ML", "DevOps", "Web Development", "Database", "Security"]
        save_category = st.selectbox("Save to category:", ["Select category..."] + categories)
    
    # Display transcript
    transcript_to_show = st.session_state['youtube_transcript'] if show_timestamps else st.session_state['youtube_transcript_text_only']
    
    with st.container():
        st.text_area(
            "Transcript:",
            value=transcript_to_show,
            height=400,
            disabled=True,
            key="transcript_display"
        )
    
    # Save to knowledgebase button
    if save_category != "Select category...":
        if st.button("💾 Save to Knowledgebase", type="primary", use_container_width=True):
            save_video_to_knowledgebase(save_category)


def display_ai_summary_tab():
    """Display the AI summary tab"""
    # Summary generation
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🤖 Generate Summary", type="primary", use_container_width=True):
            generate_video_summary()
    
    with col2:
        if st.button("🏷️ Get Category & Tags", use_container_width=True):
            generate_category_and_tags()
    
    # Display existing summary
    if 'youtube_summary' in st.session_state:
        st.markdown("### 📄 AI Summary")
        st.markdown(st.session_state['youtube_summary'])
    
    # Display category and tags
    if 'youtube_category_tags' in st.session_state:
        category_tags = st.session_state['youtube_category_tags']
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**📂 Suggested Category:**")
            st.info(category_tags.get('category', 'Unknown'))
        
        with col2:
            st.markdown("**🏷️ Suggested Tags:**")
            tags = category_tags.get('tags', [])
            if tags:
                st.info(", ".join(tags))
            else:
                st.info("No tags suggested")


def generate_video_summary():
    """Generate AI summary of the video transcript"""
    if 'youtube_transcript_text_only' not in st.session_state:
        st.error("No transcript available to summarize")
        return
    
    with st.spinner("Generating AI summary..."):
        try:
            summary = summarize_youtube_transcript(
                st.session_state['youtube_transcript_text_only'],
                st.session_state.get('youtube_video_title', 'Unknown Video')
            )
            
            if summary:
                st.session_state['youtube_summary'] = summary
                st.success("✅ Summary generated!")
                st.rerun()
            else:
                st.error("Failed to generate summary")
        except Exception as e:
            st.error(f"Error generating summary: {str(e)}")


def generate_category_and_tags():
    """Generate category and tags recommendations"""
    if 'youtube_transcript_text_only' not in st.session_state:
        st.error("No transcript available for analysis")
        return
    
    with st.spinner("Analyzing content for category and tags..."):
        try:
            category_tags = recommend_category_and_tags(
                st.session_state['youtube_transcript_text_only'],
                st.session_state.get('youtube_video_title', 'Unknown Video')
            )
            
            if category_tags:
                st.session_state['youtube_category_tags'] = category_tags
                st.success("✅ Category and tags generated!")
                st.rerun()
            else:
                st.error("Failed to generate category and tags")
        except Exception as e:
            st.error(f"Error generating category and tags: {str(e)}")


def save_video_to_knowledgebase(category):
    """Save the video transcript and metadata to the knowledgebase"""
    if 'youtube_transcript' not in st.session_state:
        st.error("No transcript to save")
        return
    
    try:
        # Check for duplicates first
        video_id = st.session_state.get('youtube_video_id')
        existing_video = find_existing_video(video_id)
        
        if existing_video:
            handle_duplicate_video(existing_video, category)
            return
        
        # Create video data structure
        video_data = create_video_data_structure(category)
        
        # Save to knowledgebase
        knowledgebase_path = Path("knowledgebase")
        knowledgebase_path.mkdir(exist_ok=True)
        
        # Create filename
        safe_title = "".join(c for c in st.session_state.get('youtube_video_title', 'Unknown') if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_title = safe_title[:50]  # Limit length
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{safe_title}.json"
        
        file_path = knowledgebase_path / filename
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(video_data, f, indent=2, ensure_ascii=False)
        
        st.success(f"✅ Video saved to knowledgebase: {filename}")
        
        # Clear session state for transcript
        cleanup_session_state()
        
    except Exception as e:
        st.error(f"Error saving video: {str(e)}")


def handle_duplicate_video(existing_video, category):
    """Handle duplicate video detection"""
    choice = get_duplicate_handling_choice(existing_video)
    
    if choice == "update":
        # Update existing video with new category/metadata
        updated_data = create_video_data_structure(category)
        success = update_existing_video_metadata(existing_video['file_path'], updated_data)
        
        if success:
            st.success("✅ Existing video updated with new information!")
        else:
            st.error("❌ Failed to update existing video")
    
    elif choice == "skip":
        st.info("⏭️ Skipped saving - video already exists")
    
    # For "save_new", continue with normal save process


def create_video_data_structure(category):
    """Create the video data structure for saving"""
    return {
        "title": st.session_state.get('youtube_video_title', 'Unknown'),
        "author": st.session_state.get('youtube_video_author', 'Unknown'),
        "video_id": st.session_state.get('youtube_video_id'),
        "url": st.session_state.get('youtube_url'),
        "thumbnail_url": st.session_state.get('youtube_thumbnail_url'),
        "category": category,
        "content": {
            "body": st.session_state.get('youtube_transcript_text_only', ''),
            "transcript_with_timestamps": st.session_state.get('youtube_transcript', '')
        },
        "created_at": datetime.now().isoformat(),
        "source": "youtube",
        "summary": st.session_state.get('youtube_summary', ''),
        "tags": st.session_state.get('youtube_category_tags', {}).get('tags', []),
        "suggested_category": st.session_state.get('youtube_category_tags', {}).get('category', ''),
        "type": "video_transcript"
    }


def cleanup_session_state():
    """Clean up YouTube-related session state after saving"""
    keys_to_remove = [
        'youtube_transcript', 'youtube_transcript_text_only', 'youtube_summary',
        'youtube_category_tags', 'youtube_video_id', 'youtube_video_title',
        'youtube_video_author', 'youtube_thumbnail_url', 'youtube_url',
        'current_video_info'
    ]
    
    for key in keys_to_remove:
        if key in st.session_state:
            del st.session_state[key]