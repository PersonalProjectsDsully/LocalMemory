import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import re
from pathlib import Path
from datetime import datetime, timedelta
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.llm_utils import summarize_youtube_transcript, recommend_category_and_tags, test_llm_connection, get_available_ollama_models, get_available_openai_models, get_available_lmstudio_models, OPENAI_AVAILABLE, extract_content_intelligence
from utils.session_state_manager import initialize_session_state, auto_save_settings
from utils.youtube_utils import extract_video_id, fetch_video_info
from utils.youtube_channel_utils import extract_channel_id, fetch_channel_videos_basic, fetch_channel_videos_with_api, fetch_channel_videos_selenium
from utils.duplicate_detection import find_existing_video, get_duplicate_handling_choice, update_existing_video_metadata, find_duplicate_videos, show_bulk_duplicate_options, show_duplicate_summary

# Page configuration
st.set_page_config(
    page_title="YouTube - Local Knowledgebase",
    page_icon="📺",
    layout="wide"
)

# Initialize session state from saved settings
initialize_session_state()

def _parse_youtube_date(published_str: str, reference_time: datetime) -> datetime:
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
    import re
    
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

# Initialize loading state
if 'is_loading_transcript' not in st.session_state:
    st.session_state.is_loading_transcript = False

# Custom CSS
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

st.title("📺 YouTube Content Manager")
st.write("Extract transcripts from videos and explore entire YouTube channels")

# Create main tabs
tab1, tab2 = st.tabs(["🎥 Single Video", "📡 Channel Explorer"])

