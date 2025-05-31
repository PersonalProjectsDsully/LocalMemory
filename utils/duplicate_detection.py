import os
import sys
from pathlib import Path
import yaml
from typing import Dict, List, Optional, Tuple
import streamlit as st

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def find_existing_video(video_id: str, knowledgebase_path: str = "knowledgebase") -> Optional[Dict]:
    """
    Search for an existing video in the knowledgebase by video_id
    Returns the file info if found, None if not found
    """
    kb_path = Path(knowledgebase_path)
    
    if not kb_path.exists():
        return None
    
    # Search through all markdown files
    for md_file in kb_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse YAML frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    try:
                        frontmatter = yaml.safe_load(parts[1]) or {}
                        
                        # Check if this is the same video
                        if frontmatter.get('video_id') == video_id:
                            return {
                                'file_path': str(md_file),
                                'relative_path': str(md_file.relative_to(kb_path)),
                                'frontmatter': frontmatter,
                                'body': parts[2].strip(),
                                'full_content': content
                            }
                    except yaml.YAMLError:
                        continue
        except Exception:
            continue
    
    return None

def find_duplicate_videos(video_list: List[Dict], knowledgebase_path: str = "knowledgebase") -> Tuple[List[Dict], List[Dict]]:
    """
    Separate video list into new videos and duplicates
    Now also checks for title similarity to catch more duplicates
    Returns (new_videos, duplicate_videos_with_existing_info)
    """
    from difflib import SequenceMatcher
    
    new_videos = []
    duplicates = []
    
    # First, scan all existing files for comprehensive duplicate detection
    kb_path = Path(knowledgebase_path)
    existing_files = {}
    existing_titles = {}
    existing_youtube_videos = {}  # New: store by title+author combo
    
    if kb_path.exists():
        for md_file in kb_path.rglob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Parse YAML frontmatter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        try:
                            frontmatter = yaml.safe_load(parts[1]) or {}
                            
                            # Store by video_id if it exists
                            video_id = frontmatter.get('video_id')
                            if video_id:
                                existing_files[video_id] = {
                                    'file_path': str(md_file),
                                    'relative_path': str(md_file.relative_to(kb_path)),
                                    'frontmatter': frontmatter,
                                    'body': parts[2].strip(),
                                    'full_content': content
                                }
                            
                            # Also store by title for similarity matching
                            title = frontmatter.get('title', '')
                            if title:
                                clean_title = _clean_title_for_comparison(title)
                                if clean_title not in existing_titles:
                                    existing_titles[clean_title] = []
                                existing_titles[clean_title].append({
                                    'file_path': str(md_file),
                                    'relative_path': str(md_file.relative_to(kb_path)),
                                    'frontmatter': frontmatter,
                                    'body': parts[2].strip(),
                                    'full_content': content,
                                    'original_title': title
                                })
                                
                                # For YouTube videos, also create title+author key
                                if frontmatter.get('type') == 'youtube':
                                    author = frontmatter.get('author', '').strip().lower()
                                    if author and author != 'unknown channel':
                                        # Create a composite key from title and author
                                        composite_key = f"{clean_title}|{author}"
                                        if composite_key not in existing_youtube_videos:
                                            existing_youtube_videos[composite_key] = []
                                        existing_youtube_videos[composite_key].append({
                                            'file_path': str(md_file),
                                            'relative_path': str(md_file.relative_to(kb_path)),
                                            'frontmatter': frontmatter,
                                            'body': parts[2].strip(),
                                            'full_content': content,
                                            'original_title': title
                                        })
                        except yaml.YAMLError:
                            continue
            except Exception:
                continue
    
    # Now check each video for duplicates
    for video in video_list:
        video_id = video.get('video_id')
        video_title = video.get('title', '')
        # Get author/channel from video - handle different possible field names
        video_author = video.get('author', video.get('channel', 'Channel Video')).strip().lower()
        is_duplicate = False
        
        # Check by video_id first (exact match)
        if video_id and video_id in existing_files:
            video_with_existing = video.copy()
            video_with_existing['existing_file'] = existing_files[video_id]
            video_with_existing['duplicate_type'] = 'video_id'
            duplicates.append(video_with_existing)
            is_duplicate = True
        
        # If not found by video_id, check by title+author for YouTube videos
        elif video_title and video_author and video_author != 'unknown channel':
            clean_video_title = _clean_title_for_comparison(video_title)
            composite_key = f"{clean_video_title}|{video_author}"
            
            # Check for exact title+author match (YouTube duplicate)
            if composite_key in existing_youtube_videos:
                # Use the first match
                existing = existing_youtube_videos[composite_key][0]
                video_with_existing = video.copy()
                video_with_existing['existing_file'] = existing
                video_with_existing['duplicate_type'] = 'youtube_title_author'
                duplicates.append(video_with_existing)
                is_duplicate = True
            elif clean_video_title in existing_titles:
                # Check for exact title match after cleaning
                # Use the first match
                existing = existing_titles[clean_video_title][0]
                video_with_existing = video.copy()
                video_with_existing['existing_file'] = existing
                video_with_existing['duplicate_type'] = 'exact_title'
                duplicates.append(video_with_existing)
                is_duplicate = True
            else:
                # Check for similar titles
                best_match = None
                best_score = 0
                
                for existing_clean_title, existing_list in existing_titles.items():
                    similarity = SequenceMatcher(None, clean_video_title, existing_clean_title).ratio()
                    if similarity > 0.85 and similarity > best_score:  # 85% similarity threshold
                        best_score = similarity
                        best_match = existing_list[0]
                
                if best_match:
                    video_with_existing = video.copy()
                    video_with_existing['existing_file'] = best_match
                    video_with_existing['duplicate_type'] = 'similar_title'
                    video_with_existing['similarity_score'] = best_score
                    duplicates.append(video_with_existing)
                    is_duplicate = True
        
        if not is_duplicate:
            new_videos.append(video)
    
    return new_videos, duplicates


