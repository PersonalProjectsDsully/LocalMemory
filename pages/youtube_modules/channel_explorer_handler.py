"""
Channel Explorer Handler Module

Handles YouTube channel exploration, video fetching, and bulk processing.
"""

import streamlit as st
from datetime import datetime, timedelta
from pathlib import Path
import json

from utils.youtube.youtube_channel_utils import (
    extract_channel_id, 
    fetch_channel_videos_basic, 
    fetch_channel_videos_with_api, 
    fetch_channel_videos_selenium
)
from utils.content.duplicate_detection import (
    find_duplicate_videos, 
    show_bulk_duplicate_options, 
    show_duplicate_summary
)
from utils.content.comprehensive_duplicate_detector import DuplicateDetector
from utils.session.classification_logger import classification_logger
from utils.llm.llm_utils import extract_content_intelligence, classify_youtube_video
from .youtube_page_utils import parse_youtube_date


def render_channel_explorer_tab():
    """Render the channel explorer tab interface"""
    st.subheader("📺 YouTube Channel Explorer")
    st.write("Enter a YouTube channel URL to fetch and process multiple videos at once.")
    
    # Channel URL input
    channel_url = st.text_input(
        "Enter YouTube Channel URL:",
        placeholder="https://www.youtube.com/@channelname or https://www.youtube.com/channel/...",
        help="Paste any YouTube channel URL here"
    )
    
    if channel_url:
        channel_id = process_channel_url(channel_url)
        
        if channel_id:
            render_fetching_interface(channel_id)
        else:
            st.error("Invalid channel URL. Please enter a valid YouTube channel URL.")
    
    # Display videos if available
    if 'channel_videos' in st.session_state and st.session_state['channel_videos']:
        display_channel_videos()


def process_channel_url(channel_url):
    """Process the channel URL and extract channel ID"""
    channel_id = extract_channel_id(channel_url)
    return channel_id


def render_fetching_interface(channel_id):
    """Render the video fetching method selection interface"""
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
    
    # Configure method-specific settings
    max_videos, api_key = configure_method_settings(method)
    
    # Fetch videos button
    if st.button("🔍 Fetch Channel Videos", type="primary", use_container_width=True):
        fetch_channel_videos(channel_id, method, max_videos, api_key)


def configure_method_settings(method):
    """Configure settings based on selected fetching method"""
    api_key = None
    
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
    
    return max_videos, api_key


def fetch_channel_videos(channel_id, method, max_videos, api_key):
    """Fetch videos from the channel using the selected method"""
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


def display_channel_videos():
    """Display and manage the fetched channel videos"""
    st.divider()
    st.subheader("📋 Available Videos")
    
    # Filter and search controls
    filtered_videos = render_video_filters()
    
    # Show filter results
    total_videos = len(st.session_state['channel_videos'])
    filtered_count = len(filtered_videos)
    
    if filtered_count != total_videos:
        st.info(f"📊 Showing {filtered_count} of {total_videos} videos")
    
    # Bulk actions
    render_bulk_actions(filtered_videos)
    
    # Video list
    render_video_list(filtered_videos)


def render_video_filters():
    """Render video filtering and search controls"""
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
    filtered_videos = apply_video_filters(
        st.session_state['channel_videos'], 
        time_filter, 
        search_query, 
        sort_option
    )
    
    return filtered_videos


def apply_video_filters(videos, time_filter, search_query, sort_option):
    """Apply filtering and sorting to the video list"""
    filtered_videos = videos.copy()
    
    # Time filtering
    if time_filter != "All time":
        filtered_videos = apply_time_filter(filtered_videos, time_filter)
    
    # Search filtering
    if search_query:
        search_query_lower = search_query.lower()
        filtered_videos = [
            video for video in filtered_videos 
            if search_query_lower in video.get('title', '').lower()
        ]
    
    # Sorting
    filtered_videos = apply_video_sorting(filtered_videos, sort_option)
    
    return filtered_videos


