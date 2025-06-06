"""
Enhanced Report Generator for Research Workflow

This module provides comprehensive report generation with proper depth,
narrative style, and completion guarantees.
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

try:
    from .llm_utils import call_llm
except ImportError:
    # Fallback for testing
    def call_llm(prompt, context=""):
        return f"[Generated content for: {context}]"


class EnhancedReportGenerator:
    """
    Generates comprehensive, narrative-style research reports with
    proper depth and structure.
    """
    
    def __init__(self):
        self.min_section_words = 300
        self.min_paragraph_words = 100
        self.max_generation_attempts = 3
        
    def generate_comprehensive_report(self, workflow_state: Dict[str, Any]) -> str:
        """
        Generate a comprehensive research report with proper depth and narrative flow.
        
        Args:
            workflow_state: Complete workflow state with research findings
            
        Returns:
            Complete, well-structured research report
        """
        try:
            # Stage 1: Generate detailed outline
            outline = self._generate_detailed_outline(workflow_state)
            
            # Stage 2: Generate executive summary
            executive_summary = self._generate_executive_summary(workflow_state)
            
            # Stage 3: Generate introduction with context
            introduction = self._generate_introduction(workflow_state)
            
            # Stage 4: Generate each main section with depth
            main_sections = []
            for section_data in outline['sections']:
                section_content = self._generate_detailed_section(
                    section_data, 
                    workflow_state,
                    previous_sections=main_sections
                )
                
                # Ensure section has proper depth
                section_content = self._ensure_section_depth(
                    section_content, 
                    section_data,
                    workflow_state
                )
                
                main_sections.append(section_content)
            
            # Stage 5: Generate synthesis section
            synthesis = self._generate_synthesis(main_sections, workflow_state)
            
            # Stage 6: Generate conclusion
            conclusion = self._generate_conclusion(workflow_state, main_sections)
            
            # Stage 7: Assemble and polish report
            full_report = self._assemble_report({
                'executive_summary': executive_summary,
                'introduction': introduction,
                'main_sections': main_sections,
                'synthesis': synthesis,
                'conclusion': conclusion
            })
            
            # Stage 8: Ensure completeness
            full_report = self._ensure_report_completeness(full_report, workflow_state)
            
            return full_report
            
        except Exception as e:
            logger.error(f"Error generating comprehensive report: {e}")
            return self._generate_fallback_report(workflow_state)
    
    def _generate_detailed_outline(self, workflow_state: Dict[str, Any]) -> Dict:
        """Generate a detailed outline for the report"""
        
        subtasks = workflow_state.get('subtasks', [])
        
        prompt = f"""
Create a DETAILED outline for a comprehensive research report.

Research Topic: {workflow_state.get('original_query', 'Unknown')}
Number of Research Tasks: {len(subtasks)}

For each subtask completed, we need a major section in the report.

Subtasks:
{self._format_subtasks_for_outline(subtasks)}

Create an outline that includes:
1. Executive Summary (overview of all findings)
2. Introduction (context, scope, methodology)
3. Main Sections (one for each subtask, with subsections as needed)
4. Synthesis (connecting all findings)
5. Conclusion (key takeaways and next steps)

For each main section, specify:
- Section title
- Key topics to cover (3-4 topics)
- Estimated word count (minimum 400 words)
- Connection to other sections

Return a structured outline in JSON format.
"""
        
        outline_json = call_llm(prompt, "report_outline_generation")
        
        try:
            # Parse JSON outline
            return json.loads(outline_json)
        except:
            # Fallback outline structure
            return self._create_default_outline(workflow_state)
    
    def _generate_executive_summary(self, workflow_state: Dict[str, Any]) -> str:
        """Generate a comprehensive executive summary"""
        
        prompt = f"""
Write a COMPREHENSIVE EXECUTIVE SUMMARY for this research report.

CRITICAL REQUIREMENTS:
- Write 2-3 full paragraphs (250-350 words total)
- NO BULLET POINTS - use flowing narrative prose
- Synthesize the most important findings across all research
- Highlight key insights and their implications
- Set the stage for the detailed report that follows

Research Topic: {workflow_state.get('original_query', '')}

Key Findings Summary:
{self._summarize_key_findings(workflow_state)}

Write the executive summary now (remember: narrative paragraphs, no bullets):
"""
        
        summary = call_llm(prompt, "executive_summary_generation")
        
        # Verify depth
        if len(summary.split()) < 200:
            summary = self._expand_content(summary, "executive summary", 250)
        
        return summary
    
    def _generate_introduction(self, workflow_state: Dict[str, Any]) -> str:
        """Generate a detailed introduction"""
        
        prompt = f"""
