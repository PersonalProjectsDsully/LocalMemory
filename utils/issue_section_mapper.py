"""
Maps QA issues to actual document sections
"""

import re
from typing import Optional, Dict, Any
from .structured_document import StructuredDocument

def find_section_for_issue(issue: Dict[str, Any], structured_doc: StructuredDocument) -> Optional[str]:
    """
    Find the actual document section that an issue refers to.
    
    Args:
        issue: QA issue dictionary with 'section_title', 'issue', 'suggested_fix'
        structured_doc: The parsed structured document
        
    Returns:
        Section ID if found, None otherwise
    """
    section_title = issue.get('section_title', '')
    issue_desc = issue.get('issue', '')
    suggested_fix = issue.get('suggested_fix', '')
    
    # Combine all text for analysis
    full_text = f"{section_title} {issue_desc} {suggested_fix}".lower()
    
    print(f"DEBUG: Analyzing issue text: {full_text[:200]}...")
    
    # Strategy 1: Look for explicit section references
    # Pattern: "Section 1", "section 1:", "first section", etc.
    section_patterns = [
        r'section\s+(\d+)',
        r'section\s+(\w+)',
        r'(\d+)(?:st|nd|rd|th)\s+section',
        r'first\s+section',
        r'second\s+section',
        r'third\s+section',
    ]
    
    for pattern in section_patterns:
        match = re.search(pattern, full_text)
        if match:
            if pattern == r'first\s+section':
                section_num = '1'
            elif pattern == r'second\s+section':
                section_num = '2'
            elif pattern == r'third\s+section':
                section_num = '3'
            else:
                section_num = match.group(1)
            
            print(f"DEBUG: Found section reference: {section_num}")
            
            # Find section with this number
            for sid, section in structured_doc.sections.items():
                if f"section {section_num}" in section.title.lower():
                    print(f"DEBUG: Matched to section: {section.title}")
                    return sid
    
    # Strategy 2: Look for keywords that match section titles
    # Common keywords in section titles
    keywords_to_sections = {
        'environment setup': ['environment', 'setup', 'configuration', 'install'],
        'api integration': ['api', 'integration', 'freshservice', 'endpoint'],
        'classification': ['classification', 'categorization', 'ticket', 'classify'],
        'triage': ['triage', 'workflow', 'routing'],
        'testing': ['test', 'validation', 'verify'],
        'documentation': ['documentation', 'deployment', 'docs'],
    }
    
    # Score each section based on keyword matches
    section_scores = {}
    
    for sid, section in structured_doc.sections.items():
        if section.level < 2:  # Skip top-level title
            continue
            
        score = 0
        section_lower = section.title.lower()
        
        # Direct title match
        if section_lower in full_text:
            score += 10
        
        # Keyword matching
        for category, keywords in keywords_to_sections.items():
            for keyword in keywords:
                if keyword in full_text and keyword in section_lower:
                    score += 3
                elif keyword in full_text or keyword in section_lower:
                    score += 1
        
        if score > 0:
            section_scores[sid] = score
            print(f"DEBUG: Section '{section.title}' score: {score}")
    
    # Return the highest scoring section
    if section_scores:
        best_section = max(section_scores.items(), key=lambda x: x[1])
        if best_section[1] >= 3:  # Minimum score threshold
            print(f"DEBUG: Best match: {structured_doc.sections[best_section[0]].title} (score: {best_section[1]})")
            return best_section[0]
    
    # Strategy 3: Default to first content section if it's a general structure issue
    if section_title in ['Structure', 'General'] or 'structure' in issue_desc or 'introduction' in full_text:
        # Find the first major content section (usually Section 1)
        for sid, section in structured_doc.sections.items():
            if section.level == 2 and 'section' in section.title.lower():
                print(f"DEBUG: Using default first section: {section.title}")
                return sid
    
    print("DEBUG: No section match found")
    return None