with tab1:
    # YouTube URL input with a unique key based on current URL
    youtube_url = st.text_input(
        "Enter YouTube URL:", 
        placeholder="https://youtube.com/watch?v=... or https://youtu.be/...",
        help="Paste any YouTube video URL here",
        key="youtube_url_input"
    )
    
    if youtube_url:
        video_id = extract_video_id(youtube_url)
        
        if video_id:
            # Fetch video info using cached function
            with st.spinner("Loading video information..."):
                video_info = fetch_video_info(video_id)
            
            # Store in session state for other functions
            st.session_state['youtube_video_id'] = video_id
            st.session_state['youtube_video_title'] = video_info['title']
            st.session_state['youtube_video_author'] = video_info['author']
            st.session_state['youtube_thumbnail_url'] = video_info['thumbnail_url']
            st.session_state['youtube_url'] = youtube_url
            
            # Display video info
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(video_info['thumbnail_url'], use_container_width=True)
            
            with col2:
                st.markdown('<div class="video-info">', unsafe_allow_html=True)
                if video_info['title'] != "YouTube Video":
                    st.subheader(video_info['title'])
                st.caption(f"Channel: {video_info['author']}")
                st.caption(f"Video ID: {video_id}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Show buttons based on transcript state
                col_btn1, col_btn2, col_btn3 = st.columns(3)
                
                with col_btn1:
                    # Only show Get Transcript if we don't have it yet
                    if 'youtube_transcript' not in st.session_state or st.session_state.get('youtube_video_id') != video_id:
                        if st.button("Get Transcript", type="primary", use_container_width=True):
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
                                
                            else:
                                # All attempts failed
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
                    else:
                        # Transcript already loaded
                        st.success("✓ Transcript loaded")
                
                with col_btn2:
                    if st.button("Check Languages", use_container_width=True):
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
                
                with col_btn3:
                    if st.button("Test LLM", use_container_width=True):
                        with st.spinner("Testing LLM connection..."):
                            success, message = test_llm_connection()
                            if success:
                                st.success(message)
                            else:
                                st.error(message)
        else:
            st.error("Invalid YouTube URL. Please enter a valid YouTube video URL.")
    
    # Display transcript if available
    if 'youtube_transcript' in st.session_state and 'youtube_video_id' in st.session_state:
        st.divider()
        
        # Create tabs for transcript and summary
        tab1_1, tab1_2 = st.tabs(["📝 Transcript", "🤖 AI Summary"])
        
        with tab1_1:
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
            
            st.text_area(
                "Transcript:", 
                transcript_to_show, 
                height=400,
                help="You can copy this transcript or download it using the button below"
            )
            
            # Action buttons
            col1, col2, col3 = st.columns([1, 1, 2])
        
            with col1:
                video_id = st.session_state.get('youtube_video_id', 'unknown')
                st.download_button(
                    label="📥 Download as .txt",
                    data=transcript_to_show,
                    file_name=f"transcript_{video_id}.txt",
                    mime="text/plain"
                )
            
            with col2:
                video_title = st.session_state.get('youtube_video_title', 'YouTube Video')
                video_id = st.session_state.get('youtube_video_id', 'unknown')
                video_author = st.session_state.get('youtube_video_author', 'Unknown Channel')
                thumbnail_url = st.session_state.get('youtube_thumbnail_url', '')
                
                markdown_content = f"""---
type: youtube
title: {video_title}
author: {video_author}
video_id: {video_id}
thumbnail_url: {thumbnail_url}
date_added: {datetime.now().strftime('%Y-%m-%d')}
---

# {video_title}

**Author**: {video_author}
**YouTube Video ID**: {video_id}

## Transcript

{transcript_to_show}"""
                
                st.download_button(
                    label="📥 Download as .md",
                    data=markdown_content,
                    file_name=f"transcript_{video_id}.md",
                    mime="text/markdown"
                )
            
            with col3:
                if save_category != "Select category..." and st.button("💾 Save to Knowledgebase", type="primary"):
                    try:
                        # Create knowledgebase directory structure
                        kb_path = Path("knowledgebase")
                        category_path = kb_path / save_category.replace("/", "_").replace(" ", "_")
                        
                        # Create directories if they don't exist
                        category_path.mkdir(parents=True, exist_ok=True)
                        
                        # Generate filename from video title or ID
                        video_id = st.session_state.get('youtube_video_id', 'unknown')
                        video_title = st.session_state.get('youtube_video_title', f'video_{video_id}')
                        video_author = st.session_state.get('youtube_video_author', 'Unknown Channel')
                        thumbnail_url = st.session_state.get('youtube_thumbnail_url', '')
                        
                        # Clean filename - replace spaces with underscores
                        safe_title = re.sub(r'[^\w\s-]', '', video_title)[:50]
                        safe_title = re.sub(r'\s+', '_', safe_title)
                        safe_title = re.sub(r'_+', '_', safe_title).strip('_')
                        
                        # Check for existing files and add number if needed
                        base_filename = f"{safe_title}"
                        filename = f"{base_filename}.md"
                        filepath = category_path / filename
                        
                        counter = 1
                        while filepath.exists():
                            filename = f"{base_filename}_{counter}.md"
                            filepath = category_path / filename
                            counter += 1
                        
                        # Prepare content with YAML frontmatter
                        content = f"""---
type: youtube
title: {video_title}
author: {video_author}
video_id: {video_id}
thumbnail_url: {thumbnail_url}
date_added: {datetime.now().strftime('%Y-%m-%d')}
category: {save_category}
---

# {video_title}

**Author**: {video_author}
**YouTube Video ID**: {video_id}

## Transcript

{transcript_to_show}"""
                        
                        # Save file
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        st.success(f"✅ Transcript saved to {save_category} category!")
                        st.info(f"File saved as: {filepath}")
                        
                    except Exception as e:
                        st.error(f"Error saving transcript: {str(e)}")
        
        with tab1_2:
            # AI Summary tab
            if 'youtube_summary' in st.session_state and 'youtube_recommendation' in st.session_state:
                # Show category and tags recommendation
                recommendation = st.session_state.get('youtube_recommendation', {})
                
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.info(f"""📚 **Recommended Category:**  
{recommendation.get('category', 'Programming')}

🏷️ **Suggested Tags:**  
{', '.join(recommendation.get('tags', []))}""")
                
                with col2:
                    if recommendation.get('category_reasoning'):
                        st.caption(f"💡 **Why this category:** {recommendation.get('category_reasoning')}")
                
                st.divider()
                
                # Display the summary
                st.markdown("### 📝 Summary")
                st.markdown(st.session_state['youtube_summary'])
                
                st.divider()
                
                # Action buttons
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    summary_with_metadata = f"""# {st.session_state.get('youtube_video_title', 'YouTube Video')} - AI Summary

**Channel**: {st.session_state.get('youtube_video_author', 'Unknown')}
**Video ID**: {st.session_state.get('youtube_video_id', 'unknown')}
**Category**: {recommendation.get('category', 'Programming')}
**Tags**: {', '.join(recommendation.get('tags', []))}
**Date**: {datetime.now().strftime('%Y-%m-%d')}

---

{st.session_state['youtube_summary']}"""
                    
                    st.download_button(
                        label="📥 Download Summary",
                        data=summary_with_metadata,
                        file_name=f"summary_{st.session_state.get('youtube_video_id', 'unknown')}.md",
                        mime="text/markdown"
                    )
                
                with col2:
                    if st.button("🔄 Regenerate", use_container_width=True, key="regenerate_single"):
                        with st.spinner("Regenerating summary and recommendations..."):
                            # Regenerate both recommendation and summary
                            recommendation = recommend_category_and_tags(
                                st.session_state.get('youtube_transcript_text_only', ''),
                                st.session_state.get('youtube_video_title', 'YouTube Video'),
                                st.session_state.get('youtube_video_author', 'Unknown Channel')
                            )
                            st.session_state['youtube_recommendation'] = recommendation
                            
                            summary = summarize_youtube_transcript(
                                st.session_state.get('youtube_transcript_text_only', ''),
                                st.session_state.get('youtube_video_title', 'YouTube Video'),
                                st.session_state.get('youtube_video_author', 'Unknown Channel')
                            )
                            if summary:
                                st.session_state['youtube_summary'] = summary
                                st.rerun()
                            else:
                                st.error("Failed to generate summary. Please check LLM settings.")
                
                with col3:
                    # Quick save button with duplicate detection
                    if st.button("🚀 Quick Save to KB", type="primary", use_container_width=True, key="quick_save_single"):
                        try:
                            video_id = st.session_state.get('youtube_video_id', 'unknown')
                            video_title = st.session_state.get('youtube_video_title', f'video_{video_id}')
                            video_author = st.session_state.get('youtube_video_author', 'Unknown Channel')
                            thumbnail_url = st.session_state.get('youtube_thumbnail_url', '')
                            
                            # Check for existing video first
                            existing_video = find_existing_video(video_id)
                            
                            if existing_video:
                                # Show duplicate handling options
                                st.warning(f"🔄 **Video Already Exists**: '{video_title[:50]}...'")
                                st.info(f"📁 Found at: `{existing_video['relative_path']}`")
                                
                                choice = st.radio(
                                    "How would you like to handle this duplicate?",
                                    [
                                        "⏭️ Cancel (keep existing version)",
                                        "🔄 Replace completely (new analysis)", 
                                        "📝 Update metadata only (keep transcript, refresh AI analysis)"
                                    ],
                                    key="single_duplicate_choice"
                                )
                                
                                if choice.startswith("⏭️"):
                                    st.info("✅ Keeping existing version. No changes made.")
                                    st.stop()
                                elif choice.startswith("📝"):
                                    # Update metadata only
                                    with st.spinner("🔄 Updating metadata with new AI analysis..."):
                                        # Get fresh AI analysis
                                        intelligence = extract_content_intelligence(
                                            st.session_state.get('youtube_transcript_text_only', ''),
                                            video_title,
                                            video_author,
                                            "youtube"
                                        )
                                        
                                        # Generate new summary
                                        new_summary = st.session_state.get('youtube_summary', '')
                                        
                                        # Update existing file
                                        updated_content = update_existing_video_metadata(
                                            existing_video, 
                                            intelligence, 
                                            new_summary
                                        )
                                        
                                        # Write updated content
                                        with open(existing_video['file_path'], 'w', encoding='utf-8') as f:
                                            f.write(updated_content)
                                        
                                        st.success(f"✅ Updated metadata for existing video!")
                                        st.info(f"📄 File: {existing_video['relative_path']}")
                                        st.stop()
                                # If "Replace completely" is selected, continue with normal processing
                            
                            # Create knowledgebase directory structure
                            kb_path = Path("knowledgebase")
                            category = recommendation.get('category', 'Programming')
                            category_path = kb_path / category.replace("/", "_").replace(" ", "_")
                            
                            # Create directories if they don't exist
                            category_path.mkdir(parents=True, exist_ok=True)
                            
                            # Clean filename
                            safe_title = re.sub(r'[^\w\s-]', '', video_title)[:50]
                            safe_title = re.sub(r'\s+', '_', safe_title)
                            safe_title = re.sub(r'_+', '_', safe_title).strip('_')
                            
                            # For replacements, use existing file path if available
                            if existing_video and choice.startswith("🔄"):
                                filepath = Path(existing_video['file_path'])
                            else:
                                # Check for existing files and create new filename if needed
                                base_filename = f"{safe_title}"
                                filename = f"{base_filename}.md"
                                filepath = category_path / filename
                                
                                counter = 1
                                while filepath.exists():
                                    filename = f"{base_filename}_{counter}.md"
                                    filepath = category_path / filename
                                    counter += 1
                            
                            # Get intelligent content analysis for single video
                            intelligence = extract_content_intelligence(
                                st.session_state.get('youtube_transcript_text_only', ''),
                                video_title,
                                video_author,
                                "youtube"
                            )
                            
                            # Use intelligent analysis category if available, fallback to recommendation
                            final_category = intelligence.get('category', recommendation.get('category', category))
                            final_tags = intelligence.get('tags', recommendation.get('tags', []))
                            
                            # Prepare content with enhanced YAML frontmatter
                            content = f"""---
type: youtube
title: {video_title}
author: {video_author}
video_id: {video_id}
video_url: https://www.youtube.com/watch?v={video_id}
thumbnail_url: {thumbnail_url}
date_added: {datetime.now().strftime('%Y-%m-%d')}
category: {final_category}
tags: {final_tags}
entities: {intelligence.get('entities', [])}
concepts: {intelligence.get('concepts', [])}
content_structure: {intelligence.get('content_structure', 'unknown')}
difficulty_level: {intelligence.get('difficulty_level', 'unknown')}
prerequisites: {intelligence.get('prerequisites', [])}
related_topics: {intelligence.get('related_topics', [])}
authority_signals: {intelligence.get('authority_signals', [])}
confidence_score: {intelligence.get('confidence_score', 0.5)}
---

# {video_title}

**Channel**: {video_author}  
**Video**: [Watch on YouTube](https://www.youtube.com/watch?v={video_id})  
**Category**: {category}  
**Tags**: {', '.join(recommendation.get('tags', []))}  

## Summary

{st.session_state['youtube_summary']}

## Full Transcript

{st.session_state.get('youtube_transcript', '')}"""
                            
                            # Save file
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(content)
                            
                            st.success(f"✅ Saved to {category} category!")
                            st.info(f"File: {filepath}")
                            
                        except Exception as e:
                            st.error(f"Error saving: {str(e)}")
            else:
                # Generate summary button
                if st.button("🤖 Generate AI Summary & Tags", type="primary", use_container_width=True):
                    with st.spinner("Analyzing video content..."):
                        # First, get category and tag recommendations
                        recommendation = recommend_category_and_tags(
                            st.session_state.get('youtube_transcript_text_only', ''),
                            st.session_state.get('youtube_video_title', 'YouTube Video'),
                            st.session_state.get('youtube_video_author', 'Unknown Channel')
                        )
                        st.session_state['youtube_recommendation'] = recommendation
                        
                    with st.spinner("Generating detailed summary..."):
                        # Then generate the summary
                        summary = summarize_youtube_transcript(
                            st.session_state.get('youtube_transcript_text_only', ''),
                            st.session_state.get('youtube_video_title', 'YouTube Video'),
                            st.session_state.get('youtube_video_author', 'Unknown Channel')
                        )
                        if summary:
                            st.session_state['youtube_summary'] = summary
                            st.success("Summary and recommendations generated successfully!")
                            st.rerun()
                        else:
                            st.error("Failed to generate summary. Please check LLM settings in the sidebar.")
                
                st.info("💡 Click the button above to generate an AI summary with category recommendation and tags.")

with tab2:
    st.subheader("📺 YouTube Channel Explorer")
    st.write("Enter a YouTube channel URL to fetch and process multiple videos at once.")
    
    # Channel URL input
    channel_url = st.text_input(
        "Enter YouTube Channel URL:",
        placeholder="https://www.youtube.com/@channelname or https://www.youtube.com/channel/...",
        help="Paste any YouTube channel URL here"
    )
    
    if channel_url:
        # Extract channel ID
        channel_id = extract_channel_id(channel_url)
        
        if channel_id:
            # Method selection
            st.subheader("🔧 Fetching Method")
            
            method = st.radio(
                "Choose video fetching method:",
                [
                    "📡 RSS Feed (Free, ~15 videos)",
                    "🚀 YouTube Data API (API key required, up to 50)",
                    "🔍 Selenium Scraping (All videos, requires setup)"
                ],
                help="Different methods have different capabilities and requirements"
            )
            
            # Video count selection based on method
            if "RSS Feed" in method:
                max_videos = st.slider("Videos to fetch:", 5, 15, 15, help="RSS is limited to ~15 recent videos")
                st.info("📡 **RSS Feed**: Free, no setup required, limited to recent videos")
            elif "YouTube Data API" in method:
                max_videos = st.slider("Videos to fetch:", 5, 50, 25, help="API can fetch up to 50 videos per request")
                api_key = st.session_state.get('youtube_api_key', '')
                if api_key:
                    st.success("🚀 **YouTube Data API**: Ready to fetch up to 50 videos")
                else:
                    st.error("❌ **YouTube Data API**: API key required (add in sidebar)")
            else:  # Selenium
                max_videos = st.slider("Videos to fetch:", 10, 500, 100, help="Selenium can fetch ALL videos from a channel")
                st.warning("🔍 **Selenium**: Can fetch ALL videos but requires Chrome/ChromeDriver installation")
                
                # Check if selenium is available
                try:
                    import selenium
                    st.success("✅ Selenium is available")
                except ImportError:
                    st.error("❌ Selenium not installed. Run: `pip install selenium beautifulsoup4`")
                    st.error("❌ Also need ChromeDriver: https://chromedriver.chromium.org/")
            
            # Fetch videos button
            if st.button("🔍 Fetch Channel Videos", type="primary", use_container_width=True):
                with st.spinner("Fetching channel videos..."):
                    # Clean up old video selection states first
                    keys_to_remove = [key for key in st.session_state.keys() if key.startswith('select_')]
                    for key in keys_to_remove:
                        del st.session_state[key]
                    
                    videos = []
                    
                    # Use selected method
                    if "RSS Feed" in method:
                        st.info("📡 Using RSS feed method...")
                        videos = fetch_channel_videos_basic(channel_id, max_videos)
                        method_name = "RSS Feed"
                        
                    elif "YouTube Data API" in method:
                        api_key = st.session_state.get('youtube_api_key', '')
                        if api_key:
                            st.info("🚀 Using YouTube Data API...")
                            videos = fetch_channel_videos_with_api(channel_id, api_key, max_videos)
                            method_name = "YouTube Data API"
                        else:
                            st.error("❌ No API key provided! Falling back to RSS feed...")
                            videos = fetch_channel_videos_basic(channel_id, max_videos)
                            method_name = "RSS Feed (fallback)"
                            
                    else:  # Selenium
                        try:
                            import selenium
                            st.info("🔍 Using Selenium web scraping...")
                            videos = fetch_channel_videos_selenium(channel_id, max_videos)
                            method_name = "Selenium Scraping"
                        except ImportError:
                            st.error("❌ Selenium not available! Falling back to RSS feed...")
                            videos = fetch_channel_videos_basic(channel_id, max_videos)
                            method_name = "RSS Feed (fallback)"
                    
                    if videos:
                        st.session_state['channel_videos'] = videos
                        
                        # Show success message with method used
                        st.success(f"✅ Found {len(videos)} videos using {method_name}!")
                        
                        # Show method-specific tips
                        if method_name == "RSS Feed" and len(videos) >= 15:
                            st.info("💡 **Tip**: Try Selenium scraping to get ALL videos from this channel!")
                        elif method_name == "Selenium Scraping":
                            st.success(f"🎉 Successfully scraped {len(videos)} videos! This includes the complete channel history.")
                        
                    else:
                        st.error("Could not fetch videos from this channel. Please check the URL.")
        else:
            st.error("Invalid channel URL. Please enter a valid YouTube channel URL.")
    
    # Display videos if available
    if 'channel_videos' in st.session_state and st.session_state['channel_videos']:
        st.divider()
        st.subheader("📋 Available Videos")
        
        # Add filtering and search controls
        st.write("**Filter and Search Options:**")
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            # Time filter
            time_filter = st.selectbox(
                "Time Period:",
                ["All time", "Last week", "Last month", "Last year"],
                help="Filter videos by publish date"
            )
        
        with col2:
            # Sort options
            sort_option = st.selectbox(
                "Sort by:",
                ["Newest first", "Oldest first", "Alphabetical A-Z", "Alphabetical Z-A"],
                help="Change video order"
            )
        
        with col3:
            # Search box
            search_query = st.text_input(
                "Search videos:",
                placeholder="Search by title keywords...",
                help="Filter videos by title content"
            )
        
        # Apply filters
        filtered_videos = st.session_state['channel_videos'].copy()
        
        # Time filtering
        if time_filter != "All time":
            now = datetime.now()
            if time_filter == "Last week":
                cutoff_date = now - timedelta(weeks=1)
            elif time_filter == "Last month":
                cutoff_date = now - timedelta(days=30)
            elif time_filter == "Last year":
                cutoff_date = now - timedelta(days=365)
            
            # Filter videos (note: published dates from different sources have different formats)
            time_filtered = []
            for video in filtered_videos:
                published = video.get('published', '').strip()
                try:
                    video_date = _parse_youtube_date(published, now)
                    if video_date >= cutoff_date:
                        time_filtered.append(video)
                except:
                    # Include video if date parsing fails
                    time_filtered.append(video)
            
            filtered_videos = time_filtered
        
        # Search filtering
        if search_query:
            search_query_lower = search_query.lower()
            filtered_videos = [
                video for video in filtered_videos 
                if search_query_lower in video.get('title', '').lower()
            ]
        
        # Sorting
        if sort_option == "Newest first":
            # Sort by parsed date, newest first
            try:
                filtered_videos.sort(key=lambda x: _parse_youtube_date(x.get('published', ''), datetime.now()), reverse=True)
            except:
                # Fallback to string sorting
                filtered_videos.sort(key=lambda x: x.get('published', ''), reverse=True)
        elif sort_option == "Oldest first":
            try:
                filtered_videos.sort(key=lambda x: _parse_youtube_date(x.get('published', ''), datetime.now()), reverse=False)
            except:
                # Fallback to string sorting
                filtered_videos.sort(key=lambda x: x.get('published', ''), reverse=False)
        elif sort_option == "Alphabetical A-Z":
            filtered_videos.sort(key=lambda x: x.get('title', '').lower())
        elif sort_option == "Alphabetical Z-A":
            filtered_videos.sort(key=lambda x: x.get('title', '').lower(), reverse=True)
        
        # Show filter results
        total_videos = len(st.session_state['channel_videos'])
        filtered_count = len(filtered_videos)
        
        if filtered_count != total_videos:
            st.info(f"📊 Showing {filtered_count} of {total_videos} videos")
        else:
            st.info(f"📊 Showing all {total_videos} videos")
        
        # Debug information for date parsing (can be removed later)
        if st.checkbox("🔍 Show Date Debug Info", key="debug_dates"):
            st.write("**Date Parsing Debug:**")
            for i, video in enumerate(filtered_videos[:5]):  # Show first 5
                published = video.get('published', '')
                try:
                    parsed_date = _parse_youtube_date(published, datetime.now())
                    st.caption(f"'{published}' → {parsed_date.strftime('%Y-%m-%d %H:%M')}")
                except Exception as e:
                    st.caption(f"'{published}' → Error: {e}")
                if i >= 4:  # Limit to 5 examples
                    break
        
        # Select all/none buttons
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            if st.button("✅ Select All Visible", use_container_width=True):
                for video in filtered_videos:
                    checkbox_key = f"select_{video['video_id']}"
                    st.session_state[checkbox_key] = True
                st.rerun()
        
        with col2:
            if st.button("❌ Clear Selection", use_container_width=True):
                for video in st.session_state['channel_videos']:
                    checkbox_key = f"select_{video['video_id']}"
                    st.session_state[checkbox_key] = False
                st.rerun()
        
        # Display filtered videos with checkboxes
        for idx, video in enumerate(filtered_videos):
            col1, col2, col3 = st.columns([0.1, 0.25, 0.65])
            
            with col1:
                # Initialize checkbox state if not exists
                checkbox_key = f"select_{video['video_id']}"
                if checkbox_key not in st.session_state:
                    st.session_state[checkbox_key] = False
                
                # Checkbox for selection (no default value since we pre-initialize)
                selected = st.checkbox(
                    "",
                    key=checkbox_key
                )
            
            with col2:
                # Thumbnail
                if video.get('thumbnail'):
                    try:
                        st.image(video['thumbnail'], use_container_width=True)
                    except:
                        st.write("🎥")  # Fallback emoji if thumbnail fails
                else:
                    st.write("🎥")
            
            with col3:
                # Video info
                st.markdown(f"**{video['title']}**")
                st.caption(f"Published: {video['published']} | Video ID: {video['video_id']}")
        
        # Process selected videos
        st.divider()
        selected_count = sum(1 for video in st.session_state['channel_videos'] 
                           if st.session_state.get(f"select_{video['video_id']}", False))
        
        # Show selection info
        selected_visible = sum(1 for video in filtered_videos 
                             if st.session_state.get(f"select_{video['video_id']}", False))
        
        if filtered_count != total_videos:
            st.caption(f"Selection: {selected_visible} of {filtered_count} visible videos, {selected_count} total selected")
        else:
            st.caption(f"Selection: {selected_count} of {total_videos} videos selected")
        
        if selected_count > 0:
            st.info(f"📊 {selected_count} videos selected for processing")
            
            # Category selection for bulk save
            categories = ["Programming", "AI/ML", "DevOps", "Web Development", "Database", "Security"]
            bulk_category = st.selectbox(
                "Default category for bulk save:",
                categories,
                help="Videos will be saved to their AI-recommended categories, but this will be used as fallback"
            )
            
            # Check for duplicates first (before processing)
            if st.button(f"🔍 Check for Duplicates & Process {selected_count} Videos", type="primary", use_container_width=True):
                # Get list of selected videos
                selected_videos = [
                    video for video in st.session_state['channel_videos'] 
                    if st.session_state.get(f"select_{video['video_id']}", False)
                ]
                
                # Check for duplicates
                new_videos, duplicate_videos = find_duplicate_videos(selected_videos)
                
                # Store in session state for next step
                st.session_state['processing_new_videos'] = new_videos
                st.session_state['processing_duplicate_videos'] = duplicate_videos
                st.session_state['processing_ready'] = True
                st.rerun()
            
            # Show duplicate handling options if we found duplicates
            if st.session_state.get('processing_ready', False):
                duplicate_videos = st.session_state.get('processing_duplicate_videos', [])
                new_videos = st.session_state.get('processing_new_videos', [])
                
                if duplicate_videos:
                    st.divider()
                    st.warning(f"🔄 Found {len(duplicate_videos)} duplicate videos")
                    
                    duplicate_actions = show_bulk_duplicate_options(duplicate_videos)
                    show_duplicate_summary(duplicate_videos, duplicate_actions)
                    
                    # Show processing button
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        if st.button("🚀 Start Processing", type="primary", use_container_width=True):
                            st.session_state['duplicate_actions'] = duplicate_actions
                            st.session_state['start_processing'] = True
                            st.rerun()
                    
                    with col2:
                        if st.button("↩️ Cancel", use_container_width=True):
                            # Clear processing state
                            for key in ['processing_ready', 'processing_new_videos', 'processing_duplicate_videos']:
                                if key in st.session_state:
                                    del st.session_state[key]
                            st.rerun()
                else:
                    # No duplicates found
                    st.success("✅ No duplicates found!")
                    if st.button("🚀 Start Processing All Videos", type="primary", use_container_width=True):
                        st.session_state['duplicate_actions'] = {}
                        st.session_state['start_processing'] = True
                        st.rerun()
            
            # Actual processing starts here
            if st.session_state.get('start_processing', False):
                # Clear the flags
                st.session_state['start_processing'] = False
                st.session_state['processing_ready'] = False
                
                # Get stored data
                new_videos = st.session_state.get('processing_new_videos', [])
                duplicate_videos = st.session_state.get('processing_duplicate_videos', [])
                duplicate_actions = st.session_state.get('duplicate_actions', {})
                
                # Create progress bar
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Process videos (new + duplicates based on user choice)
                videos_to_process = new_videos.copy()
                
                # Add duplicates based on user choices
                for video in duplicate_videos:
                    action = duplicate_actions.get(video['video_id'], 'skip')
                    if action != 'skip':
                        video['duplicate_action'] = action
                        videos_to_process.append(video)
                
                # Process each video
                processed = 0
                failed = 0
                skipped = 0
                updated = 0
                
                for idx, video in enumerate(videos_to_process):
                    # Check if this is a duplicate with special handling
                    duplicate_action = video.get('duplicate_action', None)
                    
                    if duplicate_action == 'update_metadata':
                        # Handle metadata update only
                        status_text.text(f"Updating metadata: {video['title'][:50]}...")
                        try:
                            # Get existing file info
                            existing_file = video.get('existing_file')
                            if existing_file:
                                # Get fresh AI analysis (no transcript needed)
                                intelligence = extract_content_intelligence(
                                    existing_file['body'],  # Use existing transcript
                                    video['title'],
                                    "Channel Video",
                                    "youtube"
                                )
                                
                                # No new summary for metadata-only updates
                                updated_content = update_existing_video_metadata(
                                    existing_file, 
                                    intelligence, 
                                    ""  # Empty summary to preserve existing
                                )
                                
                                # Write updated content
                                with open(existing_file['file_path'], 'w', encoding='utf-8') as f:
                                    f.write(updated_content)
                                
                                updated += 1
                                status_text.text(f"Updated metadata: {video['title'][:50]}... (✅ Complete!)")
                            else:
                                failed += 1
                        except Exception as e:
                            failed += 1
                            st.warning(f"⚠️ Failed to update '{video['title'][:40]}...': {str(e)[:50]}...")
                        
                        # Update progress
                        progress = (processed + failed + updated + skipped) / len(videos_to_process)
                        progress_bar.progress(progress)
                        continue
                    
                    # Regular processing (new videos or full reprocessing)
                    status_text.text(f"Processing: {video['title'][:50]}...")
                    
                    try:
                        # Try to fetch transcript with retry logic and better error handling
                        transcript = None
                        transcript_error = None
                        max_retries = 3
                        retry_delays = [0, 3, 6]  # 0 seconds (immediate), 3 seconds, 6 seconds
                        
                        for attempt in range(max_retries):
                            try:
                                if attempt > 0:
                                    # Update status to show retry attempt
                                    status_text.text(f"Processing: {video['title'][:50]}... (Retry {attempt}/3)")
                                    time.sleep(retry_delays[attempt])
                                
                                transcript = YouTubeTranscriptApi.get_transcript(video['video_id'])
                                break  # Success! Exit retry loop
                                
                            except Exception as transcript_exc:
                                transcript_error = str(transcript_exc)
                                
                                # If this is not the last attempt, continue to retry
                                if attempt < max_retries - 1:
                                    # Check if this is a retryable error
                                    if any(retryable in transcript_error.lower() for retryable in [
                                        'timeout', 'connection', 'network', 'temporary', 'too many requests'
                                    ]):
                                        continue  # Retry for network/rate limit issues
                                    else:
                                        # For non-retryable errors (no captions, private video), break immediately
                                        break
                                
                                # Last attempt failed, try alternative transcript sources
                                if attempt == max_retries - 1:
                                    try:
                                        status_text.text(f"Processing: {video['title'][:50]}... (Trying alternative sources)")
                                        transcript_list = YouTubeTranscriptApi.list_transcripts(video['video_id'])
                                        available_transcripts = list(transcript_list)
                                        if available_transcripts:
                                            # Try the first available transcript
                                            transcript = available_transcripts[0].fetch()
                                            break
                                    except:
                                        pass
                        
                        if transcript:
                            # Reset status to show successful processing
                            status_text.text(f"Processing: {video['title'][:50]}... (✅ Transcript obtained)")
                            
                            # Combine transcript text
                            full_transcript = ""
                            full_transcript_text_only = ""
                            
                            for entry in transcript:
                                timestamp = f"[{int(entry['start']//60):02d}:{int(entry['start']%60):02d}]"
                                full_transcript += f"{timestamp} {entry['text']}\n"
                                full_transcript_text_only += f"{entry['text']} "
                            
                            # Update status for AI processing
                            status_text.text(f"Processing: {video['title'][:50]}... (🤖 AI Analysis)")
                            
                            # Get intelligent content analysis
                            intelligence = extract_content_intelligence(
                                full_transcript_text_only,
                                video['title'],
                                "Channel Video",
                                "youtube"
                            )
                            
                            # Get AI recommendations (fallback to basic categorization)
                            recommendation = recommend_category_and_tags(
                                full_transcript_text_only,
                                video['title'],
                                "Channel Video"
                            )
                            
                            # Generate summary
                            summary = summarize_youtube_transcript(
                                full_transcript_text_only,
                                video['title'],
                                "Channel Video"
                            )
                            
                            if summary:
                                # Update status for saving
                                status_text.text(f"Processing: {video['title'][:50]}... (💾 Saving)")
                                
                                # Save to knowledgebase
                                kb_path = Path("knowledgebase")
                                category = recommendation.get('category', bulk_category)
                                category_path = kb_path / category.replace("/", "_").replace(" ", "_")
                                category_path.mkdir(parents=True, exist_ok=True)
                                
                                # Clean filename
                                safe_title = re.sub(r'[^\w\s-]', '', video['title'])[:50]
                                safe_title = re.sub(r'\s+', '_', safe_title)
                                safe_title = re.sub(r'_+', '_', safe_title).strip('_')
                                
                                # Check for existing files
                                base_filename = f"{safe_title}"
                                filename = f"{base_filename}.md"
                                filepath = category_path / filename
                                
                                counter = 1
                                while filepath.exists():
                                    filename = f"{base_filename}_{counter}.md"
                                    filepath = category_path / filename
                                    counter += 1
                                
                                # Prepare enhanced content with intelligent metadata
                                # Use intelligent analysis category if available, fallback to recommendation
                                final_category = intelligence.get('category', recommendation.get('category', category))
                                final_tags = intelligence.get('tags', recommendation.get('tags', []))
                                
                                content = f"""---
type: youtube
title: {video['title']}
author: Channel Video
video_id: {video['video_id']}
video_url: {video['link']}
thumbnail_url: {video.get('thumbnail', f"https://img.youtube.com/vi/{video['video_id']}/mqdefault.jpg")}
date_added: {datetime.now().strftime('%Y-%m-%d')}
category: {final_category}
tags: {final_tags}
entities: {intelligence.get('entities', [])}
concepts: {intelligence.get('concepts', [])}
content_structure: {intelligence.get('content_structure', 'unknown')}
difficulty_level: {intelligence.get('difficulty_level', 'unknown')}
prerequisites: {intelligence.get('prerequisites', [])}
related_topics: {intelligence.get('related_topics', [])}
authority_signals: {intelligence.get('authority_signals', [])}
confidence_score: {intelligence.get('confidence_score', 0.5)}
---

# {video['title']}

**Video**: [Watch on YouTube]({video['link']})  
**Published**: {video['published']}  
**Category**: {category}  
**Tags**: {', '.join(recommendation.get('tags', []))}  

## Summary

{summary}

## Full Transcript

{full_transcript}"""
                                
                                # Save file
                                with open(filepath, 'w', encoding='utf-8') as f:
                                    f.write(content)
                                
                                processed += 1
                                status_text.text(f"Processing: {video['title'][:50]}... (✅ Complete!)")
                            else:
                                failed += 1
                                st.warning(f"⚠️ '{video['title'][:40]}...': AI summary generation failed")
                        else:
                            # No transcript available - save video info without transcript
                            failed += 1
                            
                            # Determine the reason for failure
                            if "no element found" in transcript_error:
                                reason = "No captions available"
                            elif "Video unavailable" in transcript_error:
                                reason = "Video unavailable/private"
                            elif "Too Many Requests" in transcript_error:
                                reason = "Rate limited - try again later"
                            else:
                                reason = f"Transcript error: {transcript_error[:50]}..."
                            
                            st.warning(f"⚠️ Skipped '{video['title'][:40]}...': {reason}")
                    
                    except Exception as e:
                        failed += 1
                        error_msg = str(e)
                        if "no element found" in error_msg:
                            st.warning(f"⚠️ Skipped '{video['title'][:40]}...': No captions available")
                        elif "Video unavailable" in error_msg:
                            st.warning(f"⚠️ Skipped '{video['title'][:40]}...': Video unavailable/private")
                        elif "Too Many Requests" in error_msg:
                            st.warning(f"⚠️ Skipped '{video['title'][:40]}...': Rate limited")
                        else:
                            st.warning(f"⚠️ Skipped '{video['title'][:40]}...': {error_msg[:50]}...")
                        
                        # Update progress
                        progress = (processed + failed + updated + skipped) / len(videos_to_process)
                        progress_bar.progress(progress)
                
                # Final status
                progress_bar.empty()
                status_text.empty()
                
                # Show detailed results
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    if processed > 0:
                        st.success(f"✅ **New**: {processed} videos")
                with col2:
                    if updated > 0:
                        st.info(f"📝 **Updated**: {updated} videos")
                with col3:
                    if failed > 0:
                        st.warning(f"⚠️ **Failed**: {failed} videos")
                with col4:
                    total_handled = processed + updated + failed
                    success_rate = ((processed + updated) / total_handled * 100) if total_handled > 0 else 0
                    st.metric("Success Rate", f"{success_rate:.1f}%")
                
                # Show summary
                if processed > 0 or updated > 0:
                    total_success = processed + updated
                    st.success(f"🎉 **Successfully handled {total_success} videos!**")
                    if processed > 0:
                        st.info(f"📹 {processed} new videos processed with AI summaries")
                    if updated > 0:
                        st.info(f"📝 {updated} existing videos updated with fresh AI analysis")
                
                if failed > 0:
                    st.info(f"""
                    **Common reasons for skipped videos:**
                    - 🚫 No captions/transcripts available
                    - 🔒 Private or unavailable videos  
                    - 🌍 Region-restricted content
                    - 🔞 Age-restricted videos
                    - ⏰ Rate limiting (try again later)
                    
                    💡 **Tip**: Only videos with captions can be processed for AI summarization.
                    """)
        else:
            st.info("Select videos above to process them with AI summarization.")

# Sidebar - LLM Settings
with st.sidebar:
    st.subheader("⚙️ LLM Settings")
    st.info("💡 Settings are synced with global Settings page")
    
    # LLM Provider selection - sync with global settings
    def on_provider_change():
        provider_map = {
            "Ollama (Local)": "ollama",
            "OpenAI": "openai", 
            "LM Studio (Local)": "lmstudio"
        }
        st.session_state.llm_provider = provider_map.get(st.session_state.llm_provider_youtube, "ollama")
        auto_save_settings()
    
    # Get current provider from global settings
    current_provider = st.session_state.get('llm_provider', 'ollama')
    provider_display_map = {
        "ollama": "Ollama (Local)",
        "openai": "OpenAI",
        "lmstudio": "LM Studio (Local)"
    }
    current_display = provider_display_map.get(current_provider, "Ollama (Local)")
    
    provider_options = ["Ollama (Local)", "OpenAI", "LM Studio (Local)"]
    provider = st.selectbox(
        "LLM Provider",
        provider_options,
        index=provider_options.index(current_display),
        key="llm_provider_youtube",
        on_change=on_provider_change,
        help="Synced with global settings - choose between local Ollama, cloud OpenAI, or local LM Studio"
    )
    
    if provider == "OpenAI":
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
    elif provider == "LM Studio (Local)":
        # LM Studio settings - sync with global settings
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
    
    else:  # Ollama (Local)
        # Ollama settings
        def on_ollama_url_change():
            st.session_state.ollama_api_url = st.session_state.ollama_api_url_youtube
            auto_save_settings()
        
        api_url = st.text_input(
            "Ollama API URL",
            value=st.session_state.get('ollama_api_url', 'http://localhost:11434/api/generate'),
            key="ollama_api_url_youtube",
            on_change=on_ollama_url_change
        )
        
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
    
    st.divider()
    
    # YouTube Data API Settings (for channel explorer)
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
    
    st.divider()
    if st.session_state.get('auto_save_enabled', True):
        st.caption("🔄 Settings auto-save is enabled")
    st.caption("Local Knowledgebase v1.0")
    st.caption("© 2025 Your Organization")