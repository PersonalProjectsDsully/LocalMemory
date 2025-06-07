"""
Report generation functionality for research workflow
"""

import json
from typing import Dict, List, Any
from datetime import datetime

from ..llm.robust_json_parser import parse_llm_json
from ..qa.automatic_qa_system import automatic_qa_system


class ReportGenerator:
    """Handles report generation from research findings"""
    
    def __init__(self, llm_provider, workflow_state, persistence):
        self.llm_provider = llm_provider
        self.workflow_state = workflow_state
        self.persistence = persistence
    
    def step5_report_generation(self, all_tasks_verified: Dict) -> str:
        """Generate comprehensive markdown report from validated research"""
        # Handle parsing errors or missing fields
        if all_tasks_verified.get('parse_error') or 'all_complete' not in all_tasks_verified:
            print("Warning: Failed to parse task verification. Proceeding with report generation.")
            all_tasks_verified = self._calculate_fallback_verification()
        
        # Check if we have sufficient findings to generate a report
        if not all_tasks_verified.get('all_complete', False):
            self._handle_incomplete_tasks(all_tasks_verified)
        
        # Create report outline
        outline = self._create_report_outline()
        
        # Generate each section
        report_sections = self._generate_report_sections(outline)
        
        # Combine sections into final report
        final_report = self._combine_report_sections(report_sections, outline)
        
        # Run automatic QA and improvements
        print("🔍 Running automatic QA and improvements...")
        improved_report_result = self._run_automatic_qa_and_improvements(final_report)
        
        if improved_report_result and improved_report_result.get('ready_for_user'):
            final_report = improved_report_result['improved_report']
            # Store QA information
            qa_summary = improved_report_result.get('qa_summary', {})
            if qa_summary:
                self.workflow_state['automatic_qa_results'] = qa_summary
                improvements_count = len(qa_summary.get('improvements_applied', []))
                print(f"✅ Automatic QA completed with {improvements_count} improvements")
            else:
                print("⚠️ Automatic QA completed but no summary available")
        else:
            print("⚠️ Automatic QA failed, using original report")
            self.workflow_state['automatic_qa_results'] = {
                'automatic_qa_completed': False,
                'error': 'Automatic QA process failed',
                'timestamp': datetime.now().isoformat()
            }
        
        # Save and return final report
        self.workflow_state['final_report'] = final_report
        self.persistence.save_workflow_state(self.workflow_state)
        return final_report
    
    def _calculate_fallback_verification(self) -> Dict:
        """Calculate fallback verification based on available data"""
        total_tasks = len(self.workflow_state.get('subtasks', []))
        tasks_with_findings = sum(
            1 for scratchpad in self.workflow_state.get('scratchpads', {}).values()
            if len(scratchpad.get('high_value_findings', [])) > 0
        )
        
        return {
            'all_complete': tasks_with_findings >= total_tasks * 0.5,
            'overall_completeness': int((tasks_with_findings / total_tasks * 100) if total_tasks > 0 else 0),
            'ready_for_report': True,
            'note': 'Verification parse failed - using fallback completion check'
        }
    
    def _handle_incomplete_tasks(self, all_tasks_verified: Dict):
        """Handle incomplete tasks before report generation"""
        # Save verification report
        if self.persistence.current_session_dir:
            self.persistence._save_json(
                self.persistence.current_session_dir / "final_verification_failed.json",
                all_tasks_verified
            )
        
        # Check if we have partial findings worth reporting
        total_findings = sum(
            len(scratchpad.get('high_value_findings', [])) + 
            len(scratchpad.get('insights', []))
            for scratchpad in self.workflow_state.get('scratchpads', {}).values()
        )
        
        print(f"Total findings across all tasks: {total_findings}")
        
        # Add a note about incompleteness to the report
        if total_findings >= 10 or all_tasks_verified.get('overall_completeness', 0) >= 50:
            print("Generating report with partial findings...")
            self.workflow_state['report_note'] = (
                f"Note: This report is based on partial findings. "
                f"Overall completeness: {all_tasks_verified.get('overall_completeness', 0)}%"
            )
        else:
            print("Generating report despite incomplete tasks...")
            self.workflow_state['report_note'] = (
                "Note: This report is based on limited findings from incomplete research."
            )
    
    def _create_report_outline(self) -> Dict[str, Any]:
        """Create detailed outline for the report"""
        research_summary = self._summarize_research()
        
        outline_prompt = f"""
        Create a detailed outline for a comprehensive research report based on:
        
        Research Summary: {json.dumps(research_summary, indent=2)}
        
        The outline should include:
        1. Executive Summary
        2. Main sections covering all subtasks
        3. Logical flow and organization
        4. Subsections for detailed topics
        
        Format as JSON:
        {{
            "title": "...",
            "executive_summary": {{
                "purpose": "...",
                "key_points": ["..."]
            }},
            "sections": [
                {{
                    "id": "section_1",
                    "title": "...",
                    "purpose": "...",
                    "subsections": [
                        {{
                            "title": "...",
                            "content_points": ["..."]
                        }}
                    ],
                    "sources": ["subtask_id"]
                }}
            ],
            "conclusion": {{
                "summary_points": ["..."],
                "recommendations": ["..."]
            }}
        }}
        """
        
        return parse_llm_json(self.llm_provider.generate(outline_prompt))
    
    def _generate_report_sections(self, outline: Dict) -> Dict[str, str]:
        """Generate each section of the report"""
        sections = {}
        previous_sections = []
        
        # Handle missing or malformed outline
        if not outline or 'sections' not in outline:
            print("Warning: Outline missing sections. Creating default report structure.")
            return self._generate_default_sections()
        
        # Generate executive summary from outline
        if 'executive_summary' in outline:
            sections['executive_summary'] = self._generate_executive_summary(outline['executive_summary'])
        
        # Generate main sections
        for section in outline.get('sections', []):
            section_content = self._generate_section(section, previous_sections)
            sections[section['id']] = section_content
            previous_sections.append({
                'title': section['title'],
                'summary': self._summarize_section(section_content)
            })
        
        # Generate conclusion
        if 'conclusion' in outline:
            sections['conclusion'] = self._generate_conclusion(outline['conclusion'], previous_sections)
        
        return sections
    
    def _generate_executive_summary(self, exec_summary_data: Dict) -> str:
        """Generate executive summary section"""
        exec_summary_prompt = f"""
        Write the Executive Summary section for the research report.
        
        Key Points: {json.dumps(exec_summary_data.get('key_points', []), indent=2)}
        Main Findings: {json.dumps(exec_summary_data.get('main_findings', []), indent=2)}
        
        Research Context: {self.workflow_state.get('clarified_request', '')}
        
        Format as markdown section. Start with "## Executive Summary".
        Keep it concise but comprehensive.
        """
        return self.llm_provider.generate(exec_summary_prompt)
    
    def _generate_section(self, section: Dict, previous_sections: List[Dict]) -> str:
        """Generate a single report section"""
        section_prompt = f"""
        Write the markdown section "{section['title']}" for the research report.
        
        Section Purpose: {section['purpose']}
        Content Points: {json.dumps(section.get('subsections', []), indent=2)}
        
        Research Data: {self._get_section_research_data(section['sources'])}
        
        Previous Sections Context: {self._summarize_previous_sections(previous_sections)}
        
        Requirements:
        - Use clear markdown formatting
        - Include relevant examples and data from research
        - Maintain logical flow with previous sections
        - Be comprehensive yet concise
        - Use appropriate headers (##, ###)
        
        Write the complete section in markdown:
        """
        
        return self.llm_provider.generate(section_prompt)
    
    def _generate_conclusion(self, conclusion_data: Dict, previous_sections: List[Dict]) -> str:
        """Generate conclusion section"""
        conclusion_prompt = f"""
        Write the Conclusion section for the research report.
        
        Summary Points: {json.dumps(conclusion_data.get('summary_points', []), indent=2)}
        Recommendations: {json.dumps(conclusion_data.get('recommendations', []), indent=2)}
        
        Research Context: {self.workflow_state.get('clarified_request', '')}
        Previous Sections: {json.dumps([s['title'] for s in previous_sections], indent=2)}
        
        Format as markdown section. Start with "## Conclusion".
        Synthesize the key findings and provide actionable recommendations.
        """
        return self.llm_provider.generate(conclusion_prompt)
    
    def _generate_default_sections(self) -> Dict[str, str]:
        """Generate default report sections when outline parsing fails"""
        sections = {}
        
        # Collect all findings
        all_findings_by_task = {}
        all_insights_by_task = {}
        
        for subtask in self.workflow_state.get('subtasks', []):
            task_id = subtask['id']
            scratchpad = self.workflow_state.get('scratchpads', {}).get(task_id, {})
            doc_analysis = self.workflow_state.get('document_analysis', {}).get(task_id, {})
            
            findings = list(scratchpad.get('high_value_findings', []))
            insights = list(scratchpad.get('insights', []))
            
            # Add findings from document analysis if needed
            if not findings and doc_analysis:
                if 'key_information' in doc_analysis:
                    findings.extend(doc_analysis.get('key_information', []))
                if 'document_analyses' in doc_analysis:
                    for doc in doc_analysis['document_analyses']:
                        findings.extend(doc.get('key_information', []))
                        insights.extend(doc.get('insights', []))
            
            all_findings_by_task[task_id] = findings
            all_insights_by_task[task_id] = insights
        
        # Generate executive summary
        sections['executive_summary'] = self._create_default_executive_summary(all_findings_by_task)
        
        # Generate sections for each subtask
        for subtask in self.workflow_state.get('subtasks', []):
            task_id = subtask['id']
            if task_id in all_findings_by_task and all_findings_by_task[task_id]:
                sections[task_id] = self._create_task_section(
                    subtask, all_findings_by_task[task_id], all_insights_by_task.get(task_id, [])
                )
        
        # Generate conclusion
        sections['conclusion'] = self._create_default_conclusion(all_insights_by_task)
        
        return sections
    
    def _create_default_executive_summary(self, all_findings_by_task: Dict) -> str:
        """Create default executive summary"""
        key_findings = self._extract_key_findings()[:5]  # Top 5 findings
        
        if key_findings:
            exec_summary = f"""## Executive Summary

This comprehensive report presents the findings from our research on: {self.workflow_state.get('clarified_request', 'the requested topic')}.

**Key Takeaways:**
"""
            for i, finding in enumerate(key_findings, 1):
                exec_summary += f"{i}. {finding}\n"
            
            return exec_summary
        else:
            return f"""## Executive Summary

This report summarizes our research findings on: {self.workflow_state.get('clarified_request', 'the requested topic')}.

The research has been conducted based on available knowledge and documentation."""
    
    def _create_task_section(self, subtask: Dict, findings: List[str], insights: List[str]) -> str:
        """Create a section for a specific task"""
        section_content = f"""## {subtask.get('title', f'Section {subtask["id"]}')}

{subtask.get('objective', 'This section presents findings from the research.')}

### Key Findings

"""
        # Add findings for this task
        for finding in findings[:5]:  # Limit to 5 findings per section
            section_content += f"- {finding}\n"
        
        # Add insights if available
        if insights:
            section_content += "\n### Insights\n\n"
            for insight in insights[:3]:
                section_content += f"- {insight}\n"
        
        return section_content
    
    def _create_default_conclusion(self, all_insights_by_task: Dict) -> str:
        """Create default conclusion"""
        all_insights = []
        for task_insights in all_insights_by_task.values():
            all_insights.extend(task_insights)
        
        if all_insights:
            conclusion = """## Conclusion

Based on the research conducted, we have identified the following key insights:

"""
            # Add up to 5 unique insights
            unique_insights = []
            for insight in all_insights:
                if insight not in unique_insights:
                    unique_insights.append(insight)
                if len(unique_insights) >= 5:
                    break
            
            for insight in unique_insights:
                conclusion += f"- {insight}\n"
            
            conclusion += f"\n### Next Steps\nBased on these findings, we recommend further investigation into specific areas relevant to your use case."
            return conclusion
        else:
            return f"""## Conclusion

This research has examined: {self.workflow_state.get('clarified_request', 'the requested topic')}.

The findings presented in this report provide a foundation for informed decision-making. We recommend evaluating these insights against your specific requirements and constraints."""
    
    def _combine_report_sections(self, sections: Dict[str, str], outline: Dict) -> str:
        """Combine report sections into final markdown report"""
        report_parts = []
        
        # Title
        default_title = f"Research Report: {self.workflow_state.get('clarified_request', 'Research Analysis')[:50]}"
        title = default_title
        if outline and isinstance(outline, dict):
            title = outline.get('title', default_title)
        
        report_parts.append(f"# {title}")
        report_parts.append("")
        
        # Add any notes about report completeness
        if 'report_note' in self.workflow_state:
            report_parts.append(f"*{self.workflow_state.get('report_note', '')}*")
            report_parts.append("")
        
        # Executive Summary
        if 'executive_summary' in sections:
            content = sections['executive_summary']
            if not content.strip().startswith('## Executive Summary'):
                report_parts.append("## Executive Summary")
            report_parts.append(content)
            report_parts.append("")
        
        # Add each section in order
        ordered_sections = []
        
        # First add task-based sections in order
        for subtask in self.workflow_state.get('subtasks', []):
            task_id = subtask['id']
            if task_id in sections:
                ordered_sections.append((task_id, sections[task_id]))
        
        # Then add any other sections
        for section_key, section_content in sections.items():
            if section_key not in ['executive_summary', 'conclusion'] and not any(s[0] == section_key for s in ordered_sections):
                ordered_sections.append((section_key, section_content))
        
        # Add ordered sections
        for section_key, section_content in ordered_sections:
            if not section_content.strip().startswith('##'):
                section_title = section_key.replace('_', ' ').replace('task ', 'Task ').title()
                report_parts.append(f"## {section_title}")
            report_parts.append(section_content)
            report_parts.append("")
        
        # Add conclusion
        if 'conclusion' in sections:
            report_parts.append(sections['conclusion'])
            report_parts.append("")
        
        # Metadata
        report_parts.append("---")
        report_parts.append(f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        total_findings = self._count_total_findings()
        report_parts.append(f"*Total findings analyzed: {total_findings}*")
        
        return "\n".join(report_parts)
    
    def _run_automatic_qa_and_improvements(self, report: str) -> Optional[Dict[str, Any]]:
        """Run automatic QA and improvements on the generated report"""
        try:
            # Get necessary data for QA
            original_query = self.workflow_state.get('original_query', 
                                                   self.workflow_state.get('clarified_request', ''))
            subtasks = self.workflow_state.get('subtasks', [])
            scratchpads = self.workflow_state.get('scratchpads', {})
            
            # Run automatic QA
            return automatic_qa_system.run_automatic_qa(
                report=report,
                original_query=original_query,
                subtasks=subtasks,
                scratchpads=scratchpads
            )
            
        except Exception as e:
            print(f"Error in automatic QA: {e}")
            return None
    
    # Helper methods
    def _summarize_research(self) -> Dict[str, Any]:
        """Summarize all research findings"""
        return {
            'request': self.workflow_state.get('clarified_request'),
            'subtasks': self.workflow_state.get('subtasks', []),
            'key_findings': self._extract_key_findings(),
            'total_documents_analyzed': self._count_analyzed_documents()
        }
    
    def _extract_key_findings(self) -> List[str]:
        """Extract key findings from all scratchpads and document analysis"""
        findings = []
        
        # Get from scratchpads
        for scratchpad in self.workflow_state['scratchpads'].values():
            findings.extend(scratchpad.get('high_value_findings', []))
            findings.extend(scratchpad.get('insights', []))
        
        # Also get from document analysis if scratchpads are empty
        if len(findings) < 5:
            for analysis in self.workflow_state.get('document_analysis', {}).values():
                if isinstance(analysis, dict):
                    if 'key_information' in analysis:
                        findings.extend(analysis.get('key_information', []))
                    if 'insights' in analysis:
                        findings.extend(analysis.get('insights', []))
                    if 'document_analyses' in analysis:
                        for doc in analysis['document_analyses']:
                            findings.extend(doc.get('key_information', []))
                            findings.extend(doc.get('insights', []))
        
        # Remove duplicates while preserving order
        seen = set()
        unique_findings = []
        for finding in findings:
            if finding not in seen:
                seen.add(finding)
                unique_findings.append(finding)
        
        return unique_findings[:20]  # Top 20 unique findings
    
    def _count_total_findings(self) -> int:
        """Count total unique findings without truncation"""
        findings = set()  # Use set to avoid double counting
        
        # Get from scratchpads
        for scratchpad in self.workflow_state['scratchpads'].values():
            findings.update(scratchpad.get('high_value_findings', []))
            findings.update(scratchpad.get('insights', []))
        
        # Also get from document analysis
        for analysis in self.workflow_state.get('document_analysis', {}).values():
            if isinstance(analysis, dict):
                if 'key_information' in analysis:
                    findings.update(analysis.get('key_information', []))
                if 'insights' in analysis:
                    findings.update(analysis.get('insights', []))
                if 'document_analyses' in analysis:
                    for doc in analysis['document_analyses']:
                        findings.update(doc.get('key_information', []))
                        findings.update(doc.get('insights', []))
        
        return len(findings)
    
    def _count_analyzed_documents(self) -> int:
        """Count total documents analyzed"""
        count = 0
        for analysis in self.workflow_state['document_analysis'].values():
            if 'document_analyses' in analysis:
                count += len(analysis['document_analyses'])
        return count
    
    def _get_section_research_data(self, source_ids: List[str]) -> str:
        """Get research data for specific subtasks"""
        data = []
        for task_id in source_ids:
            if task_id in self.workflow_state['scratchpads']:
                data.append(f"Research for {task_id}:")
                data.append(json.dumps(self.workflow_state['scratchpads'][task_id], indent=2))
        return '\n'.join(data)
    
    def _summarize_previous_sections(self, sections: List[Dict]) -> str:
        """Summarize previous sections for context"""
        if not sections:
            return "This is the first section."
        
        summaries = []
        for section in sections[-3:]:  # Last 3 sections
            summaries.append(f"- {section['title']}: {section['summary']}")
        
        return '\n'.join(summaries)
    
    def _summarize_section(self, content: str) -> str:
        """Create brief summary of a section"""
        # Take first 200 characters as simple summary
        return content[:200].replace('\n', ' ') + '...'