#!/usr/bin/env python3
"""
Update all YouTube videos in the knowledgebase to have "AI Engineer" as the author
"""
import os
import re
from pathlib import Path

def update_all_youtube_authors():
    """Update all YouTube videos to have 'AI Engineer' as author"""
    kb_path = Path("knowledgebase")
    
    if not kb_path.exists():
        print("Knowledgebase path does not exist")
        return
    
    updated_count = 0
    unchanged_count = 0
    error_count = 0
    
    print("Updating all YouTube videos to have 'AI Engineer' as author...")
    
    for md_file in kb_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if this is a YouTube video file
            if not content.startswith('---'):
                continue
                
            parts = content.split('---', 2)
            if len(parts) < 3:
                continue
            
            frontmatter_text = parts[1]
            body = parts[2]
            
            # Check if it's a YouTube video
            type_match = re.search(r'^type:\s*(.*)$', frontmatter_text, re.MULTILINE)
            if not type_match or type_match.group(1).strip() != 'youtube':
                continue
            
            # Get current author
            author_match = re.search(r'^author:\s*(.*)$', frontmatter_text, re.MULTILINE)
            current_author = author_match.group(1).strip() if author_match else ''
            
            # Check if already correct
            if current_author == 'AI Engineer':
                unchanged_count += 1
                continue
            
            # Update the author field
            if author_match:
                # Replace existing author
                new_frontmatter = re.sub(
                    r'^author:\s*.*$', 
                    'author: AI Engineer', 
                    frontmatter_text, 
                    flags=re.MULTILINE
                )
            else:
                # Add author field after type field
                new_frontmatter = re.sub(
                    r'^(type:\s*.*)$', 
                    r'\1\nauthor: AI Engineer', 
                    frontmatter_text, 
                    flags=re.MULTILINE
                )
            
            # Reconstruct content
            new_content = f"---\n{new_frontmatter}---{body}"
            
            # Write back to file
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            relative_path = str(md_file.relative_to(kb_path))
            print(f"✅ Updated: {relative_path}")
            print(f"   Changed author from '{current_author}' to 'AI Engineer'")
            updated_count += 1
            
        except Exception as e:
            error_count += 1
            relative_path = str(md_file.relative_to(kb_path))
            print(f"❌ Error updating {relative_path}: {e}")
    
    print(f"\n=== SUMMARY ===")
    print(f"✅ Updated: {updated_count} videos")
    print(f"📝 Already correct: {unchanged_count} videos")
    print(f"❌ Errors: {error_count} videos")
    print(f"📊 Total processed: {updated_count + unchanged_count + error_count} videos")

if __name__ == "__main__":
    update_all_youtube_authors()