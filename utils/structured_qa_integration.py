"""
Integration module for using structured documents with the QA improvement system.

This module provides enhanced QA functionality that leverages the structured document
system for precise section identification and modification.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime

from .structured_document import (
    StructuredDocument, 
    DocumentSection, 
    QAIssue,
    load_or_create_structured_document,
    create_structured_document_from_markdown
)

class StructuredQAManager:
    """Manages QA operations on structured documents with precise section targeting."""
    
    def __init__(self, workspace_path: Path):
        self.workspace_path = Path(workspace_path)
        self.documents: Dict[str, StructuredDocument] = {}
    
    def import_existing_report(self, report_content: str, document_id: str) -> StructuredDocument:
        """Import an existing markdown report into the structured system."""
        doc = create_structured_document_from_markdown(
            report_content, document_id, self.workspace_path
        )
        self.documents[document_id] = doc
        return doc
    
    def convert_legacy_qa_issues(self, qa_results: Dict[str, Any], document_id: str) -> List[str]:
        """Convert legacy QA issue format to structured QA issues."""
        if document_id not in self.documents:
            return []
        
        doc = self.documents[document_id]
        issue_ids = []
        
        legacy_issues = qa_results.get('inaccurate_or_confusing_sections', [])
        
        for i, legacy_issue in enumerate(legacy_issues):
            section_title = legacy_issue.get('section_title', 'General')
            issue_description = legacy_issue.get('issue', 'Not specified')
            suggested_fix = legacy_issue.get('suggested_fix', '')
            
            # Find matching section by title
            section_id = self.find_section_by_title(doc, section_title)
            
            if section_id:
                # Determine issue type based on content
                issue_type = self.classify_issue_type(issue_description)
                
                issue_id = doc.add_qa_issue(
                    section_id=section_id,
                    issue_type=issue_type,
                    description=issue_description,
                    suggested_fix=suggested_fix
                )
                issue_ids.append(issue_id)
            else:
                # Create a general issue if section not found
                print(f"Warning: Could not find section '{section_title}' for issue {i+1}")
        
        doc.save_structure()
        return issue_ids
    
    def find_section_by_title(self, doc: StructuredDocument, title: str) -> Optional[str]:
        """Find section ID by title with fuzzy matching."""
        # Exact match first
        for section_id, section in doc.sections.items():
            if section.title == title:
                return section_id
        
        # Clean the input title for comparison
        title_lower = title.lower()
        clean_title = self._clean_section_title(title_lower)
        
        # Find best match by calculating similarity
        best_match = None
        best_score = 0
        
        for section_id, section in doc.sections.items():
            section_title_lower = section.title.lower()
            clean_section_title = self._clean_section_title(section_title_lower)
            
            # Calculate similarity score
            if clean_title == clean_section_title:
                return section_id  # Perfect match after cleaning
            elif clean_title in clean_section_title or clean_section_title in clean_title:
                # Calculate overlap ratio for partial matches
                overlap = len(set(clean_title.split()) & set(clean_section_title.split()))
                total_words = len(set(clean_title.split()) | set(clean_section_title.split()))
                score = overlap / total_words if total_words > 0 else 0
                
                if score > best_score:
                    best_score = score
                    best_match = section_id
        
        # Only return match if score is reasonable (>= 50% overlap)
        return best_match if best_score >= 0.5 else None
    
    def _clean_section_title(self, title: str) -> str:
        """Clean section title for better matching."""
        import re
        # Remove section numbers, colons, etc.
        cleaned = re.sub(r'^(section\s*\d+:?\s*|^\d+\.?\s*)', '', title.strip())
        return cleaned.strip()
    
    def classify_issue_type(self, description: str) -> str:
        """Classify issue type based on description."""
        description_lower = description.lower()
        
        if any(word in description_lower for word in ['structure', 'organization', 'heading', 'section']):
            return 'structure'
        elif any(word in description_lower for word in ['clarity', 'confusing', 'unclear', 'readability']):
            return 'clarity'
        elif any(word in description_lower for word in ['accuracy', 'incorrect', 'error', 'mistake']):
            return 'accuracy'
        elif any(word in description_lower for word in ['style', 'tone', 'formatting', 'consistency']):
            return 'style'
        else:
            return 'general'
    
    def apply_selective_fixes(self, document_id: str, selected_issue_ids: List[str], 
                            llm_function, custom_instructions: Dict[str, str] = None) -> Dict[str, Any]:
        """Apply fixes to selected issues using precise section replacement."""
        if document_id not in self.documents:
            return {"status": "error", "message": "Document not found"}
        
        doc = self.documents[document_id]
        content = doc.load_content()
        custom_instructions = custom_instructions or {}
        
        improvements_made = []
        sections_modified = []
        
        # Group issues by section for efficient processing
        issues_by_section = {}
        for issue_id in selected_issue_ids:
            if issue_id in doc.qa_issues:
                issue = doc.qa_issues[issue_id]
                if issue.section_id not in issues_by_section:
                    issues_by_section[issue.section_id] = []
                issues_by_section[issue.section_id].append(issue)
        
        # Process sections in reverse order (from end to beginning) to avoid position conflicts
        # Sort by section start position to ensure we process from end to beginning
        sorted_sections = sorted(issues_by_section.items(), 
                               key=lambda x: doc.sections[x[0]].char_start, 
                               reverse=True)
        
        # Process each section with its issues
        for section_id, section_issues in sorted_sections:
            section_content = doc.get_section_content(section_id, content)
            section = doc.sections[section_id]
            
            # Prepare improvement context for this section
            improvement_context = {
                "section_title": section.title,
                "section_content": section_content,
                "issues": []
            }
            
            for issue in section_issues:
                issue_context = {
                    "issue_id": issue.id,
                    "type": issue.type,
                    "description": issue.description,
                    "suggested_fix": issue.suggested_fix
                }
                
                # Add custom instruction if provided
                if issue.id in custom_instructions:
                    issue_context["custom_instruction"] = custom_instructions[issue.id]
                    issue.custom_instruction = custom_instructions[issue.id]
                
                improvement_context["issues"].append(issue_context)
            
            # Call LLM to improve this section
            try:
                print(f"DEBUG: Improving section '{section.title}' with {len(section_issues)} issues")
                print(f"DEBUG: Section content length: {len(section_content)}")
                print(f"DEBUG: Issues: {[issue.description for issue in section_issues]}")
                
                improved_section_content = llm_function(improvement_context)
                
                print(f"DEBUG: LLM returned content length: {len(improved_section_content) if improved_section_content else 0}")
                
                # Check if content actually changed
                if improved_section_content and improved_section_content.strip() != section_content.strip():
                    # Apply the improvement using precise section replacement
                    content = doc.replace_section_content(section_id, content, improved_section_content)
                    
                    # Mark issues as resolved
                    for issue in section_issues:
                        issue.status = "resolved"
                        doc.qa_issues[issue.id] = issue
                    
                    sections_modified.append({
                        "section_id": section_id,
                        "section_title": section.title,
                        "issues_resolved": [issue.id for issue in section_issues],
                        "original_length": len(section_content),
                        "new_length": len(improved_section_content)
                    })
                    
                    improvements_made.append(f"Improved '{section.title}' - resolved {len(section_issues)} issue(s)")
                else:
                    print(f"DEBUG: No changes made for section '{section.title}'")
                    if not improved_section_content:
                        print("DEBUG: LLM returned empty content")
                    elif improved_section_content.strip() == section_content.strip():
                        print("DEBUG: LLM returned unchanged content")
                        print(f"DEBUG: Original first 100 chars: {section_content[:100]}")
                        print(f"DEBUG: Improved first 100 chars: {improved_section_content[:100]}")
                
            except Exception as e:
                print(f"Error improving section {section_id}: {e}")
                import traceback
                traceback.print_exc()
                continue
        
        if improvements_made:
            # Save updated content and structure
            doc.save_content(content)
            doc.save_structure()
            
            # Create version snapshot
            doc.create_version_snapshot(
                content, 
                f"Applied fixes to {len(selected_issue_ids)} selected issues"
            )
            
            return {
                "status": "improved",
                "improved_report": content,
                "improvements_made": improvements_made,
                "sections_modified": sections_modified,
                "issues_resolved": len(selected_issue_ids)
            }
        else:
            return {
                "status": "no_changes",
                "message": "No improvements were made to the selected issues"
            }
    
    def get_section_issues_summary(self, document_id: str) -> Dict[str, Any]:
        """Get a summary of all issues organized by section."""
        if document_id not in self.documents:
            return {}
        
        doc = self.documents[document_id]
        summary = {
            "document_id": document_id,
            "total_sections": len(doc.sections),
            "total_issues": len(doc.qa_issues),
            "sections_with_issues": 0,
            "issues_by_type": {},
            "issues_by_status": {},
            "sections": {}
        }
        
        # Organize issues by section
        for section_id, section in doc.sections.items():
            section_issues = doc.get_issues_for_section(section_id)
            
            if section_issues:
                summary["sections_with_issues"] += 1
                
                summary["sections"][section_id] = {
                    "title": section.title,
                    "level": section.level,
                    "issue_count": len(section_issues),
                    "issues": [
                        {
                            "id": issue.id,
                            "type": issue.type,
                            "description": issue.description,
                            "status": issue.status,
                            "has_custom_instruction": bool(issue.custom_instruction)
                        }
                        for issue in section_issues
                    ]
                }
                
                # Count by type and status
                for issue in section_issues:
                    summary["issues_by_type"][issue.type] = summary["issues_by_type"].get(issue.type, 0) + 1
                    summary["issues_by_status"][issue.status] = summary["issues_by_status"].get(issue.status, 0) + 1
        
        return summary
    
    def create_legacy_compatible_issues(self, document_id: str) -> List[Dict[str, Any]]:
        """Create legacy-compatible issue format for existing UI."""
        if document_id not in self.documents:
            return []
        
        doc = self.documents[document_id]
        legacy_issues = []
        
        for issue in doc.qa_issues.values():
            if issue.status == "open":  # Only show unresolved issues
                section = doc.sections.get(issue.section_id)
                section_title = section.title if section else "General"
                
                legacy_issue = {
                    "section_title": section_title,
                    "issue": issue.description,
                    "suggested_fix": issue.suggested_fix,
                    "_structured_id": issue.id,  # Hidden field for integration
                    "_section_id": issue.section_id  # Hidden field for precise targeting
                }
                
                legacy_issues.append(legacy_issue)
        
        return legacy_issues

def create_llm_improvement_function(llm_call_function):
    """Create an LLM function compatible with structured QA system."""
    
    def improve_section(improvement_context: Dict[str, Any]) -> str:
        """Improve a specific section based on its issues."""
        section_title = improvement_context["section_title"]
        section_content = improvement_context["section_content"]
        issues = improvement_context["issues"]
        
        # Build improvement prompt
        prompt = f"""You are improving a section titled "{section_title}".

Current section content:
```
{section_content}
```

Issues to address:
"""
        
        for i, issue in enumerate(issues, 1):
            prompt += f"\n{i}. **{issue['type'].title()} Issue**: {issue['description']}\n"
            
            if issue.get('custom_instruction'):
                prompt += f"   **Custom Instruction**: {issue['custom_instruction']}\n"
            else:
                prompt += f"   **Suggested Fix**: {issue['suggested_fix']}\n"
        
        prompt += """
Please provide an improved version of this section that addresses all the identified issues. 
Return ONLY the improved section content, maintaining the same markdown structure and formatting.
Do not add explanations or comments outside the content.
"""
        
        print(f"DEBUG: LLM Prompt:\n{prompt[:500]}...")  # Show first 500 chars of prompt
        
        try:
            response = llm_call_function(prompt)
            print(f"DEBUG: LLM Response length: {len(response) if response else 0}")
            if response:
                print(f"DEBUG: LLM Response first 200 chars: {response[:200]}...")
            return response.strip() if response else section_content
        except Exception as e:
            print(f"LLM call failed: {e}")
            import traceback
            traceback.print_exc()
            return section_content
    
    return improve_section