def _clean_title_for_comparison(title: str) -> str:
    """Clean title for comparison - remove special chars, numbers at end, etc."""
    import re
    
    # Remove common suffixes like _1, _2, (1), (2), etc.
    title = re.sub(r'[_\-\s]+\d+$', '', title)
    title = re.sub(r'\s*\(\d+\)$', '', title)
    title = re.sub(r'\s*\[\d+\]$', '', title)
    
    # Remove special characters and normalize
    title = re.sub(r'[^\w\s]', ' ', title)
    title = ' '.join(title.lower().split())
    
    return title

def get_duplicate_handling_choice(video_title: str, existing_file_path: str) -> str:
    """
    Show UI for user to choose how to handle duplicate video
    Returns: 'skip', 'reprocess', 'update_metadata'
    """
    st.warning(f"🔄 **Duplicate Found**: '{video_title[:50]}...'")
    st.info(f"📁 Already exists at: `{existing_file_path}`")
    
    choice = st.radio(
        "How would you like to handle this duplicate?",
        [
            "⏭️ Skip (keep existing version)",
            "🔄 Reprocess completely (replace with new analysis)", 
            "📝 Update metadata only (keep transcript, refresh AI analysis)"
        ],
        key=f"duplicate_choice_{video_title[:20]}"
    )
    
    if choice.startswith("⏭️"):
        return "skip"
    elif choice.startswith("🔄"):
        return "reprocess"
    else:
        return "update_metadata"

def show_bulk_duplicate_options(duplicates: List[Dict]) -> Dict[str, str]:
    """
    Show bulk options for handling multiple duplicates
    Returns dict mapping video_id to action
    """
    if not duplicates:
        return {}
    
    # Count duplicate types
    video_id_dups = sum(1 for d in duplicates if d.get('duplicate_type') == 'video_id')
    exact_title_dups = sum(1 for d in duplicates if d.get('duplicate_type') == 'exact_title')
    similar_title_dups = sum(1 for d in duplicates if d.get('duplicate_type') == 'similar_title')
    youtube_title_author_dups = sum(1 for d in duplicates if d.get('duplicate_type') == 'youtube_title_author')
    
    st.warning(f"🔄 **Found {len(duplicates)} duplicate videos**")
    
    # Show breakdown
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Video ID Matches", video_id_dups)
    with col2:
        st.metric("Title + Channel", youtube_title_author_dups)
    with col3:
        st.metric("Exact Title", exact_title_dups)
    with col4:
        st.metric("Similar Titles", similar_title_dups)
    
    # Global option
    st.write("**Choose default action for all duplicates:**")
    
    global_action = st.radio(
        "Default action:",
        [
            "⏭️ Skip all duplicates (keep existing versions)",
            "🔄 Reprocess all duplicates (replace with new analysis)",
            "📝 Update metadata for all (keep transcripts, refresh AI analysis)",
            "🎛️ Choose individually for each video"
        ],
        key="global_duplicate_action"
    )
    
    actions = {}
    
    if global_action.startswith("⏭️"):
        # Skip all
        for i, video in enumerate(duplicates):
            video_key = video.get('video_id', f"video_{i}")
            actions[video_key] = "skip"
    elif global_action.startswith("🔄"):
        # Reprocess all
        for i, video in enumerate(duplicates):
            video_key = video.get('video_id', f"video_{i}")
            actions[video_key] = "reprocess"
    elif global_action.startswith("📝"):
        # Update metadata for all
        for i, video in enumerate(duplicates):
            video_key = video.get('video_id', f"video_{i}")
            actions[video_key] = "update_metadata"
    else:
        # Individual choices
        st.write("**Choose action for each duplicate:**")
        for i, video in enumerate(duplicates):
            dup_type = video.get('duplicate_type', 'unknown')
            type_emoji = {
                'video_id': '🎬',
                'exact_title': '📝',
                'similar_title': '🔍',
                'youtube_title_author': '📺'
            }.get(dup_type, '❓')
            
            with st.expander(f"{type_emoji} {video['title'][:50]}..."):
                existing_path = video['existing_file']['relative_path']
                st.caption(f"Existing file: `{existing_path}`")
                
                # Show duplicate type info
                if dup_type == 'video_id':
                    st.info("🎬 **Exact match**: Same YouTube video ID")
                elif dup_type == 'youtube_title_author':
                    st.info("📺 **YouTube duplicate**: Same video title and channel")
                    existing_author = video['existing_file']['frontmatter'].get('author', 'Unknown')
                    st.caption(f"Channel: {existing_author}")
                elif dup_type == 'exact_title':
                    st.info("📝 **Exact title match**: Title is identical after normalization")
                elif dup_type == 'similar_title':
                    similarity = video.get('similarity_score', 0) * 100
                    st.info(f"🔍 **Similar title**: {similarity:.0f}% match")
                    st.caption(f"Existing title: {video['existing_file'].get('original_title', 'Unknown')}")
                
                choice = st.radio(
                    f"Action for this video:",
                    [
                        "⏭️ Skip",
                        "🔄 Reprocess", 
                        "📝 Update metadata"
                    ],
                    key=f"individual_choice_{i}_{video.get('video_id', i)}"
                )
                
                video_key = video.get('video_id', f"video_{i}")
                if choice.startswith("⏭️"):
                    actions[video_key] = "skip"
                elif choice.startswith("🔄"):
                    actions[video_key] = "reprocess"
                else:
                    actions[video_key] = "update_metadata"
    
    return actions