def apply_time_filter(videos, time_filter):
    """Apply time-based filtering to videos"""
    now = datetime.now()
    
    if time_filter == "Last week":
        cutoff_date = now - timedelta(weeks=1)
    elif time_filter == "Last month":
        cutoff_date = now - timedelta(days=30)
    elif time_filter == "Last year":
        cutoff_date = now - timedelta(days=365)
    else:
        return videos
    
    time_filtered = []
    for video in videos:
        published = video.get('published', '').strip()
        try:
            video_date = parse_youtube_date(published, now)
            if video_date >= cutoff_date:
                time_filtered.append(video)
        except:
            # Include video if date parsing fails
            time_filtered.append(video)
    
    return time_filtered


def apply_video_sorting(videos, sort_option):
    """Apply sorting to the video list"""
    if sort_option == "Newest first":
        try:
            videos.sort(key=lambda x: parse_youtube_date(x.get('published', ''), datetime.now()), reverse=True)
        except:
            videos.sort(key=lambda x: x.get('published', ''), reverse=True)
    elif sort_option == "Oldest first":
        try:
            videos.sort(key=lambda x: parse_youtube_date(x.get('published', ''), datetime.now()), reverse=False)
        except:
            videos.sort(key=lambda x: x.get('published', ''), reverse=False)
    elif sort_option == "Alphabetical A-Z":
        videos.sort(key=lambda x: x.get('title', '').lower())
    elif sort_option == "Alphabetical Z-A":
        videos.sort(key=lambda x: x.get('title', '').lower(), reverse=True)
    
    return videos


def render_bulk_actions(filtered_videos):
    """Render bulk action controls"""
    st.divider()
    
    # Bulk selection
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("✅ Select All", use_container_width=True):
            for i, video in enumerate(filtered_videos):
                st.session_state[f'select_{i}'] = True
            st.rerun()
    
    with col2:
        if st.button("❌ Clear All", use_container_width=True):
            for i, video in enumerate(filtered_videos):
                st.session_state[f'select_{i}'] = False
            st.rerun()
    
    with col3:
        # Count selected videos
        selected_count = sum(1 for i, video in enumerate(filtered_videos) 
                           if st.session_state.get(f'select_{i}', False))
        st.metric("Selected", selected_count)
    
    with col4:
        if st.button("🔍 Check Duplicates", use_container_width=True):
            check_for_duplicates(filtered_videos)
    
    # Bulk processing
    if selected_count > 0:
        render_bulk_processing_options(filtered_videos, selected_count)


def render_bulk_processing_options(filtered_videos, selected_count):
    """Render bulk processing options for selected videos"""
    st.markdown("### 🚀 Bulk Processing Options")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Category for saving
        categories = ["Programming", "AI/ML", "DevOps", "Web Development", "Database", "Security"]
        bulk_category = st.selectbox("Category for selected videos:", ["Select category..."] + categories)
    
    with col2:
        # Processing options
        enable_ai_analysis = st.checkbox("🤖 Enable AI Analysis", value=True, 
                                       help="Generate summaries and extract insights")
    
    with col3:
        # Advanced options
        skip_duplicates = st.checkbox("⏭️ Skip Duplicates", value=True,
                                    help="Automatically skip videos that already exist")
    
    # Process button
    if bulk_category != "Select category...":
        if st.button(f"🚀 Process {selected_count} Selected Videos", type="primary", use_container_width=True):
            handle_bulk_processing(filtered_videos, bulk_category, enable_ai_analysis, skip_duplicates)


def check_for_duplicates(filtered_videos):
    """Check for duplicate videos in the selection"""
    with st.spinner("Checking for duplicates..."):
        try:
            # Initialize duplicate detector
            detector = DuplicateDetector()
            
            # Check each video
            duplicate_results = []
            for video in filtered_videos:
                video_id = video.get('video_id', '')
                if video_id:
                    duplicates = find_duplicate_videos(video_id)
                    if duplicates:
                        duplicate_results.append({
                            'video': video,
                            'duplicates': duplicates
                        })
            
            if duplicate_results:
                show_duplicate_summary(duplicate_results)
                show_bulk_duplicate_options(duplicate_results)
            else:
                st.success("✅ No duplicates found!")
                
        except Exception as e:
            st.error(f"Error checking duplicates: {str(e)}")


