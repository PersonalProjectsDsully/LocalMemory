#!/usr/bin/env python3
"""
Analyze the sources of the 105 YouTube videos in the knowledgebase
"""
import os
import re
from pathlib import Path
from collections import Counter

def analyze_video_sources():
    """Analyze where the YouTube videos came from"""
    kb_path = Path("knowledgebase")
    
    if not kb_path.exists():
        print("Knowledgebase path does not exist")
        return
    
    youtube_videos = []
    
    print("Analyzing YouTube videos in the knowledgebase...")
    
    for md_file in kb_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic frontmatter parsing
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter_text = parts[1]
                    
                    # Extract fields manually
                    title_match = re.search(r'^title:\s*(.*)$', frontmatter_text, re.MULTILINE)
                    author_match = re.search(r'^author:\s*(.*)$', frontmatter_text, re.MULTILINE)
                    type_match = re.search(r'^type:\s*(.*)$', frontmatter_text, re.MULTILINE)
                    video_id_match = re.search(r'^video_id:\s*(.*)$', frontmatter_text, re.MULTILINE)
                    date_added_match = re.search(r'^date_added:\s*(.*)$', frontmatter_text, re.MULTILINE)
                    
                    title = title_match.group(1).strip() if title_match else ''
                    author = author_match.group(1).strip() if author_match else ''
                    file_type = type_match.group(1).strip() if type_match else ''
                    video_id = video_id_match.group(1).strip() if video_id_match else ''
                    date_added = date_added_match.group(1).strip() if date_added_match else ''
                    
                    if file_type == 'youtube':
                        youtube_videos.append({
                            'title': title,
                            'author': author,
                            'video_id': video_id,
                            'date_added': date_added,
                            'file_path': str(md_file.relative_to(kb_path))
                        })
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFound {len(youtube_videos)} YouTube videos")
    
    # Analyze by author/channel
    print("\n=== ANALYSIS BY CHANNEL/AUTHOR ===")
    author_counts = Counter([video['author'] for video in youtube_videos])
    
    for author, count in author_counts.most_common():
        print(f"{author}: {count} videos")
    
    # Analyze by date added
    print("\n=== ANALYSIS BY DATE ADDED ===")
    date_counts = Counter([video['date_added'] for video in youtube_videos])
    
    for date, count in sorted(date_counts.items(), reverse=True):
        print(f"{date}: {count} videos")
    
    # Show some sample video titles from each major channel
    print("\n=== SAMPLE VIDEOS BY CHANNEL ===")
    for author, count in author_counts.most_common(5):  # Top 5 channels
        print(f"\n{author} ({count} videos):")
        author_videos = [v for v in youtube_videos if v['author'] == author]
        for i, video in enumerate(author_videos[:5]):  # Show first 5 videos
            print(f"  - {video['title']}")
        if len(author_videos) > 5:
            print(f"  ... and {len(author_videos) - 5} more")
    
    # Check for potential bulk imports
    print("\n=== POTENTIAL BULK IMPORTS ===")
    for date, count in sorted(date_counts.items(), reverse=True):
        if count > 5:  # More than 5 videos on the same date suggests bulk import
            print(f"{date}: {count} videos (possible bulk import)")
            date_videos = [v for v in youtube_videos if v['date_added'] == date]
            authors_on_date = Counter([v['author'] for v in date_videos])
            for author, author_count in authors_on_date.items():
                print(f"  - {author}: {author_count} videos")

if __name__ == "__main__":
    analyze_video_sources()