Write a DETAILED INTRODUCTION for this research report.

REQUIREMENTS:
- Write 3-4 full paragraphs (400-500 words total)
- First paragraph: Introduce the topic and its importance
- Second paragraph: Explain the research scope and approach
- Third paragraph: Describe the methodology and structure
- Fourth paragraph: Preview key findings and report organization
- Use smooth transitions between paragraphs
- NO BULLET POINTS - narrative prose only

Research Context:
Topic: {workflow_state.get('original_query', '')}
Clarified Request: {workflow_state.get('clarified_request', '')}
Number of Research Tasks: {len(workflow_state.get('subtasks', []))}

Write the introduction now:
"""
        
        introduction = call_llm(prompt, "introduction_generation")
        
        # Ensure proper depth
        if len(introduction.split()) < 350:
            introduction = self._expand_content(introduction, "introduction", 400)
        
        return introduction
    
    def _generate_detailed_section(self, section_data: Dict, 
                                  workflow_state: Dict,
                                  previous_sections: List[str]) -> str:
        """Generate a detailed section with proper depth"""
        
        # Extract relevant findings for this section
        section_findings = self._extract_section_findings(
            section_data, 
            workflow_state
        )
        
        # Build context from previous sections
        context_summary = self._summarize_previous_sections(previous_sections)
        
        prompt = f"""
Write a DETAILED section for the research report.

SECTION TITLE: {section_data.get('title', 'Research Findings')}

CRITICAL REQUIREMENTS:
- Write 4-5 full paragraphs (500-700 words total)
- Start with a strong topic paragraph introducing this section
- Present findings as a flowing narrative, NOT bullet points
- Include specific examples and evidence from the research
- Use transitions between paragraphs for smooth flow
- Connect to previous sections where relevant
- End with a bridge to the next topic

Research Findings for This Section:
{section_findings}

Context from Previous Sections:
{context_summary}

Key Topics to Cover:
{json.dumps(section_data.get('topics', []), indent=2)}

Write the complete section now (remember: full paragraphs, no bullets):
"""
        
        section = call_llm(prompt, f"section_generation_{section_data.get('title', 'unknown')}")
        
        return section
    
    def _ensure_section_depth(self, content: str, section_data: Dict, 
                            workflow_state: Dict) -> str:
        """Ensure section has proper depth and completeness"""
        
        word_count = len(content.split())
        
        if word_count < self.min_section_words:
            logger.info(f"Section too short ({word_count} words), expanding...")
            
            expansion_prompt = f"""
The following section is too brief and needs expansion.

CURRENT SECTION ({word_count} words):
{content}

REQUIREMENTS:
- Expand this to at least {self.min_section_words} words
- Add more specific examples and details
- Elaborate on key points with evidence
- Include implications and analysis
- Maintain narrative flow (no bullets)
- DO NOT repeat existing content, ADD new insights

Additional context to incorporate:
{self._get_expansion_context(section_data, workflow_state)}

Write the EXPANDED section:
"""
            
            expanded = call_llm(expansion_prompt, "section_expansion")
            
            # Combine original and expansion
            return f"{content}\n\n{expanded}"
        
        return content
    
    def _generate_synthesis(self, main_sections: List[str], 
                           workflow_state: Dict) -> str:
        """Generate synthesis section connecting all findings"""
        
        prompt = f"""
Write a SYNTHESIS section that connects all research findings.

REQUIREMENTS:
- Write 3-4 paragraphs (400-500 words)
- Identify patterns and connections across different findings
- Highlight surprising insights or contradictions
- Discuss the bigger picture implications
- Show how different aspects relate to each other
- NO BULLET POINTS - use narrative prose

Research Topic: {workflow_state.get('original_query', '')}
Number of Main Sections: {len(main_sections)}

Key Themes to Synthesize:
{self._extract_key_themes(main_sections)}

Write the synthesis section now:
"""
        
        synthesis = call_llm(prompt, "synthesis_generation")
        
        # Ensure depth
        if len(synthesis.split()) < 350:
            synthesis = self._expand_content(synthesis, "synthesis", 400)
        
        return synthesis
    
    def _generate_conclusion(self, workflow_state: Dict, 
                           main_sections: List[str]) -> str:
        """Generate comprehensive conclusion"""
        
        prompt = f"""
Write a COMPREHENSIVE CONCLUSION for this research report.

