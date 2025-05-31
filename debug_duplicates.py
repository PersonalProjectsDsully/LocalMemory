#!/usr/bin/env python3
"""
Debug script to understand what duplicates are being found
"""

import os
import re
from pathlib import Path
import hashlib
from difflib import SequenceMatcher

def _clean_title(title: str) -> str:
    """Clean title for comparison - remove special chars, lowercase, etc."""
    # Remove common suffixes like _1, _2, (1), (2), etc.
    title = re.sub(r'[_\-\s]+\d+$', '', title)
    title = re.sub(r'\s*\(\d+\)$', '', title)
    title = re.sub(r'\s*\[\d+\]$', '', title)
    
    # Remove special characters and normalize
    title = re.sub(r'[^\w\s]', ' ', title)
    title = ' '.join(title.lower().split())
    
    return title

def debug_duplicate_detection(knowledgebase_path: str = "knowledgebase"):
    """Debug duplicate detection"""
    kb_path = Path(knowledgebase_path)
    
    if not kb_path.exists():
        print(f"Knowledge base path {knowledgebase_path} does not exist")
        return
    
    files_data = []
    youtube_files = []
    
    print("Scanning files...")
    
    # Find all markdown files
    for md_file in kb_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if it's a YouTube video file
            if 'type: youtube' not in content:
                continue
                
            # Parse the frontmatter
            if not content.startswith('---'):
                continue
                
            parts = content.split('---', 2)
            if len(parts) < 3:
                continue
            
            frontmatter_text = parts[1]
            body = parts[2].strip()
            
            # Extract fields manually
            title_match = re.search(r'^title:\s*(.*)$', frontmatter_text, re.MULTILINE)
            author_match = re.search(r'^author:\s*(.*)$', frontmatter_text, re.MULTILINE)
            video_id_match = re.search(r'^video_id:\s*(.*)$', frontmatter_text, re.MULTILINE)
            
            title = title_match.group(1).strip() if title_match else ''
            author = author_match.group(1).strip() if author_match else ''
            video_id = video_id_match.group(1).strip() if video_id_match else ''
            
            # Calculate content hash
            content_hash = hashlib.md5(body.encode()).hexdigest()
            
            # Clean title for comparison
            clean_title = _clean_title(title)
            
            file_data = {
                'file_path': md_file,
                'relative_path': str(md_file.relative_to(kb_path)),
                'title': title,
                'clean_title': clean_title,
                'author': author,
                'video_id': video_id,
                'content_hash': content_hash,
                'content_length': len(body)
            }
            
            files_data.append(file_data)
            youtube_files.append(file_data)
            
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFound {len(youtube_files)} YouTube files")
    
    # Check for duplicates
    print("\n=== ANALYZING DUPLICATES ===")
    
    # 1. Content duplicates
    content_groups = {}
    for file_data in files_data:
        hash_key = file_data['content_hash']
        if hash_key not in content_groups:
            content_groups[hash_key] = []
        content_groups[hash_key].append(file_data)
    
    exact_content_duplicates = 0
    for hash_key, files in content_groups.items():
        if len(files) > 1:
            exact_content_duplicates += len(files) - 1
            print(f"\nEXACT CONTENT DUPLICATE GROUP ({len(files)} files):")
            for f in files:
                print(f"  - {f['relative_path']}")
                print(f"    Title: {f['title']}")
    
    # 2. YouTube title+author duplicates
    youtube_title_author_groups = {}
    for file_data in youtube_files:
        author = file_data['author'].strip().lower()
        title = file_data['clean_title']
        
        if author and author != 'unknown channel' and title:
            composite_key = f"{title}|{author}"
            if composite_key not in youtube_title_author_groups:
                youtube_title_author_groups[composite_key] = []
            youtube_title_author_groups[composite_key].append(file_data)
    
    youtube_duplicates = 0
    print(f"\n=== YOUTUBE TITLE+AUTHOR ANALYSIS ===")
    print(f"Total composite keys created: {len(youtube_title_author_groups)}")
    
    for composite_key, files in youtube_title_author_groups.items():
        if len(files) > 1:
            youtube_duplicates += len(files) - 1
            title_part, author_part = composite_key.split('|', 1)
            print(f"\nYOUTUBE TITLE+AUTHOR DUPLICATE GROUP ({len(files)} files):")
            print(f"  Key: {composite_key}")
            print(f"  Title: '{title_part}' | Author: '{author_part}'")
            for f in files:
                print(f"    - {f['relative_path']}")
                print(f"      Original title: {f['title']}")
                print(f"      Clean title: {f['clean_title']}")
                print(f"      Author: {f['author']}")
    
    # 3. Similar title analysis
    similar_title_duplicates = 0
    processed = set()
    
    for i, file1 in enumerate(files_data):
        if file1['file_path'] in processed:
            continue
            
        similar_group = [file1]
        processed.add(file1['file_path'])
        
        for j, file2 in enumerate(files_data[i+1:], i+1):
            if file2['file_path'] in processed:
                continue
                
            # Calculate title similarity
            similarity = SequenceMatcher(None, file1['clean_title'], file2['clean_title']).ratio()
            
            # If titles are very similar (>85% match)
            if similarity > 0.85:
                similar_group.append(file2)
                processed.add(file2['file_path'])
        
        if len(similar_group) > 1:
            similar_title_duplicates += len(similar_group) - 1
            print(f"\nSIMILAR TITLE GROUP ({len(similar_group)} files):")
            for f in similar_group:
                print(f"  - {f['relative_path']}")
                print(f"    Title: {f['title']}")
                print(f"    Clean: {f['clean_title']}")
    
    # 4. Check what the UI duplicate detector might be seeing
    print(f"\n=== DETAILED TITLE ANALYSIS ===")
    
    # Group by exact clean title
    title_groups = {}
    for file_data in files_data:
        clean_title = file_data['clean_title']
        if clean_title not in title_groups:
            title_groups[clean_title] = []
        title_groups[clean_title].append(file_data)
    
    exact_title_matches = 0
    for title, files in title_groups.items():
        if len(files) > 1:
            exact_title_matches += len(files) - 1
            print(f"\nEXACT TITLE MATCH GROUP ({len(files)} files):")
            print(f"  Clean title: '{title}'")
            for f in files:
                print(f"    - {f['relative_path']}")
                print(f"      Original: {f['title']}")
    
    # Show some example titles to understand the pattern
    print(f"\n=== SAMPLE TITLES ===")
    for i, file_data in enumerate(youtube_files[:10]):
        print(f"{i+1}. Original: {file_data['title']}")
        print(f"   Clean:    {file_data['clean_title']}")
        print(f"   Author:   {file_data['author']}")
        print()
    
    print(f"\n=== SUMMARY ===")
    print(f"Total YouTube files: {len(youtube_files)}")
    print(f"Exact content duplicates: {exact_content_duplicates}")
    print(f"Exact title matches: {exact_title_matches}")
    print(f"YouTube title+author duplicates: {youtube_duplicates}")
    print(f"Similar title duplicates: {similar_title_duplicates}")
    print(f"Total duplicates found: {exact_content_duplicates + exact_title_matches + youtube_duplicates + similar_title_duplicates}")

if __name__ == "__main__":
    debug_duplicate_detection()