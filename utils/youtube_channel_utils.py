import streamlit as st
from typing import List, Dict, Optional, Tuple
import requests
import re
from datetime import datetime
import json
import time

def extract_channel_id(channel_input: str) -> Optional[str]:
    """
    Extract channel ID from various YouTube channel URL formats or direct ID
    
    Supports:
    - Channel ID: UCxxxxx
    - Channel URL: youtube.com/channel/UCxxxxx
    - User URL: youtube.com/user/username  
    - Custom URL: youtube.com/@handle or youtube.com/c/customname
    """
    # Direct channel ID
    if channel_input.startswith('UC') and len(channel_input) == 24:
        return channel_input
    
    # Channel URL
    channel_match = re.search(r'youtube\.com/channel/(UC[\w-]{22})', channel_input)
    if channel_match:
        return channel_match.group(1)
    
    # Handle @username URLs by resolving them to channel ID
    username_match = re.search(r'youtube\.com/@([\w-]+)', channel_input)
    if username_match:
        username = username_match.group(1)
        
        # Note: Add hardcoded mappings here for channels with resolution issues if needed
        # if username == "problematic-channel":
        #     return "UC_KNOWN_CHANNEL_ID"
        
        try:
            st.info(f"Resolving @{username} to channel ID...")
            # Get the channel page to find the actual channel ID
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(f"https://www.youtube.com/@{username}", headers=headers, timeout=10)
            if response.status_code == 200:
                content = response.text
                
                # Look for channel ID in the page source
                patterns = [
                    r'"channelId":"(UC[\w-]{22})"',
                    r'"externalId":"(UC[\w-]{22})"',
                    r'channel/(UC[\w-]{22})',
                    r'"browseId":"(UC[\w-]{22})"'
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, content)
                    if match:
                        channel_id = match.group(1)
                        st.success(f"Found channel ID: {channel_id} (length: {len(channel_id)})")
                        return channel_id
                
                st.warning(f"Could not find channel ID in @{username} page")
            else:
                st.error(f"Failed to fetch @{username} page. Status: {response.status_code}")
                        
        except Exception as e:
            st.error(f"Error resolving @{username}: {str(e)}")
            # If we can't resolve it, fall back to None
            pass
    
    # Handle /c/ custom URLs (similar to @username)
    custom_match = re.search(r'youtube\.com/c/([\w-]+)', channel_input)
    if custom_match:
        custom_name = custom_match.group(1)
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(f"https://www.youtube.com/c/{custom_name}", headers=headers, timeout=10)
            if response.status_code == 200:
                content = response.text
                
                patterns = [
                    r'"channelId":"(UC[\w-]{22})"',
                    r'"externalId":"(UC[\w-]{22})"',
                    r'channel/(UC[\w-]{22})',
                    r'"browseId":"(UC[\w-]{22})"'
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, content)
                    if match:
                        return match.group(1)
                        
        except Exception as e:
            pass
    
    return None