REQUIREMENTS:
- Write 2-3 full paragraphs (300-400 words)
- First paragraph: Summarize key findings and insights
- Second paragraph: Discuss practical implications and applications
- Third paragraph: Suggest next steps and future directions
- End on a forward-looking note
- NO BULLET POINTS - narrative prose only

Research Topic: {workflow_state.get('original_query', '')}

Key Takeaways to Emphasize:
{self._extract_key_takeaways(workflow_state, main_sections)}

Write the conclusion now:
"""
        
        conclusion = call_llm(prompt, "conclusion_generation")
        
        # Ensure proper length
        if len(conclusion.split()) < 250:
            conclusion = self._expand_content(conclusion, "conclusion", 300)
        
        return conclusion
    
    def _assemble_report(self, components: Dict[str, Any]) -> str:
        """Assemble all components into a cohesive report"""
        
        report_parts = [
            "# Comprehensive Research Report",
            f"\n*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n",
            "## Executive Summary\n",
            components['executive_summary'],
            "\n## Introduction\n",
            components['introduction']
        ]
        
        # Add main sections
        for i, section in enumerate(components['main_sections'], 1):
            report_parts.extend([
                f"\n## Section {i}: {self._extract_section_title(section)}\n",
                section
            ])
        
        # Add synthesis and conclusion
        report_parts.extend([
            "\n## Synthesis and Integration\n",
            components['synthesis'],
            "\n## Conclusion\n",
            components['conclusion']
        ])
        
        return "\n".join(report_parts)
    
    def _ensure_report_completeness(self, report: str, 
                                   workflow_state: Dict) -> str:
        """Ensure report is complete and not cut off"""
        
        # Check for incompleteness indicators
        if self._is_report_incomplete(report):
            logger.info("Report appears incomplete, completing...")
            
            for attempt in range(self.max_generation_attempts):
                completion_prompt = f"""
The following report appears to be incomplete and needs completion.

CURRENT REPORT:
{report}

REQUIREMENTS:
1. Continue from EXACTLY where the text ends
2. Complete any unfinished sections
3. Ensure all sections have proper conclusions
4. Add any missing sections based on the outline
5. DO NOT restart or repeat existing content
6. Maintain the same writing style and depth

Continue and complete the report:
"""
                
                completion = call_llm(completion_prompt, f"report_completion_attempt_{attempt}")
                
                # Append completion
                report = f"{report}\n\n{completion}"
                
                # Check if now complete
                if not self._is_report_incomplete(report):
                    break
        
        return report
    
    def _is_report_incomplete(self, report: str) -> bool:
        """Check if report appears incomplete"""
        
        if not report or len(report.strip()) < 1000:
            return True
        
        stripped = report.strip()
        
        # Check for incomplete endings
        incomplete_indicators = [
            stripped.endswith(','),
            stripped.endswith('and'),
            stripped.endswith('the'),
            stripped.endswith(':'),
            stripped.endswith('-'),
            not stripped.endswith(('.', '!', '?', '"', ')')),
            'Conclusion' not in report,
            len(report.split('\n\n')) < 10  # Too few sections
        ]
        
        return any(incomplete_indicators)
    
    def _expand_content(self, content: str, content_type: str, 
                       target_words: int) -> str:
        """Expand content to meet word count requirements"""
        
        current_words = len(content.split())
        
        prompt = f"""
Expand the following {content_type} to approximately {target_words} words.

CURRENT CONTENT ({current_words} words):
{content}

REQUIREMENTS:
- Add depth and detail, don't just add fluff
- Include more specific examples
- Elaborate on important points
- Add analysis and implications
- Maintain the original message and flow
- Write in narrative paragraphs, no bullets

