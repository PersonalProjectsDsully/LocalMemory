"""
Report Depth Enhancer - Ensures reports have proper narrative depth

This module specifically addresses the issue of shallow, bullet-point heavy
reports by enforcing narrative prose and minimum depth requirements.
"""

import re
from typing import Dict, List, Tuple, Optional
import logging

logger = logging.getLogger(__name__)

try:
    from .llm_utils import call_llm
except ImportError:
    def call_llm(prompt, context=""):
        return f"[Generated content for: {context}]"


class ReportDepthEnhancer:
    """
    Enhances report sections to ensure proper depth and narrative style
    """
    
    def __init__(self):
        self.min_paragraph_sentences = 4
        self.min_section_paragraphs = 3
        self.bullet_point_patterns = [
            r'^\s*[-•*]\s+',  # Bullet points
            r'^\s*\d+\.\s+',  # Numbered lists
            r'^\s*[a-z]\)\s+', # Letter lists
        ]
    
    def enhance_report_depth(self, report_content: str) -> str:
        """
        Enhance an entire report to ensure proper depth and narrative style
        
        Args:
            report_content: The original report content
            
        Returns:
            Enhanced report with proper depth
        """
        # Split into sections
        sections = self._split_into_sections(report_content)
        
        # Enhance each section
        enhanced_sections = []
        for section in sections:
            enhanced = self._enhance_section(section)
            enhanced_sections.append(enhanced)
        
        # Reassemble report
        return self._reassemble_report(enhanced_sections)
    
    def _enhance_section(self, section: Dict[str, str]) -> Dict[str, str]:
        """Enhance a single section for depth and narrative style"""
        
        content = section.get('content', '')
        
        # Check if section has bullet points
        if self._has_bullet_points(content):
            logger.info(f"Converting bullet points to narrative in section: {section.get('title', 'Unknown')}")
            content = self._convert_bullets_to_narrative(content, section.get('title', ''))
        
        # Check paragraph count and depth
        paragraphs = self._extract_paragraphs(content)
        
        if len(paragraphs) < self.min_section_paragraphs:
            logger.info(f"Expanding section depth: {section.get('title', 'Unknown')}")
            content = self._expand_section_depth(content, section.get('title', ''))
        
        # Check for incomplete sections
        if self._is_section_incomplete(content):
            logger.info(f"Completing incomplete section: {section.get('title', 'Unknown')}")
            content = self._complete_section(content, section.get('title', ''))
        
        section['content'] = content
        return section
    
    def _has_bullet_points(self, content: str) -> bool:
        """Check if content contains bullet points"""
        for pattern in self.bullet_point_patterns:
            if re.search(pattern, content, re.MULTILINE):
                return True
        return False
    
    def _convert_bullets_to_narrative(self, content: str, section_title: str) -> str:
        """Convert bullet points to narrative paragraphs"""
        
        prompt = f"""
Convert the following section from bullet points to flowing narrative prose.

SECTION TITLE: {section_title}

CURRENT CONTENT (with bullets):
{content}

REQUIREMENTS:
1. Transform ALL bullet points into complete, flowing paragraphs
2. Each paragraph should be 4-6 sentences
3. Use transitions between ideas
4. Maintain all the information but present it as a story
5. Add context and explanation to make points clearer
6. NO BULLETS OR LISTS in the output

Example transformation:
BEFORE: "- Python is easy to learn\n- It has simple syntax\n- Great for beginners"
AFTER: "Python stands out as an exceptionally accessible programming language for newcomers to coding. Its syntax closely resembles natural English, making it intuitive for beginners to understand and write. This simplicity doesn't come at the cost of power, as Python remains versatile enough for complex applications. These characteristics have made it the go-to choice for educational institutions teaching programming fundamentals."

Now convert the content to narrative prose:
"""
        
        narrative = call_llm(prompt, f"bullet_to_narrative_{section_title}")
        return narrative
    
    def _expand_section_depth(self, content: str, section_title: str) -> str:
        """Expand a section to have proper depth"""
        
        current_paragraphs = self._extract_paragraphs(content)
        needed_paragraphs = self.min_section_paragraphs - len(current_paragraphs)
        
        prompt = f"""
Expand the following section to have proper depth and detail.

SECTION TITLE: {section_title}

CURRENT CONTENT ({len(current_paragraphs)} paragraphs):
{content}

REQUIREMENTS:
1. Add {needed_paragraphs} more detailed paragraphs
2. Each new paragraph should be 4-6 sentences
3. Expand on existing ideas with:
   - Specific examples
   - Deeper explanation
   - Context and background
   - Implications and connections
4. Maintain narrative flow between paragraphs
5. NO BULLET POINTS - only flowing prose

Topics to explore in the expansion:
- Real-world applications and examples
- Common challenges and how to address them
- Best practices and recommendations
- Connections to related concepts
- Future implications and trends

Write the COMPLETE expanded section:
"""
        
        expanded = call_llm(prompt, f"section_expansion_{section_title}")
        return expanded
    
    def _complete_section(self, content: str, section_title: str) -> str:
        """Complete an incomplete section"""
        
        prompt = f"""
Complete the following section that appears to be cut off or incomplete.

SECTION TITLE: {section_title}

INCOMPLETE CONTENT:
{content}

REQUIREMENTS:
1. Continue from where the content ends
2. Provide a proper conclusion to the section
3. Ensure all ideas are fully developed
4. Add 1-2 concluding paragraphs that:
   - Summarize key points
   - Connect to the broader topic
   - Transition to the next section
5. Maintain the same tone and style
6. NO BULLET POINTS - narrative prose only

Complete the section:
"""
        
        completion = call_llm(prompt, f"section_completion_{section_title}")
        
        # Combine original and completion
        return f"{content}\n\n{completion}"
    
    def transform_findings_to_narrative(self, findings_list: List[str], topic: str) -> str:
        """Transform a list of findings into narrative paragraphs"""
        
        prompt = f"""
Transform these research findings into a cohesive narrative explanation.

TOPIC: {topic}

FINDINGS (as bullet points):
{self._format_findings_list(findings_list)}

REQUIREMENTS:
1. Create 3-4 flowing paragraphs that tell the story of these findings
2. Start with context - why these findings matter
3. Present each finding with explanation and examples
4. Show relationships between findings
5. End with implications and significance
6. Each paragraph should be 4-6 sentences
7. Use transitions like "Furthermore," "Additionally," "This suggests that," etc.
8. NO BULLET POINTS - pure narrative prose

Write the narrative explanation:
"""
        
        narrative = call_llm(prompt, f"findings_narrative_{topic}")
        return narrative
    
    def ensure_learning_path_depth(self, learning_path_content: str) -> str:
        """Specifically enhance learning path sections to avoid restarts"""
        
        prompt = f"""
Enhance this learning path section to be a comprehensive, flowing narrative.

CURRENT CONTENT:
{learning_path_content}

WRITE A COMPLETE LEARNING PATH SECTION WITH:

1. Opening paragraph (4-5 sentences): Explain why a structured learning path matters for AI education, 
   the challenges learners face without guidance, and the benefits of a systematic approach.

2. Philosophy paragraph (4-5 sentences): Describe the pedagogical approach - why certain topics 
   precede others, how foundational concepts build toward advanced applications, and the importance
   of balancing theory with practice.

3. For each learning stage, write a full paragraph (5-6 sentences each) covering:
   - What the learner will study and why it's positioned here
   - Key concepts and skills they'll develop
   - Recommended resources and why they were chosen
   - Expected outcomes and how to measure progress
   - How this stage prepares them for the next

4. Pacing paragraph (4-5 sentences): Discuss realistic timelines, how to adapt based on background,
   when to move forward vs. when to review, and maintaining motivation.

5. Conclusion paragraph (4-5 sentences): Address transitioning to advanced topics, continuing
   education, and joining the AI community.

Target: 600-800 words of engaging, helpful prose with NO BULLETS.
"""
        
        enhanced = call_llm(prompt, "learning_path_enhancement")
        return enhanced
    
    # Helper methods
    
    def _split_into_sections(self, report: str) -> List[Dict[str, str]]:
        """Split report into sections"""
        sections = []
        
        # Split by markdown headers
        parts = re.split(r'^(#{1,3}\s+.+)$', report, flags=re.MULTILINE)
        
        current_title = "Introduction"
        current_content = []
        
        for i, part in enumerate(parts):
            if re.match(r'^#{1,3}\s+', part):
                # This is a header
                if current_content:
                    sections.append({
                        'title': current_title,
                        'content': '\n'.join(current_content).strip()
                    })
                current_title = part.strip('# ').strip()
                current_content = []
            else:
                # This is content
                if part.strip():
                    current_content.append(part)
        
        # Don't forget the last section
        if current_content:
            sections.append({
                'title': current_title,
                'content': '\n'.join(current_content).strip()
            })
        
        return sections
    
    def _reassemble_report(self, sections: List[Dict[str, str]]) -> str:
        """Reassemble sections into complete report"""
        report_parts = []
        
        for section in sections:
            # Add header
            if section['title'] != "Introduction":
                report_parts.append(f"\n## {section['title']}\n")
            
            # Add content
            report_parts.append(section['content'])
        
        return '\n'.join(report_parts)
    
    def _extract_paragraphs(self, content: str) -> List[str]:
        """Extract paragraphs from content"""
        # Split by double newlines
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        
        # Filter out very short paragraphs (likely not real paragraphs)
        real_paragraphs = [p for p in paragraphs if len(p.split('.')) >= 2]
        
        return real_paragraphs
    
    def _is_section_incomplete(self, content: str) -> bool:
        """Check if section appears incomplete"""
        if not content:
            return True
        
        # Check last character
        last_char = content.strip()[-1] if content.strip() else ''
        if last_char not in '.!?"\')}]':
            return True
        
        # Check if very short
        if len(content.split()) < 100:
            return True
        
        # Check if ends mid-sentence
        last_sentence = content.strip().split('.')[-1].strip()
        if len(last_sentence) > 50 and not any(last_sentence.endswith(p) for p in '.!?"\')}]'):
            return True
        
        return False
    
    def _format_findings_list(self, findings: List[str]) -> str:
        """Format findings list for prompt"""
        formatted = []
        for i, finding in enumerate(findings, 1):
            formatted.append(f"- {finding}")
        return '\n'.join(formatted)


# Convenience functions

def enhance_report_depth(report: str) -> str:
    """Enhance report depth using the default enhancer"""
    enhancer = ReportDepthEnhancer()
    return enhancer.enhance_report_depth(report)


def ensure_narrative_style(content: str, topic: str = "Research Findings") -> str:
    """Ensure content uses narrative style instead of bullets"""
    enhancer = ReportDepthEnhancer()
    
    if enhancer._has_bullet_points(content):
        return enhancer._convert_bullets_to_narrative(content, topic)
    
    return content