def fetch_channel_videos_basic(channel_id: str, max_videos: int = 50) -> List[Dict]:
    """
    Fetch videos from a YouTube channel using RSS feed
    Note: RSS feeds are limited to ~15 recent videos. For more videos, use YouTube Data API
    """
    videos = []
    
    if not channel_id:
        st.error("No channel ID provided")
        return videos
    
    # Try to get channel RSS feed (limited but doesn't require API key)
    rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    
    try:
        st.info(f"Fetching recent videos from channel ID: {channel_id}")
        st.warning("⚠️ RSS feeds are limited to the most recent ~15 videos. For more videos, you would need the YouTube Data API.")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(rss_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            # Parse XML manually for basic info
            content = response.text
            
            # Check if we got a valid RSS feed
            if "<feed" not in content:
                st.error("Invalid RSS response - not a valid feed")
                return videos
            
            # Extract video entries
            entries = re.findall(r'<entry>(.*?)</entry>', content, re.DOTALL)
            actual_count = len(entries)
            st.info(f"Found {actual_count} recent videos (RSS feed limitation)")
            
            for entry in entries:
                video = {}
                
                # Extract video ID
                video_id_match = re.search(r'<yt:videoId>([^<]+)</yt:videoId>', entry)
                if video_id_match:
                    video['video_id'] = video_id_match.group(1)
                
                # Extract title
                title_match = re.search(r'<title>([^<]+)</title>', entry)
                if title_match:
                    video['title'] = title_match.group(1)
                
                # Extract published date
                published_match = re.search(r'<published>([^<]+)</published>', entry)
                if published_match:
                    video['published'] = published_match.group(1)
                
                # Extract channel name
                author_match = re.search(r'<author>\s*<name>([^<]+)</name>', entry)
                if author_match:
                    video['channel'] = author_match.group(1)
                
                # Construct URLs
                if video.get('video_id'):
                    video['link'] = f"https://www.youtube.com/watch?v={video['video_id']}"
                    # Use mqdefault.jpg (medium quality) as it's more reliable than maxresdefault.jpg
                    video['thumbnail'] = f"https://img.youtube.com/vi/{video['video_id']}/mqdefault.jpg"
                
                if video.get('video_id') and video.get('title'):
                    videos.append(video)
        else:
            st.error(f"Failed to fetch RSS feed. Status code: {response.status_code}")
            
    except Exception as e:
        st.error(f"Error fetching channel videos: {str(e)}")
    
    return videos

def fetch_channel_videos_with_api(channel_id: str, api_key: str, max_videos: int = 50) -> List[Dict]:
    """
    Fetch videos from a YouTube channel using YouTube Data API v3
    This method can fetch many more videos but requires an API key
    """
    videos = []
    
    if not api_key:
        st.error("YouTube Data API key is required for fetching more than 15 videos")
        return videos
    
    try:
        # YouTube Data API endpoint
        url = "https://www.googleapis.com/youtube/v3/search"
        
        params = {
            'key': api_key,
            'channelId': channel_id,
            'part': 'snippet',
            'order': 'date',
            'type': 'video',
            'maxResults': min(max_videos, 50)  # API limit is 50 per request
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            for item in data.get('items', []):
                video = {
                    'video_id': item['id']['videoId'],
                    'title': item['snippet']['title'],
                    'published': item['snippet']['publishedAt'],
                    'channel': item['snippet']['channelTitle'],
                    'link': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                    'thumbnail': f"https://img.youtube.com/vi/{item['id']['videoId']}/mqdefault.jpg"
                }
                videos.append(video)
                
            st.success(f"Fetched {len(videos)} videos using YouTube Data API")
            
        else:
            st.error(f"API request failed with status code: {response.status_code}")
            if response.status_code == 403:
                st.error("API key may be invalid or quota exceeded")
            
    except Exception as e:
        st.error(f"Error using YouTube Data API: {str(e)}")
    
    return videos

def fetch_channel_videos_selenium(channel_id: str, max_videos: int = 500) -> List[Dict]:
    """
    Fetch videos from a YouTube channel using Selenium web scraping
    This method can fetch ALL videos from a channel by scrolling through the /videos page
    """
    videos = []
    
    try:
        # Try to import selenium and related modules
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException, NoSuchElementException
        from bs4 import BeautifulSoup
        
        st.info("🔍 Using Selenium to scrape ALL videos from channel...")
        st.warning("⏳ This may take a while for channels with many videos. Please be patient.")
        
        # Set up Chrome options for headless browsing
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in background
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            # Navigate to the channel's videos page
            videos_url = f"https://www.youtube.com/channel/{channel_id}/videos"
            st.info(f"📡 Loading channel videos page: {videos_url}")
            driver.get(videos_url)
            
            # Wait for initial content to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "ytd-rich-item-renderer"))
            )
            
            # Create progress indicators
            progress_placeholder = st.empty()
            status_placeholder = st.empty()
            
            # Scroll to load all videos
            last_height = driver.execute_script("return document.documentElement.scrollHeight")
            videos_found = 0
            scroll_attempts = 0
            no_new_content_count = 0
            max_no_new_content = 3  # Stop after 3 consecutive scrolls with no new content
            
            while scroll_attempts < 100 and no_new_content_count < max_no_new_content and videos_found < max_videos:
                # Scroll down to bottom
                driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                
                # Wait for new content to load
                time.sleep(2)
                
                # Check current number of videos
                current_videos = driver.find_elements(By.TAG_NAME, "ytd-rich-item-renderer")
                current_count = len(current_videos)
                
                # Update progress
                progress_placeholder.info(f"🔄 Scrolling... Found {current_count} videos (scroll #{scroll_attempts + 1})")
                
                # Check if new content loaded
                new_height = driver.execute_script("return document.documentElement.scrollHeight")
                if new_height == last_height and current_count == videos_found:
                    no_new_content_count += 1
                    status_placeholder.warning(f"⏳ No new content detected ({no_new_content_count}/{max_no_new_content})")
                else:
                    no_new_content_count = 0
                    status_placeholder.success(f"✅ New videos loaded! Total: {current_count}")
                
                last_height = new_height
                videos_found = current_count
                scroll_attempts += 1
                
                # Break if we've found enough videos
                if videos_found >= max_videos:
                    status_placeholder.info(f"🎯 Reached maximum video limit: {max_videos}")
                    break
            
            # Clear progress indicators
            progress_placeholder.empty()
            status_placeholder.empty()
            
            st.success(f"🏁 Finished scrolling! Found {videos_found} video elements")
            
            # Now extract video information
            st.info("📊 Extracting video metadata...")
            
            # Get page source and parse with BeautifulSoup
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Find all video elements
            video_elements = soup.find_all('ytd-rich-item-renderer')
            
            extraction_progress = st.progress(0)
            
            for i, element in enumerate(video_elements[:max_videos]):
                try:
                    # Extract video ID from href
                    video_link = element.find('a', {'id': 'video-title-link'})
                    if not video_link or not video_link.get('href'):
                        continue
                    
                    href = video_link['href']
                    video_id_match = re.search(r'/watch\?v=([^&]+)', href)
                    if not video_id_match:
                        continue
                    
                    video_id = video_id_match.group(1)
                    
                    # Extract title
                    title_element = element.find('yt-formatted-string', {'id': 'video-title'})
                    title = title_element.get_text(strip=True) if title_element else f"Video {video_id}"
                    
                    # Extract view count and publish date
                    metadata_elements = element.find_all('span', class_='inline-metadata-item')
                    views = "Unknown views"
                    published = "Unknown date"
                    
                    if len(metadata_elements) >= 2:
                        views = metadata_elements[0].get_text(strip=True)
                        published = metadata_elements[1].get_text(strip=True)
                    elif len(metadata_elements) == 1:
                        # Could be either views or date
                        text = metadata_elements[0].get_text(strip=True)
                        if 'ago' in text:
                            published = text
                        else:
                            views = text
                    
                    # Create video object
                    video = {
                        'video_id': video_id,
                        'title': title,
                        'published': published,
                        'views': views,
                        'channel': '',  # Will be filled from channel info
                        'link': f"https://www.youtube.com/watch?v={video_id}",
                        'thumbnail': f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
                    }
                    
                    videos.append(video)
                    
                    # Update progress
                    extraction_progress.progress((i + 1) / min(len(video_elements), max_videos))
                    
                except Exception as e:
                    # Skip problematic videos
                    continue
            
            extraction_progress.empty()
            
            # Get channel name from page
            try:
                channel_name_element = soup.find('yt-formatted-string', {'id': 'text', 'class': 'style-scope ytd-channel-name'})
                if not channel_name_element:
                    # Try alternative selector
                    channel_name_element = soup.find('title')
                    if channel_name_element:
                        channel_name = channel_name_element.get_text().replace(' - YouTube', '')
                    else:
                        channel_name = "Unknown Channel"
                else:
                    channel_name = channel_name_element.get_text(strip=True)
                
                # Update all videos with channel name
                for video in videos:
                    video['channel'] = channel_name
                    
            except Exception:
                # Use default if channel name extraction fails
                for video in videos:
                    video['channel'] = "Unknown Channel"
            
            st.success(f"✅ Successfully extracted {len(videos)} videos using Selenium scraping!")
            
        finally:
            # Always close the driver
            driver.quit()
            
    except ImportError:
        st.error("🚨 Selenium not available")
        st.info("Install selenium to use this feature: `pip install selenium beautifulsoup4`")
        st.info("You'll also need ChromeDriver installed on your system.")
        
    except Exception as e:
        st.error(f"❌ Selenium scraping failed: {str(e)}")
        st.info("💡 Falling back to RSS feed method...")
        # Fallback to RSS method
        return fetch_channel_videos_basic(channel_id, max_videos)
    
    return videos

def get_channel_info(channel_input: str) -> Dict:
    """
    Get basic channel information
    """
    channel_info = {
        'channel_id': None,
        'channel_name': 'Unknown Channel',
        'channel_url': None
    }
    
    # Extract channel ID
    channel_id = extract_channel_id(channel_input)
    if channel_id:
        channel_info['channel_id'] = channel_id
        channel_info['channel_url'] = f"https://www.youtube.com/channel/{channel_id}"
        
        # Try to get channel name from RSS feed
        rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
        try:
            response = requests.get(rss_url, timeout=5)
            if response.status_code == 200:
                name_match = re.search(r'<author>\s*<name>([^<]+)</name>', response.text)
                if name_match:
                    channel_info['channel_name'] = name_match.group(1)
        except:
            pass
    
    return channel_info

def fetch_channel_playlists(channel_id: str) -> List[Dict]:
    """
    Fetch playlists from a channel (basic implementation)
    Note: Limited without API. Returns empty list for now.
    """
    # This would require YouTube Data API for proper implementation
    # For now, return empty list
    return []

def search_youtube_channel(query: str, channel_id: str = None) -> List[Dict]:
    """
    Search for videos within a channel or globally
    Note: Basic implementation - would need YouTube API for better results
    """
    videos = []
    
    # If channel_id provided, search within channel
    if channel_id:
        all_videos = fetch_channel_videos_basic(channel_id, max_videos=100)
        query_lower = query.lower()
        
        # Filter videos by query
        for video in all_videos:
            if query_lower in video.get('title', '').lower():
                videos.append(video)
    
    return videos