def handle_bulk_processing(filtered_videos, category, enable_ai_analysis, skip_duplicates):
    """Handle bulk processing of selected videos"""
    selected_videos = [
        video for i, video in enumerate(filtered_videos)
        if st.session_state.get(f'select_{i}', False)
    ]
    
    if not selected_videos:
        st.error("No videos selected for processing")
        return
    
    # Initialize progress tracking
    progress_bar = st.progress(0)
    status_text = st.empty()
    results_container = st.empty()
    
    success_count = 0
    error_count = 0
    skipped_count = 0
    
    results = {
        'processed': [],
        'errors': [],
        'skipped': []
    }
    
    total_videos = len(selected_videos)
    
    for i, video in enumerate(selected_videos):
        progress = (i + 1) / total_videos
        progress_bar.progress(progress)
        status_text.text(f"Processing video {i+1}/{total_videos}: {video.get('title', 'Unknown')[:50]}...")
        
        try:
            result = process_single_video_bulk(video, category, enable_ai_analysis, skip_duplicates)
            
            if result['status'] == 'success':
                success_count += 1
                results['processed'].append(result)
            elif result['status'] == 'skipped':
                skipped_count += 1
                results['skipped'].append(result)
            else:
                error_count += 1
                results['errors'].append(result)
                
        except Exception as e:
            error_count += 1
            results['errors'].append({
                'video': video,
                'error': str(e),
                'status': 'error'
            })
    
    # Complete processing
    progress_bar.progress(1.0)
    status_text.text("✅ Bulk processing complete!")
    
    # Show results summary
    show_bulk_processing_results(results, success_count, error_count, skipped_count)
    
    # Clear selections
    for i in range(len(filtered_videos)):
        if f'select_{i}' in st.session_state:
            del st.session_state[f'select_{i}']


def process_single_video_bulk(video, category, enable_ai_analysis, skip_duplicates):
    """Process a single video in bulk processing"""
    video_id = video.get('video_id', '')
    
    # Check for duplicates if enabled
    if skip_duplicates and video_id:
        from utils.content.duplicate_detection import find_existing_video
        existing = find_existing_video(video_id)
        if existing:
            return {
                'status': 'skipped',
                'video': video,
                'reason': 'Duplicate video already exists'
            }
    
    try:
        # Create video data structure
        video_data = create_bulk_video_data(video, category)
        
        # Add AI analysis if enabled
        if enable_ai_analysis and video.get('description'):
            ai_results = perform_ai_analysis(video)
            video_data.update(ai_results)
        
        # Save video
        file_path = save_bulk_video(video_data)
        
        # Log classification
        classification_logger.log_classification(
            content_title=video.get('title', 'Unknown'),
            suggested_category=category,
            final_category=category,
            content_type='youtube_video',
            auto_classified=True
        )
        
        return {
            'status': 'success',
            'video': video,
            'file_path': file_path
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'video': video,
            'error': str(e)
        }


def create_bulk_video_data(video, category):
    """Create video data structure for bulk processing"""
    return {
        "title": video.get('title', 'Unknown'),
        "author": video.get('channel_title', 'Unknown'),
        "video_id": video.get('video_id', ''),
        "url": video.get('url', ''),
        "thumbnail_url": video.get('thumbnail_url', ''),
        "category": category,
        "content": {
            "body": video.get('description', ''),
            "duration": video.get('duration', ''),
            "published": video.get('published', '')
        },
        "created_at": datetime.now().isoformat(),
        "source": "youtube_channel",
        "type": "video_metadata",
        "view_count": video.get('view_count', ''),
        "published_date": video.get('published', '')
    }