Write the expanded version:
"""
        
        return call_llm(prompt, f"{content_type}_expansion")
    
    # Helper methods
    def _format_subtasks_for_outline(self, subtasks: List[Dict]) -> str:
        """Format subtasks for outline generation"""
        formatted = []
        for i, task in enumerate(subtasks, 1):
            formatted.append(
                f"{i}. {task.get('title', 'Unknown')}: "
                f"{task.get('objective', 'No objective specified')}"
            )
        return "\n".join(formatted)
    
    def _summarize_key_findings(self, workflow_state: Dict) -> str:
        """Summarize key findings from all research"""
        # Implementation depends on your workflow state structure
        findings = []
        
        for task_id, analysis in workflow_state.get('document_analysis', {}).items():
            if 'key_findings' in analysis:
                findings.extend(analysis['key_findings'][:3])
        
        return "\n".join(findings[:10])  # Top 10 findings
    
    def _extract_section_findings(self, section_data: Dict, 
                                 workflow_state: Dict) -> str:
        """Extract findings relevant to a specific section"""
        # Implementation depends on how sections map to tasks
        task_id = section_data.get('task_id', '')
        
        if task_id in workflow_state.get('document_analysis', {}):
            analysis = workflow_state['document_analysis'][task_id]
            return json.dumps(analysis, indent=2)
        
        return "No specific findings available for this section"
    
    def _summarize_previous_sections(self, previous_sections: List[str]) -> str:
        """Create a brief summary of previous sections for context"""
        if not previous_sections:
            return "This is the first main section of the report."
        
        # Take first paragraph of each previous section
        summaries = []
        for section in previous_sections[-2:]:  # Last 2 sections
            first_para = section.split('\n\n')[0] if section else ""
            if first_para:
                summaries.append(first_para[:200] + "...")
        
        return " Previous sections discussed: " + " ".join(summaries)
    
    def _get_expansion_context(self, section_data: Dict, 
                              workflow_state: Dict) -> str:
        """Get additional context for section expansion"""
        # Extract relevant scratchpad data
        task_id = section_data.get('task_id', '')
        scratchpad = workflow_state.get('scratchpads', {}).get(task_id, {})
        
        return f"""
Task Objective: {section_data.get('objective', 'Unknown')}
Key Topics: {', '.join(section_data.get('topics', []))}
Additional Findings: {json.dumps(scratchpad.get('insights', [])[:3])}
"""
    
    def _extract_key_themes(self, main_sections: List[str]) -> str:
        """Extract key themes from main sections"""
        # Simple extraction - could be enhanced with NLP
        themes = []
        for section in main_sections:
            # Extract section headings or key phrases
            lines = section.split('\n')
            for line in lines[:5]:  # Check first few lines
                if len(line) > 20 and len(line) < 100:
                    themes.append(line.strip())
        
        return "\n".join(themes[:10])
    
    def _extract_key_takeaways(self, workflow_state: Dict, 
                               main_sections: List[str]) -> str:
        """Extract key takeaways for conclusion"""
        takeaways = []
        
        # From workflow state
        if 'final_insights' in workflow_state:
            takeaways.extend(workflow_state['final_insights'][:5])
        
        # From sections (look for conclusion-like statements)
        for section in main_sections:
            paragraphs = section.split('\n\n')
            if paragraphs:
                # Last paragraph often contains conclusions
                takeaways.append(paragraphs[-1][:150] + "...")
        
        return "\n".join(takeaways[:8])
    
    def _extract_section_title(self, section_content: str) -> str:
        """Extract title from section content"""
        lines = section_content.split('\n')
        for line in lines:
            if line.strip() and len(line) < 100:
                return line.strip()
        return "Research Findings"
    
    def _create_default_outline(self, workflow_state: Dict) -> Dict:
        """Create a default outline structure"""
        subtasks = workflow_state.get('subtasks', [])
        
        sections = []
        for i, task in enumerate(subtasks):
            sections.append({
                'title': task.get('title', f'Finding {i+1}'),
                'task_id': task.get('id', f'task_{i+1}'),
                'topics': [
                    'Overview and context',
                    'Key findings and insights',
                    'Implications and applications',
                    'Connections to other findings'
                ],
                'min_words': 500
            })
        
        return {
            'sections': sections,
            'total_sections': len(sections)
        }
    
    def _generate_fallback_report(self, workflow_state: Dict) -> str:
        """Generate a basic report if enhanced generation fails"""
        logger.warning("Falling back to basic report generation")
        
        report_parts = [
            f"# Research Report: {workflow_state.get('original_query', 'Unknown Topic')}",
            f"\n*Generated on: {datetime.now().strftime('%Y-%m-%d')}*\n",
            "## Overview\n",
            f"This report presents findings from research on: {workflow_state.get('original_query', 'the requested topic')}.\n",
            "## Research Findings\n"
        ]
        
        # Add basic task summaries
        for i, task in enumerate(workflow_state.get('subtasks', []), 1):
            report_parts.append(f"\n### {i}. {task.get('title', 'Finding')}\n")
            report_parts.append(f"{task.get('objective', 'No description available.')}\n")
        
        report_parts.append("\n## Conclusion\n")
        report_parts.append("This research provides initial insights into the topic. Further investigation may reveal additional findings.\n")
        
        return "\n".join(report_parts)


def create_enhanced_report_generator() -> EnhancedReportGenerator:
    """Factory function to create report generator"""
    return EnhancedReportGenerator()