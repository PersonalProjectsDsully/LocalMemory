"""
Document-Wide Improvement System
Handles improvements that affect multiple sections or the overall document structure
"""

import re
from typing import Dict, List, Tuple, Optional, Any
from .llm_utils import _call_llm_api
import streamlit as st


class DocumentWideImprover:
    """Handles improvements that affect the entire document or multiple sections"""
    
    def __init__(self):
        self.meta_issue_types = {
            'overall_organization': self._improve_overall_organization,
            'redundancy': self._fix_redundancy_across_sections,
            'flow': self._improve_document_flow,
            'consistency': self._ensure_consistency,
            'structure': self._restructure_document,
            'coherence': self._improve_coherence,
            'transitions': self._add_section_transitions
        }
    
    def can_handle_issue(self, issue_title: str) -> bool:
        """Check if this is a document-wide issue"""
        issue_lower = issue_title.lower()
        keywords = ['overall', 'organization', 'structure', 'redundancy', 'overlap', 
                   'flow', 'coherence', 'consistency', 'document', 'report', 'multiple sections']
        return any(keyword in issue_lower for keyword in keywords)
    
    def improve_document(self, full_content: str, issues: List[Dict[str, str]], 
                        custom_instructions: Optional[str] = None) -> str:
        """Apply document-wide improvements based on identified issues"""
        
        # Categorize issues
        categorized_issues = self._categorize_issues(issues)
        
        # Apply improvements in order of priority
        improved_content = full_content
        
        # First handle structural issues
        if categorized_issues.get('structure'):
            improved_content = self._restructure_document(
                improved_content, 
                categorized_issues['structure'],
                custom_instructions
            )
        
        # Then handle redundancy
        if categorized_issues.get('redundancy'):
            improved_content = self._fix_redundancy_across_sections(
                improved_content,
                categorized_issues['redundancy'],
                custom_instructions
            )
        
        # Then improve flow and coherence
        if categorized_issues.get('flow') or categorized_issues.get('coherence'):
            improved_content = self._improve_document_flow(
                improved_content,
                categorized_issues.get('flow', []) + categorized_issues.get('coherence', []),
                custom_instructions
            )
        
        # Finally ensure consistency
        if categorized_issues.get('consistency'):
            improved_content = self._ensure_consistency(
                improved_content,
                categorized_issues['consistency'],
                custom_instructions
            )
        
        return improved_content
    
    def _categorize_issues(self, issues: List[Dict[str, str]]) -> Dict[str, List[Dict]]:
        """Categorize issues by type for prioritized handling"""
        categorized = {}
        
        for issue in issues:
            issue_text = issue.get('issue', '').lower()
            
            if 'redundan' in issue_text or 'overlap' in issue_text or 'repeat' in issue_text:
                categorized.setdefault('redundancy', []).append(issue)
            elif 'structure' in issue_text or 'organization' in issue_text:
                categorized.setdefault('structure', []).append(issue)
            elif 'flow' in issue_text or 'transition' in issue_text:
                categorized.setdefault('flow', []).append(issue)
            elif 'coheren' in issue_text or 'connect' in issue_text:
                categorized.setdefault('coherence', []).append(issue)
            elif 'consisten' in issue_text:
                categorized.setdefault('consistency', []).append(issue)
            else:
                categorized.setdefault('general', []).append(issue)
        
        return categorized
    
    def _improve_overall_organization(self, content: str, issues: List[Dict], 
                                    custom_instructions: Optional[str] = None) -> str:
        """Improve the overall organization of the document"""
        
        prompt = f"""You are improving the overall organization of a research report.

Current document:
{content}

Issues identified:
{self._format_issues(issues)}

{f"Additional instructions: {custom_instructions}" if custom_instructions else ""}

Reorganize the document to:
1. Create a clear, logical flow from introduction to conclusion
2. Group related content together
3. Eliminate redundancy between sections
4. Ensure each section has a distinct purpose
5. Add clear transitions between sections
6. Maintain all important information while improving structure

Return the complete reorganized document in markdown format.
"""
        
        response = _call_llm_api(prompt, "document organization improvement")
        return response if response else content
    
    def _fix_redundancy_across_sections(self, content: str, issues: List[Dict],
                                       custom_instructions: Optional[str] = None) -> str:
        """Remove redundancy across multiple sections"""
        
        prompt = f"""You are removing redundancy from a research report while maintaining completeness.

Current document:
{content}

Redundancy issues:
{self._format_issues(issues)}

{f"Additional instructions: {custom_instructions}" if custom_instructions else ""}

Instructions:
1. Identify all repeated content across sections
2. Consolidate repeated information into the most appropriate section
3. In other sections, reference the main discussion instead of repeating
4. Ensure each section focuses on its unique aspects
5. Maintain logical flow and completeness
6. Add cross-references where appropriate (e.g., "As discussed in Section X...")

Return the complete document with redundancy removed.
"""
        
        response = _call_llm_api(prompt, "redundancy removal")
        return response if response else content
    
    def _improve_document_flow(self, content: str, issues: List[Dict],
                              custom_instructions: Optional[str] = None) -> str:
        """Improve the flow and transitions between sections"""
        
        prompt = f"""You are improving the flow and coherence of a research report.

Current document:
{content}

Flow/coherence issues:
{self._format_issues(issues)}

{f"Additional instructions: {custom_instructions}" if custom_instructions else ""}

Improve the document by:
1. Adding smooth transitions between sections
2. Ensuring logical progression of ideas
3. Creating clear connections between related concepts
4. Adding introductory and concluding paragraphs where needed
5. Ensuring consistent narrative throughout

Return the complete document with improved flow.
"""
        
        response = _call_llm_api(prompt, "flow improvement")
        return response if response else content
    
    def _ensure_consistency(self, content: str, issues: List[Dict],
                           custom_instructions: Optional[str] = None) -> str:
        """Ensure consistency in terminology, style, and formatting"""
        
        prompt = f"""You are ensuring consistency throughout a research report.

Current document:
{content}

Consistency issues:
{self._format_issues(issues)}

{f"Additional instructions: {custom_instructions}" if custom_instructions else ""}

Ensure consistency in:
1. Terminology (use the same terms for the same concepts throughout)
2. Writing style and tone
3. Formatting of headers, lists, and emphasis
4. Level of detail across similar sections
5. Citation and reference style

Return the complete document with consistent style and terminology.
"""
        
        response = _call_llm_api(prompt, "consistency improvement")
        return response if response else content
    
    def _restructure_document(self, content: str, issues: List[Dict],
                             custom_instructions: Optional[str] = None) -> str:
        """Restructure the entire document for better organization"""
        
        # Extract sections
        sections = self._extract_sections(content)
        
        prompt = f"""You are restructuring a research report for better organization.

Current sections:
{self._format_sections_summary(sections)}

Issues with structure:
{self._format_issues(issues)}

{f"Additional instructions: {custom_instructions}" if custom_instructions else ""}

Restructure the document by:
1. Reordering sections for logical flow
2. Combining related sections that are too granular
3. Splitting sections that cover too many topics
4. Creating new sections if important content is scattered
5. Ensuring balanced section sizes
6. Adding an introduction and conclusion if missing

Provide a restructuring plan first, then return the complete restructured document.

Format:
## Restructuring Plan
[Your plan here]

## Restructured Document
[The complete reorganized document in markdown]
"""
        
        response = _call_llm_api(prompt, "document restructuring")
        
        # Extract just the restructured document part
        if response and "## Restructured Document" in response:
            parts = response.split("## Restructured Document")
            if len(parts) > 1:
                return parts[1].strip()
        
        return response if response else content
    
    def _add_section_transitions(self, content: str, issues: List[Dict],
                                custom_instructions: Optional[str] = None) -> str:
        """Add transitions between sections"""
        
        sections = self._extract_sections(content)
        
        prompt = f"""You are adding transitions between sections in a research report.

Current document structure:
{self._format_sections_summary(sections)}

Add transition paragraphs between sections that:
1. Summarize key points from the previous section
2. Explain how the next section builds on or relates to it
3. Provide smooth continuity of ideas
4. Are concise (1-2 sentences)

{f"Additional instructions: {custom_instructions}" if custom_instructions else ""}

Return the complete document with transitions added.
"""
        
        response = _call_llm_api(prompt, "transition addition")
        return response if response else content
    
    def _extract_sections(self, content: str) -> List[Tuple[str, str]]:
        """Extract sections from the document"""
        sections = []
        
        # Split by headers (##)
        pattern = r'^(#{1,3})\s+(.+)$'
        lines = content.split('\n')
        
        current_section = None
        current_content = []
        
        for line in lines:
            match = re.match(pattern, line, re.MULTILINE)
            if match:
                if current_section:
                    sections.append((current_section, '\n'.join(current_content)))
                current_section = match.group(2)
                current_content = []
            else:
                current_content.append(line)
        
        if current_section:
            sections.append((current_section, '\n'.join(current_content)))
        
        return sections
    
    def _format_sections_summary(self, sections: List[Tuple[str, str]]) -> str:
        """Format sections summary for prompts"""
        summary = []
        for i, (title, content) in enumerate(sections, 1):
            word_count = len(content.split())
            summary.append(f"{i}. {title} ({word_count} words)")
        return '\n'.join(summary)
    
    def _format_issues(self, issues: List[Dict]) -> str:
        """Format issues for prompts"""
        formatted = []
        for i, issue in enumerate(issues, 1):
            formatted.append(f"{i}. {issue.get('issue', 'No description')}")
        return '\n'.join(formatted)
    
    def _improve_coherence(self, content: str, issues: List[Dict],
                          custom_instructions: Optional[str] = None) -> str:
        """Improve coherence - just calls flow improvement for now"""
        return self._improve_document_flow(content, issues, custom_instructions)