def perform_ai_analysis(video):
    """Perform AI analysis on video content"""
    ai_results = {}
    
    try:
        # Extract content intelligence
        intelligence = extract_content_intelligence(
            video.get('description', ''),
            video.get('title', '')
        )
        
        if intelligence:
            ai_results['ai_analysis'] = intelligence
        
        # Classify video
        classification = classify_youtube_video(
            video.get('title', ''),
            video.get('description', '')
        )
        
        if classification:
            ai_results['classification'] = classification
            
    except Exception as e:
        ai_results['ai_analysis_error'] = str(e)
    
    return ai_results


def save_bulk_video(video_data):
    """Save video data to knowledgebase"""
    knowledgebase_path = Path("knowledgebase")
    knowledgebase_path.mkdir(exist_ok=True)
    
    # Create filename
    safe_title = "".join(c for c in video_data.get('title', 'Unknown') if c.isalnum() or c in (' ', '-', '_')).rstrip()
    safe_title = safe_title[:50]  # Limit length
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_id = video_data.get('video_id', 'unknown')
    filename = f"{timestamp}_{video_id}_{safe_title}.json"
    
    file_path = knowledgebase_path / filename
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(video_data, f, indent=2, ensure_ascii=False)
    
    return str(file_path)


def show_bulk_processing_results(results, success_count, error_count, skipped_count):
    """Show the results of bulk processing"""
    st.markdown("### 📊 Processing Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("✅ Processed", success_count)
    
    with col2:
        st.metric("⏭️ Skipped", skipped_count)
    
    with col3:
        st.metric("❌ Errors", error_count)
    
    # Show detailed results
    if results['errors']:
        with st.expander(f"❌ Errors ({len(results['errors'])})", expanded=False):
            for error in results['errors']:
                st.error(f"**{error['video'].get('title', 'Unknown')}**: {error.get('error', 'Unknown error')}")
    
    if results['skipped']:
        with st.expander(f"⏭️ Skipped ({len(results['skipped'])})", expanded=False):
            for skipped in results['skipped']:
                st.info(f"**{skipped['video'].get('title', 'Unknown')}**: {skipped.get('reason', 'Unknown reason')}")


def render_video_list(filtered_videos):
    """Render the list of videos with selection checkboxes"""
    st.markdown("### 📺 Video List")
    
    # Display videos
    for i, video in enumerate(filtered_videos):
        with st.container():
            col1, col2, col3 = st.columns([0.5, 6, 1.5])
            
            with col1:
                # Selection checkbox
                selected = st.checkbox("", key=f'select_{i}', label_visibility="collapsed")
            
            with col2:
                # Video info
                st.markdown(f'<div class="channel-video-item">', unsafe_allow_html=True)
                st.markdown(f"**{video.get('title', 'Unknown Title')}**")
                
                # Video metadata
                info_parts = []
                if video.get('published'):
                    info_parts.append(f"📅 {video['published']}")
                if video.get('duration'):
                    info_parts.append(f"⏱️ {video['duration']}")
                if video.get('view_count'):
                    info_parts.append(f"👁️ {video['view_count']}")
                
                if info_parts:
                    st.caption(" | ".join(info_parts))
                
                # Description preview
                if video.get('description'):
                    desc_preview = video['description'][:150] + "..." if len(video.get('description', '')) > 150 else video.get('description', '')
                    st.caption(desc_preview)
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col3:
                # Quick actions
                if st.button("🔗 Open", key=f'open_{i}', use_container_width=True):
                    if video.get('url'):
                        st.write(f"[Open Video]({video['url']})")
                
                if video.get('video_id'):
                    if st.button("📝 Get Transcript", key=f'transcript_{i}', use_container_width=True):
                        # Set up for transcript extraction
                        st.session_state['youtube_video_id'] = video['video_id']
                        st.session_state['youtube_video_title'] = video.get('title', 'Unknown')
                        st.info(f"Transcript extraction set up for: {video.get('title', 'Unknown')[:30]}...")
            
            st.divider()