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
    Returns (new_videos, duplicate_videos_with_existing_info)
    """
    new_videos = []
    duplicates = []
    
    for video in video_list:
        video_id = video.get('video_id')
        if not video_id:
            new_videos.append(video)
            continue
        
        existing = find_existing_video(video_id, knowledgebase_path)
        if existing:
            # Add existing file info to the video data
            video_with_existing = video.copy()
            video_with_existing['existing_file'] = existing
            duplicates.append(video_with_existing)
        else:
            new_videos.append(video)
    
    return new_videos, duplicates

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
    
    st.warning(f"🔄 **Found {len(duplicates)} duplicate videos**")
    
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
        for video in duplicates:
            actions[video['video_id']] = "skip"
    elif global_action.startswith("🔄"):
        # Reprocess all
        for video in duplicates:
            actions[video['video_id']] = "reprocess"
    elif global_action.startswith("📝"):
        # Update metadata for all
        for video in duplicates:
            actions[video['video_id']] = "update_metadata"
    else:
        # Individual choices
        st.write("**Choose action for each duplicate:**")
        for i, video in enumerate(duplicates):
            with st.expander(f"📹 {video['title'][:50]}..."):
                existing_path = video['existing_file']['relative_path']
                st.caption(f"Existing file: `{existing_path}`")
                
                choice = st.radio(
                    f"Action for this video:",
                    [
                        "⏭️ Skip",
                        "🔄 Reprocess", 
                        "📝 Update metadata"
                    ],
                    key=f"individual_choice_{i}_{video['video_id']}"
                )
                
                if choice.startswith("⏭️"):
                    actions[video['video_id']] = "skip"
                elif choice.startswith("🔄"):
                    actions[video['video_id']] = "reprocess"
                else:
                    actions[video['video_id']] = "update_metadata"
    
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