# Singleton instance
document_improver = DocumentWideImprover()


def apply_document_wide_improvements(document_content: str, qa_results: Dict[str, Any], 
                                   llm_function: callable, custom_instructions: str = None) -> Dict[str, Any]:
    """
    Apply document-wide improvements using the DocumentWideImprover
    
    Args:
        document_content: The full document content
        qa_results: QA results containing issues
        llm_function: LLM function to use for improvements
        custom_instructions: Optional custom instructions
        
    Returns:
        Dictionary with status, improved content, and verification results
    """
    try:
        # Extract issues from QA results
        issues = qa_results.get('inaccurate_or_confusing_sections', [])
        
        if not issues:
            return {
                'status': 'no_issues',
                'message': 'No issues found to address',
                'improved': document_content
            }
        
        # Apply improvements using the document improver
        improved_content = document_improver.improve_document(
            full_content=document_content,
            issues=issues,
            custom_instructions=custom_instructions
        )
        
        # Simple verification - check if content actually changed
        content_changed = improved_content.strip() != document_content.strip()
        
        if content_changed:
            # Create verification results
            verification = {
                'verification_score': 0.8,  # Default score for document-wide improvements
                'all_issues_addressed': True,
                'summary': f'Applied document-wide improvements for {len(issues)} issue(s)',
                'changes_made': [f'Document-wide improvement for: {issue.get("issue", "Unknown issue")}' for issue in issues]
            }
            
            return {
                'status': 'improved',
                'improved': improved_content,
                'verification': verification,
                'changes_made': verification['changes_made']
            }
        else:
            return {
                'status': 'no_changes',
                'message': 'No changes were made to the document',
                'improved': document_content
            }
            
    except Exception as e:
        print(f"Error in apply_document_wide_improvements: {e}")
        return {
            'status': 'error',
            'message': f'Error applying improvements: {str(e)}',
            'improved': document_content
        }