def update_existing_video_metadata(existing_file: Dict, new_intelligence: Dict, new_summary: str) -> str:
    """
    Update existing video file with new AI analysis while preserving transcript
    Returns the updated content
    """
    frontmatter = existing_file['frontmatter'].copy()
    body = existing_file['body']
    
    # Update with new intelligent metadata
    frontmatter.update({
        'entities': new_intelligence.get('entities', []),
        'concepts': new_intelligence.get('concepts', []),
        'content_structure': new_intelligence.get('content_structure', 'unknown'),
        'difficulty_level': new_intelligence.get('difficulty_level', 'unknown'),
        'prerequisites': new_intelligence.get('prerequisites', []),
        'related_topics': new_intelligence.get('related_topics', []),
        'authority_signals': new_intelligence.get('authority_signals', []),
        'confidence_score': new_intelligence.get('confidence_score', 0.5),
        'last_updated': st.session_state.get('current_date', '2025-01-26')
    })
    
    # Update category if AI suggests a better one
    if new_intelligence.get('category') and new_intelligence.get('category') != 'General':
        frontmatter['category'] = new_intelligence.get('category')
    
    # Merge tags
    existing_tags = frontmatter.get('tags', [])
    new_tags = new_intelligence.get('tags', [])
    
    # Combine tags, avoiding duplicates
    all_tags = list(existing_tags)
    for tag in new_tags:
        if tag not in all_tags:
            all_tags.append(tag)
    
    frontmatter['tags'] = all_tags
    
    # Update summary in the body if it exists
    if new_summary:
        # Look for existing summary section and replace it
        if "## Summary" in body:
            parts = body.split("## Summary", 1)
            if len(parts) == 2:
                # Find end of summary (next ## heading or end of content)
                after_summary = parts[1]
                next_section = after_summary.find("\n## ")
                if next_section != -1:
                    # Replace summary but keep everything after
                    body = parts[0] + "## Summary\n\n" + new_summary + "\n" + after_summary[next_section:]
                else:
                    # Replace summary, keep transcript
                    body = parts[0] + "## Summary\n\n" + new_summary + "\n\n## Full Transcript" + after_summary.split("## Full Transcript", 1)[-1] if "## Full Transcript" in after_summary else after_summary
        else:
            # Add summary section before transcript
            if "## Full Transcript" in body:
                parts = body.split("## Full Transcript", 1)
                body = parts[0] + "## Summary\n\n" + new_summary + "\n\n## Full Transcript" + parts[1]
            else:
                # Add summary at the end
                body += f"\n\n## Summary\n\n{new_summary}"
    
    # Create updated content
    yaml_content = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
    updated_content = f"---\n{yaml_content}---\n\n{body}"
    
    return updated_content

def show_duplicate_summary(duplicates: List[Dict], actions: Dict[str, str]):
    """
    Show summary of what will happen to duplicates
    """
    if not duplicates or not actions:
        return
    
    skip_count = sum(1 for action in actions.values() if action == "skip")
    reprocess_count = sum(1 for action in actions.values() if action == "reprocess") 
    update_count = sum(1 for action in actions.values() if action == "update_metadata")
    
    st.info("📊 **Duplicate Handling Summary:**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if skip_count > 0:
            st.metric("⏭️ Will Skip", skip_count)
    
    with col2:
        if reprocess_count > 0:
            st.metric("🔄 Will Reprocess", reprocess_count)
    
    with col3:
        if update_count > 0:
            st.metric("📝 Will Update", update_count)