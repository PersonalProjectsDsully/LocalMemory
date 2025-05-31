#!/usr/bin/env python3
"""
Script to update all YouTube videos in the knowledge base to have "AI Engineer" as the author.
Uses basic string manipulation instead of YAML parsing to avoid dependencies.
"""

import os
import re
from pathlib import Path

def update_youtube_authors(knowledgebase_path: str = "knowledgebase"):
    """Update all YouTube videos to have AI Engineer as author"""
    kb_path = Path(knowledgebase_path)
    
    if not kb_path.exists():
        print(f"Knowledge base path {knowledgebase_path} does not exist")
        return
    
    updated_count = 0
    error_count = 0
    youtube_count = 0
    
    print("Scanning for YouTube videos...")
    
    # Find all markdown files
    for md_file in kb_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if it's a YouTube video file by looking for type: youtube
            if 'type: youtube' not in content:
                continue
                
            youtube_count += 1
            relative_path = str(md_file.relative_to(kb_path))
            print(f"Processing: {relative_path}")
            
            # Find current author line
            author_match = re.search(r'^author:\s*(.*)$', content, re.MULTILINE)
            if author_match:
                current_author = author_match.group(1).strip()
                print(f"  Current author: {current_author}")
                
                # Replace the author line
                new_content = re.sub(
                    r'^author:\s*.*$', 
                    'author: AI Engineer', 
                    content, 
                    flags=re.MULTILINE
                )
            else:
                print(f"  No author field found, adding it")
                # Add author field after type: youtube line
                new_content = re.sub(
                    r'^(type: youtube)$', 
                    r'\1\nauthor: AI Engineer', 
                    content, 
                    flags=re.MULTILINE
                )
            
            # Write back to file
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            updated_count += 1
            print(f"  ✅ Updated to: AI Engineer")
            
        except Exception as e:
            error_count += 1
            print(f"  ❌ Error processing {md_file}: {e}")
    
    print(f"\n📊 Summary:")
    print(f"  YouTube videos found: {youtube_count}")
    print(f"  Successfully updated: {updated_count}")
    print(f"  Errors: {error_count}")

if __name__ == "__main__":
    update_youtube_authors()