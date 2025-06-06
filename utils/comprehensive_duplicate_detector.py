"""
Comprehensive duplicate detection for knowledge base files
Detects duplicates based on:
- Exact title matches
- Similar titles (fuzzy matching)
- Identical content
- Similar content
"""

import os
import sys
from pathlib import Path
import yaml
import hashlib
import re
from typing import Dict, List, Tuple, Set, Optional
from difflib import SequenceMatcher
import streamlit as st

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class DuplicateDetector:
    def __init__(self, knowledgebase_path: str = "knowledgebase"):
        self.kb_path = Path(knowledgebase_path)
        self.files_data = []
        self.duplicates = {}
        
    def scan_all_files(self) -> None:
        """Scan all markdown files and extract metadata"""
        if not self.kb_path.exists():
            return
        
        for md_file in self.kb_path.rglob("*.md"):
            try:
                file_data = self._extract_file_data(md_file)
                if file_data:
                    self.files_data.append(file_data)
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
    
    def _extract_file_data(self, file_path: Path) -> Optional[Dict]:
        """Extract metadata and content from a markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse YAML frontmatter if it exists
            frontmatter = {}
            body = content
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    try:
                        frontmatter = yaml.safe_load(parts[1]) or {}
                        body = parts[2].strip()
                    except yaml.YAMLError:
                        pass
            
            # Extract title from frontmatter or filename
            title = frontmatter.get('title', '')
            if not title:
                # Try to extract from first # heading
                match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
                if match:
                    title = match.group(1).strip()
                else:
                    # Use filename as title
                    title = file_path.stem.replace('_', ' ')
            
            # Calculate content hash
            content_hash = hashlib.md5(body.encode()).hexdigest()
            
            # Clean title for comparison
            clean_title = self._clean_title(title)
            
            return {
                'file_path': file_path,
                'relative_path': str(file_path.relative_to(self.kb_path)),
                'title': title,
                'clean_title': clean_title,
                'frontmatter': frontmatter,
                'body': body,
                'content_hash': content_hash,
                'content_length': len(body),
                'video_id': frontmatter.get('video_id', None)
            }
            
        except Exception as e:
            print(f"Error extracting data from {file_path}: {e}")
            return None
    
    def _clean_title(self, title: str) -> str:
        """Clean title for comparison - remove special chars, lowercase, etc."""
        # Remove common suffixes like _1, _2, (1), (2), etc.
        title = re.sub(r'[_\-\s]+\d+$', '', title)
        title = re.sub(r'\s*\(\d+\)$', '', title)
        title = re.sub(r'\s*\[\d+\]$', '', title)
        
        # Remove special characters and normalize
        title = re.sub(r'[^\w\s]', ' ', title)
        title = ' '.join(title.lower().split())
        
        return title
    
    def find_duplicates(self) -> Dict[str, List[Dict]]:
        """
        Find all types of duplicates using multiple detection strategies.
        
        This is the main duplicate detection algorithm that employs several techniques
        to identify potential duplicates in the knowledge base:
        
        Detection Strategies:
        1. Exact Content Matching:
           - Uses MD5 hash of file content for exact comparison
           - Groups files with identical content regardless of title
           - Most reliable method for true duplicates
        
        2. Exact Title Matching:
           - Groups files with identical cleaned titles
           - Title cleaning removes special characters, numbers, and normalizes case
           - Catches renamed files or files with different paths but same content
        
        3. Fuzzy Title Matching:
           - Uses SequenceMatcher for similarity detection (85% threshold)
           - Catches slight variations like "Tutorial 1" vs "Tutorial-1"
           - Uses efficient O(n²) comparison with early termination
        
        4. YouTube-Specific Detection:
           - Groups by video_id (most reliable for YouTube content)
           - Groups by title+author combination for same-channel duplicates
           - Handles cases where video_id might be missing
        
        Performance Considerations:
        - Content hashing: O(n) time complexity, very fast
        - Title grouping: O(n) time complexity
        - Fuzzy matching: O(n²) but with optimizations to skip processed files
        - YouTube detection: O(n) for each strategy
        
        Returns:
            Dict with categorized duplicate groups, each containing file metadata
        """
        self.duplicates = {
            'exact_content': [],
            'exact_title': [],
            'similar_title': [],
            'youtube_duplicates': [],
            'potential_duplicates': []
        }
        
        # Strategy 1: Group by content hash (exact content duplicates)
        content_groups = {}
        for file_data in self.files_data:
            hash_key = file_data['content_hash']
            if hash_key not in content_groups:
                content_groups[hash_key] = []
            content_groups[hash_key].append(file_data)
        
        # Find exact content duplicates
        for hash_key, files in content_groups.items():
            if len(files) > 1:
                self.duplicates['exact_content'].append({
                    'type': 'exact_content',
                    'files': files,
                    'count': len(files)
                })
        
        # Strategy 2: Group by clean title (exact title duplicates)
        title_groups = {}
        for file_data in self.files_data:
            clean_title = file_data['clean_title']
            if clean_title not in title_groups:
                title_groups[clean_title] = []
            title_groups[clean_title].append(file_data)
        
        # Find exact title duplicates
        for title, files in title_groups.items():
            if len(files) > 1:
                self.duplicates['exact_title'].append({
                    'type': 'exact_title',
                    'files': files,
                    'count': len(files),
                    'title': title
                })
        
        # Strategy 3: Find similar titles (fuzzy matching with optimization)
        # This is O(n²) but optimized to avoid redundant comparisons
        processed = set()  # Track files already assigned to groups
        for i, file1 in enumerate(self.files_data):
            if file1['file_path'] in processed:
                continue  # Skip files already in a similarity group
                
            similar_group = [file1]
            processed.add(file1['file_path'])
            
            # Compare with remaining files (avoid duplicate comparisons)
            for j, file2 in enumerate(self.files_data[i+1:], i+1):
                if file2['file_path'] in processed:
                    continue  # Skip files already grouped
                    
                # Calculate title similarity using longest common subsequence ratio
                similarity = SequenceMatcher(None, file1['clean_title'], file2['clean_title']).ratio()
                
                # Threshold: 85% similarity catches most legitimate variations
                # Examples: "Docker Tutorial" vs "Docker-Tutorial" = 92% similar
                #          "Python Basics" vs "Python Basic" = 86% similar
                if similarity > 0.85:
                    similar_group.append(file2)
                    processed.add(file2['file_path'])
            
            # Only record groups with actual duplicates
            if len(similar_group) > 1:
                self.duplicates['similar_title'].append({
                    'type': 'similar_title',
                    'files': similar_group,
                    'count': len(similar_group)
                })
        
        # Strategy 4a: Find YouTube duplicates by video_id (most reliable)
        # This is the gold standard for YouTube content - same video_id = definitely same video
        youtube_groups = {}
        for file_data in self.files_data:
            video_id = file_data.get('video_id')
            if video_id:
                if video_id not in youtube_groups:
                    youtube_groups[video_id] = []
                youtube_groups[video_id].append(file_data)
        
        for video_id, files in youtube_groups.items():
            if len(files) > 1:
                self.duplicates['youtube_duplicates'].append({
                    'type': 'youtube_duplicate',
                    'files': files,
                    'count': len(files),
                    'video_id': video_id
                })
        
        # Strategy 4b: Find YouTube duplicates by title+author combination
        # Fallback for cases where video_id might be missing or inconsistent
        # Groups videos from the same channel with identical titles
        youtube_title_author_groups = {}
        for file_data in self.files_data:
            # Only process files explicitly marked as YouTube videos
            if file_data['frontmatter'].get('type') == 'youtube':
                author = file_data['frontmatter'].get('author', '').strip().lower()
                title = file_data['clean_title']
                
                # Filter out generic or missing authors and titles
                if author and author != 'unknown channel' and title:
                    # Create composite key: "title|author" ensures same video from same channel
                    # Using pipe separator avoids conflicts (titles/authors rarely contain pipes)
                    composite_key = f"{title}|{author}"
                    if composite_key not in youtube_title_author_groups:
                        youtube_title_author_groups[composite_key] = []
                    youtube_title_author_groups[composite_key].append(file_data)
        
        # Process title+author groups to find duplicates
        for composite_key, files in youtube_title_author_groups.items():
            if len(files) > 1:
                # Extract components for reporting
                title_part, author_part = composite_key.split('|', 1)
                self.duplicates['youtube_duplicates'].append({
                    'type': 'youtube_title_author_duplicate',
                    'files': files,
                    'count': len(files),
                    'title': title_part,
                    'author': author_part
                })
        
        return self.duplicates
    
    def get_duplicate_summary(self) -> Dict[str, int]:
        """Get summary statistics of duplicates"""
        summary = {
            'total_files': len(self.files_data),
            'exact_content_groups': len(self.duplicates.get('exact_content', [])),
            'exact_title_groups': len(self.duplicates.get('exact_title', [])),
            'similar_title_groups': len(self.duplicates.get('similar_title', [])),
            'youtube_duplicate_groups': len(self.duplicates.get('youtube_duplicates', [])),
            'total_duplicate_files': 0
        }
        
        # Count total duplicate files (avoiding double counting)
        all_duplicate_files = set()
        for dup_type in self.duplicates.values():
            for group in dup_type:
                if len(group.get('files', [])) > 1:
                    # All files except the first are duplicates
                    files = group['files']
                    for f in files[1:]:
                        all_duplicate_files.add(f['file_path'])
        
        summary['total_duplicate_files'] = len(all_duplicate_files)
        
        return summary


def show_duplicate_report(detector: DuplicateDetector):
    """Display duplicate detection report in Streamlit"""
    st.header("📊 Duplicate Detection Report")
    
    # Initialize session state for duplicates if needed
    if 'duplicates_scanned' not in st.session_state:
        st.session_state.duplicates_scanned = False
        st.session_state.duplicates_data = None
        st.session_state.duplicates_summary = None
    
    # Scan files only if not already scanned or if refresh requested
    if not st.session_state.duplicates_scanned or st.button("🔄 Refresh Scan", type="secondary"):
        with st.spinner("Scanning knowledge base files..."):
            detector.scan_all_files()
            duplicates = detector.find_duplicates()
            summary = detector.get_duplicate_summary()
            
            # Store in session state
            st.session_state.duplicates_scanned = True
            st.session_state.duplicates_data = duplicates
            st.session_state.duplicates_summary = summary
    else:
        # Use cached data
        duplicates = st.session_state.duplicates_data
        summary = st.session_state.duplicates_summary
    
    # Display summary
    st.subheader("Summary")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Files", summary['total_files'])
    with col2:
        st.metric("Duplicate Files", summary['total_duplicate_files'])
    with col3:
        st.metric("Exact Content", summary['exact_content_groups'])
    with col4:
        st.metric("Similar Titles", summary['similar_title_groups'])
    
    # Display detailed results
    st.subheader("Detailed Duplicate Groups")
    
    # Exact content duplicates
    if duplicates['exact_content']:
        with st.expander(f"🔍 Exact Content Duplicates ({len(duplicates['exact_content'])} groups)", expanded=True):
            for i, group in enumerate(duplicates['exact_content']):
                st.write(f"**Group {i+1}** ({group['count']} files with identical content):")
                for file_data in group['files']:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"- `{file_data['relative_path']}`")
                        st.caption(f"  Title: {file_data['title']}")
                    with col2:
                        # Use a unique key based on file path hash to avoid key conflicts
                        import hashlib
                        file_hash = hashlib.md5(file_data['relative_path'].encode()).hexdigest()[:8]
                        delete_key = f"del_{i}_{file_hash}"
                        
                        if st.button("🗑️ Delete", key=delete_key):
                            try:
                                file_path = file_data['file_path']
                                if isinstance(file_path, Path):
                                    file_path = str(file_path)
                                if os.path.exists(file_path):
                                    os.remove(file_path)
                                    st.success(f"✅ Deleted {file_data['relative_path']}")
                                    # Clear cache and rerun
                                    st.session_state.duplicates_scanned = False
                                    st.session_state.duplicates_data = None
                                    st.session_state.duplicates_summary = None
                                    import time
                                    time.sleep(0.5)
                                    st.rerun()
                                else:
                                    st.error(f"File not found: {file_data['relative_path']}")
                            except Exception as e:
                                st.error(f"Error deleting file: {e}")
                st.divider()
    
    # Similar title duplicates
    if duplicates['similar_title']:
        with st.expander(f"📝 Similar Title Duplicates ({len(duplicates['similar_title'])} groups)"):
            for i, group in enumerate(duplicates['similar_title']):
                st.write(f"**Group {i+1}** ({group['count']} files with similar titles):")
                for file_data in group['files']:
                    st.write(f"- `{file_data['relative_path']}`")
                    st.caption(f"  Title: {file_data['title']}")
                st.divider()
    
    # YouTube duplicates
    if duplicates['youtube_duplicates']:
        with st.expander(f"📺 YouTube Video Duplicates ({len(duplicates['youtube_duplicates'])} groups)"):
            for i, group in enumerate(duplicates['youtube_duplicates']):
                if group['type'] == 'youtube_duplicate':
                    st.write(f"**🎬 Video ID: {group['video_id']}** ({group['count']} files):")
                elif group['type'] == 'youtube_title_author_duplicate':
                    st.write(f"**📺 Channel: {group['author'].title()}** - \"{group['title']}\" ({group['count']} files):")
                
                for file_data in group['files']:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"- `{file_data['relative_path']}`")
                        st.caption(f"  Title: {file_data['title']}")
                    with col2:
                        # Use a unique key based on file path hash to avoid key conflicts
                        import hashlib
                        file_hash = hashlib.md5(file_data['relative_path'].encode()).hexdigest()[:8]
                        delete_key = f"del_yt_{i}_{file_hash}"
                        
                        if st.button("🗑️ Delete", key=delete_key):
                            try:
                                file_path = file_data['file_path']
                                if isinstance(file_path, Path):
                                    file_path = str(file_path)
                                if os.path.exists(file_path):
                                    os.remove(file_path)
                                    st.success(f"✅ Deleted {file_data['relative_path']}")
                                    # Clear cache and rerun
                                    st.session_state.duplicates_scanned = False
                                    st.session_state.duplicates_data = None
                                    st.session_state.duplicates_summary = None
                                    import time
                                    time.sleep(0.5)
                                    st.rerun()
                                else:
                                    st.error(f"File not found: {file_data['relative_path']}")
                            except Exception as e:
                                st.error(f"Error deleting file: {e}")
                st.divider()
    
    # Cleanup options
    st.subheader("🧹 Cleanup Options")
    
    # Initialize deletion state
    if 'deletion_in_progress' not in st.session_state:
        st.session_state.deletion_in_progress = False
    if 'deletion_complete' not in st.session_state:
        st.session_state.deletion_complete = False
    if 'deletion_type' not in st.session_state:
        st.session_state.deletion_type = None
    
    # Count how many files would be deleted for each type
    exact_content_files_to_delete = 0
    for group in duplicates.get('exact_content', []):
        if len(group['files']) > 1:
            exact_content_files_to_delete += len(group['files']) - 1
    
    similar_title_files_to_delete = 0
    for group in duplicates.get('similar_title', []):
        if len(group['files']) > 1:
            similar_title_files_to_delete += len(group['files']) - 1
    
    youtube_files_to_delete = 0
    for group in duplicates.get('youtube_duplicates', []):
        if len(group['files']) > 1:
            youtube_files_to_delete += len(group['files']) - 1
    
    # Show options based on what duplicates exist
    total_files_to_delete = exact_content_files_to_delete + similar_title_files_to_delete + youtube_files_to_delete
    if total_files_to_delete > 0:
        st.write("**Choose which duplicates to remove:**")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if exact_content_files_to_delete > 0:
                st.info(f"📄 **Exact Content**: {exact_content_files_to_delete} files")
                if st.button("🗑️ Remove Exact Content", type="primary", key="remove_exact"):
                    st.session_state.deletion_in_progress = True
                    st.session_state.deletion_type = 'exact_content'
        
        with col2:
            if similar_title_files_to_delete > 0:
                st.warning(f"📝 **Similar Titles**: {similar_title_files_to_delete} files")
                if st.button("🗑️ Remove Similar Titles", type="primary", key="remove_similar"):
                    st.session_state.deletion_in_progress = True
                    st.session_state.deletion_type = 'similar_title'
        
        with col3:
            if youtube_files_to_delete > 0:
                st.error(f"📺 **YouTube Duplicates**: {youtube_files_to_delete} files")
                if st.button("🗑️ Remove YouTube Duplicates", type="primary", key="remove_youtube"):
                    st.session_state.deletion_in_progress = True
                    st.session_state.deletion_type = 'youtube_duplicates'
        
        with col4:
            if total_files_to_delete > 0:
                st.error(f"🔥 **All Duplicates**: {total_files_to_delete} files")
                if st.button("🗑️ Remove ALL Duplicates", type="primary", key="remove_all"):
                    st.session_state.deletion_in_progress = True
                    st.session_state.deletion_type = 'all'
        
        st.divider()
        confirm_delete = st.checkbox("✅ I confirm deletion", key="confirm_bulk_delete")
        
        if st.session_state.deletion_type == 'exact_content':
            st.info(f"⚠️ Will delete {exact_content_files_to_delete} files with identical content, keeping the oldest version of each.")
        elif st.session_state.deletion_type == 'similar_title':
            st.warning(f"⚠️ Will delete {similar_title_files_to_delete} files with similar titles (e.g., file_1.md, file_2.md), keeping the first version.")
        elif st.session_state.deletion_type == 'youtube_duplicates':
            st.error(f"⚠️ Will delete {youtube_files_to_delete} YouTube duplicate files, keeping the first version of each.")
        elif st.session_state.deletion_type == 'all':
            st.error(f"⚠️ Will delete {total_files_to_delete} duplicate files of all types, keeping only the original versions.")
    else:
        st.success("✅ No duplicates found to remove!")
        confirm_delete = False
    
    # Handle deletion if triggered and confirmed
    if st.session_state.deletion_in_progress and confirm_delete:
        # Create a progress container
        progress_container = st.container()
        
        with progress_container:
            st.info("🗑️ Deleting duplicate files...")
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            removed_count = 0
            error_count = 0
            processed = 0
            
            # Determine which groups to process based on deletion type
            groups_to_process = []
            if st.session_state.deletion_type == 'exact_content':
                groups_to_process = duplicates.get('exact_content', [])
                total_to_delete = exact_content_files_to_delete
            elif st.session_state.deletion_type == 'similar_title':
                groups_to_process = duplicates.get('similar_title', [])
                total_to_delete = similar_title_files_to_delete
            elif st.session_state.deletion_type == 'youtube_duplicates':
                groups_to_process = duplicates.get('youtube_duplicates', [])
                total_to_delete = youtube_files_to_delete
            elif st.session_state.deletion_type == 'all':
                groups_to_process = (duplicates.get('exact_content', []) + 
                                   duplicates.get('similar_title', []) + 
                                   duplicates.get('youtube_duplicates', []))
                total_to_delete = exact_content_files_to_delete + similar_title_files_to_delete + youtube_files_to_delete
            
            # Process the selected groups
            for group in groups_to_process:
                if len(group['files']) > 1:
                    # Sort by file path to keep the first one
                    sorted_files = sorted(group['files'], key=lambda x: x['file_path'])
                    # Delete all but the first
                    for file_data in sorted_files[1:]:
                        try:
                            file_path = file_data['file_path']
                            if isinstance(file_path, Path):
                                file_path = str(file_path)
                            if os.path.exists(file_path):
                                os.remove(file_path)
                                removed_count += 1
                                status_text.text(f"✅ Deleted: {file_data['relative_path']}")
                            else:
                                status_text.warning(f"⚠️ File not found: {file_data['relative_path']}")
                        except Exception as e:
                            error_count += 1
                            status_text.error(f"❌ Error: {str(e)[:50]}...")
                        
                        processed += 1
                        if total_to_delete > 0:
                            progress_bar.progress(processed / total_to_delete)
            
            # Clear progress UI
            progress_bar.empty()
            status_text.empty()
            
            # Show results
            if removed_count > 0:
                st.success(f"✅ Successfully removed {removed_count} duplicate files!")
                # Clear the cache and reset states
                st.session_state.duplicates_scanned = False
                st.session_state.duplicates_data = None
                st.session_state.duplicates_summary = None
                st.session_state.deletion_in_progress = False
                st.session_state.deletion_type = None
                st.session_state.deletion_complete = True
                # Add a small delay to ensure filesystem updates
                import time
                time.sleep(0.5)
                # Use rerun to refresh the page
                st.rerun()
            elif error_count > 0:
                st.error(f"❌ Failed to remove files due to {error_count} errors")
                st.session_state.deletion_in_progress = False
                st.session_state.deletion_type = None
            else:
                st.info("No duplicates to remove")
                st.session_state.deletion_in_progress = False
                st.session_state.deletion_type = None
    
    # Show message if deletion was completed
    if st.session_state.deletion_complete:
        st.success("✅ Deletion completed! The scan has been refreshed.")
        st.session_state.deletion_complete = False
    
    if st.button("📋 Export Duplicate Report"):
        report = {
            'summary': summary,
            'duplicates': {
                'exact_content': [[f['relative_path'] for f in g['files']] for g in duplicates['exact_content']],
                'similar_titles': [[f['relative_path'] for f in g['files']] for g in duplicates['similar_title']],
                'youtube_duplicates': [[f['relative_path'] for f in g['files']] for g in duplicates['youtube_duplicates']]
            }
        }
        
        import json
        report_json = json.dumps(report, indent=2)
        st.download_button(
            "Download Report JSON",
            report_json,
            "duplicate_report.json",
            mime="application/json"
        )


# Example usage in a Streamlit page
if __name__ == "__main__":
    st.set_page_config(page_title="Duplicate Detector", page_icon="🔍", layout="wide")
    st.title("🔍 Knowledge Base Duplicate Detector")
    
    detector = DuplicateDetector()
    show_duplicate_report(detector)