"""
QA Quality Module

Handles QA response parsing, extraction, and improvement pipeline functionality.
"""

import re
import json
import streamlit as st
from datetime import datetime


def parse_qa_response_manually(response_text: str) -> dict:
    """
    Manually parse QA response when JSON parsing fails
    """
    # Initialize result structure
    qa_results = {
        "inaccurate_or_confusing_sections": [],
        "overall_score": 0.7,
        "suggestions": []
    }
    
    try:
        # Look for section issues in the text
        section_patterns = [
            r'[Ss]ection\s+(\d+[:\-\s]?[^:\n]*)',
            r'##\s*([^:\n]+)',
            r'Problem[:\s]+([^\n]+)',
            r'Issue[:\s]+([^\n]+)'
        ]
        
        # Extract issues by looking for patterns
        issues_found = []
        lines = response_text.split('\n')
        current_section = "Analysis"
        current_issue = ""
        current_fix = ""
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Look for section mentions
            for pattern in section_patterns:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    current_section = match.group(1).strip()
                    break
            
            # Look for issue descriptions
            if any(keyword in line.lower() for keyword in ['issue:', 'problem:', 'concern:', 'error:']):
                current_issue = re.sub(r'^[^:]*:', '', line).strip()
            
            # Look for suggestions/fixes
            if any(keyword in line.lower() for keyword in ['fix:', 'suggest:', 'recommend:', 'solution:']):
                current_fix = re.sub(r'^[^:]*:', '', line).strip()
            
            # If we have both issue and fix, create an entry
            if current_issue and current_fix:
                issues_found.append({
                    "section_title": current_section,
                    "issue": current_issue,
                    "suggested_fix": current_fix,
                    "confidence": 0.8
                })
                current_issue = ""
                current_fix = ""
        
        # If no structured issues found, create a general one
        if not issues_found:
            # Extract the main content as a general issue
            content_lines = [line for line in lines if line.strip() and not line.startswith('#')]
            if content_lines:
                main_content = ' '.join(content_lines[:3])  # First 3 non-empty lines
                issues_found.append({
                    "section_title": "General Analysis",
                    "issue": "QA analysis completed - see detailed feedback",
                    "suggested_fix": main_content[:300] + "..." if len(main_content) > 300 else main_content,
                    "confidence": 0.7
                })
        
        qa_results["inaccurate_or_confusing_sections"] = issues_found
        
        # Look for overall score
        score_match = re.search(r'score[:\s]*(\d+\.?\d*)', response_text, re.IGNORECASE)
        if score_match:
            qa_results["overall_score"] = float(score_match.group(1))
            if qa_results["overall_score"] > 1.0:  # If it's out of 10, convert to 0-1
                qa_results["overall_score"] = qa_results["overall_score"] / 10.0
        
        # Extract general suggestions
        suggestion_lines = [line for line in lines if any(word in line.lower() for word in ['recommend', 'suggest', 'consider', 'should'])]
        qa_results["suggestions"] = suggestion_lines[:3]  # Max 3 suggestions
        
    except Exception as e:
        print(f"Manual parsing error: {e}")
        # Absolute fallback
        qa_results = {
            "inaccurate_or_confusing_sections": [
                {
                    "section_title": "Manual Analysis",
                    "issue": "QA analysis completed but formatting needs improvement",
                    "suggested_fix": "Please review the analysis manually as automatic parsing failed",
                    "confidence": 0.6
                }
            ],
            "overall_score": 0.7,
            "suggestions": ["Review QA analysis manually"]
        }
    
    return qa_results


