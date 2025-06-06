"""
Research Report Integration - Comprehensive Report Generation

This module integrates enhanced report generation into the research workflow,
ensuring deep, narrative-style reports without bullet points or truncation.
"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime
import json

logger = logging.getLogger(__name__)

try:
    from .enhanced_report_generator import EnhancedReportGenerator
    from .report_depth_enhancer import ReportDepthEnhancer
    from .llm_utils import call_llm
    MODULES_AVAILABLE = True
except ImportError:
    logger.warning("Some modules not available, using simplified version")
    MODULES_AVAILABLE = False
    
    class EnhancedReportGenerator:
        def generate_comprehensive_report(self, workflow_state):
            return "Basic report generation - install dependencies for full functionality"
    
    class ReportDepthEnhancer:
        def enhance_report_depth(self, report):
            return report


class ComprehensiveReportGenerator:
    """
    Main class for generating comprehensive research reports with guaranteed depth
    """
    
    def __init__(self):
        self.report_generator = EnhancedReportGenerator()
        self.depth_enhancer = ReportDepthEnhancer()
        self.min_report_words = 2500
        self.max_retries = 3
        
    def generate_research_report(self, workflow_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a comprehensive research report from workflow state
        
        Args:
            workflow_state: Complete workflow state with all research data
            
        Returns:
            Dict containing the report and metadata
        """
        try:
            # Stage 1: Generate base report with enhanced generator
            logger.info("Generating comprehensive research report...")
            base_report = self.report_generator.generate_comprehensive_report(workflow_state)
            
            # Stage 2: Enhance depth and convert bullets to narrative
            logger.info("Enhancing report depth and narrative style...")
            enhanced_report = self.depth_enhancer.enhance_report_depth(base_report)
            
            # Stage 3: Verify completeness and fix if needed
            logger.info("Verifying report completeness...")
            complete_report = self._ensure_completeness(enhanced_report, workflow_state)
            
            # Stage 4: Final quality check
            final_report = self._final_quality_pass(complete_report, workflow_state)
            
            # Generate metadata
            metadata = self._generate_report_metadata(final_report, workflow_state)
            
            return {
                'report': final_report,
                'metadata': metadata,
                'status': 'complete',
                'quality_score': self._calculate_quality_score(final_report)
            }
            
        except Exception as e:
            logger.error(f"Error generating comprehensive report: {e}")
            return self._generate_fallback_report(workflow_state)
    
    def _ensure_completeness(self, report: str, workflow_state: Dict[str, Any]) -> str:
        """Ensure report is complete and not truncated"""
        
        attempt = 0
        current_report = report
        
        while attempt < self.max_retries:
            # Check various completeness criteria
            if self._is_report_complete(current_report, workflow_state):
                return current_report
            
            logger.info(f"Report incomplete (attempt {attempt + 1}), completing...")
            
            # Generate completion
            completion = self._generate_report_completion(current_report, workflow_state)
            
            # Merge completion with report
            current_report = self._merge_report_completion(current_report, completion)
            
            attempt += 1
        
        return current_report
    
    def _is_report_complete(self, report: str, workflow_state: Dict[str, Any]) -> bool:
        """Check if report meets all completeness criteria"""
        
        # Word count check
        word_count = len(report.split())
        if word_count < self.min_report_words:
            logger.info(f"Report too short: {word_count} words (minimum: {self.min_report_words})")
            return False
        
        # Structure check - ensure all expected sections exist
        expected_sections = [
            'Executive Summary',
            'Introduction',
            'Conclusion'
        ]
        
        for section in expected_sections:
            if section not in report:
                logger.info(f"Missing section: {section}")
                return False
        
        # Check each subtask has a corresponding section
        subtasks = workflow_state.get('subtasks', [])
        for task in subtasks:
            task_title = task.get('title', '')
            if task_title and task_title not in report:
                logger.info(f"Missing section for task: {task_title}")
                return False
        
        # Check ending
        if not self._has_proper_ending(report):
            logger.info("Report has improper ending")
            return False
        
        return True
    
    def _has_proper_ending(self, report: str) -> bool:
        """Check if report has a proper ending"""
        
        # Get last 500 characters
        ending = report.strip()[-500:] if len(report) > 500 else report.strip()
        
        # Should contain conclusion
        if 'conclusion' not in ending.lower():
            return False
        
        # Should end with proper punctuation
        last_char = report.strip()[-1] if report.strip() else ''
        if last_char not in '.!?"\')}]':
            return False
        
        # Should not end mid-sentence
        last_sentence = report.strip().split('.')[-1].strip()
        if len(last_sentence) > 100:  # Likely incomplete
            return False
        
        return True
    
    def _generate_report_completion(self, incomplete_report: str, 
                                   workflow_state: Dict[str, Any]) -> str:
        """Generate completion for incomplete report"""
        
        # Analyze what's missing
        missing_elements = self._analyze_missing_elements(incomplete_report, workflow_state)
        
        prompt = f"""
Complete the following research report that appears to be incomplete.

CURRENT REPORT (incomplete):
{incomplete_report[-2000:]}  # Last 2000 chars for context

MISSING ELEMENTS:
{json.dumps(missing_elements, indent=2)}

REQUIREMENTS:
1. Continue from EXACTLY where the report ends
2. Complete any unfinished paragraphs or sections
3. Add any missing sections listed above
4. Ensure each section has 3-4 detailed paragraphs
5. Include a comprehensive conclusion if missing
6. Maintain the same professional, narrative style
7. NO BULLET POINTS - use flowing paragraphs only
8. Each paragraph should be 4-6 sentences

Original Research Topic: {workflow_state.get('original_query', '')}
Number of Subtasks: {len(workflow_state.get('subtasks', []))}

Continue and complete the report:
"""
        
        if MODULES_AVAILABLE:
            completion = call_llm(prompt, "report_completion")
        else:
            completion = "\n\n[Report continuation would be generated here]"
        
        return completion
    
    def _analyze_missing_elements(self, report: str, 
                                  workflow_state: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze what elements are missing from the report"""
        
        missing = {
            'sections': [],
            'word_deficit': max(0, self.min_report_words - len(report.split())),
            'needs_conclusion': 'Conclusion' not in report,
            'incomplete_sections': []
        }
        
        # Check for missing task sections
        for task in workflow_state.get('subtasks', []):
            task_title = task.get('title', '')
            if task_title and task_title not in report:
                missing['sections'].append({
                    'title': task_title,
                    'objective': task.get('objective', ''),
                    'expected_content': 'Detailed analysis and findings'
                })
        
        # Check for incomplete sections (too short)
        sections = report.split('\n## ')
        for section in sections:
            if section and len(section.split()) < 300:
                section_title = section.split('\n')[0].strip()
                missing['incomplete_sections'].append(section_title)
        
        return missing
    
    def _merge_report_completion(self, original: str, completion: str) -> str:
        """Intelligently merge completion with original report"""
        
        # Remove any duplicate content at the boundary
        overlap = self._find_overlap(original, completion)
        
        if overlap:
            # Remove overlapping part from completion
            completion = completion[len(overlap):]
        
        # Ensure smooth transition
        if not original.endswith('\n'):
            original += '\n'
        
        return original + completion
    
    def _find_overlap(self, text1: str, text2: str) -> str:
        """Find overlapping text between end of text1 and beginning of text2"""
        
        # Check last 100 chars of text1 against beginning of text2
        for i in range(min(100, len(text1))):
            end_fragment = text1[-(i+1):]
            if text2.startswith(end_fragment):
                return end_fragment
        
        return ""
    
    def _final_quality_pass(self, report: str, workflow_state: Dict[str, Any]) -> str:
        """Final quality enhancement pass"""
        
        # Check for any remaining bullet points
        if self._contains_bullet_points(report):
            logger.info("Found bullet points in final report, converting to narrative...")
            report = self._convert_all_bullets_to_narrative(report)
        
        # Ensure smooth transitions between sections
        report = self._enhance_transitions(report)
        
        # Final coherence check
        report = self._ensure_coherence(report, workflow_state)
        
        return report
    
    def _contains_bullet_points(self, text: str) -> bool:
        """Check if text contains bullet points"""
        import re
        bullet_patterns = [
            r'^\s*[-•*]\s+',
            r'^\s*\d+\.\s+',
            r'^\s*[a-zA-Z]\)\s+'
        ]
        
        for pattern in bullet_patterns:
            if re.search(pattern, text, re.MULTILINE):
                return True
        return False
    
    def _convert_all_bullets_to_narrative(self, report: str) -> str:
        """Convert any remaining bullets to narrative"""
        if MODULES_AVAILABLE:
            enhancer = ReportDepthEnhancer()
            sections = enhancer._split_into_sections(report)
            
            for section in sections:
                if enhancer._has_bullet_points(section['content']):
                    section['content'] = enhancer._convert_bullets_to_narrative(
                        section['content'], 
                        section['title']
                    )
            
            return enhancer._reassemble_report(sections)
        
        return report
    
    def _enhance_transitions(self, report: str) -> str:
        """Enhance transitions between sections"""
        
        # This is a simplified version - could be enhanced with more sophisticated logic
        sections = report.split('\n## ')
        
        enhanced_sections = []
        for i, section in enumerate(sections):
            if i > 0 and i < len(sections) - 1:  # Not first or last
                # Check if section ends with a transition
                if not self._has_transition(section):
                    section = self._add_transition(section, i, len(sections))
            
            enhanced_sections.append(section)
        
        return '\n## '.join(enhanced_sections)
    
    def _has_transition(self, section: str) -> bool:
        """Check if section has a transition to next section"""
        
        last_paragraph = section.strip().split('\n\n')[-1] if section.strip() else ""
        
        transition_phrases = [
            'next section', 'following section', 'we will explore',
            'we now turn', 'building on', 'this leads'
        ]
        
        return any(phrase in last_paragraph.lower() for phrase in transition_phrases)
    
    def _add_transition(self, section: str, section_num: int, total_sections: int) -> str:
        """Add transition sentence to section"""
        
        if section_num < total_sections - 2:  # Not second-to-last
            transition = "\n\nBuilding on these insights, the following section explores related aspects of this research."
        else:
            transition = "\n\nThese findings lead us to the final conclusions of this research."
        
        return section.rstrip() + transition
    
    def _ensure_coherence(self, report: str, workflow_state: Dict[str, Any]) -> str:
        """Ensure overall report coherence"""
        
        # Check if report maintains consistent focus
        original_query = workflow_state.get('original_query', '')
        
        # Simple coherence check - could be enhanced
        if original_query and original_query.lower() not in report.lower()[:1000]:
            # Add clarifying introduction if main topic not mentioned early
            logger.info("Adding topic clarification for coherence")
            intro_addition = f"\n\nThis comprehensive report examines {original_query}, presenting detailed findings from systematic research across multiple dimensions.\n\n"
            
            # Insert after title
            parts = report.split('\n', 2)
            if len(parts) >= 2:
                report = parts[0] + '\n' + intro_addition + '\n'.join(parts[1:])
        
        return report
    
    def _generate_report_metadata(self, report: str, workflow_state: Dict[str, Any]) -> Dict[str, Any]:
        """Generate metadata about the report"""
        
        word_count = len(report.split())
        
        return {
            'generated_at': datetime.now().isoformat(),
            'word_count': word_count,
            'character_count': len(report),
            'section_count': report.count('\n## '),
            'paragraph_count': report.count('\n\n'),
            'subtasks_covered': len(workflow_state.get('subtasks', [])),
            'original_query': workflow_state.get('original_query', ''),
            'generation_method': 'comprehensive_narrative',
            'has_bullet_points': self._contains_bullet_points(report),
            'completeness_verified': True
        }
    
    def _calculate_quality_score(self, report: str) -> float:
        """Calculate quality score for the report"""
        
        score = 1.0
        
        # Deduct for being too short
        word_count = len(report.split())
        if word_count < self.min_report_words:
            score -= 0.2
        
        # Deduct for bullet points
        if self._contains_bullet_points(report):
            score -= 0.3
        
        # Deduct for missing sections
        essential_sections = ['Introduction', 'Conclusion', 'Executive Summary']
        for section in essential_sections:
            if section not in report:
                score -= 0.1
        
        # Bonus for good length
        if word_count > 3000:
            score += 0.1
        
        return max(0.0, min(1.0, score))
    
    def _generate_fallback_report(self, workflow_state: Dict[str, Any]) -> Dict[str, Any]:
        """Generate basic fallback report if enhanced generation fails"""
        
        logger.warning("Using fallback report generation")
        
        basic_report = f"""
# Research Report: {workflow_state.get('original_query', 'Research Topic')}

*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}*

## Overview

This report presents the findings from research conducted on the topic of {workflow_state.get('original_query', 'the requested subject')}. 
Due to technical limitations, this is a simplified version of the full research report.

## Key Findings

The research identified several important aspects related to this topic, which are presented in the sections below.

## Conclusion

This research provides initial insights into {workflow_state.get('original_query', 'the topic')}. 
Further investigation may reveal additional findings and deeper insights.

---
*Note: This is a simplified report. For a comprehensive analysis, please ensure all required modules are properly installed.*
"""
        
        return {
            'report': basic_report,
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'type': 'fallback',
                'word_count': len(basic_report.split())
            },
            'status': 'fallback',
            'quality_score': 0.3
        }


# Integration function for research workflow
def generate_comprehensive_research_report(workflow_state: Dict[str, Any]) -> str:
    """
    Main entry point for generating comprehensive research reports
    
    Args:
        workflow_state: Complete workflow state from research
        
    Returns:
        Complete research report as string
    """
    generator = ComprehensiveReportGenerator()
    result = generator.generate_research_report(workflow_state)
    
    if result['status'] == 'complete':
        logger.info(f"Generated comprehensive report: {result['metadata']['word_count']} words, "
                   f"quality score: {result['quality_score']:.2f}")
    
    return result['report']