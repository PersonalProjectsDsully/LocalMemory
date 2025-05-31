#!/usr/bin/env python3
"""
Test script to understand channel import duplicate detection
"""
import os
import sys
import re
from pathlib import Path

# Add current directory to path
sys.path.append('.')

def _clean_title_for_comparison(title: str) -> str:
    """Clean title for comparison - remove special chars, numbers at end, etc."""
    # Remove common suffixes like _1, _2, (1), (2), etc.
    title = re.sub(r'[_\-\s]+\d+$', '', title)
    title = re.sub(r'\s*\(\d+\)$', '', title)
    title = re.sub(r'\s*\[\d+\]$', '', title)
    
    # Remove special characters and normalize
    title = re.sub(r'[^\w\s]', ' ', title)
    title = ' '.join(title.lower().split())
    
    return title

def test_duplicate_detection():
    """Test duplicate detection logic"""
    kb_path = Path("knowledgebase")
    
    if not kb_path.exists():
        print("Knowledgebase path does not exist")
        return
    
    # Scan existing files
    existing_titles = {}
    existing_youtube_videos = {}
    file_count = 0
    
    print("Scanning existing files...")
    
    for md_file in kb_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_count += 1
            
            # Basic frontmatter parsing
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter_text = parts[1]
                    
                    # Extract fields manually to avoid yaml dependency
                    title_match = re.search(r'^title:\s*(.*)$', frontmatter_text, re.MULTILINE)
                    author_match = re.search(r'^author:\s*(.*)$', frontmatter_text, re.MULTILINE)
                    type_match = re.search(r'^type:\s*(.*)$', frontmatter_text, re.MULTILINE)
                    
                    title = title_match.group(1).strip() if title_match else ''
                    author = author_match.group(1).strip() if author_match else ''
                    file_type = type_match.group(1).strip() if type_match else ''
                    
                    if title:
                        clean_title = _clean_title_for_comparison(title)
                        
                        # Store by title
                        if clean_title not in existing_titles:
                            existing_titles[clean_title] = []
                        existing_titles[clean_title].append({
                            'file_path': str(md_file),
                            'relative_path': str(md_file.relative_to(kb_path)),
                            'title': title,
                            'author': author,
                            'type': file_type
                        })
                        
                        # For YouTube videos, also create title+author key
                        if file_type == 'youtube' and author:
                            author_clean = author.lower().strip()
                            if author_clean and author_clean != 'unknown channel':
                                composite_key = f"{clean_title}|{author_clean}"
                                if composite_key not in existing_youtube_videos:
                                    existing_youtube_videos[composite_key] = []
                                existing_youtube_videos[composite_key].append({
                                    'file_path': str(md_file),
                                    'relative_path': str(md_file.relative_to(kb_path)),
                                    'title': title,
                                    'author': author,
                                    'type': file_type
                                })
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"Scanned {file_count} files")
    print(f"Found {len(existing_titles)} unique titles")
    print(f"Found {len(existing_youtube_videos)} YouTube title+author combinations")
    
    # Test some fake videos that match existing ones
    test_videos = [
        {
            'title': 'Agent Evals: Finally, With The Map',
            'video_id': 'test_1',
            'author': 'AI Engineer',
            'channel': 'AI Engineer'
        },
        {
            'title': 'The Price of Intelligence - AI Agent Pricing in 2025',
            'video_id': 'test_2', 
            'author': 'AI Engineer',
            'channel': 'AI Engineer'
        },
        {
            'title': 'Mission-Critical Evals at Scale (Learnings from 100k medical decisions)',
            'video_id': 'test_3',
            'author': 'AI Engineer', 
            'channel': 'AI Engineer'
        }
    ]
    
    print("\nTesting duplicate detection:")
    duplicates_found = 0
    
    for video in test_videos:
        video_title = video.get('title', '')
        video_author = video.get('author', video.get('channel', 'Channel Video')).strip().lower()
        
        if video_title and video_author and video_author != 'unknown channel':
            clean_video_title = _clean_title_for_comparison(video_title)
            composite_key = f"{clean_video_title}|{video_author}"
            
            print(f"\nTesting: '{video_title}'")
            print(f"  Clean title: '{clean_video_title}'")
            print(f"  Author: '{video_author}'")
            print(f"  Composite key: '{composite_key}'")
            
            # Check for exact title+author match
            if composite_key in existing_youtube_videos:
                existing = existing_youtube_videos[composite_key][0]
                print(f"  ✅ DUPLICATE: Found YouTube title+author match")
                print(f"    Existing file: {existing['relative_path']}")
                duplicates_found += 1
            elif clean_video_title in existing_titles:
                existing = existing_titles[clean_video_title][0]
                print(f"  ✅ DUPLICATE: Found exact title match")
                print(f"    Existing file: {existing['relative_path']}")
                duplicates_found += 1
            else:
                print(f"  ❌ No duplicate found")
    
    print(f"\nTotal duplicates detected: {duplicates_found}")
    
    # Show some existing YouTube videos for comparison
    print(f"\nSample existing YouTube videos:")
    count = 0
    for key, files in existing_youtube_videos.items():
        if count < 5:
            title_part, author_part = key.split('|', 1)
            print(f"  {title_part} | {author_part}")
            count += 1

if __name__ == "__main__":
    test_duplicate_detection()