def extract_json_aggressively(response_text: str) -> dict:
    """
    Aggressively extract and reconstruct JSON from malformed responses
    """
    try:
        # Look for individual components in the response
        sections = []
        overall_score = 0.7
        suggestions = []
        
        # Extract sections using multiple patterns
        section_patterns = [
            r'"section_title":\s*"([^"]+)"[,\s]*"issue":\s*"([^"]+)"[,\s]*"suggested_fix":\s*"([^"]+)"',
            r'section_title["\']?\s*:\s*["\']([^"\']+)["\'][,\s]*issue["\']?\s*:\s*["\']([^"\']+)["\'][,\s]*suggested_fix["\']?\s*:\s*["\']([^"\']+)["\']',
        ]
        
        for pattern in section_patterns:
            matches = re.findall(pattern, response_text, re.DOTALL | re.IGNORECASE)
            for match in matches:
                if len(match) >= 3:
                    sections.append({
                        "section_title": match[0].strip(),
                        "issue": match[1].strip(),
                        "suggested_fix": match[2].strip(),
                        "confidence": 0.8
                    })
        
        # Look for overall score
        score_patterns = [
            r'"overall_score":\s*([0-9.]+)',
            r'overall_score["\']?\s*:\s*([0-9.]+)',
            r'score[:\s]*([0-9.]+)'
        ]
        
        for pattern in score_patterns:
            match = re.search(pattern, response_text, re.IGNORECASE)
            if match:
                score = float(match.group(1))
                if score > 1.0:  # Convert from 0-10 to 0-1
                    score = score / 10.0
                overall_score = score
                break
        
        # Look for suggestions
        suggestion_patterns = [
            r'"suggestions":\s*\[(.*?)\]',
            r'suggestions["\']?\s*:\s*\[(.*?)\]'
        ]
        
        for pattern in suggestion_patterns:
            match = re.search(pattern, response_text, re.DOTALL | re.IGNORECASE)
            if match:
                suggestion_text = match.group(1)
                # Extract individual suggestions
                individual_suggestions = re.findall(r'"([^"]+)"', suggestion_text)
                suggestions = individual_suggestions[:3]  # Max 3
                break
        
        # If no structured sections found, try to extract from free text
        if not sections:
            lines = response_text.split('\n')
            current_section = "Analysis"
            current_issue = ""
            current_fix = ""
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Look for section references
                if re.search(r'section\s+\d+', line, re.IGNORECASE):
                    section_match = re.search(r'section\s+(\d+[^:\n]*)', line, re.IGNORECASE)
                    if section_match:
                        current_section = f"Section {section_match.group(1)}"
                
                # Look for issues/problems
                if any(keyword in line.lower() for keyword in ['issue:', 'problem:', 'error:', 'incorrect:']):
                    current_issue = re.sub(r'^[^:]*:\s*', '', line).strip()
                
                # Look for fixes/suggestions
                if any(keyword in line.lower() for keyword in ['fix:', 'suggest:', 'solution:', 'correct:']):
                    current_fix = re.sub(r'^[^:]*:\s*', '', line).strip()
                
                # If we have both, add to sections
                if current_issue and current_fix:
                    sections.append({
                        "section_title": current_section,
                        "issue": current_issue,
                        "suggested_fix": current_fix,
                        "confidence": 0.7
                    })
                    current_issue = ""
                    current_fix = ""
        
        # Construct result
        if sections or suggestions:
            return {
                "inaccurate_or_confusing_sections": sections,
                "overall_score": overall_score,
                "suggestions": suggestions
            }
        else:
            return None
            
    except Exception as e:
        print(f"Aggressive extraction error: {e}")
        return None


def safe_improvement_pipeline_call(search_engine, current_report, issues, sources, query_description):
    """Safely call improvement pipeline with error handling and logging"""
    try:
        # Backup session state before attempting improvement
        if 'manual_improvement_applied' in st.session_state:
            st.session_state._qa_backup = st.session_state.manual_improvement_applied.copy()
        
        # Log the operation
        log_qa_operation("Starting improvement pipeline", f"Issues count: {len(issues)}")
        
        # Create a unique session ID for this QA run
        if 'qa_session_id' not in st.session_state:
            st.session_state.qa_session_id = f"qa_{int(datetime.now().timestamp())}"
        
        # Call the improvement pipeline
        improved_report, improvements_made = search_engine.improve_report_with_issues(
            current_report,
            issues,
            sources,
            query_description
        )
        
        # Log success
        log_qa_operation("Improvement pipeline completed", f"Improvements made: {len(improvements_made)}")
        
        return improved_report, improvements_made
        
    except Exception as e:
        # Log the error
        log_qa_operation("Improvement pipeline failed", error=str(e))
        
        # Try to restore from backup
        if '_qa_backup' in st.session_state and st.session_state._qa_backup:
            st.session_state.manual_improvement_applied = st.session_state._qa_backup.copy()
        
        # Show error to user
        st.error(f"Failed to apply improvements: {str(e)}")
        
        # Return original report and empty improvements
        return current_report, []


def log_qa_operation(operation, details=None, error=None):
    """Log QA operations for debugging"""
    try:
        import time
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] QA Operation: {operation}"
        if details:
            log_entry += f" | Details: {details}"
        if error:
            log_entry += f" | Error: {error}"
        
        # Initialize log if it doesn't exist
        if 'qa_operation_log' not in st.session_state:
            st.session_state.qa_operation_log = []
        
        # Keep only last 50 entries
        st.session_state.qa_operation_log.append(log_entry)
        if len(st.session_state.qa_operation_log) > 50:
            st.session_state.qa_operation_log = st.session_state.qa_operation_log[-50:]
            
        print(log_entry)  # Also print to console
    except Exception as e:
        print(f"Warning: Failed to log QA operation: {e}")