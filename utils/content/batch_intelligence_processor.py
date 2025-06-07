import os
import sys
from pathlib import Path
import yaml
import streamlit as st
from datetime import datetime
from typing import List, Dict, Any

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.llm_utils import extract_content_intelligence

def process_existing_content(knowledgebase_path: str = "knowledgebase") -> Dict[str, Any]:
    """
    Batch process existing content to add intelligent metadata
    """
    kb_path = Path(knowledgebase_path)
    
    if not kb_path.exists():
        return {
            "status": "error",
            "message": "Knowledgebase directory not found",
            "processed": 0,
            "total": 0,
            "errors": []
        }
    
    # Find all markdown files
    md_files = list(kb_path.rglob("*.md"))
    total_files = len(md_files)
    processed_files = 0
    errors = []
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, md_file in enumerate(md_files):
        try:
            status_text.text(f"Processing: {md_file.stem}...")
            
            # Read current content
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse existing frontmatter
            frontmatter, body = _parse_frontmatter(content)
            
            # Check if intelligent metadata already exists
            if _has_intelligent_metadata(frontmatter):
                status_text.text(f"Skipping: {md_file.stem} (already processed)")
                processed_files += 1
                progress_bar.progress((i + 1) / total_files)
                continue
            
            # Extract intelligent metadata
            title = frontmatter.get('title', md_file.stem)
            author = frontmatter.get('author', 'Unknown')
            content_type = frontmatter.get('type', 'document')
            
            intelligence = extract_content_intelligence(
                body,
                title,
                author,
                content_type
            )
            
            # Merge with existing frontmatter
            enhanced_frontmatter = _merge_metadata(frontmatter, intelligence)
            
            # Write back enhanced content
            enhanced_content = _create_enhanced_content(enhanced_frontmatter, body)
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(enhanced_content)
            
            processed_files += 1
            status_text.text(f"Enhanced: {md_file.stem}")
            
        except Exception as e:
            error_msg = f"Error processing {md_file}: {str(e)}"
            errors.append(error_msg)
            status_text.text(f"Error: {md_file.stem}")
        
        progress_bar.progress((i + 1) / total_files)
    
    progress_bar.empty()
    status_text.empty()
    
    return {
        "status": "success" if not errors else "partial",
        "message": f"Processed {processed_files} of {total_files} files",
        "processed": processed_files,
        "total": total_files,
        "errors": errors
    }

def _parse_frontmatter(content: str) -> tuple:
    """Parse YAML frontmatter from markdown content"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
                return frontmatter, body
            except yaml.YAMLError:
                pass
    
    return {}, content

def _has_intelligent_metadata(frontmatter: Dict) -> bool:
    """Check if frontmatter already has intelligent metadata"""
    intelligent_fields = ['entities', 'concepts', 'content_structure', 'difficulty_level']
    return any(field in frontmatter for field in intelligent_fields)

def _merge_metadata(existing: Dict, intelligence: Dict) -> Dict:
    """Merge existing frontmatter with new intelligent metadata"""
    merged = existing.copy()
    
    # Add intelligent fields
    merged.update({
        'entities': intelligence.get('entities', []),
        'concepts': intelligence.get('concepts', []),
        'content_structure': intelligence.get('content_structure', 'unknown'),
        'difficulty_level': intelligence.get('difficulty_level', 'unknown'),
        'prerequisites': intelligence.get('prerequisites', []),
        'related_topics': intelligence.get('related_topics', []),
        'authority_signals': intelligence.get('authority_signals', []),
        'confidence_score': intelligence.get('confidence_score', 0.5),
        'intelligence_processed': datetime.now().strftime('%Y-%m-%d')
    })
    
    # Update category if intelligence suggests a better one
    if intelligence.get('category') and intelligence.get('category') != 'General':
        if not existing.get('category') or existing.get('category') == 'General':
            merged['category'] = intelligence.get('category')
    
    # Merge tags
    existing_tags = existing.get('tags', [])
    intelligent_tags = intelligence.get('tags', [])
    
    # Combine tags, avoiding duplicates
    all_tags = list(existing_tags)
    for tag in intelligent_tags:
        if tag not in all_tags:
            all_tags.append(tag)
    
    merged['tags'] = all_tags
    
    return merged

def _create_enhanced_content(frontmatter: Dict, body: str) -> str:
    """Create enhanced markdown content with updated frontmatter"""
    # Convert frontmatter to YAML
    yaml_content = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
    
    # Create complete content
    enhanced_content = f"""---
{yaml_content}---

{body}"""
    
    return enhanced_content

def analyze_knowledgebase_metadata(knowledgebase_path: str = "knowledgebase") -> Dict[str, Any]:
    """
    Analyze current state of metadata in knowledgebase
    """
    kb_path = Path(knowledgebase_path)
    
    if not kb_path.exists():
        return {"status": "error", "message": "Knowledgebase not found"}
    
    md_files = list(kb_path.rglob("*.md"))
    
    stats = {
        "total_files": len(md_files),
        "with_intelligent_metadata": 0,
        "without_intelligent_metadata": 0,
        "unique_entities": set(),
        "unique_concepts": set(),
        "categories": set(),
        "content_structures": set(),
        "difficulty_levels": set()
    }
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter, _ = _parse_frontmatter(content)
            
            if _has_intelligent_metadata(frontmatter):
                stats["with_intelligent_metadata"] += 1
                
                # Collect metadata
                stats["unique_entities"].update(frontmatter.get('entities', []))
                stats["unique_concepts"].update(frontmatter.get('concepts', []))
                stats["content_structures"].add(frontmatter.get('content_structure', 'unknown'))
                stats["difficulty_levels"].add(frontmatter.get('difficulty_level', 'unknown'))
            else:
                stats["without_intelligent_metadata"] += 1
            
            stats["categories"].add(frontmatter.get('category', 'General'))
            
        except Exception:
            continue
    
    # Convert sets to counts
    stats["unique_entities"] = len(stats["unique_entities"])
    stats["unique_concepts"] = len(stats["unique_concepts"])
    stats["categories"] = len(stats["categories"])
    stats["content_structures"] = len(stats["content_structures"])
    stats["difficulty_levels"] = len(stats["difficulty_levels"])
    
    return {
        "status": "success",
        "stats": stats
    }