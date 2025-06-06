import streamlit as st
import json
from datetime import datetime
from pathlib import Path
import pandas as pd
import time
from utils.intelligent_search_enhanced import EnhancedIntelligentSearchEngine
from utils.batch_intelligence_processor import process_existing_content
from utils.session_state_manager import initialize_session_state
from utils.settings_manager import settings_manager
try:
    from utils.research_workflow import ResearchWorkflow, WorkflowOrchestrator
except ImportError as e:
    st.error(f"Import error: {e}")
    st.error("Please restart the Streamlit app to reload the modules.")
    st.stop()
from utils.workflow_persistence import workflow_persistence
from utils.workflow_tracker import workflow_tracker
from utils.progress_reporter import ProgressReporter, set_progress_reporter
from utils.llm_utils import call_llm

st.set_page_config(
    page_title="Intelligent Search - Personal Knowledge Base",
    page_icon="🧠",
    layout="wide"
)

def _is_report_incomplete(report_text: str) -> bool:
    """Detect if a report is incomplete based on various indicators"""
    if not report_text or len(report_text.strip()) < 500:
        # print(f"DEBUG: Report too short: {len(report_text.strip()) if report_text else 0} chars")
        return True
    
    stripped_text = report_text.strip()
    last_50_chars = stripped_text[-50:]
    # print(f"DEBUG: Last 50 chars: '{last_50_chars}'")
    
    # Check for incomplete sentences or abrupt endings
    incomplete_indicators = [
        # Incomplete sentences
        stripped_text.endswith('('),
        stripped_text.endswith(','),
        stripped_text.endswith('and'),
        stripped_text.endswith('or'),
        stripped_text.endswith('the'),
        stripped_text.endswith('to'),
        stripped_text.endswith('for'),
        stripped_text.endswith('with'),
        stripped_text.endswith('in'),
        stripped_text.endswith('on'),
        stripped_text.endswith('at'),
        stripped_text.endswith('by'),
        stripped_text.endswith('—'),  # Em dash
        stripped_text.endswith('-'),  # Regular dash
        stripped_text.endswith('–'),  # En dash
        stripped_text.endswith(':'),  # Colon without content after
        
        # Check for incomplete sentences ending with specific patterns
        stripped_text.endswith('monitoring'),  # Likely part of incomplete sentence
        stripped_text.endswith('testing'),
        stripped_text.endswith('allows'),
        stripped_text.endswith('of'),
        stripped_text.endswith('from'),
        
        # Check if last sentence doesn't end with proper punctuation
        not stripped_text.endswith(('.', '!', '?', '"', "'", ')', ']', '}')),
        
        # Incomplete sections
        "Step-by-Step Guide" in report_text and not report_text.count("##") >= 4,
        "Implementation" in report_text and len(report_text.split("Implementation")[-1]) < 500,
        
        # Incomplete table (starts table but doesn't finish it)
        report_text.count('|') > 0 and stripped_text.endswith(('|', '—', '-', '–')),
        
        # Table header without body
        "Factor" in report_text and "Comments" in report_text and report_text.count('\n') - report_text.rfind("Comments") < 5,
        
        # Missing conclusion
        not any(conclusion in report_text.lower() for conclusion in ["conclusion", "summary", "next steps", "recommendations"]),
        
        # Very short for a comprehensive report
        len(stripped_text) < 2000,
    ]
    
    # Debug each indicator
    indicator_names = [
        "ends with '('", "ends with ','", "ends with 'and'", "ends with 'or'", "ends with 'the'",
        "ends with 'to'", "ends with 'for'", "ends with 'with'", "ends with 'in'", "ends with 'on'",
        "ends with 'at'", "ends with 'by'", "ends with '—'", "ends with '-'", "ends with '–'", "ends with ':'",
        "ends with 'monitoring'", "ends with 'testing'", "ends with 'allows'", "ends with 'of'", "ends with 'from'",
        "missing proper punctuation",
        "incomplete step guide", "incomplete implementation", "incomplete table", "incomplete table header",
        "missing conclusion", "too short overall"
    ]
    
    triggered_indicators = []
    for i, indicator in enumerate(incomplete_indicators):
        if indicator:
            triggered_indicators.append(indicator_names[i])
            # print(f"DEBUG: Triggered indicator: {indicator_names[i]}")
    
    result = any(incomplete_indicators)
    # print(f"DEBUG: Overall incomplete result: {result}")
    # print(f"DEBUG: Triggered indicators: {triggered_indicators}")
    
    return result

def _complete_incomplete_report(partial_report: str, workflow_orchestrator=None, workflow_state_data=None) -> str:
    """Complete an incomplete report by calling the LLM to continue generation"""
    try:
        from utils.llm_utils import call_llm
        
        print(f"DEBUG: Starting report completion. Original length: {len(partial_report)}")
        
        # Extract context about where the report left off
        last_lines = partial_report.strip().split('\n')[-10:]  # Last 10 lines for context
        context = '\n'.join(last_lines)
        
        # Get research data for context - support both orchestrator and direct state data
        if workflow_orchestrator and hasattr(workflow_orchestrator, 'workflow') and hasattr(workflow_orchestrator.workflow, 'workflow_state'):
            scratchpads = workflow_orchestrator.workflow.workflow_state.get('scratchpads', {})
            subtasks = workflow_orchestrator.workflow.workflow_state.get('subtasks', [])
        elif workflow_state_data:
            scratchpads = workflow_state_data.get('scratchpads', {})
            subtasks = workflow_state_data.get('subtasks', [])
        else:
            print("DEBUG: No workflow data available, using minimal context")
            scratchpads = {}
            subtasks = []
        
        # Create a summarized context of available research
        research_context = []
        for task in subtasks:
            task_id = task['id']
            if task_id in scratchpads:
                findings = scratchpads[task_id].get('high_value_findings', [])
                if findings:
                    research_context.append(f"**{task['title']}:**")
                    research_context.extend([f"- {finding}" for finding in findings[:3]])
        
        research_summary = '\n'.join(research_context[:20])  # Limit context size
        
        completion_prompt = f"""The following research report appears to be incomplete. Please continue and complete it based on the available research data.

CURRENT REPORT (ending incomplete):
{partial_report}

AVAILABLE RESEARCH DATA:
{research_summary}

INSTRUCTIONS:
1. Continue from exactly where the report left off
2. Complete any unfinished sentences or sections
3. Add missing sections if needed (especially conclusion/recommendations)
4. Ensure the report flows naturally from the existing content
5. Keep the same style and formatting as the existing report
6. Make it comprehensive but focused
7. End with a proper conclusion and next steps

Please continue the report from where it left off:"""

        # Call the LLM to complete the report
        completion = call_llm(completion_prompt, "report completion")
        
        if completion:
            # Find where to splice the completion
            # Look for the last complete sentence or section
            lines = partial_report.strip().split('\n')
            
            # Find the last line that ends properly
            splice_point = len(lines)
            for i in range(len(lines) - 1, -1, -1):
                line = lines[i].strip()
                if line and (line.endswith('.') or line.endswith(':') or line.startswith('#')):
                    splice_point = i + 1
                    break
            
            # Combine the complete part with the new completion
            if splice_point < len(lines):
                complete_part = '\n'.join(lines[:splice_point])
                completed_report = complete_part + '\n\n' + completion.strip()
            else:
                completed_report = partial_report + '\n\n' + completion.strip()
            
            print(f"DEBUG: Report completed. New length: {len(completed_report)}")
            return completed_report
        else:
            print("DEBUG: No completion received from LLM")
        
    except Exception as e:
        print(f"Error completing report: {e}")
        import traceback
        traceback.print_exc()
        return None
    
    return None

def parse_qa_response_manually(response_text: str) -> dict:
    """
    Manually parse QA response when JSON parsing fails
    """
    import re
    
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
    import re
    import json
    
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

st.title("🧠 Intelligent Search")
st.markdown("Advanced AI-powered search with comprehensive research workflow")

# Initialize components
try:
    from utils.enhanced_search_thesaurus import EnhancedIntelligentSearchEngine as ThesaurusSearchEngine
    search_engine = ThesaurusSearchEngine(use_cache=True, cache_size=10000)
    print("Using thesaurus-enhanced search engine with synonym expansion")
except ImportError:
    try:
        from utils.intelligent_search_refined import get_refined_search_engine
        search_engine = get_refined_search_engine()
        print("Using refined search engine with improved scoring and intent handling")
    except ImportError:
        from utils.intelligent_search_enhanced import EnhancedIntelligentSearchEngine
        search_engine = EnhancedIntelligentSearchEngine()
        print("Using standard enhanced search engine")

workflow_orchestrator = WorkflowOrchestrator()

# Initialize session state
initialize_session_state()

# Get settings
settings = settings_manager.load_settings()

# Initialize page-specific session state
if 'search_history' not in st.session_state:
    st.session_state.search_history = []
if 'current_results' not in st.session_state:
    st.session_state.current_results = None
if 'show_analysis' not in st.session_state:
    st.session_state.show_analysis = False
if 'workflow_mode' not in st.session_state:
    st.session_state.workflow_mode = False
if 'workflow_state' not in st.session_state:
    st.session_state.workflow_state = None
if 'clarification_responses' not in st.session_state:
    st.session_state.clarification_responses = {}
if 'prefill_task' not in st.session_state:
    st.session_state.prefill_task = None
if 'prefill_task_used' not in st.session_state:
    st.session_state.prefill_task_used = False
if 'qa_session_id' not in st.session_state:
    st.session_state.qa_session_id = None

# Helper function for managing QA improvements session state
def update_improvement_session_state(original_report, improved_report, improvements_made, fix_type='general', fix_details=None):
    """
    Helper function to safely update improvement session state
    """
    if 'manual_improvement_applied' not in st.session_state:
        # First improvement - initialize with truly original report
        st.session_state.manual_improvement_applied = {
            'original_report': original_report,
            'improved_report': improved_report,
            'improvements_made': improvements_made,
            'individual_fixes': [],
            'layer_fixes': [],
            'timestamp': datetime.now()
        }
    else:
        # Subsequent improvements - preserve original report, update improved version
        st.session_state.manual_improvement_applied['improved_report'] = improved_report
        st.session_state.manual_improvement_applied['improvements_made'].extend(improvements_made)
        
        # Ensure arrays exist
        if 'individual_fixes' not in st.session_state.manual_improvement_applied:
            st.session_state.manual_improvement_applied['individual_fixes'] = []
        if 'layer_fixes' not in st.session_state.manual_improvement_applied:
            st.session_state.manual_improvement_applied['layer_fixes'] = []
    
    # Add specific fix details based on type
    if fix_type == 'individual' and fix_details:
        st.session_state.manual_improvement_applied['individual_fixes'].append(fix_details)
    elif fix_type == 'layer' and fix_details:
        st.session_state.manual_improvement_applied['layer_fixes'].append(fix_details)

def get_unique_key(base_key):
    """Generate unique widget key using QA session ID"""
    session_id = st.session_state.get('qa_session_id', 'default')
    return f"{base_key}_{session_id}"

def backup_session_state():
    """Create a backup of current session state for error recovery"""
    try:
        if 'manual_improvement_applied' in st.session_state:
            st.session_state._qa_backup = st.session_state.manual_improvement_applied.copy()
        return True
    except Exception as e:
        print(f"Warning: Failed to backup session state: {e}")
        return False

def restore_session_state():
    """Restore session state from backup"""
    try:
        if '_qa_backup' in st.session_state and st.session_state._qa_backup:
            st.session_state.manual_improvement_applied = st.session_state._qa_backup.copy()
            return True
        return False
    except Exception as e:
        print(f"Warning: Failed to restore session state: {e}")
        return False

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

def safe_improvement_pipeline_call(search_engine, current_report, issues, sources, query_description):
    """Safely call improvement pipeline with error handling and logging"""
    try:
        # Backup session state before attempting improvement
        backup_session_state()
        
        # Log the operation
        log_qa_operation("improvement_pipeline_call", f"Issues: {len(issues)}, Query: {query_description[:50]}...")
        
        # Verify improvement pipeline is available
        if not hasattr(search_engine, 'improvement_pipeline') or search_engine.improvement_pipeline is None:
            raise Exception("Improvement pipeline is not available")
        
        # Call the improvement pipeline
        improved_report, improvements_made = search_engine.improvement_pipeline._apply_fixes(
            current_report, 
            issues,
            sources,
            query_description
        )
        
        # Log success
        log_qa_operation("improvement_pipeline_success", f"Changes made: {improved_report != current_report}")
        
        return improved_report, improvements_made, None
        
    except Exception as e:
        error_msg = str(e)
        log_qa_operation("improvement_pipeline_error", error=error_msg)
        
        # Attempt to restore session state on error
        restore_session_state()
        
        return current_report, [], error_msg

# Sidebar for options
with st.sidebar:
    st.header("Search Options")
    
    # Mode selection
    search_mode = st.radio(
        "Search Mode",
        ["Quick Search", "Research Workflow"],
        help="Quick Search: Fast results\nResearch Workflow: Comprehensive multi-step research"
    )
    
    st.session_state.workflow_mode = (search_mode == "Research Workflow")
    
    if not st.session_state.workflow_mode:
        # Quick search options
        search_depth = st.select_slider(
            "Search Depth",
            options=["Shallow", "Moderate", "Deep"],
            value="Moderate",
            help="Deeper searches analyze more content but take longer"
        )
        
        show_query_analysis = st.checkbox(
            "Show Query Analysis",
            value=st.session_state.show_analysis,
            help="Display how your query was interpreted"
        )
        st.session_state.show_analysis = show_query_analysis
        
        # QA and improvement settings
        st.subheader("Quality Assurance")
        
        enable_qa = st.checkbox(
            "Enable QA Improvement",
            value=st.session_state.get('enable_qa_improvement', True),
            help="Automatically analyze and improve generated reports"
        )
        st.session_state.enable_qa_improvement = enable_qa
        
        if enable_qa:
            qa_config = st.selectbox(
                "QA Configuration",
                options=["basic", "comprehensive", "trust_focused", "suggest_only"],
                index=1,  # Default to comprehensive
                help="Basic: Fast accuracy check\nComprehensive: Full analysis\nTrust-focused: Enhanced trust scoring\nSuggest only: No auto-fixes"
            )
            st.session_state.qa_config = qa_config
            
            # Configure the search engine's QA system
            search_engine.configure_qa_system(qa_config)
        
        st.divider()
        
        # Thesaurus settings
        st.subheader("🔤 Synonym Expansion")
        
        use_thesaurus = st.checkbox(
            "Enable Thesaurus Expansion",
            value=st.session_state.get('use_thesaurus', True),
            help="Automatically expand your search with synonyms from Moby Thesaurus"
        )
        st.session_state.use_thesaurus = use_thesaurus
        
        if use_thesaurus:
            col1, col2 = st.columns(2)
            with col1:
                expansion_weight = st.slider(
                    "Expansion Weight",
                    min_value=0.0,
                    max_value=1.0,
                    value=st.session_state.get('expansion_weight', 0.7),
                    step=0.1,
                    help="How much to weight synonym-based results (0=ignore, 1=equal weight)"
                )
                st.session_state.expansion_weight = expansion_weight
            
            with col2:
                max_synonyms = st.number_input(
                    "Max Synonyms per Word",
                    min_value=1,
                    max_value=10,
                    value=st.session_state.get('max_synonyms', 3),
                    help="Maximum number of synonyms to use for each word"
                )
                st.session_state.max_synonyms = max_synonyms
            
            # Check thesaurus health
            if hasattr(search_engine, 'health_check'):
                health = search_engine.health_check()
                if health.get('thesaurus_health', {}).get('initialized'):
                    st.success(f"✅ Thesaurus loaded: {health['thesaurus_health'].get('total_words', 0):,} words")
                else:
                    st.warning("⚠️ Thesaurus not fully initialized - synonym expansion may be limited")
        
        st.divider()
        
        # Batch processing section
        st.header("Content Enhancement")
        if st.button("🚀 Process All Content", type="secondary"):
            with st.spinner("Processing all documents..."):
                stats = process_existing_content()
                st.success(f"Processed {stats['processed']} documents!")
                st.json(stats)
    else:
        # Research workflow options
        st.info("Research Workflow will guide you through a comprehensive research process")
        
        # Previous sessions
        st.divider()
        st.subheader("Previous Research Sessions")
        sessions = workflow_persistence.list_sessions()
        if sessions:
            session_names = [f"{s['created_at'][:10]} - {s['original_query'][:50]}..." for s in sessions[:5]]
            selected_session = st.selectbox("Load previous session:", ["Select a session..."] + session_names)
            
            if selected_session and selected_session != "Select a session..." and st.button("Load Session"):
                # Load the selected session
                session_idx = session_names.index(selected_session)
                session = sessions[session_idx]
                loaded_state = workflow_persistence.load_workflow_state(session['session_dir'])
                
                if loaded_state:
                    # Store session info for orchestrator restoration
                    st.session_state.research_workflow = {
                        'session_dir': session['session_dir'],
                        'loaded_state': loaded_state
                    }
                    # Restore workflow state
                    workflow_orchestrator.workflow.workflow_state = loaded_state
                    workflow_persistence.set_current_session(session['session_dir'])
                    
                    # Restore tracking data if available
                    if 'tracking_data' in loaded_state:
                        workflow_tracker.restore_tracking_data(loaded_state['tracking_data'])
                    else:
                        # Generate estimated tracking data from loaded state
                        scratchpads = loaded_state.get('scratchpads', {})
                        document_analysis = loaded_state.get('document_analysis', {})
                        
                        # Estimate operations based on content
                        estimated_llm_calls = sum(len(sp.get('high_value_findings', [])) + len(sp.get('insights', [])) for sp in scratchpads.values())
                        estimated_operations = len(scratchpads) + len(document_analysis)
                        
                        # Ensure workflow_tracking is initialized before restoring
                        workflow_tracker._ensure_initialized()
                        
                        # Restore basic tracking
                        st.session_state.workflow_tracking['operation_counts'] = {
                            'llm_generation': estimated_llm_calls // 2,
                            'llm_response': estimated_llm_calls // 2,
                            'document_search': len(document_analysis),
                            'validation_iteration': sum(sp.get('iteration_count', 1) for sp in scratchpads.values())
                        }
                        st.session_state.workflow_tracking['total_llm_calls'] = estimated_llm_calls
                    
                    # Determine current stage from loaded state
                    if loaded_state.get('final_report'):
                        # Check if workflow is marked as completed
                        is_completed = loaded_state.get('report_completed', False) or loaded_state.get('force_completed', False)
                        stage = 'complete' if is_completed else 'report_generation'
                        
                        workflow_orchestrator.current_stage = 'report_generation' if not is_completed else 'complete'
                        
                        # Ensure workflow_orchestrator has the loaded state for QA access
                        if hasattr(workflow_orchestrator, 'workflow') and hasattr(workflow_orchestrator.workflow, 'workflow_state'):
                            workflow_orchestrator.workflow.workflow_state.update(loaded_state)
                        
                        st.session_state.workflow_state = {
                            'stage': stage,
                            'data': {
                                'report': loaded_state['final_report'],
                                'metadata': {
                                    'generated_at': session.get('last_updated', datetime.now().isoformat()),
                                    'subtasks_completed': len(loaded_state.get('subtasks', [])),
                                    'documents_analyzed': len(loaded_state.get('document_analysis', {}))
                                },
                                'forced_complete': loaded_state.get('force_completed', False)
                            },
                            'loaded_state': loaded_state  # Include loaded state for future operations
                        }
                    elif loaded_state.get('document_analysis'):
                        workflow_orchestrator.current_stage = 'document_research'
                        # Reconstruct research results from loaded state
                        research_results = []
                        subtasks = loaded_state.get('subtasks', [])
                        scratchpads = loaded_state.get('scratchpads', {})
                        document_analysis = loaded_state.get('document_analysis', {})
                        
                        for subtask in subtasks:
                            subtask_id = subtask['id']
                            # Get the scratchpad for this subtask
                            scratchpad = scratchpads.get(subtask_id, {})
                            
                            # Create validation structure based on scratchpad contents
                            validation = {
                                'sufficient': len(scratchpad.get('high_value_findings', [])) > 0 or len(scratchpad.get('insights', [])) > 0,
                                'completeness_score': min(100, len(scratchpad.get('high_value_findings', [])) * 10 + len(scratchpad.get('insights', [])) * 5),
                                'total_findings': len(scratchpad.get('high_value_findings', [])) + len(scratchpad.get('insights', [])),
                                'missing_elements': []
                            }
                            
                            # Try to load saved task verification if it exists
                            # Construct proper path - session_dir already includes research_workspace
                            workspace_path = Path(session['session_dir'])
                            verification_file = workspace_path / '06_task_verifications' / f'{subtask_id}_verification.json'
                            
                            if verification_file.exists():
                                try:
                                    with open(verification_file, 'r', encoding='utf-8') as f:
                                        verification_data = json.load(f)
                                        if 'verification' in verification_data:
                                            validation['completion_verified'] = verification_data['verification'].get('verified', False)
                                            validation['completion_details'] = verification_data['verification']
                                except Exception as e:
                                    print(f"Error loading verification for {subtask_id}: {e}")
                            
                            # Create research structure
                            research = {
                                'documents_found': len(scratchpad.get('documents_analyzed', [])),
                                'analysis': document_analysis.get(subtask_id, {})
                            }
                            
                            research_results.append({
                                'subtask': subtask,
                                'research': research,
                                'validation': validation
                            })
                        
                        st.session_state.workflow_state = {
                            'stage': 'document_research',
                            'data': research_results,
                            'scratchpads': scratchpads,  # Include scratchpads in workflow state
                            'document_analysis': document_analysis,  # Include document analysis
                            'loaded_state': loaded_state  # Keep full loaded state for reference
                        }
                    elif loaded_state.get('subtasks'):
                        workflow_orchestrator.current_stage = 'task_decomposition'
                        # Reconstruct task decomposition state
                        decomposition = {
                            'subtasks': loaded_state.get('subtasks', [])
                        }
                        
                        # Create a basic verification structure
                        verification = {
                            'approved': True,  # Assume approved since we have subtasks
                            'completeness_score': 100,
                            'gaps': [],
                            'suggestions': []
                        }
                        
                        st.session_state.workflow_state = {
                            'stage': 'task_decomposition',
                            'data': {
                                'decomposition': decomposition,
                                'verification': verification
                            }
                        }
                    
                    st.success(f"Loaded session: {session['original_query'][:50]}...")
                    st.rerun()
        
        if st.session_state.workflow_state:
            st.divider()
            st.subheader("Workflow Progress")
            current_stage = st.session_state.workflow_state.get('stage', 'Not started')
            st.metric("Current Stage", current_stage.replace('_', ' ').title())
            
            # Add workflow tracking display
            with st.expander("📊 Workflow Tracking & Monitoring", expanded=True):
                workflow_tracker.display_status()
                
                # Export tracking data button
                col1, col2, col3 = st.columns([2, 1, 1])
                with col2:
                    if st.button("🔄 Reset Tracking"):
                        workflow_tracker.reset_tracking()
                        st.success("Tracking data reset")
                        st.rerun()
                with col3:
                    if st.button("📥 Export Tracking"):
                        tracking_data = workflow_tracker.export_tracking_data()
                        st.download_button(
                            "Download JSON",
                            tracking_data,
                            f"workflow_tracking_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                            mime="application/json"
                        )
            
            # Show progress
            stages = ['inquiry_clarification', 'task_decomposition', 'document_research', 'report_generation']
            current_idx = stages.index(workflow_orchestrator.current_stage) if workflow_orchestrator.current_stage in stages else 0
            progress = (current_idx + 1) / len(stages)
            st.progress(progress)
            
            # Show workspace location
            if workflow_persistence.current_session_dir:
                st.caption(f"📁 Workspace: {workflow_persistence.current_session_dir}")
    
    # Search history
    st.divider()
    st.header("Search History")
    if st.session_state.search_history:
        for i, item in enumerate(reversed(st.session_state.search_history[-5:])):
            if st.button(f"📝 {item['query'][:30]}...", key=f"history_{i}"):
                st.session_state.query_rerun = item['query']
                st.rerun()

# Main search interface
if st.session_state.workflow_mode:
    # Research Workflow Interface
    st.header("🔬 Comprehensive Research Workflow")
    
    if not st.session_state.workflow_state:
        # Initial query input
        st.markdown("### Step 1: Describe Your Research Need")
        query = st.text_area(
            "What would you like to research?",
            placeholder="Enter a detailed description of what you want to learn or investigate...",
            height=100
        )
        
        if st.button("🚀 Start Research", type="primary", disabled=not query):
            with st.spinner("Analyzing your request..."):
                try:
                    # Clear all workflow-related session state to start fresh
                    workflow_keys_to_clear = [
                        'workflow_state',
                        'research_workflow',
                        'workflow_tracking',
                        'editable_decomposition',
                        'pending_tasks',
                        'completed_tasks'
                    ]
                    
                    for key in workflow_keys_to_clear:
                        if key in st.session_state:
                            del st.session_state[key]
                    
                    # Reset workflow persistence to ensure new session
                    workflow_persistence.current_session_dir = None
                    
                    # Clear workflow tracker state if available
                    if hasattr(workflow_tracker, 'reset'):
                        workflow_tracker.reset()
                    
                    # Create a new workflow orchestrator instance to ensure clean state
                    new_workflow_orchestrator = WorkflowOrchestrator(query)
                    
                    # Execute the new workflow
                    result = new_workflow_orchestrator.execute_workflow(query)
                    st.session_state.workflow_state = result
                    
                    # Update the main workflow_orchestrator reference
                    workflow_orchestrator = new_workflow_orchestrator
                    
                    st.rerun()
                except Exception as e:
                    st.error(f"Failed to start research: {str(e)}")
                    print(f"Workflow execution error: {e}")
    
    else:
        # Handle workflow stages
        workflow_state = st.session_state.workflow_state
        stage = workflow_state['stage']
        
        # Debug: Show what stage we're in
        # print(f"DEBUG: Current detected stage: {stage}")
        # print(f"DEBUG: Workflow state keys: {list(workflow_state.keys())}")
        if 'data' in workflow_state:
            data = workflow_state['data']
            if isinstance(data, dict):
                pass  # print(f"DEBUG: Data keys: {list(data.keys())}")
            elif isinstance(data, list):
                pass  # print(f"DEBUG: Data is a list with {len(data)} items")
            else:
                pass  # print(f"DEBUG: Data type: {type(data)}")
        
        if stage == 'inquiry_clarification':
            st.markdown("### Step 1: Clarifying Your Research Request")
            
            data = workflow_state['data']
            
            # Handle parse errors - try to extract data from raw_response
            if data.get('parse_error') and 'raw_response' in data:
                try:
                    import json
                    # Try to parse the raw response
                    raw_data = json.loads(data['raw_response'])
                    # Merge the parsed data into the data dict
                    data.update(raw_data)
                except:
                    st.warning("There was an issue parsing the clarification questions. Proceeding with defaults.")
                    # Create default clarification structure
                    data['clarifying_questions'] = []
                    data['query_analysis'] = {
                        'main_topic': 'AI Agents vs Other AI Systems',
                        'implicit_needs': ['Comparison of approaches', 'Use cases', 'Implementation guidance']
                    }
            
            # Show analysis
            with st.expander("Query Analysis", expanded=True):
                if 'query_analysis' in data:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**Main Topic:**")
                        st.write(data['query_analysis'].get('main_topic', 'Not identified'))
                    with col2:
                        st.markdown("**Implicit Needs:**")
                        for need in data['query_analysis'].get('implicit_needs', []):
                            st.write(f"- {need}")
            
            # Clarifying questions
            clarifying_questions = data.get('clarifying_questions', [])
            
            if clarifying_questions:
                st.markdown("**Please answer these questions to help refine your research:**")
                
                for i, question_data in enumerate(clarifying_questions):
                    question = question_data['question']
                    purpose = question_data.get('purpose', '')
                    options = question_data.get('options', [])
                    
                    st.markdown(f"**{i+1}. {question}**")
                    if purpose:
                        st.caption(purpose)
                    
                    if options:
                        response = st.selectbox(
                            "Select an option or write your own:",
                            [""] + options + ["Other (specify below)"],
                            key=f"q_{i}"
                        )
                        if response == "Other (specify below)":
                            response = st.text_input("Your answer:", key=f"q_text_{i}")
                    else:
                        response = st.text_area("Your answer:", key=f"q_area_{i}", height=70)
                    
                    st.session_state.clarification_responses[question] = response
            else:
                st.info("No clarifying questions needed. Proceeding with the analysis of your request.")
            
            # Suggested refinement
            if 'suggested_refinement' in data:
                st.info(f"💡 Suggested refined request: {data['suggested_refinement']}")
            
            # Continue button
            all_answered = True  # Default to true if no questions
            if clarifying_questions:
                all_answered = all(
                    st.session_state.clarification_responses.get(q['question']) 
                    for q in clarifying_questions
                )
            
            if st.button("Continue to Task Planning →", type="primary", disabled=not all_answered):
                with st.spinner("Planning research tasks..."):
                    # Build clarified request from user responses before proceeding
                    original_query = workflow_orchestrator.workflow.workflow_state.get('original_query', '')
                    clarified_request = ""
                    if clarifying_questions and st.session_state.clarification_responses:
                        responses = []
                        for q in clarifying_questions:
                            question = q['question']
                            answer = st.session_state.clarification_responses.get(question, "")
                            if answer and answer.strip():
                                responses.append(f"Q: {question}\nA: {answer}")
                        
                        if responses:
                            clarified_request = f"Original query: {original_query}\n\nClarifications:\n" + "\n\n".join(responses)
                        else:
                            # No valid responses, use original query
                            clarified_request = f"Original query: {original_query}\n\n(No additional clarifications provided)"
                    else:
                        # No responses at all, use original query
                        clarified_request = f"Original query: {original_query}\n\n(No additional clarifications provided)"
                    
                    # Set the clarified request in workflow state before changing stage
                    if clarified_request and len(clarified_request.strip()) > 10:
                        workflow_orchestrator.workflow.workflow_state['clarified_request'] = clarified_request
                        workflow_orchestrator.workflow.workflow_state['current_stage'] = 'task_decomposition'
                        workflow_orchestrator.current_stage = 'task_decomposition'
                        
                        # Save the updated workflow state with new stage
                        workflow_persistence.save_workflow_state(workflow_orchestrator.workflow.workflow_state)
                        
                        result = workflow_orchestrator.execute_workflow(
                            "", 
                            st.session_state.clarification_responses
                        )
                        st.session_state.workflow_state = result
                        st.rerun()
                    else:
                        st.error("Please provide valid responses to all questions to continue.")
        
        elif stage == 'task_decomposition':
            st.markdown("### Step 2: Research Task Planning")
            
            data = workflow_state['data']
            decomposition = data['decomposition']
            verification = data['verification']
            
            # Initialize editable decomposition in session state if not exists
            if 'editable_decomposition' not in st.session_state:
                # Deep copy the decomposition to avoid reference issues
                import copy
                st.session_state.editable_decomposition = copy.deepcopy(decomposition)
                st.session_state.task_edits = {}
                
                # Ensure subtasks key exists
                if 'subtasks' not in st.session_state.editable_decomposition:
                    st.session_state.editable_decomposition['subtasks'] = []
            
            # Show task breakdown with editing capability
            st.markdown("**Proposed Research Tasks:**")
            
            subtasks = st.session_state.editable_decomposition.get('subtasks', [])
            
            for i, task in enumerate(subtasks):
                with st.expander(f"📋 Task {i+1}: {task['title']}", expanded=True):
                    # Edit mode toggle
                    edit_key = f"edit_task_{i}"
                    if st.checkbox("Edit this task", key=edit_key):
                        # Editable fields
                        new_title = st.text_input("Title:", value=task['title'], key=f"title_{i}")
                        new_objective = st.text_area("Objective:", value=task['objective'], key=f"obj_{i}", height=70)
                        new_scope = st.text_area("Scope:", value=task['scope'], key=f"scope_{i}", height=70)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            new_complexity = st.selectbox("Complexity:", ["low", "medium", "high"], 
                                                        index=["low", "medium", "high"].index(task['complexity']), 
                                                        key=f"comp_{i}")
                        with col2:
                            new_est_docs = st.number_input("Est. Docs:", value=task['estimated_documents'], 
                                                         min_value=1, max_value=20, key=f"docs_{i}")
                        
                        # Store edits
                        st.session_state.task_edits[i] = {
                            'title': new_title,
                            'objective': new_objective,
                            'scope': new_scope,
                            'complexity': new_complexity,
                            'estimated_documents': new_est_docs
                        }
                    else:
                        # Display mode
                        col1, col2, col3 = st.columns([2, 1, 1])
                        with col1:
                            st.markdown(f"**Objective:** {task['objective']}")
                            st.markdown(f"**Scope:** {task['scope']}")
                        with col2:
                            st.metric("Complexity", task['complexity'])
                        with col3:
                            st.metric("Est. Docs", task['estimated_documents'])
                    
                    # Remove task button
                    if st.button(f"🗑️ Remove Task", key=f"remove_{i}"):
                        subtasks.pop(i)
                        st.session_state.editable_decomposition['subtasks'] = subtasks
                        st.rerun()
            
            # Add new task section
            has_prefill = bool(st.session_state.get('prefill_task'))
            with st.expander("➕ Add New Task", expanded=has_prefill):
                # Check for pre-filled values - don't mark as used until task is actually added
                prefill = st.session_state.get('prefill_task', {})
                # Ensure prefill is a dict (not None)
                if prefill is None:
                    prefill = {}
                
                # Show prefill indicator
                if has_prefill:
                    st.info("📋 Pre-filled from suggestion/gap - modify as needed")
                
                new_task_title = st.text_input("Task Title:", 
                                             value=prefill.get('title', ''),
                                             key="new_task_title")
                new_task_objective = st.text_area("Task Objective:", 
                                                value=prefill.get('objective', ''),
                                                key="new_task_obj", height=70)
                new_task_scope = st.text_area("Task Scope:", 
                                            value=prefill.get('scope', ''),
                                            key="new_task_scope", height=70)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    new_task_complexity = st.selectbox("Complexity:", ["low", "medium", "high"], key="new_task_comp")
                with col2:
                    new_task_docs = st.number_input("Est. Docs:", value=5, min_value=1, max_value=20, key="new_task_docs")
                with col3:
                    col3a, col3b = st.columns(2)
                    with col3a:
                        if st.button("Add Task", type="primary"):
                            if new_task_title and new_task_objective:
                                # Get current tasks from session state to ensure accurate count
                                current_tasks = st.session_state.editable_decomposition.get('subtasks', [])
                                new_task = {
                                    'id': f"task_{len(current_tasks)+1}",
                                    'title': new_task_title,
                                    'objective': new_task_objective,
                                    'scope': new_task_scope,
                                    'complexity': new_task_complexity,
                                    'estimated_documents': new_task_docs,
                                    'dependencies': []
                                }
                                st.session_state.editable_decomposition['subtasks'].append(new_task)
                                
                                # Clear the prefill task since we successfully added the task
                                st.session_state.prefill_task = None
                                
                                st.success(f"✅ Added task: {new_task_title}")
                                st.rerun()
                            else:
                                st.error("❌ Please provide both title and objective")
                    
                    with col3b:
                        # Show cancel button only if there's a prefill task
                        if st.session_state.get('prefill_task'):
                            if st.button("Cancel", key="cancel_prefill"):
                                st.session_state.prefill_task = None
                                st.rerun()
            
            # Verification results
            if verification:
                st.divider()
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Completeness Score", f"{verification.get('completeness_score', 0)}%")
                with col2:
                    status = "✅ Approved" if verification.get('approved') else "⚠️ Needs Revision"
                    st.metric("Status", status)
                
                # Gaps with ability to address them
                if verification.get('gaps'):
                    st.warning("**Identified Gaps:**")
                    for i, gap in enumerate(verification['gaps']):
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.write(f"- {gap}")
                        with col2:
                            if st.button("Address", key=f"gap_{i}"):
                                # Create task based on the gap
                                if "theoretical" in gap.lower() or "framework" in gap.lower():
                                    # Special handling for theoretical framework gaps
                                    st.session_state.prefill_task = {
                                        'title': "Compare Theoretical Frameworks",
                                        'objective': "Analyze and compare theoretical models (e.g., control theory, decision theory, complexity theory) for AI agents vs prompts",
                                        'scope': "Focus on autonomy metrics, environmental dynamics, and decision-making frameworks"
                                    }
                                else:
                                    # General gap handling
                                    st.session_state.prefill_task = {
                                        'title': f"Address: {gap[:50]}...",
                                        'objective': f"Fill the identified gap: {gap}",
                                        'scope': gap
                                    }
                                st.rerun()
                
                # Suggestions with ability to implement them
                if verification.get('suggestions'):
                    st.info("**Suggestions:**")
                    for i, suggestion in enumerate(verification['suggestions']):
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.write(f"- {suggestion}")
                        with col2:
                            if st.button("Implement", key=f"sug_{i}"):
                                # Store the suggestion info for pre-filling
                                st.session_state.prefill_task = {
                                    'title': f"Implement: {suggestion[:50]}...",
                                    'objective': suggestion,
                                    'scope': 'As suggested by the verification process'
                                }
                                st.rerun()
            
            # Action buttons
            st.divider()
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("💾 Apply Edits", type="secondary"):
                    # Apply any task edits
                    for idx, edits in st.session_state.task_edits.items():
                        if idx < len(st.session_state.editable_decomposition['subtasks']):
                            st.session_state.editable_decomposition['subtasks'][idx].update(edits)
                    
                    # Update the workflow decomposition
                    workflow_orchestrator.workflow.workflow_state['subtasks'] = st.session_state.editable_decomposition['subtasks']
                    st.success("Tasks updated!")
                    st.session_state.task_edits = {}
                    st.rerun()
            
            with col2:
                if st.button("🔄 Re-verify Tasks", type="secondary"):
                    # Re-run verification with edited tasks
                    with st.spinner("Re-verifying tasks..."):
                        new_verification = workflow_orchestrator.workflow._verify_task_decomposition(
                            st.session_state.editable_decomposition,
                            workflow_orchestrator.workflow.workflow_state['clarified_request']
                        )
                        st.session_state.workflow_state['data']['verification'] = new_verification
                        st.rerun()
            
            with col3:
                # Allow proceeding even if not approved, with warning
                proceed_anyway = not verification.get('approved') and st.checkbox("Proceed anyway")
                if st.button("🔍 Begin Research →", type="primary", 
                           disabled=not (verification.get('approved') or proceed_anyway)):
                    with st.spinner("Starting document research..."):
                        # Apply any pending edits
                        for idx, edits in st.session_state.task_edits.items():
                            if idx < len(st.session_state.editable_decomposition['subtasks']):
                                st.session_state.editable_decomposition['subtasks'][idx].update(edits)
                        
                        # Update workflow with final tasks
                        workflow_orchestrator.workflow.workflow_state['subtasks'] = st.session_state.editable_decomposition['subtasks']
                        
                        # Set and save the stage properly
                        workflow_orchestrator.workflow.workflow_state['current_stage'] = 'document_research'
                        workflow_orchestrator.current_stage = 'document_research'
                        
                        # Import workflow_persistence to save state
                        from utils.workflow_persistence import workflow_persistence
                        workflow_persistence.save_workflow_state(workflow_orchestrator.workflow.workflow_state)
                        
                        result = workflow_orchestrator.execute_workflow("", {})
                        st.session_state.workflow_state = result
                        st.rerun()
        
        elif stage == 'document_research':
            st.markdown("### Step 3: Document Research & Analysis")
            
            data = workflow_state['data']
            
            # Progress overview - use all subtasks, not just data
            all_subtasks = workflow_orchestrator.workflow.workflow_state.get('subtasks', [])
            total_tasks = len(all_subtasks)
            
            # Check if we have tasks to research
            if total_tasks == 0:
                st.error("❌ No research tasks found. It looks like the task planning stage didn't generate any tasks.")
                st.info("This might happen if the original query was not properly captured. Please restart the research workflow with your actual research question.")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Back to Task Planning", type="secondary"):
                        workflow_orchestrator.workflow.workflow_state['current_stage'] = 'task_decomposition'
                        workflow_orchestrator.current_stage = 'task_decomposition'
                        workflow_persistence.save_workflow_state(workflow_orchestrator.workflow.workflow_state)
                        st.rerun()
                
                with col2:
                    if st.button("🔄 Start New Research", type="primary"):
                        # Clear workflow state to start fresh
                        st.session_state.workflow_state = None
                        workflow_orchestrator.current_stage = None
                        workflow_persistence.current_session_dir = None
                        st.rerun()
            else:
                # Count completed tasks from multiple sources
                completed_count = 0
                for subtask in all_subtasks:
                    task_id = subtask['id']
                    # Check in data results
                    task_result = next((r for r in data if r.get('subtask', {}).get('id') == task_id), None)
                    if task_result and (task_result.get('completed', False) or task_result.get('validation', {}).get('sufficient', False)):
                        completed_count += 1
                    # Also check in scratchpads for tasks with findings
                    elif task_id in workflow_orchestrator.workflow.workflow_state.get('scratchpads', {}):
                        scratchpad = workflow_orchestrator.workflow.workflow_state['scratchpads'][task_id]
                        if scratchpad.get('iteration_count', 0) >= 3 and (scratchpad.get('high_value_findings') or scratchpad.get('insights')):
                            completed_count += 1
                
                st.progress(completed_count / total_tasks if total_tasks > 0 else 0)
                st.markdown(f"**Research Progress:** {completed_count}/{total_tasks} tasks completed")
                
                # Get all subtasks from workflow state
                all_subtasks = workflow_orchestrator.workflow.workflow_state.get('subtasks', [])
                scratchpads = workflow_orchestrator.workflow.workflow_state.get('scratchpads', {})
                doc_analysis = workflow_orchestrator.workflow.workflow_state.get('document_analysis', {})
                
                # Show research results for ALL subtasks
                for subtask in all_subtasks:
                    # Find result for this subtask in data
                    result = next((r for r in data if r['subtask']['id'] == subtask['id']), None)
                    
                    if result:
                        research = result['research']
                        validation = result['validation']
                    else:
                        # Create placeholder for tasks not yet in data
                        research = {'documents_found': 0, 'keywords': {}, 'analysis': {}}
                        validation = {'sufficient': False, 'total_findings': 0}
                        result = {'subtask': subtask, 'research': research, 'validation': validation}
                    
                    with st.expander(f"📚 {subtask['title']}", expanded=not validation.get('sufficient', False)):
                        # Research summary
                        col1, col2, col3 = st.columns([2, 1, 1])
                        with col1:
                            st.markdown("**Documents Found:**")
                            st.write(f"{research['documents_found']} relevant documents")
                        with col2:
                            st.metric("Completeness", f"{validation['completeness_score']}%")
                        with col3:
                            status = "✅" if validation.get('sufficient', False) else "🔄"
                            st.metric("Status", status)
                        
                        # Check if web search was performed
                        task_scratchpad = scratchpads.get(subtask['id'], {})
                        if task_scratchpad.get('search_enhanced'):
                            st.info("🌐 Enhanced with web search results")
                        
                        # Key findings
                        if 'analysis' in research and 'document_analyses' in research['analysis']:
                            st.markdown("**Key Findings:**")
                            for doc_analysis in research['analysis']['document_analyses'][:3]:
                                if doc_analysis['relevance_score'] >= 7:
                                    st.markdown(f"📄 **{doc_analysis['document_title']}** (Score: {doc_analysis['relevance_score']}/10)")
                                    for insight in doc_analysis.get('insights', [])[:2]:
                                        st.write(f"  - {insight}")
                        
                        # Display web search results if available
                        if task_scratchpad.get('web_search_results'):
                            st.markdown("**🔍 Web Search Results:**")
                            for i, result in enumerate(task_scratchpad['web_search_results'][:2]):
                                st.markdown(f"**Query {i+1}:** {result['query']}")
                                # Display in a container instead of expander
                                with st.container():
                                    st.info(result['result'][:500] + "..." if len(result['result']) > 500 else result['result'])
                        
                        # Show completion verification if available
                        if validation.get('completion_verified') is not None:
                            st.divider()
                            completion = validation.get('completion_details', {})
                            
                            if validation['completion_verified']:
                                st.success("✅ Task Completion Verified")
                                if completion.get('completion_summary'):
                                    st.write(f"**Summary:** {completion['completion_summary']}")
                                
                                # Show coverage metrics
                                if 'objective_coverage' in completion:
                                    coverage = completion['objective_coverage']
                                    col1, col2 = st.columns(2)
                                    with col1:
                                        st.metric("Objective Coverage", f"{coverage.get('percentage', 0)}%")
                                    with col2:
                                        if 'quality_assessment' in completion:
                                            quality = completion['quality_assessment']
                                            st.metric("Quality", quality.get('depth', 'unknown'))
                            else:
                                st.warning("⚠️ Task Not Yet Complete")
                                if completion.get('recommendation'):
                                    st.info(f"**Recommendation:** {completion['recommendation'].replace('_', ' ').title()}")
                                if completion.get('missing_requirements'):
                                    st.write("**Missing Requirements:**")
                                    for req in completion['missing_requirements']:
                                        st.write(f"- {req}")
                        
                        # Missing information
                        if not validation.get('sufficient', False) and validation.get('missing_elements'):
                            st.warning("**Still need information about:**")
                            for element in validation['missing_elements']:
                                st.write(f"- {element}")
                
                # Gap Filling with Web Search Option
                st.divider()
                with st.expander("🔍 Advanced: Fill Gaps with Web Search", expanded=False):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        enable_search = st.checkbox("Enable GPT-4o Search Preview", 
                                                   help="Use GPT-4o with web search to find up-to-date information for incomplete tasks")
                    
                    with col2:
                        completion_threshold = st.slider("Completion Threshold (%)", 
                                                       min_value=50, 
                                                       max_value=90, 
                                                       value=70,
                                                       step=5,
                                                       disabled=not enable_search,
                                                       help="Tasks below this completion score will be enhanced with web search")
                    
                    with col3:
                        search_iterations = st.number_input("Search Iterations per Task", 
                                                          min_value=1, 
                                                          max_value=5, 
                                                          value=2,
                                                          disabled=not enable_search,
                                                          help="Number of search queries to generate per incomplete task")
                    
                    if enable_search:
                        # Find tasks that need gap filling
                        tasks_needing_search = []
                        for subtask in all_subtasks:
                            result = next((r for r in data if r.get('subtask', {}).get('id') == subtask['id']), None)
                            if result:
                                validation = result.get('validation', {})
                                completion_score = validation.get('completeness_score', 0)
                                if completion_score < completion_threshold:
                                    tasks_needing_search.append({
                                        'task': subtask,
                                        'completion_score': completion_score,
                                        'missing_elements': validation.get('missing_elements', [])
                                    })
                        
                        if tasks_needing_search:
                            st.info(f"Found {len(tasks_needing_search)} tasks below {completion_threshold}% completion")
                            
                            if st.button("🌐 Run Web Search Gap Filling", type="primary"):
                                with st.spinner("Generating search queries and fetching information..."):
                                    # Import the new search function
                                    from utils.llm_utils import search_with_gpt4o_preview
                                    
                                    for task_info in tasks_needing_search:
                                        task = task_info['task']
                                        st.write(f"Searching for: {task['title']}")
                                        
                                        # Generate search questions based on task and missing elements
                                        search_context = {
                                            'task_title': task['title'],
                                            'task_objective': task['objective'],
                                            'task_scope': task['scope'],
                                            'missing_elements': task_info['missing_elements'],
                                            'original_query': workflow_orchestrator.workflow.workflow_state.get('original_query', '')
                                        }
                                        
                                        # Generate and execute searches
                                        search_results = []
                                        for i in range(search_iterations):
                                            # Create specific search queries using a more sophisticated prompt
                                            query_prompt = f"""Generate 3 specific web search queries to find up-to-date information for this research task.

Research Context:
- Task: {task['title']}
- Objective: {task['objective']}
- Scope: {task['scope']}
- Original Research Question: {workflow_orchestrator.workflow.workflow_state.get('original_query', '')}

Missing Information Gaps:
{chr(10).join(f"- {elem}" for elem in task_info['missing_elements'][:5])}

Query Set {i+1} of {search_iterations}:
Generate 3 different search queries that would help fill these information gaps. Focus on:
1. Recent developments (2024-2025)
2. Practical implementations and case studies
3. Technical specifications or best practices

Format as a JSON array of 3 query strings."""
                                            
                                            # Generate queries
                                            queries_response = call_llm(query_prompt, "generate search queries")
                                            
                                            # Parse queries
                                            try:
                                                import json
                                                queries = json.loads(queries_response)
                                                if not isinstance(queries, list):
                                                    queries = [queries_response]
                                            except:
                                                # Fallback to simple query extraction
                                                queries = [line.strip() for line in queries_response.split('\n') if line.strip() and not line.startswith('{')][:3]
                                            
                                            # Execute searches for each query
                                            for j, search_query in enumerate(queries[:3]):
                                                st.write(f"  Query {i*3 + j + 1}: {search_query}")
                                                
                                                # Use the search preview model
                                                search_result = search_with_gpt4o_preview(search_query)
                                                if search_result:
                                                    search_results.append({
                                                        'query': search_query,
                                                        'result': search_result,
                                                        'timestamp': datetime.now().isoformat()
                                                    })
                                        
                                        # Update task's research data with search results
                                        if task['id'] not in workflow_orchestrator.workflow.workflow_state.get('scratchpads', {}):
                                            workflow_orchestrator.workflow.workflow_state['scratchpads'][task['id']] = {}
                                        
                                        scratchpad = workflow_orchestrator.workflow.workflow_state['scratchpads'][task['id']]
                                        scratchpad['web_search_results'] = search_results
                                        scratchpad['search_timestamp'] = datetime.now().isoformat()
                                        scratchpad['search_enhanced'] = True
                                        
                                        # Add search results to high value findings
                                        if 'high_value_findings' not in scratchpad:
                                            scratchpad['high_value_findings'] = []
                                        
                                        # Process each search result and extract key information
                                        for result in search_results:
                                            finding = f"[Web Search - {result['query']}]: {result['result'][:200]}..."
                                            scratchpad['high_value_findings'].append(finding)
                                    
                                    # Save updated workflow state
                                    from utils.workflow_persistence import workflow_persistence
                                    workflow_persistence.save_workflow_state(workflow_orchestrator.workflow.workflow_state)
                                    
                                    st.success("✅ Web search gap filling complete!")
                                    st.rerun()
                        else:
                            st.success(f"All tasks are above {completion_threshold}% completion!")
                
                # Action buttons
                col1, col2 = st.columns(2)
                with col1:
                    if any(not r.get('validation', {}).get('sufficient', False) for r in data):
                        if st.button("🔄 Continue Research", type="secondary"):
                            # Create a status container for real-time updates
                            with st.status("Continuing research...", expanded=True) as status:
                                # Create and set progress reporter
                                progress_reporter = ProgressReporter(status)
                                set_progress_reporter(progress_reporter)
                                
                                # Show current tracking status
                                progress_reporter.update("🔍 Starting research iteration...")
                                
                                # Get initial status
                                initial_status = workflow_tracker.get_current_status()
                                progress_reporter.update_metrics(
                                    initial_status['total_operations'], 
                                    initial_status['total_llm_calls']
                                )
                                
                                # Execute workflow
                                result = workflow_orchestrator.execute_workflow("", {})
                                
                                # Show final status
                                final_status = workflow_tracker.get_current_status()
                                progress_reporter.success(
                                    f"Completed - Operations: {final_status['total_operations']} | "
                                    f"LLM Calls: {final_status['total_llm_calls']} | "
                                    f"Time: {final_status['elapsed_minutes']:.1f} min"
                                )
                                
                                # Clear progress reporter
                                set_progress_reporter(None)
                                
                                st.session_state.workflow_state = result
                                status.update(label="Research iteration complete!", state="complete")
                                st.rerun()
                
                with col2:
                    all_sufficient = all(r.get('validation', {}).get('sufficient', False) for r in data)
                    completed_tasks = sum(1 for r in data if r.get('validation', {}).get('sufficient', False))
                    total_tasks = len(data)
                    
                    # Allow report generation if at least some tasks have findings
                    # Try multiple sources for scratchpads
                    scratchpads = workflow_state.get('scratchpads', {})
                    if not scratchpads and 'loaded_state' in workflow_state:
                        scratchpads = workflow_state['loaded_state'].get('scratchpads', {})
                    if not scratchpads:
                        # Try to get from workflow orchestrator
                        scratchpads = workflow_orchestrator.workflow.workflow_state.get('scratchpads', {})
                    
                    has_findings = any(
                        scratchpad.get('high_value_findings') or scratchpad.get('insights') 
                        for scratchpad in scratchpads.values()
                    )
                    
                    # Debug info
                    print(f"DEBUG: Scratchpads found: {len(scratchpads)}")
                    print(f"DEBUG: Has findings: {has_findings}")
                    print(f"DEBUG: Completed tasks: {completed_tasks}/{total_tasks}")
                    
                    # Always allow report generation - we'll create default content if needed
                    has_findings = True  # Force enable the button
                    
                    # Show both buttons for better user experience
                    col2a, col2b = st.columns(2)
                    
                    with col2a:
                        button_text = "📝 Generate Report →" if all_sufficient else f"📝 Generate Partial Report ({completed_tasks}/{total_tasks} complete)"
                        
                        if st.button(button_text, type="primary", disabled=not has_findings):
                            with st.spinner("Generating comprehensive report..."):
                                workflow_orchestrator.current_stage = 'report_generation'
                                result = workflow_orchestrator.execute_workflow("", {})
                                
                                # Debug: Check what we got back
                                print(f"DEBUG: Report generation result: {result}")
                                print(f"DEBUG: Result stage: {result.get('stage', 'NO STAGE')}")
                                print(f"DEBUG: Result keys: {list(result.keys())}")
                                
                                st.session_state.workflow_state = result
                                st.rerun()
                    
                    with col2b:
                        # Force report generation button as backup
                        if st.button("🚀 Force Generate Report", type="secondary", help="Generate report regardless of completion status"):
                            with st.spinner("Forcing report generation..."):
                                # Force stage transition
                                workflow_orchestrator.current_stage = 'report_generation'
                                workflow_orchestrator.workflow.workflow_state['current_stage'] = 'report_generation'
                                
                                # Call report generation directly
                                result = workflow_orchestrator.handle_report_generation()
                                
                                print(f"DEBUG: Forced report result: {result}")
                                print(f"DEBUG: Forced result stage: {result.get('stage', 'NO STAGE')}")
                                
                                st.session_state.workflow_state = result
                                st.rerun()
        
        elif stage == 'report_generation':
            st.markdown("### Step 4: Research Report")
            
            # Get the report from multiple possible locations
            data = workflow_state.get('data', {})
            
            # Handle both dict and list data types
            if isinstance(data, dict):
                report = data.get('report', 'No report generated')
                metadata = data.get('metadata', {})
            else:
                # data is a list (from document research), no report yet
                report = 'No report generated'
                metadata = {}
            
            # Check if report is stored directly in workflow state
            if (not report or report == 'No report generated') and workflow_orchestrator:
                orchestrator_report = workflow_orchestrator.workflow.workflow_state.get('final_report')
                if orchestrator_report:
                    report = orchestrator_report
                    # Update metadata from orchestrator
                    metadata = {
                        'generated_at': datetime.now().isoformat(),
                        'subtasks_completed': len(workflow_orchestrator.workflow.workflow_state.get('subtasks', [])),
                        'documents_analyzed': workflow_orchestrator.workflow._count_analyzed_documents()
                    }
                else:
                    # No report exists, generate it now
                    st.info("🔄 Generating report now...")
                    with st.spinner("Creating comprehensive report..."):
                        try:
                            result = workflow_orchestrator.handle_report_generation()
                            if result and 'data' in result and 'report' in result['data']:
                                report = result['data']['report']
                                metadata = result['data']['metadata']
                                
                                # Check if report is complete
                                if _is_report_incomplete(report):
                                    st.warning("⚠️ Report appears incomplete, continuing generation...")
                                    complete_report = _complete_incomplete_report(report, workflow_orchestrator=workflow_orchestrator)
                                    if complete_report:
                                        report = complete_report
                                        # Update the workflow state with the complete report
                                        workflow_orchestrator.workflow.workflow_state['final_report'] = report
                                        workflow_persistence.save_workflow_state(workflow_orchestrator.workflow.workflow_state)
                                        st.success("✅ Report completed successfully!")
                                    else:
                                        st.warning("⚠️ Could not complete report, showing partial version")
                                else:
                                    st.success("✅ Report generated successfully!")
                                st.rerun()
                            else:
                                st.error("❌ Failed to generate report - invalid result structure")
                        except Exception as e:
                            st.error(f"❌ Error generating report: {str(e)}")
                            print(f"Report generation error: {e}")
            
            # Also check if existing report is incomplete
            elif report and report != 'No report generated' and _is_report_incomplete(report):
                st.warning("📝 Report appears to be incomplete")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🔄 Complete Report", type="primary", help="Continue generating the incomplete report", key="complete_report_btn_alt"):
                        with st.spinner("Completing report..."):
                            complete_report = _complete_incomplete_report(report, workflow_orchestrator=workflow_orchestrator)
                            if complete_report:
                                # Use the update_report method to properly save and update all state
                                result = workflow_orchestrator.update_report(complete_report)
                                
                                # Update session state with the new result
                                st.session_state.workflow_state = result
                                
                                st.success("✅ Report completed!")
                                time.sleep(0.5)  # Brief pause to ensure UI updates
                                st.rerun()
                            else:
                                st.error("❌ Failed to complete report")
                with col2:
                    if st.button("📤 Use Partial Report", type="secondary", help="Continue with the incomplete report", key="use_partial_report_btn_alt"):
                        st.info("Using partial report as-is")
            
            # Debug info
            if not report or report == 'No report generated':
                st.warning("⚠️ Report generation may still be in progress or encountered an issue.")
                with st.expander("Debug Info", expanded=False):
                    st.write("Workflow state keys:", list(workflow_state.keys()))
                    if isinstance(data, dict):
                        st.write("Data keys:", list(data.keys()))
                    elif isinstance(data, list):
                        st.write("Data is a list with", len(data), "items")
                    else:
                        st.write("Data type:", type(data))
                    st.write("Report length:", len(report) if report else 0)
                    if workflow_orchestrator:
                        final_report = workflow_orchestrator.workflow.workflow_state.get('final_report')
                        st.write("Orchestrator final_report length:", len(final_report) if final_report else 0)
            
            # Report metadata
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Subtasks Completed", metadata.get('subtasks_completed', 0))
            with col2:
                st.metric("Documents Analyzed", metadata.get('documents_analyzed', 0))
            with col3:
                generated_at = metadata.get('generated_at', datetime.now().isoformat())
                st.metric("Generated", datetime.fromisoformat(generated_at).strftime("%Y-%m-%d %H:%M"))
            
            # Report actions
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if st.button("🆕 Start New Research", type="secondary", help="Clear current research and start a new one"):
                    # Clear all workflow states
                    if 'workflow_state' in st.session_state:
                        del st.session_state.workflow_state
                    if 'research_workflow' in st.session_state:
                        del st.session_state.research_workflow
                    workflow_persistence.current_session_dir = None
                    st.rerun()
            
            with col2:
                # Download button - use improved version if available
                download_report = report
                download_label = "📥 Download Report (Markdown)"
                if 'manual_improvement_applied' in st.session_state:
                    download_report = st.session_state.manual_improvement_applied['improved_report']
                    download_label = "📥 Download Improved Report"
                
                st.download_button(
                    label=download_label,
                    data=download_report,
                    file_name=f"research_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )
            
            with col2:
                # Copy to clipboard functionality
                if st.button("📋 Copy to Clipboard"):
                    st.write("Report copied! (Use Ctrl+A, Ctrl+C on the report below)")
                    st.info("Select all text below and copy")
            
            with col3:
                # Manual QA Review button
                qa_button_text = "🔍 Manual QA Review"
                qa_help_text = "Run additional manual QA review (automatic QA already completed)"
                if st.button(qa_button_text, help=qa_help_text):
                    # Generate unique session ID for this QA review
                    import time
                    st.session_state.qa_session_id = f"qa_{int(time.time())}"
                    
                    with st.spinner("Running manual QA review..."):
                        try:
                            # Get the enhanced search engine and run QA on the report
                            from utils.intelligent_search_enhanced import get_enhanced_search_engine
                            search_engine = get_enhanced_search_engine()
                            
                            # Configure QA system - use comprehensive by default for manual review
                            search_engine.configure_qa_system("comprehensive")
                            
                            # Verify QA system is available
                            if not hasattr(search_engine, 'qa_system') or search_engine.qa_system is None:
                                st.error("❌ QA system is not available. Please check the configuration.")
                            else:
                                # Extract sources from workflow state if available
                                workflow_state = st.session_state.get('workflow_state', {})
                                sources = []
                            
                                # Try to reconstruct sources from workflow data
                                if 'data' in workflow_state:
                                    data = workflow_state['data']
                                    if isinstance(data, list):
                                        # Document research stage format
                                        for result in data:
                                            if 'research' in result and 'analysis' in result['research']:
                                                analysis = result['research']['analysis']
                                                if 'document_analyses' in analysis:
                                                    for doc_analysis in analysis['document_analyses'][:5]:
                                                        sources.append({
                                                            'title': doc_analysis.get('document_title', 'Research Document'),
                                                            'content': {'body': doc_analysis.get('content_excerpt', '')},
                                                            'author': 'Research Analysis',
                                                            'category': 'Research'
                                                        })
                                    elif isinstance(data, dict) and 'report' in data:
                                        # Report generation stage - create generic source
                                        sources = [{
                                            'title': 'Research Report Analysis',
                                            'content': {'body': report[:1000]},  # Use beginning of report
                                            'author': 'Workflow System',
                                            'category': 'Research'
                                        }]
                                
                                # If no sources, create a default one
                                if not sources:
                                    sources = [{
                                        'title': 'Manual QA Review',
                                        'content': {'body': 'Manual quality assessment review'},
                                        'author': 'User Request',
                                        'category': 'Quality Assurance'
                                    }]
                                
                                # Use current report (may be improved version)
                                current_report = report
                                if 'manual_improvement_applied' in st.session_state:
                                    current_report = st.session_state.manual_improvement_applied['improved_report']
                                
                                # Run QA using the new structured system
                                try:
                                    from utils.structured_qa_integration import StructuredQAManager
                                    from utils.llm_utils import _call_llm_api
                                    
                                    # Use structured QA for better analysis
                                    workspace_path = Path(st.session_state.workflow_state.get('workspace_path', '.'))
                                    qa_manager = StructuredQAManager(workspace_path)
                                    
                                    # Import the report into structured format
                                    structured_doc = qa_manager.import_existing_report(current_report, "qa_review")
                                    
                                    # Perform comprehensive QA analysis using LLM
                                    qa_prompt = f"""Please analyze this research report for quality and accuracy. 

REPORT CONTENT:
{current_report[:8000]}

CONTEXT: Manual quality assessment of research report
SOURCES USED: {len(sources)} sources

Please identify any issues with:
1. Technical accuracy and factual correctness
2. Clarity and readability 
3. Completeness of information
4. Structure and organization
5. Practical applicability

For each issue found, provide:
- Section title where the issue occurs
- Description of the specific issue
- Suggested fix or improvement
- Confidence level (0.0-1.0)

IMPORTANT: Return ONLY valid JSON format without any additional text, markdown formatting, or code blocks:

{{
  "inaccurate_or_confusing_sections": [
    {{
      "section_title": "Section Name",
      "issue": "Description of issue",
      "suggested_fix": "How to fix it",
      "confidence": 0.9
    }}
  ],
  "structural_issues": [
    {{
      "section_title": "Structure",
      "issue": "Document organization or flow issues",
      "suggested_fix": "How to improve structure",
      "confidence": 0.9
    }}
  ],
  "overall_score": 0.8,
  "confidence": 0.85,
  "trust_score": 0.82,
  "suggestions": ["General suggestion 1", "General suggestion 2"]
}}

Do not include ```json``` code blocks or any other formatting - just the raw JSON object."""

                                    response = _call_llm_api(qa_prompt, "QA analysis")
                                    
                                    if response:
                                        try:
                                            # Clean and extract JSON from response
                                            import json
                                            import re
                                            
                                            # Handle case where full API response is received instead of just content
                                            if isinstance(response, str) and '"choices"' in response and '"message"' in response:
                                                try:
                                                    api_response = json.loads(response)
                                                    if "choices" in api_response and len(api_response["choices"]) > 0:
                                                        message = api_response["choices"][0].get("message", {})
                                                        response = message.get("content", response)
                                                        print("DEBUG: Extracted content from OpenAI API response structure")
                                                except json.JSONDecodeError:
                                                    pass  # Continue with original response if not valid JSON
                                            
                                            # Remove code block markers and thinking tags
                                            cleaned_response = response.strip()
                                            
                                            # Remove thinking tags (common in qwen models)
                                            if '<think>' in cleaned_response:
                                                parts = cleaned_response.split('</think>')
                                                if len(parts) > 1:
                                                    cleaned_response = parts[1].strip()
                                            
                                            # Remove code block markers
                                            if cleaned_response.startswith('```json'):
                                                cleaned_response = cleaned_response[7:]
                                            if cleaned_response.startswith('```'):
                                                cleaned_response = cleaned_response[3:]
                                            if cleaned_response.endswith('```'):
                                                cleaned_response = cleaned_response[:-3]
                                            
                                            # Fix common JSON issues
                                            # Remove trailing commas before } or ]
                                            cleaned_response = re.sub(r',(\s*[}\]])', r'\1', cleaned_response)
                                            # Fix unescaped quotes in strings
                                            cleaned_response = re.sub(r'(?<!\\)"(?=[^",\s]*[^",\s:}])', r'\\"', cleaned_response)
                                            # Ensure proper closing braces
                                            if cleaned_response.count('{') > cleaned_response.count('}'):
                                                cleaned_response += '}'
                                            if cleaned_response.count('[') > cleaned_response.count(']'):
                                                cleaned_response += ']'
                                            
                                            # Try to find JSON in the response
                                            json_match = re.search(r'\{.*?"inaccurate_or_confusing_sections".*?\}', cleaned_response, re.DOTALL)
                                            if json_match:
                                                json_str = json_match.group()
                                                # Fix trailing commas in the matched JSON too
                                                json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)
                                                qa_results = json.loads(json_str)
                                                print(f"DEBUG: Successfully parsed JSON with {len(qa_results.get('inaccurate_or_confusing_sections', []))} issues")
                                            elif cleaned_response.strip().startswith('{') and cleaned_response.strip().endswith('}'):
                                                qa_results = json.loads(cleaned_response.strip())
                                                print("DEBUG: Parsed full response as JSON")
                                            else:
                                                raise ValueError("No valid JSON structure found in response")
                                                
                                            # Validate the parsed structure
                                            if not isinstance(qa_results.get('inaccurate_or_confusing_sections'), list):
                                                raise ValueError("Invalid JSON structure - missing or invalid inaccurate_or_confusing_sections")
                                                
                                        except json.JSONDecodeError as e:
                                            print(f"DEBUG: JSON decode error: {e}")
                                            print(f"DEBUG: Response preview: {response[:300]}...")
                                            # Try a more aggressive JSON extraction first
                                            try:
                                                qa_results = extract_json_aggressively(response)
                                                if qa_results:
                                                    print("DEBUG: Aggressive JSON extraction succeeded")
                                                else:
                                                    raise ValueError("Aggressive extraction failed")
                                            except:
                                                print("DEBUG: Falling back to manual parsing")
                                                qa_results = parse_qa_response_manually(response)
                                        except Exception as e:
                                            print(f"DEBUG: JSON parsing failed: {e}")
                                            print(f"DEBUG: Response preview: {response[:300]}...")
                                            # Try aggressive extraction first
                                            try:
                                                qa_results = extract_json_aggressively(response)
                                                if qa_results:
                                                    print("DEBUG: Aggressive JSON extraction succeeded")
                                                else:
                                                    raise ValueError("Aggressive extraction failed")
                                            except:
                                                print("DEBUG: Falling back to manual parsing")
                                                qa_results = parse_qa_response_manually(response)
                                    else:
                                        qa_results = {
                                            "inaccurate_or_confusing_sections": [],
                                            "overall_score": 0.7,
                                            "suggestions": ["QA analysis was not available"]
                                        }
                                        
                                except Exception as structured_error:
                                    print(f"Structured QA failed, falling back to legacy: {structured_error}")
                                    # Fallback to legacy system
                                    qa_results = search_engine.qa_system.run_report_qa(
                                        current_report, 
                                        sources, 
                                        "Manual quality assessment of research report"
                                    )
                                
                                # Store QA results in session state for display
                                st.session_state.manual_qa_results = qa_results
                                st.session_state.manual_qa_timestamp = datetime.now()
                                
                                st.success("✅ Manual QA review completed!")
                                st.rerun()
                            
                        except Exception as e:
                            st.error(f"❌ QA review failed: {str(e)}")
                            print(f"Manual QA error: {e}")
            
            with col4:
                # Start new research
                if st.button("🔄 New Research"):
                    st.session_state.workflow_state = None
                    st.session_state.clarification_responses = {}
                    # Clear any manual QA results and improvements
                    if 'manual_qa_results' in st.session_state:
                        del st.session_state.manual_qa_results
                    if 'manual_qa_timestamp' in st.session_state:
                        del st.session_state.manual_qa_timestamp
                    if 'manual_improvement_applied' in st.session_state:
                        del st.session_state.manual_improvement_applied
                    workflow_orchestrator.current_stage = 'inquiry_clarification'
                    # Reset workflow persistence to force new session creation
                    workflow_persistence.current_session_dir = None
                    st.rerun()
            
            # Display report
            st.divider()
            st.markdown("## 📄 Research Report")
            
            # Show file location
            if workflow_persistence.current_session_dir:
                report_path = workflow_persistence.current_session_dir / "05_final_report.md"
                st.caption(f"📁 Report saved to: {report_path}")
            
            # Report container with custom styling
            st.markdown(
                """
                <style>
                .report-container {
                    background-color: #f8f9fa;
                    padding: 2rem;
                    border-radius: 10px;
                    margin: 1rem 0;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            
            with st.container():
                # Display improved report if available, otherwise original
                display_report = report
                if 'manual_improvement_applied' in st.session_state:
                    display_report = st.session_state.manual_improvement_applied['improved_report']
                    st.info("📝 Showing improved version of the report (improvements have been applied)")
                
                # Show the actual report
                if display_report and display_report != 'No report generated':
                    st.markdown("---")
                    st.markdown(display_report)
                else:
                    st.error("❌ No report content available. Please try regenerating the report.")
                    if st.button("🔄 Try Regenerating Report"):
                        # Force regeneration
                        workflow_orchestrator.current_stage = 'report_generation'
                        result = workflow_orchestrator.execute_workflow("", {})
                        st.session_state.workflow_state = result
                        st.rerun()
            
            # Display automatic QA results if available
            if workflow_orchestrator.workflow.workflow_state.get('automatic_qa_results'):
                automatic_qa = workflow_orchestrator.workflow.workflow_state['automatic_qa_results']
                
                st.divider()
                st.markdown("## 🤖 Automatic QA & Improvements")
                
                if automatic_qa.get('automatic_qa_completed', False):
                    # QA completed successfully
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        content_score = automatic_qa.get('content_qa', {}).get('query_satisfaction_score', 85)
                        st.metric("Content Quality", f"{content_score}%")
                    
                    with col2:
                        structure_score = automatic_qa.get('structure_qa', {}).get('overall_structure_score', 85)
                        st.metric("Structure Quality", f"{structure_score}%")
                    
                    with col3:
                        improvements_count = len(automatic_qa.get('improvements_applied', []))
                        st.metric("Auto Improvements", improvements_count)
                    
                    with col4:
                        final_score = automatic_qa.get('final_verification', {}).get('overall_readiness', 85)
                        st.metric("Overall Readiness", f"{final_score}%")
                    
                    # Show improvements applied
                    if automatic_qa.get('improvements_applied'):
                        with st.expander("📋 Automatic Improvements Applied", expanded=False):
                            for improvement in automatic_qa['improvements_applied']:
                                st.write(f"**{improvement.get('type', 'Unknown').replace('_', ' ').title()}:** {improvement.get('description', 'No description')}")
                    
                    # Show QA timestamp
                    try:
                        qa_time = datetime.fromisoformat(automatic_qa['timestamp']).strftime("%Y-%m-%d %H:%M:%S")
                        st.caption(f"🕒 Automatic QA completed: {qa_time}")
                    except (ValueError, KeyError):
                        st.caption("🕒 Automatic QA completed")
                    
                    if final_score >= 80:
                        st.success("✅ Report passed automatic QA and is ready for use!")
                    elif final_score >= 60:
                        st.warning("⚠️ Report passed automatic QA with minor issues")
                        # Show specific issues for scores 60-79
                        if automatic_qa.get('content_qa', {}).get('issues_identified'):
                            with st.expander("⚠️ Minor Issues Identified", expanded=False):
                                for issue in automatic_qa['content_qa']['issues_identified']:
                                    st.write(f"• **{issue.get('type', 'Issue')}:** {issue.get('description', 'No description')}")
                    else:
                        st.error("❌ Report has quality issues despite automatic improvements")
                        
                        # Show detailed quality issues
                        with st.expander("🔍 Quality Issues Detected", expanded=True):
                            # Content quality issues
                            content_qa = automatic_qa.get('content_qa', {})
                            if content_qa.get('issues_identified'):
                                st.markdown("**Content Quality Issues:**")
                                for issue in content_qa['issues_identified']:
                                    issue_type = issue.get('type', 'Issue').replace('_', ' ').title()
                                    issue_desc = issue.get('description', 'No description')
                                    severity = issue.get('severity', 'medium')
                                    
                                    if severity == 'high':
                                        st.error(f"🔴 **{issue_type}:** {issue_desc}")
                                    elif severity == 'medium':
                                        st.warning(f"🟡 **{issue_type}:** {issue_desc}")
                                    else:
                                        st.info(f"🔵 **{issue_type}:** {issue_desc}")
                            
                            # Structure quality issues
                            structure_qa = automatic_qa.get('structure_qa', {})
                            if structure_qa.get('structural_issues'):
                                st.markdown("**Structure Quality Issues:**")
                                for issue in structure_qa['structural_issues']:
                                    st.write(f"• **{issue.get('section', 'Unknown section')}:** {issue.get('issue', 'No description')}")
                            
                            # Verification issues
                            verification = automatic_qa.get('final_verification', {})
                            if verification.get('remaining_issues'):
                                st.markdown("**Remaining Issues After Improvements:**")
                                for issue in verification['remaining_issues']:
                                    st.write(f"• {issue}")
                            
                            # Missing information
                            if verification.get('missing_critical_info'):
                                st.markdown("**Missing Critical Information:**")
                                for missing in verification['missing_critical_info']:
                                    st.write(f"• {missing}")
                            
                            # If no specific issues found, show general score breakdown
                            if (not content_qa.get('issues_identified') and 
                                not structure_qa.get('structural_issues') and 
                                not verification.get('remaining_issues')):
                                st.markdown("**Score Breakdown:**")
                                st.write(f"• Content Quality: {content_score}%")
                                st.write(f"• Structure Quality: {structure_score}%")
                                st.write(f"• Overall Readiness: {final_score}%")
                                st.info("💡 The low score may be due to missing information or complexity of the research topic. Consider using the manual QA review for more detailed analysis.")
                
                else:
                    # QA failed
                    st.error(f"❌ Automatic QA failed: {automatic_qa.get('error', 'Unknown error')}")
                    st.warning("Using original report without automatic improvements")
            
            # Check if report is incomplete after automatic QA
            final_report_to_check = display_report if display_report else report
            
            # Debug incomplete detection
            if final_report_to_check:
                # print(f"DEBUG: Checking report completeness...")
                # print(f"DEBUG: Report length: {len(final_report_to_check)}")
                # print(f"DEBUG: Report ends with: '{final_report_to_check.strip()[-50:]}'")
                is_incomplete = _is_report_incomplete(final_report_to_check)
                # print(f"DEBUG: Is incomplete: {is_incomplete}")
            
            if final_report_to_check and _is_report_incomplete(final_report_to_check):
                st.divider()
                st.warning("📝 Report appears to be incomplete")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🔄 Complete Report", type="primary", help="Continue generating the incomplete report", key="complete_report_btn"):
                        with st.spinner("Completing report..."):
                            complete_report = _complete_incomplete_report(final_report_to_check, workflow_orchestrator=workflow_orchestrator)
                            if complete_report:
                                # Use the update_report method to properly save and update all state
                                result = workflow_orchestrator.update_report(complete_report)
                                
                                # Update session state with the new result
                                st.session_state.workflow_state = result
                                
                                st.success("✅ Report completed!")
                                time.sleep(0.5)  # Brief pause to ensure UI updates
                                st.rerun()
                            else:
                                st.error("❌ Failed to complete report")
                with col2:
                    if st.button("🔄 Regenerate Entire Report", type="secondary", help="Generate a new report from scratch", key="regenerate_report_btn"):
                        workflow_orchestrator.current_stage = 'report_generation'
                        result = workflow_orchestrator.execute_workflow("", {})
                        st.session_state.workflow_state = result
                        st.rerun()
                with col3:
                    if st.button("📤 Use Partial Report", help="Continue with the incomplete report as-is", key="use_partial_report_btn"):
                        st.info("Using partial report")
            
            # Always show force complete button for report generation control
            st.divider()
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("✅ Force Complete Report", type="secondary", 
                           help="Mark the research as complete and finalize the report", 
                           key="force_complete_report_btn"):
                    try:
                        with st.spinner("Finalizing report..."):
                            # Get the current report and metadata from the current context
                            current_data = workflow_state.get('data', {})
                            if isinstance(current_data, dict):
                                current_report = current_data.get('report', 'No report generated')
                                current_metadata = current_data.get('metadata', {})
                            else:
                                current_report = 'No report generated'
                                current_metadata = {}
                            
                            # Check if report is stored directly in workflow state
                            if (not current_report or current_report == 'No report generated') and workflow_orchestrator:
                                orchestrator_report = workflow_orchestrator.workflow.workflow_state.get('final_report')
                                if orchestrator_report:
                                    current_report = orchestrator_report
                                    # Generate metadata if needed
                                    current_metadata = {
                                        'generated_at': datetime.now().isoformat(),
                                        'subtasks_completed': len(workflow_orchestrator.workflow.workflow_state.get('subtasks', [])),
                                        'documents_analyzed': workflow_orchestrator.workflow._count_analyzed_documents() if hasattr(workflow_orchestrator.workflow, '_count_analyzed_documents') else 0
                                    }
                            
                            # Determine which report to use
                            final_report = current_report  # Start with current report
                            
                            # Check if we have a manually improved report
                            if 'manual_improvement_applied' in st.session_state:
                                final_report = st.session_state.manual_improvement_applied.get('improved_report', current_report)
                            
                            # Check if we have an automatically improved report
                            elif workflow_orchestrator and hasattr(workflow_orchestrator.workflow, 'workflow_state'):
                                auto_qa = workflow_orchestrator.workflow.workflow_state.get('automatic_qa_results', {})
                                if auto_qa.get('automatic_qa_completed') and auto_qa.get('improved_report'):
                                    final_report = auto_qa['improved_report']
                            
                            # Ensure we have a report
                            if not final_report or final_report == 'No report generated':
                                st.error("❌ No report found to finalize!")
                                st.stop()
                            
                            # Update workflow state to mark as complete
                            workflow_orchestrator.workflow.workflow_state['report_completed'] = True
                            workflow_orchestrator.workflow.workflow_state['force_completed'] = True
                            workflow_orchestrator.workflow.workflow_state['final_report'] = final_report
                            
                            # Save the final report state
                            workflow_persistence.save_workflow_state(workflow_orchestrator.workflow.workflow_state)
                            
                            # Create a complete workflow result
                            result = {
                                'stage': 'complete',
                                'data': {
                                    'report': final_report,
                                    'metadata': current_metadata,
                                    'forced_complete': True
                                },
                                'next_action': 'Research complete (forced)'
                            }
                            
                            # Update session state
                            st.session_state.workflow_state = result
                            st.success("✅ Report marked as complete!")
                            time.sleep(0.5)
                            st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error completing report: {str(e)}")
                        import traceback
                        st.error(traceback.format_exc())
            
            # Display manual QA results if available
            if 'manual_qa_results' in st.session_state:
                st.divider()
                st.markdown("## 🔍 Manual QA Review Results")
                
                qa_results = st.session_state.manual_qa_results
                qa_timestamp = st.session_state.get('manual_qa_timestamp', datetime.now())
                
                st.caption(f"📅 QA Review completed: {qa_timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
                
                # QA metrics in expandable section
                with st.expander("📊 Quality Assessment Metrics", expanded=True):
                    # Overall metrics
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        overall_score = qa_results.get('overall_score', 0) * 100
                        st.metric("Overall Quality", f"{overall_score:.0f}%")
                    with col2:
                        qa_confidence = qa_results.get('confidence', 0) * 100
                        st.metric("QA Confidence", f"{qa_confidence:.0f}%")
                    with col3:
                        trust_score = qa_results.get('trust_score', 0) * 100
                        st.metric("Trust Score", f"{trust_score:.0f}%")
                    with col4:
                        accuracy_issues = len(qa_results.get('inaccurate_or_confusing_sections', []))
                        structural_issues = len(qa_results.get('structural_issues', []))
                        total_issues = accuracy_issues + structural_issues
                        st.metric("Issues Found", total_issues)
                    
                    # Show trust/fix decision information
                    if qa_results.get('fix_decision_reasoning'):
                        st.markdown("**QA Decision Analysis:**")
                        
                        # Display fix recommendation status
                        if qa_results.get('auto_fix_recommended'):
                            st.success("✅ **Auto-fix Recommended** - High confidence fixes could be applied automatically")
                        elif qa_results.get('suggest_review'):
                            st.info("⚠️ **Suggest Review** - Moderate confidence, suitable for review")
                        elif qa_results.get('manual_review_required'):
                            st.warning("🔍 **Manual Review Required** - Complex issues need human attention")
                        
                        # Show reasoning
                        for reason in qa_results['fix_decision_reasoning']:
                            st.write(f"• {reason}")
                    
                    # Layer-specific scores
                    if qa_results.get('layer_scores'):
                        st.markdown("**Quality by Category:**")
                        layer_cols = st.columns(len(qa_results['layer_scores']))
                        for i, (layer, layer_data) in enumerate(qa_results['layer_scores'].items()):
                            with layer_cols[i]:
                                score = layer_data.get('score', 0) * 100
                                st.metric(layer.title(), f"{score:.0f}%")
                
                # Issues and recommendations
                if qa_results.get('inaccurate_or_confusing_sections'):
                    with st.expander("⚠️ Issues & Recommendations", expanded=False):
                        # Add "Select Issues to Apply" section at the top
                        st.markdown("**Select Issues to Apply:**")
                        col_select_all, col_apply_selected = st.columns([2, 1])
                        
                        with col_select_all:
                            select_all = st.checkbox("Select All Issues", key=get_unique_key("select_all_issues"))
                        
                        # Track selected issues
                        selected_issues = []
                        selected_custom_instructions = {}
                        
                        st.divider()
                        
                        for i, issue in enumerate(qa_results['inaccurate_or_confusing_sections']):
                            # Issue header with checkbox
                            col_check, col_title = st.columns([0.5, 4])
                            
                            with col_check:
                                issue_selected = st.checkbox(
                                    "", 
                                    value=select_all,
                                    key=get_unique_key(f"select_issue_{i}"),
                                    help=f"Select Issue {i+1} for batch application"
                                )
                            
                            with col_title:
                                st.markdown(f"**Issue {i+1}: {issue.get('section_title', 'General')}**")
                            
                            st.write(f"**Problem:** {issue.get('issue', 'Not specified')}")
                            if issue.get('suggested_fix'):
                                st.write(f"**Suggested Fix:** {issue.get('suggested_fix')}")
                            
                            # Custom instruction input and apply buttons
                            col1, col2, col3 = st.columns([3, 1, 1])
                            
                            with col1:
                                custom_instruction = st.text_area(
                                    f"Custom instructions for Issue {i+1}:",
                                    placeholder=f"Optional: Provide specific instructions for fixing this issue...\ne.g., 'Fix the lack of explicit intro and conclusion sections, make headings clearer'",
                                    height=80,
                                    key=get_unique_key(f"custom_instruction_{i}"),
                                    help="Leave empty to use the suggested fix, or provide your own specific instructions"
                                )
                            
                            # Track selected issues and their custom instructions
                            if issue_selected:
                                # Create a copy of the issue with custom instructions if provided
                                issue_copy = issue.copy()
                                if custom_instruction and custom_instruction.strip():
                                    issue_copy['custom_instruction'] = custom_instruction.strip()
                                selected_issues.append(issue_copy)
                                if custom_instruction and custom_instruction.strip():
                                    selected_custom_instructions[i] = custom_instruction.strip()
                            
                            with col2:
                                # Apply with suggested fix using structured approach
                                if st.button(f"🔧 Apply Suggested", key=get_unique_key(f"apply_suggested_{i}"), help=f"Apply suggested fix for Issue {i+1}"):
                                    with st.spinner(f"Applying suggested fix for Issue {i+1} using structured approach..."):
                                        try:
                                            from utils.structured_qa_integration import StructuredQAManager, create_llm_improvement_function
                                            from utils.llm_utils import _call_llm_api
                                            from utils.document_wide_improvements import apply_document_wide_improvements
                                            
                                            # Get current report
                                            current_report = report
                                            if 'manual_improvement_applied' in st.session_state:
                                                current_report = st.session_state.manual_improvement_applied['improved_report']
                                            
                                            # Initialize structured QA manager
                                            workspace_path = Path("research_workspace") / st.session_state.get('current_session_directory', '')
                                            qa_manager = StructuredQAManager(workspace_path)
                                            
                                            # Import current report into structured system
                                            structured_doc = qa_manager.import_existing_report(current_report, "final_report")
                                            
                                            # Convert single issue to structured format
                                            section_title = issue.get('section_title', 'General')
                                            issue_desc = issue.get('issue', '')
                                            
                                            print(f"DEBUG: Section title: '{section_title}'")
                                            print(f"DEBUG: Issue: {issue_desc}")
                                            
                                            # Check if this is a document-wide issue using the DocumentWideImprover
                                            from utils.document_wide_improvements import document_improver
                                            
                                            # Use both section title and issue description to detect document-wide issues
                                            issue_title = f"{section_title}: {issue_desc}"
                                            is_document_wide = document_improver.can_handle_issue(issue_title)
                                            
                                            # Also check for specific structural indicators
                                            is_structural = (
                                                section_title in ['Structure', 'General', 'Overall organization'] or
                                                'structure' in issue_desc.lower() or
                                                'organization' in issue_desc.lower() or
                                                'introduction' in issue_desc.lower() or
                                                'conclusion' in issue_desc.lower() or
                                                'overview' in issue_desc.lower() or
                                                'flow' in issue_desc.lower() or
                                                'multiple sections' in issue_desc.lower() or
                                                'document' in issue_desc.lower()
                                            )
                                            
                                            is_document_wide = is_document_wide or is_structural
                                            
                                            if is_document_wide:
                                                print("DEBUG: Detected document-wide issue")
                                                
                                                # Apply document-wide improvements
                                                result = apply_document_wide_improvements(
                                                    document_content=current_report,
                                                    qa_results={'inaccurate_or_confusing_sections': [issue]},
                                                    llm_function=_call_llm_api,
                                                    custom_instructions=custom_instruction if custom_instruction and custom_instruction.strip() else None
                                                )
                                                
                                                if result.get('status') == 'improved':
                                                    improved_report = result['improved']
                                                    verification = result.get('verification', {})
                                                    
                                                    # Update workflow state
                                                    try:
                                                        if ('workflow_state' in st.session_state and 
                                                            st.session_state.workflow_state is not None and
                                                            'data' in st.session_state.workflow_state):
                                                            if isinstance(st.session_state.workflow_state['data'], dict):
                                                                st.session_state.workflow_state['data']['report'] = improved_report
                                                    except Exception as e:
                                                        print(f"Warning: Could not update workflow state: {e}")
                                                    
                                                    # Store improvement info
                                                    st.session_state.manual_improvement_applied = {
                                                        'original_report': current_report,
                                                        'improved_report': improved_report,
                                                        'improvements_made': result.get('changes_made', []),
                                                        'score_improvement': verification.get('verification_score', 0),
                                                        'timestamp': datetime.now(),
                                                        'selected_issues_count': 1,
                                                        'custom_instructions_count': 1 if custom_instruction else 0,
                                                        'method': 'document_wide',
                                                        'verification': verification
                                                    }
                                                    
                                                    st.success(f"✅ Applied document-wide structural improvements")
                                                    
                                                    # Show verification results
                                                    if verification:
                                                        st.markdown("**📊 Verification Results:**")
                                                        col1, col2 = st.columns(2)
                                                        with col1:
                                                            st.metric("Verification Score", f"{verification.get('verification_score', 0) * 100:.0f}%")
                                                        with col2:
                                                            st.metric("Issues Addressed", "✅" if verification.get('all_issues_addressed') else "⚠️")
                                                        
                                                        if verification.get('summary'):
                                                            st.write("**Summary:** " + verification['summary'])
                                                    
                                                    st.rerun()
                                                else:
                                                    st.warning(f"⚠️ No structural changes made")
                                                    print(f"DEBUG: Document-wide result: {result}")
                                                
                                                # Skip the rest of the section-based logic
                                                continue
                                            
                                            # Original section-based logic for non-structural issues
                                            print(f"DEBUG: Looking for section '{section_title}'")
                                            print(f"DEBUG: Available sections: {[s.title for s in structured_doc.sections.values()]}")
                                            
                                            # Special handling for QA category labels like "Structure", "Clarity", etc.
                                            section_id = None
                                            if section_title in ['Structure', 'Clarity', 'Accuracy', 'Style', 'General']:
                                                # These are QA categories, not actual sections
                                                # Try to find the section mentioned in the issue description
                                                issue_desc = issue.get('issue', '')
                                                
                                                # Look for "Section X" patterns in the issue
                                                import re
                                                section_match = re.search(r'Section (\d+)', issue_desc)
                                                if section_match:
                                                    section_num = section_match.group(1)
                                                    # Find section with this number
                                                    for sid, section in structured_doc.sections.items():
                                                        if f"Section {section_num}" in section.title:
                                                            section_id = sid
                                                            print(f"DEBUG: Found section by number: {section.title}")
                                                            break
                                                
                                                # If still not found, check the first major section
                                                if not section_id:
                                                    for sid, section in structured_doc.sections.items():
                                                        if section.level == 2 and "Section" in section.title:
                                                            section_id = sid
                                                            print(f"DEBUG: Using first major section: {section.title}")
                                                            break
                                            else:
                                                # Normal section title lookup
                                                section_id = qa_manager.find_section_by_title(structured_doc, section_title)
                                            
                                            print(f"DEBUG: Found section ID: {section_id}")
                                            
                                            if section_id:
                                                issue_id = structured_doc.add_qa_issue(
                                                    section_id=section_id,
                                                    issue_type=qa_manager.classify_issue_type(issue.get('issue', '')),
                                                    description=issue.get('issue', ''),
                                                    suggested_fix=issue.get('suggested_fix', '')
                                                )
                                                
                                                # Create LLM function
                                                try:
                                                    llm_function = create_llm_improvement_function(_call_llm_api)
                                                    print("DEBUG: LLM function created successfully")
                                                except Exception as e:
                                                    print(f"DEBUG: Failed to create LLM function: {e}")
                                                    st.error(f"❌ Failed to create LLM function: {str(e)}")
                                                    continue
                                                
                                                # Apply fix for just this issue
                                                result = qa_manager.apply_selective_fixes(
                                                    document_id="final_report",
                                                    selected_issue_ids=[issue_id],
                                                    llm_function=llm_function
                                                )
                                                
                                                if result.get('status') == 'improved':
                                                    # Update workflow state
                                                    try:
                                                        if ('workflow_state' in st.session_state and 
                                                            st.session_state.workflow_state is not None and
                                                            'data' in st.session_state.workflow_state):
                                                            if isinstance(st.session_state.workflow_state['data'], dict):
                                                                st.session_state.workflow_state['data']['report'] = result['improved_report']
                                                    except Exception as e:
                                                        print(f"Warning: Could not update workflow state: {e}")
                                                    
                                                    # Store improvement info
                                                    st.session_state.manual_improvement_applied = {
                                                        'original_report': current_report,
                                                        'improved_report': result['improved_report'],
                                                        'improvements_made': result.get('improvements_made', []),
                                                        'score_improvement': 0,
                                                        'timestamp': datetime.now(),
                                                        'selected_issues_count': 1,
                                                        'custom_instructions_count': 0,
                                                        'sections_modified': result.get('sections_modified', []),
                                                        'method': 'structured_qa'
                                                    }
                                                    
                                                    st.success(f"✅ Applied suggested fix for Issue {i+1}")
                                                    st.rerun()
                                                else:
                                                    st.warning(f"⚠️ No changes made for Issue {i+1}")
                                                    print(f"DEBUG: Result status: {result.get('status')}")
                                                    print(f"DEBUG: Result message: {result.get('message', 'No message')}")
                                                    if result.get('status') == 'no_changes':
                                                        st.info("💡 The LLM may have determined that no changes were needed, or returned the same content.")
                                            else:
                                                st.error(f"❌ Could not find section for issue. Section title: '{section_title}'")
                                                
                                                # Check if this could be handled as document-wide issue
                                                from utils.document_wide_improvements import document_improver
                                                issue_title = f"{section_title}: {issue_desc}"
                                                if document_improver.can_handle_issue(issue_title):
                                                    st.info("💡 This appears to be a document-wide issue. Try using the batch application feature to apply document-wide improvements.")
                                                elif section_title in ['Structure', 'Clarity', 'Accuracy', 'Style', 'General']:
                                                    st.info("💡 This appears to be a QA category label. The issue description should indicate which section needs improvement, or it may be a document-wide issue.")
                                                else:
                                                    st.info("💡 Section not found. This might be a document-wide issue that affects multiple sections.")
                                                
                                        except Exception as e:
                                            st.error(f"❌ Failed to apply fix: {str(e)}")
                                            import traceback
                                            print(traceback.format_exc())
                            
                            with col3:
                                # Apply with custom instruction using structured approach
                                if custom_instruction and custom_instruction.strip():
                                    if st.button(f"🛠️ Apply Custom", key=get_unique_key(f"apply_custom_{i}"), help=f"Apply custom fix for Issue {i+1}"):
                                        with st.spinner(f"Applying custom fix for Issue {i+1} using structured approach..."):
                                            try:
                                                from utils.structured_qa_integration import StructuredQAManager, create_llm_improvement_function
                                                from utils.llm_utils import _call_llm_api
                                                
                                                # Get current report
                                                current_report = report
                                                if 'manual_improvement_applied' in st.session_state:
                                                    current_report = st.session_state.manual_improvement_applied['improved_report']
                                                
                                                # Initialize structured QA manager
                                                workspace_path = Path("research_workspace") / st.session_state.get('current_session_directory', '')
                                                qa_manager = StructuredQAManager(workspace_path)
                                                
                                                # Import current report into structured system
                                                structured_doc = qa_manager.import_existing_report(current_report, "final_report")
                                                
                                                # Convert single issue to structured format
                                                section_title = issue.get('section_title', 'General')
                                                issue_desc = issue.get('issue', '')
                                                
                                                # Check if this is a document-wide issue
                                                from utils.document_wide_improvements import document_improver
                                                issue_title = f"{section_title}: {issue_desc}"
                                                is_document_wide = document_improver.can_handle_issue(issue_title)
                                                
                                                # Also check for specific structural indicators
                                                is_structural = (
                                                    section_title in ['Structure', 'General', 'Overall organization'] or
                                                    'structure' in issue_desc.lower() or
                                                    'organization' in issue_desc.lower() or
                                                    'introduction' in issue_desc.lower() or
                                                    'conclusion' in issue_desc.lower() or
                                                    'overview' in issue_desc.lower() or
                                                    'flow' in issue_desc.lower() or
                                                    'multiple sections' in issue_desc.lower() or
                                                    'document' in issue_desc.lower()
                                                )
                                                
                                                is_document_wide = is_document_wide or is_structural
                                                
                                                if is_document_wide:
                                                    print("DEBUG: Custom instruction - detected document-wide issue")
                                                    
                                                    # Apply document-wide improvements with custom instruction
                                                    from utils.document_wide_improvements import apply_document_wide_improvements
                                                    
                                                    result = apply_document_wide_improvements(
                                                        document_content=current_report,
                                                        qa_results={'inaccurate_or_confusing_sections': [issue]},
                                                        llm_function=_call_llm_api,
                                                        custom_instructions=custom_instruction.strip()
                                                    )
                                                    
                                                    if result.get('status') == 'improved':
                                                        improved_report = result['improved']
                                                        verification = result.get('verification', {})
                                                        
                                                        # Update workflow state
                                                        try:
                                                            if ('workflow_state' in st.session_state and 
                                                                st.session_state.workflow_state is not None and
                                                                'data' in st.session_state.workflow_state):
                                                                if isinstance(st.session_state.workflow_state['data'], dict):
                                                                    st.session_state.workflow_state['data']['report'] = improved_report
                                                        except Exception as e:
                                                            print(f"Warning: Could not update workflow state: {e}")
                                                        
                                                        # Store improvement info
                                                        st.session_state.manual_improvement_applied = {
                                                            'original_report': current_report,
                                                            'improved_report': improved_report,
                                                            'improvements_made': result.get('changes_made', []),
                                                            'score_improvement': verification.get('verification_score', 0),
                                                            'timestamp': datetime.now(),
                                                            'selected_issues_count': 1,
                                                            'custom_instructions_count': 1,
                                                            'method': 'document_wide_custom',
                                                            'verification': verification
                                                        }
                                                        
                                                        st.success(f"✅ Applied custom document-wide improvements")
                                                        
                                                        # Show verification results
                                                        if verification:
                                                            st.markdown("**📊 Verification Results:**")
                                                            col1, col2 = st.columns(2)
                                                            with col1:
                                                                st.metric("Verification Score", f"{verification.get('verification_score', 0) * 100:.0f}%")
                                                            with col2:
                                                                st.metric("Issues Addressed", "✅" if verification.get('all_issues_addressed') else "⚠️")
                                                            
                                                            if verification.get('summary'):
                                                                st.write("**Summary:** " + verification['summary'])
                                                        
                                                        st.rerun()
                                                    else:
                                                        st.warning(f"⚠️ No custom changes made")
                                                    
                                                    # Skip the rest of the section-based logic
                                                else:
                                                    # Section-based logic for non-document-wide issues
                                                    section_id = qa_manager.find_section_by_title(structured_doc, section_title)
                                                    
                                                    if section_id:
                                                        issue_id = structured_doc.add_qa_issue(
                                                            section_id=section_id,
                                                            issue_type=qa_manager.classify_issue_type(issue.get('issue', '')),
                                                            description=issue.get('issue', ''),
                                                            suggested_fix=issue.get('suggested_fix', '')
                                                        )
                                                        
                                                        # Create LLM function
                                                        llm_function = create_llm_improvement_function(_call_llm_api)
                                                        
                                                        # Apply fix with custom instruction
                                                        result = qa_manager.apply_selective_fixes(
                                                            document_id="final_report",
                                                            selected_issue_ids=[issue_id],
                                                            llm_function=llm_function,
                                                            custom_instructions={issue_id: custom_instruction.strip()}
                                                        )
                                                        
                                                        if result.get('status') == 'improved':
                                                            # Update workflow state
                                                            try:
                                                                if ('workflow_state' in st.session_state and 
                                                                    st.session_state.workflow_state is not None and
                                                                    'data' in st.session_state.workflow_state):
                                                                    if isinstance(st.session_state.workflow_state['data'], dict):
                                                                        st.session_state.workflow_state['data']['report'] = result['improved_report']
                                                            except Exception as e:
                                                                print(f"Warning: Could not update workflow state: {e}")
                                                            
                                                            # Store improvement info
                                                            st.session_state.manual_improvement_applied = {
                                                                'original_report': current_report,
                                                                'improved_report': result['improved_report'],
                                                                'improvements_made': result.get('improvements_made', []),
                                                                'score_improvement': 0,
                                                                'timestamp': datetime.now(),
                                                                'selected_issues_count': 1,
                                                                'custom_instructions_count': 1,
                                                                'sections_modified': result.get('sections_modified', []),
                                                                'method': 'structured_qa'
                                                            }
                                                            
                                                            st.success(f"✅ Applied custom fix for Issue {i+1}")
                                                            st.rerun()
                                                        else:
                                                            st.warning(f"⚠️ No changes made for Issue {i+1}")
                                                    else:
                                                        st.error(f"❌ Could not find section '{section_title}' in document")
                                                        
                                                        # Check if this could be handled as document-wide issue
                                                        from utils.document_wide_improvements import document_improver
                                                        issue_title = f"{section_title}: {issue_desc}"
                                                        if document_improver.can_handle_issue(issue_title):
                                                            st.info("💡 This appears to be a document-wide issue. Try using the batch application feature to apply document-wide improvements.")
                                                        elif section_title in ['Structure', 'Clarity', 'Accuracy', 'Style', 'General']:
                                                            st.info("💡 This appears to be a QA category label. The issue description should indicate which section needs improvement, or it may be a document-wide issue.")
                                                        else:
                                                            st.info("💡 Section not found. This might be a document-wide issue that affects multiple sections.")
                                                    
                                            except Exception as e:
                                                st.error(f"❌ Failed to apply fix: {str(e)}")
                                                import traceback
                                                print(traceback.format_exc())
                                            
                                            # Skip to next iteration if structural issue was handled
                                            if is_structural:
                                                continue
                                else:
                                    st.button(f"🛠️ Apply Custom", disabled=True, key=get_unique_key(f"apply_custom_disabled_{i}"), help="Enter custom instructions first")
                            
                            if i < len(qa_results['inaccurate_or_confusing_sections']) - 1:
                                st.divider()
                        
                        # Display structural issues separately if they exist
                        if qa_results.get('structural_issues'):
                            st.divider()
                            st.markdown("### 🏗️ Structural Issues")
                            st.markdown("Issues related to document organization, flow, and structure:")
                            
                            for j, structural_issue in enumerate(qa_results['structural_issues']):
                                issue_num = len(qa_results.get('inaccurate_or_confusing_sections', [])) + j + 1
                                
                                # Structural issue header with checkbox
                                col_check, col_title = st.columns([0.5, 4])
                                
                                with col_check:
                                    structural_selected = st.checkbox(
                                        "", 
                                        value=select_all,
                                        key=get_unique_key(f"select_structural_{j}"),
                                        help=f"Select Structural Issue {j+1} for batch application"
                                    )
                                
                                with col_title:
                                    st.markdown(f"**Structural Issue {j+1}: {structural_issue.get('section_title', 'Structure')}**")
                                
                                st.write(f"**Problem:** {structural_issue.get('issue', 'Not specified')}")
                                if structural_issue.get('suggested_fix'):
                                    st.write(f"**Suggested Fix:** {structural_issue.get('suggested_fix')}")
                                
                                if structural_selected:
                                    selected_issues.append(structural_issue)
                                
                                # Custom instruction for structural issue
                                col1, col2, col3 = st.columns([3, 1, 1])
                                
                                with col1:
                                    structural_custom_instruction = st.text_area(
                                        f"Custom instructions for Structural Issue {j+1}:",
                                        placeholder=f"Optional: Provide specific instructions for fixing this structural issue...\ne.g., 'Add proper introduction and conclusion sections, reorganize content flow'",
                                        height=80,
                                        key=get_unique_key(f"structural_custom_instruction_{j}"),
                                        help="Leave empty to use the suggested fix, or provide your own specific instructions"
                                    )
                                
                                if j < len(qa_results['structural_issues']) - 1:
                                    st.divider()
                        
                        # Update the apply selected button in the header
                        with col_apply_selected:
                            if selected_issues:
                                if st.button(f"🚀 Apply {len(selected_issues)} Selected", type="primary", help=f"Apply fixes for {len(selected_issues)} selected issues using the reliable Force Apply method"):
                                    st.session_state['apply_selected_clicked'] = True
                                    st.rerun()
                            else:
                                st.button("🚀 Apply Selected", disabled=True, help="Select issues first")
                        
                        # Handle Apply Selected button click with structured approach
                        if st.session_state.get('apply_selected_clicked', False):
                            st.session_state['apply_selected_clicked'] = False  # Reset the flag
                            
                            if selected_issues:
                                with st.spinner(f"Applying {len(selected_issues)} selected issue fixes using structured approach..."):
                                    try:
                                        from utils.structured_qa_integration import StructuredQAManager, create_llm_improvement_function
                                        from utils.llm_utils import _call_llm_api
                                        
                                        # Get current report
                                        current_report = report
                                        if 'manual_improvement_applied' in st.session_state:
                                            current_report = st.session_state.manual_improvement_applied['improved_report']
                                        
                                        # Initialize structured QA manager
                                        workspace_path = Path("research_workspace") / st.session_state.get('current_session_directory', '')
                                        qa_manager = StructuredQAManager(workspace_path)
                                        
                                        # Create document ID from current session
                                        document_id = "final_report"
                                        
                                        # Import current report into structured system
                                        structured_doc = qa_manager.import_existing_report(current_report, document_id)
                                        
                                        # Convert selected issues to structured format
                                        selected_issue_ids = []
                                        custom_instructions_map = {}
                                        
                                        for i, issue in enumerate(selected_issues):
                                            # Find or create structured issue
                                            section_title = issue.get('section_title', 'General')
                                            section_id = qa_manager.find_section_by_title(structured_doc, section_title)
                                            
                                            if section_id:
                                                issue_id = structured_doc.add_qa_issue(
                                                    section_id=section_id,
                                                    issue_type=qa_manager.classify_issue_type(issue.get('issue', '')),
                                                    description=issue.get('issue', ''),
                                                    suggested_fix=issue.get('suggested_fix', '')
                                                )
                                                selected_issue_ids.append(issue_id)
                                                
                                                # Add custom instruction if provided
                                                if issue.get('custom_instruction'):
                                                    custom_instructions_map[issue_id] = issue['custom_instruction']
                                        
                                        if selected_issue_ids:
                                            # Create LLM function for structured QA
                                            llm_function = create_llm_improvement_function(_call_llm_api)
                                            
                                            # Apply selective fixes using structured approach
                                            result = qa_manager.apply_selective_fixes(
                                                document_id=document_id,
                                                selected_issue_ids=selected_issue_ids,
                                                llm_function=llm_function,
                                                custom_instructions=custom_instructions_map
                                            )
                                            
                                            if result.get('status') == 'improved':
                                                improved_report = result['improved_report']
                                                
                                                # Update the workflow state with improved report (safely)
                                                try:
                                                    if ('workflow_state' in st.session_state and 
                                                        st.session_state.workflow_state is not None and
                                                        'data' in st.session_state.workflow_state):
                                                        if isinstance(st.session_state.workflow_state['data'], dict):
                                                            st.session_state.workflow_state['data']['report'] = improved_report
                                                except Exception as e:
                                                    print(f"Warning: Could not update workflow state: {e}")
                                                
                                                # Store improvement info
                                                st.session_state.manual_improvement_applied = {
                                                    'original_report': current_report,
                                                    'improved_report': improved_report,
                                                    'improvements_made': result.get('improvements_made', []),
                                                    'score_improvement': 0,  # Could calculate this
                                                    'timestamp': datetime.now(),
                                                    'selected_issues_count': len(selected_issues),
                                                    'custom_instructions_count': len(selected_custom_instructions),
                                                    'sections_modified': result.get('sections_modified', []),
                                                    'method': 'structured_qa'
                                                }
                                                
                                                st.success(f"✅ Applied fixes for {len(selected_issues)} selected issues using structured approach!")
                                                st.rerun()
                                            else:
                                                st.warning("⚠️ No improvements were applied. The selected issues may already be resolved.")
                                        else:
                                            st.warning("⚠️ Could not map selected issues to document sections.")
                                                
                                    except Exception as e:
                                        st.error(f"❌ Failed to apply selected issue fixes: {str(e)}")
                                        import traceback
                                        print(f"Detailed error: {traceback.format_exc()}")
                        
                        
                
                # Layer-specific details
                if qa_results.get('layer_scores'):
                    with st.expander("📋 Detailed Layer Analysis", expanded=False):
                        for layer, layer_data in qa_results['layer_scores'].items():
                            st.markdown(f"### {layer.title()} Analysis")
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                score = layer_data.get('score', 0) * 100
                                st.metric("Score", f"{score:.0f}%")
                            with col2:
                                issues_count = len(layer_data.get('issues', []))
                                st.metric("Issues", issues_count)
                            
                            if layer_data.get('issues'):
                                st.markdown("**Issues:**")
                                for idx, issue in enumerate(layer_data['issues']):
                                    st.write(f"• {issue}")
                                    
                                    # Custom instruction for layer issue
                                    layer_col1, layer_col2, layer_col3 = st.columns([3, 1, 1])
                                    
                                    with layer_col1:
                                        layer_custom_instruction = st.text_input(
                                            f"Custom fix for {layer} issue {idx+1}:",
                                            placeholder=f"Optional: Custom instruction for this {layer} issue...",
                                            key=get_unique_key(f"layer_custom_{layer}_{idx}"),
                                            help="Leave empty to use default fix"
                                        )
                                    
                                    with layer_col2:
                                        # Apply suggested fix for layer issue
                                        if st.button("🔧 Default", key=get_unique_key(f"apply_layer_default_{layer}_{idx}"), help=f"Apply default fix for {layer} issue"):
                                            with st.spinner(f"Applying {layer} fix..."):
                                                try:
                                                    from utils.intelligent_search_enhanced import get_enhanced_search_engine
                                                    search_engine = get_enhanced_search_engine()
                                                    
                                                    if hasattr(search_engine, 'improvement_pipeline') and search_engine.improvement_pipeline is not None:
                                                        # Get current report
                                                        current_report = report
                                                        if 'manual_improvement_applied' in st.session_state:
                                                            current_report = st.session_state.manual_improvement_applied['improved_report']
                                                        
                                                        # Create a synthetic issue for layer-specific fixes
                                                        synthetic_issue = {
                                                            'section_title': f"{layer.title()} Issue",
                                                            'issue': issue,
                                                            'suggested_fix': f"Address {layer} concern: {issue}"
                                                        }
                                                        
                                                        sources = [{"title": "Layer-specific QA Fix", "content": {"body": f"{layer} improvement"}, "author": "User", "category": "QA"}]
                                                        improved_report, improvements_made, error = safe_improvement_pipeline_call(
                                                            search_engine,
                                                            current_report, 
                                                            [synthetic_issue],
                                                            sources,
                                                            f"Fix for {layer} issue: {issue[:50]}..."
                                                        )
                                                        
                                                        if error:
                                                            st.error(f"❌ Failed to apply {layer} fix: {error}")
                                                            continue
                                                        
                                                        if improved_report != current_report:
                                                            # Use helper function to update session state
                                                            fix_details = {
                                                                'layer': layer,
                                                                'issue': issue,
                                                                'fix_type': 'default',
                                                                'fix_applied': datetime.now()
                                                            }
                                                            
                                                            # Get the truly original report (before any improvements)
                                                            original_report = report
                                                            if 'manual_improvement_applied' in st.session_state:
                                                                original_report = st.session_state.manual_improvement_applied.get('original_report', report)
                                                            
                                                            update_improvement_session_state(
                                                                original_report, 
                                                                improved_report, 
                                                                improvements_made, 
                                                                'layer', 
                                                                fix_details
                                                            )
                                                            
                                                            # Update workflow state
                                                            try:
                                                                if ('workflow_state' in st.session_state and 
                                                                    st.session_state.workflow_state is not None and
                                                                    'data' in st.session_state.workflow_state and
                                                                    isinstance(st.session_state.workflow_state['data'], dict)):
                                                                    st.session_state.workflow_state['data']['report'] = improved_report
                                                            except Exception as e:
                                                                print(f"Warning: Could not update workflow state: {e}")
                                                            
                                                            st.success(f"✅ Applied {layer} fix")
                                                            st.rerun()
                                                        else:
                                                            st.warning(f"⚠️ No changes made for {layer} issue")
                                                    else:
                                                        st.error("❌ Improvement pipeline not available")
                                                except Exception as e:
                                                    st.error(f"❌ Failed to apply {layer} fix: {str(e)}")
                                    
                                    with layer_col3:
                                        # Apply custom fix for layer issue
                                        layer_custom_disabled = not layer_custom_instruction.strip()
                                        if st.button("✏️ Custom", key=get_unique_key(f"apply_layer_custom_{layer}_{idx}"), 
                                                   disabled=layer_custom_disabled,
                                                   help=f"Apply custom fix for {layer} issue" if not layer_custom_disabled else "Enter custom instruction first"):
                                            with st.spinner(f"Applying custom {layer} fix..."):
                                                try:
                                                    from utils.intelligent_search_enhanced import get_enhanced_search_engine
                                                    search_engine = get_enhanced_search_engine()
                                                    
                                                    if hasattr(search_engine, 'improvement_pipeline') and search_engine.improvement_pipeline is not None:
                                                        # Get current report
                                                        current_report = report
                                                        if 'manual_improvement_applied' in st.session_state:
                                                            current_report = st.session_state.manual_improvement_applied['improved_report']
                                                        
                                                        # Create custom synthetic issue with user's instruction
                                                        custom_synthetic_issue = {
                                                            'section_title': f"{layer.title()} Issue",
                                                            'issue': issue,
                                                            'suggested_fix': layer_custom_instruction.strip()
                                                        }
                                                        
                                                        sources = [{"title": "Layer-specific QA Fix - Custom", "content": {"body": f"{layer} custom improvement"}, "author": "User", "category": "QA"}]
                                                        improved_report, improvements_made, error = safe_improvement_pipeline_call(
                                                            search_engine,
                                                            current_report, 
                                                            [custom_synthetic_issue],
                                                            sources,
                                                            f"Custom fix for {layer} issue: {layer_custom_instruction[:50]}..."
                                                        )
                                                        
                                                        if error:
                                                            st.error(f"❌ Failed to apply custom {layer} fix: {error}")
                                                            continue
                                                        
                                                        if improved_report != current_report:
                                                            # Use helper function to update session state
                                                            fix_details = {
                                                                'layer': layer,
                                                                'issue': issue,
                                                                'fix_type': 'custom',
                                                                'custom_instruction': layer_custom_instruction.strip(),
                                                                'fix_applied': datetime.now()
                                                            }
                                                            
                                                            # Get the truly original report (before any improvements)
                                                            original_report = report
                                                            if 'manual_improvement_applied' in st.session_state:
                                                                original_report = st.session_state.manual_improvement_applied.get('original_report', report)
                                                            
                                                            update_improvement_session_state(
                                                                original_report, 
                                                                improved_report, 
                                                                improvements_made, 
                                                                'layer', 
                                                                fix_details
                                                            )
                                                            
                                                            # Update workflow state
                                                            try:
                                                                if ('workflow_state' in st.session_state and 
                                                                    st.session_state.workflow_state is not None and
                                                                    'data' in st.session_state.workflow_state and
                                                                    isinstance(st.session_state.workflow_state['data'], dict)):
                                                                    st.session_state.workflow_state['data']['report'] = improved_report
                                                            except Exception as e:
                                                                print(f"Warning: Could not update workflow state: {e}")
                                                            
                                                            st.success(f"✅ Applied custom {layer} fix")
                                                            st.rerun()
                                                        else:
                                                            st.warning(f"⚠️ No changes made for {layer} issue")
                                                    else:
                                                        st.error("❌ Improvement pipeline not available")
                                                except Exception as e:
                                                    st.error(f"❌ Failed to apply custom {layer} fix: {str(e)}")
                                    
                                    st.markdown("---")
                            
                            if layer_data.get('strengths'):
                                st.markdown("**Strengths:**")
                                for strength in layer_data['strengths']:
                                    st.write(f"• {strength}")
                            
                            st.divider()
                
                # Action buttons for QA results
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    # Apply improvements if QA suggests fixes OR manual override
                    has_issues = qa_results.get('inaccurate_or_confusing_sections', [])
                    recommended_fixes = qa_results.get('auto_fix_recommended') or qa_results.get('suggest_review')
                    
                    improvement_clicked = False
                    
                    if recommended_fixes and has_issues:
                        improvement_clicked = st.button("🔧 Apply Improvements", type="primary")
                    elif has_issues:  # Manual override for low-trust scenarios
                        improvement_clicked = st.button("⚠️ Force Apply Improvements", type="secondary", 
                                   help="Apply improvements despite low trust score - use with caution")
                    else:
                        st.info("No improvements recommended")
                    
                    if improvement_clicked:
                        with st.spinner("Applying QA improvements to report..."):
                            try:
                                from utils.intelligent_search_enhanced import get_enhanced_search_engine
                                search_engine = get_enhanced_search_engine()
                                
                                # Verify improvement pipeline is available
                                if not hasattr(search_engine, 'improvement_pipeline') or search_engine.improvement_pipeline is None:
                                    st.error("❌ Improvement pipeline is not available. Please check the configuration.")
                                else:
                                    # Use improvement pipeline to fix the report
                                    sources = [{"title": "Manual QA Review", "content": {"body": "Manual improvement"}, "author": "User", "category": "QA"}]
                                    
                                    # Use current report (may already be improved)
                                    current_report = report
                                    if 'manual_improvement_applied' in st.session_state:
                                        current_report = st.session_state.manual_improvement_applied['improved_report']
                                    
                                    improvement_result = search_engine.improvement_pipeline.improve_report(
                                        current_report, sources, "Manual QA improvement request"
                                    )
                                    
                                    if improvement_result.get('status') == 'improved':
                                        # Update the workflow state with improved report (safely)
                                        try:
                                            if ('workflow_state' in st.session_state and 
                                                st.session_state.workflow_state is not None and
                                                'data' in st.session_state.workflow_state):
                                                if isinstance(st.session_state.workflow_state['data'], dict):
                                                    st.session_state.workflow_state['data']['report'] = improvement_result['improved_report']
                                        except Exception as e:
                                            print(f"Warning: Could not update workflow state: {e}")
                                        
                                        # Store improvement info
                                        st.session_state.manual_improvement_applied = {
                                            'original_report': improvement_result['original_report'],
                                            'improved_report': improvement_result['improved_report'],
                                            'improvements_made': improvement_result.get('improvements_made', []),
                                            'score_improvement': improvement_result.get('score_improvement', 0),
                                            'timestamp': datetime.now()
                                        }
                                        
                                        st.success("✅ Improvements applied successfully!")
                                        st.rerun()
                                    else:
                                        st.warning("⚠️ No improvements were applied. The report may already be of sufficient quality.")
                                        
                            except Exception as e:
                                st.error(f"❌ Failed to apply improvements: {str(e)}")
                    else:
                        st.info("No improvements recommended")
                
                with col2:
                    if st.button("🗑️ Clear QA Results", type="secondary"):
                        del st.session_state.manual_qa_results
                        if 'manual_qa_timestamp' in st.session_state:
                            del st.session_state.manual_qa_timestamp
                        if 'manual_improvement_applied' in st.session_state:
                            del st.session_state.manual_improvement_applied
                        st.rerun()
                
                with col3:
                    # Option to run improved QA with different config
                    qa_config_options = ["basic", "comprehensive", "trust_focused", "suggest_only"]
                    selected_config = st.selectbox(
                        "Re-run with config:",
                        qa_config_options,
                        index=1,  # Default to comprehensive
                        key=get_unique_key("manual_qa_config")
                    )
                
                with col4:
                    if st.button("🔄 Re-run QA", type="primary"):
                        with st.spinner(f"Re-running QA with {selected_config} configuration..."):
                            try:
                                from utils.intelligent_search_enhanced import get_enhanced_search_engine
                                search_engine = get_enhanced_search_engine()
                                search_engine.configure_qa_system(selected_config)
                                
                                # Verify QA system is available
                                if not hasattr(search_engine, 'qa_system') or search_engine.qa_system is None:
                                    st.error("❌ QA system is not available. Please check the configuration.")
                                else:
                                    
                                    # Use current report (may be improved version)
                                    current_report = report
                                    if 'manual_improvement_applied' in st.session_state:
                                        current_report = st.session_state.manual_improvement_applied['improved_report']
                                    
                                    sources = [{"title": "Manual QA Review", "content": {"body": "Re-run assessment"}, "author": "User", "category": "QA"}]
                                    
                                    # Use new structured QA system for re-run
                                    try:
                                        from utils.structured_qa_integration import StructuredQAManager
                                        from utils.llm_utils import _call_llm_api
                                        
                                        workspace_path = Path(st.session_state.workflow_state.get('workspace_path', '.'))
                                        qa_manager = StructuredQAManager(workspace_path)
                                        
                                        # Enhanced QA prompt for re-run
                                        qa_prompt = f"""Re-analyze this research report with {selected_config} configuration.

REPORT CONTENT:
{current_report[:8000]}

CONTEXT: Manual QA re-run with enhanced analysis
CONFIGURATION: {selected_config}

Please provide a thorough quality assessment focusing on:
1. Technical accuracy and factual correctness
2. Clarity and readability 
3. Completeness of information
4. Structure and organization
5. Practical applicability

IMPORTANT: Return ONLY valid JSON format without any additional text, markdown formatting, or code blocks:

{{
  "inaccurate_or_confusing_sections": [
    {{
      "section_title": "Section Name",
      "issue": "Description of issue",
      "suggested_fix": "How to fix it",
      "confidence": 0.9
    }}
  ],
  "structural_issues": [
    {{
      "section_title": "Structure",
      "issue": "Document organization or flow issues",
      "suggested_fix": "How to improve structure",
      "confidence": 0.9
    }}
  ],
  "overall_score": 0.8,
  "confidence": 0.85,
  "trust_score": 0.82,
  "suggestions": ["General suggestion 1", "General suggestion 2"]
}}

Do not include ```json``` code blocks or any other formatting - just the raw JSON object."""

                                        response = _call_llm_api(qa_prompt, "QA re-analysis")
                                        
                                        if response:
                                            try:
                                                # Clean and extract JSON from response
                                                import json
                                                import re
                                                
                                                # Remove code block markers and thinking tags
                                                cleaned_response = response.strip()
                                                
                                                # Remove thinking tags (common in qwen models)
                                                if '<think>' in cleaned_response:
                                                    parts = cleaned_response.split('</think>')
                                                    if len(parts) > 1:
                                                        cleaned_response = parts[1].strip()
                                                
                                                # Remove code block markers
                                                if cleaned_response.startswith('```json'):
                                                    cleaned_response = cleaned_response[7:]
                                                if cleaned_response.startswith('```'):
                                                    cleaned_response = cleaned_response[3:]
                                                if cleaned_response.endswith('```'):
                                                    cleaned_response = cleaned_response[:-3]
                                                
                                                # Fix common JSON issues (trailing commas, etc.)
                                                cleaned_response = re.sub(r',(\s*[}\]])', r'\1', cleaned_response)
                                                
                                                # Try to find JSON in the response
                                                json_match = re.search(r'\{.*?"inaccurate_or_confusing_sections".*?\}', cleaned_response, re.DOTALL)
                                                if json_match:
                                                    json_str = json_match.group()
                                                    # Fix trailing commas in the matched JSON too
                                                    json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)
                                                    qa_results = json.loads(json_str)
                                                    print(f"DEBUG: Re-analysis parsed JSON with {len(qa_results.get('inaccurate_or_confusing_sections', []))} issues")
                                                elif cleaned_response.strip().startswith('{') and cleaned_response.strip().endswith('}'):
                                                    qa_results = json.loads(cleaned_response.strip())
                                                    print("DEBUG: Re-analysis parsed full response as JSON")
                                                else:
                                                    raise ValueError("No valid JSON structure found in re-analysis response")
                                                    
                                                # Validate the parsed structure
                                                if not isinstance(qa_results.get('inaccurate_or_confusing_sections'), list):
                                                    raise ValueError("Invalid JSON structure in re-analysis")
                                                    
                                            except json.JSONDecodeError as e:
                                                print(f"DEBUG: Re-analysis JSON decode error: {e}")
                                                print(f"DEBUG: Re-analysis response preview: {response[:300]}...")
                                                # Try aggressive extraction first
                                                try:
                                                    qa_results = extract_json_aggressively(response)
                                                    if qa_results:
                                                        print("DEBUG: Re-analysis aggressive JSON extraction succeeded")
                                                    else:
                                                        raise ValueError("Re-analysis aggressive extraction failed")
                                                except:
                                                    print("DEBUG: Re-analysis falling back to manual parsing")
                                                    qa_results = parse_qa_response_manually(response)
                                            except Exception as e:
                                                print(f"DEBUG: Re-analysis JSON parsing failed: {e}")
                                                print(f"DEBUG: Re-analysis response preview: {response[:300]}...")
                                                # Try aggressive extraction first
                                                try:
                                                    qa_results = extract_json_aggressively(response)
                                                    if qa_results:
                                                        print("DEBUG: Re-analysis aggressive JSON extraction succeeded")
                                                    else:
                                                        raise ValueError("Re-analysis aggressive extraction failed")
                                                except:
                                                    print("DEBUG: Re-analysis falling back to manual parsing")
                                                    qa_results = parse_qa_response_manually(response)
                                        else:
                                            qa_results = {
                                                "inaccurate_or_confusing_sections": [],
                                                "overall_score": 0.7,
                                                "suggestions": ["QA re-analysis was not available"]
                                            }
                                    except Exception as structured_error:
                                        print(f"Structured QA re-run failed, falling back to legacy: {structured_error}")
                                        # Fallback to legacy
                                        qa_results = search_engine.qa_system.run_report_qa(
                                            current_report, sources, f"Manual QA re-run with {selected_config} config"
                                        )
                                    
                                    st.session_state.manual_qa_results = qa_results
                                    st.session_state.manual_qa_timestamp = datetime.now()
                                    st.success(f"✅ QA re-run completed with {selected_config} configuration!")
                                    st.rerun()
                            except Exception as e:
                                st.error(f"❌ QA re-run failed: {str(e)}")
                
                # Show improvement history if available
                if 'manual_improvement_applied' in st.session_state:
                    st.divider()
                    improvement_info = st.session_state.manual_improvement_applied
                    
                    with st.expander("🔧 Applied Improvements", expanded=False):
                        st.caption(f"📅 Improvements applied: {improvement_info['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
                        
                        if improvement_info.get('score_improvement', 0) > 0:
                            st.success(f"📈 Quality Score Improved by: {improvement_info['score_improvement']:.2f} points")
                        
                        if improvement_info.get('improvements_made'):
                            st.markdown("**Improvements Made:**")
                            for improvement in improvement_info['improvements_made']:
                                # Handle both string and dictionary formats
                                if isinstance(improvement, str):
                                    st.write(f"• {improvement}")
                                elif isinstance(improvement, dict):
                                    st.markdown(f"**{improvement['section']}**")
                                    st.write("Issues addressed:")
                                    for issue in improvement['issues_addressed']:
                                        st.write(f"• {issue}")
                        
                        # Show sections modified if using structured approach
                        if improvement_info.get('sections_modified') and improvement_info.get('method') == 'structured_qa':
                            st.markdown("**Sections Modified:**")
                            for section in improvement_info['sections_modified']:
                                st.write(f"• **{section['section_title']}** - {len(section['issues_resolved'])} issue(s) resolved")
                                if section['original_length'] != section['new_length']:
                                    st.caption(f"  Content size: {section['original_length']} → {section['new_length']} characters")
                        
                        # Show verification results for document-wide improvements
                        if improvement_info.get('method') == 'document_wide' and improvement_info.get('verification'):
                            verification = improvement_info['verification']
                            st.markdown("**📊 Document-Wide Improvement Verification:**")
                            
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                score = verification.get('verification_score', 0) * 100
                                st.metric("Verification Score", f"{score:.0f}%")
                            with col2:
                                addressed = "✅" if verification.get('all_issues_addressed') else "❌"
                                st.metric("Issues Addressed", addressed)
                            with col3:
                                preserved = "✅" if verification.get('information_preserved') else "❌"
                                st.metric("Content Preserved", preserved)
                            
                            if verification.get('summary'):
                                st.info(f"**Verification Summary:** {verification['summary']}")
                            
                            if verification.get('addressed_issues'):
                                st.write("**Successfully Addressed:**")
                                for item in verification['addressed_issues']:
                                    st.write(f"  ✅ {item}")
                            
                            if verification.get('remaining_issues'):
                                st.write("**Still Needs Attention:**")
                                for item in verification['remaining_issues']:
                                    st.write(f"  ⚠️ {item}")
                        
                        # Show individual fixes if any
                        if improvement_info.get('individual_fixes'):
                            st.markdown("**Individual Issue Fixes Applied:**")
                            for fix in improvement_info['individual_fixes']:
                                fix_type = fix.get('fix_type', 'unknown')
                                if fix_type == 'custom' and fix.get('custom_instruction'):
                                    st.write(f"✏️ Issue {fix['issue_number']}: {fix['section']} - **Custom Fix** - {fix['fix_applied'].strftime('%H:%M:%S')}")
                                    st.caption(f"   Instruction: {fix['custom_instruction']}")
                                else:
                                    st.write(f"🔧 Issue {fix['issue_number']}: {fix['section']} - **Suggested Fix** - {fix['fix_applied'].strftime('%H:%M:%S')}")
                        
                        # Show layer fixes if any
                        if improvement_info.get('layer_fixes'):
                            st.markdown("**Layer-specific Fixes Applied:**")
                            for fix in improvement_info['layer_fixes']:
                                fix_type = fix.get('fix_type', 'default')
                                if fix_type == 'custom' and fix.get('custom_instruction'):
                                    st.write(f"✏️ {fix['layer'].title()}: {fix['issue'][:60]}... - **Custom Fix** - {fix['fix_applied'].strftime('%H:%M:%S')}")
                                    st.caption(f"   Instruction: {fix['custom_instruction']}")
                                else:
                                    st.write(f"🔧 {fix['layer'].title()}: {fix['issue'][:60]}... - **Default Fix** - {fix['fix_applied'].strftime('%H:%M:%S')}")
                        
                        # Option to compare before/after
                        if st.checkbox("Show Before/After Comparison"):
                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown("**Original Report:**")
                                original_preview = improvement_info.get('original_report', '')[:1000]
                                if len(improvement_info.get('original_report', '')) > 1000:
                                    original_preview += "..."
                                st.text_area("", value=original_preview, height=200, disabled=True, key="original_compare")
                            with col2:
                                st.markdown("**Improved Report:**")
                                improved_preview = improvement_info.get('improved_report', '')[:1000]
                                if len(improvement_info.get('improved_report', '')) > 1000:
                                    improved_preview += "..."
                                st.text_area("", value=improved_preview, height=200, disabled=True, key="improved_compare")
                
                # Debug panel for QA operations
                if st.session_state.get('qa_operation_log'):
                    with st.expander("🔧 QA Operation Log (Debug)", expanded=False):
                        st.caption("Recent QA operations for debugging")
                        for log_entry in reversed(st.session_state.qa_operation_log[-10:]):  # Show last 10
                            if "error" in log_entry.lower():
                                st.error(log_entry)
                            elif "success" in log_entry.lower():
                                st.success(log_entry)
                            else:
                                st.info(log_entry)
                        
                        if st.button("Clear Log", key="clear_qa_log"):
                            st.session_state.qa_operation_log = []
                            st.rerun()
        
        elif stage == 'complete':
            st.markdown("### ✅ Research Complete")
            
            # Get the report from workflow state data
            data = workflow_state.get('data', {})
            if isinstance(data, dict):
                report = data.get('report', 'No report found')
                metadata = data.get('metadata', {})
                forced_complete = data.get('forced_complete', False)
                
                if forced_complete:
                    st.info("📌 This research was manually marked as complete")
                
                # Display the final report
                if report and report != 'No report found':
                    st.markdown("## 📄 Final Research Report")
                    
                    # Check if report appears incomplete (regardless of forced_complete status)
                    if _is_report_incomplete(report):
                        if forced_complete:
                            st.warning("⚠️ This report appears to be incomplete despite being marked as complete!")
                        else:
                            st.warning("⚠️ This report appears to be incomplete!")
                        col1, col2, col3 = st.columns([1, 2, 1])
                        with col2:
                            if st.button("🔄 Complete the Report", type="primary", key="complete_incomplete_final_report"):
                                with st.spinner("Completing the report..."):
                                    # Get workflow data for completion - try multiple sources
                                    workflow_data = None
                                    if workflow_orchestrator and hasattr(workflow_orchestrator, 'workflow') and hasattr(workflow_orchestrator.workflow, 'workflow_state'):
                                        workflow_data = workflow_orchestrator.workflow.workflow_state
                                    elif 'loaded_state' in workflow_state:
                                        workflow_data = workflow_state['loaded_state']
                                    elif hasattr(st.session_state, 'research_workflow') and st.session_state.research_workflow:
                                        workflow_data = st.session_state.research_workflow.get('loaded_state')
                                    
                                    # Use the report completion function
                                    completed_report = _complete_incomplete_report(
                                        report, 
                                        workflow_orchestrator=workflow_orchestrator, 
                                        workflow_state_data=workflow_data
                                    )
                                    if completed_report:
                                        # Update the workflow state with the completed report
                                        workflow_state['data']['report'] = completed_report
                                        st.session_state.workflow_state = workflow_state
                                        
                                        # Save to persistence
                                        if workflow_orchestrator and hasattr(workflow_orchestrator, 'workflow') and hasattr(workflow_orchestrator.workflow, 'workflow_state'):
                                            workflow_orchestrator.workflow.workflow_state['final_report'] = completed_report
                                            workflow_persistence.save_workflow_state(workflow_orchestrator.workflow.workflow_state)
                                        elif workflow_data and hasattr(st.session_state, 'research_workflow') and st.session_state.research_workflow:
                                            # Fallback: update the loaded state and save directly
                                            session_dir = st.session_state.research_workflow.get('session_dir')
                                            if session_dir and workflow_data:
                                                workflow_data['final_report'] = completed_report
                                                workflow_persistence.save_workflow_state(workflow_data, session_dir)
                                        
                                        st.success("✅ Report completed successfully!")
                                        time.sleep(0.5)
                                        st.rerun()
                                    else:
                                        st.error("❌ Failed to complete the report")
                    
                    # Add download button
                    st.download_button(
                        label="📥 Download Report (Markdown)",
                        data=report,
                        file_name=f"research_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                        mime="text/markdown",
                        help="Download the complete research report as a markdown file"
                    )
                    
                    # Display the report
                    with st.container():
                        st.markdown(report)
                    
                    # Display automatic QA results if available
                    automatic_qa = None
                    if workflow_orchestrator and hasattr(workflow_orchestrator, 'workflow') and hasattr(workflow_orchestrator.workflow, 'workflow_state'):
                        automatic_qa = workflow_orchestrator.workflow.workflow_state.get('automatic_qa_results')
                    elif 'loaded_state' in workflow_state and workflow_state['loaded_state'].get('automatic_qa_results'):
                        automatic_qa = workflow_state['loaded_state']['automatic_qa_results']
                    
                    if automatic_qa:
                        st.divider()
                        st.markdown("## 🤖 Automatic QA & Improvements")
                        
                        if automatic_qa.get('automatic_qa_completed', False):
                            # QA completed successfully
                            col1, col2, col3, col4 = st.columns(4)
                            
                            with col1:
                                content_score = automatic_qa.get('content_qa', {}).get('query_satisfaction_score', 85)
                                st.metric("Content Quality", f"{content_score}%")
                            
                            with col2:
                                structure_score = automatic_qa.get('structure_qa', {}).get('overall_structure_score', 85)
                                st.metric("Structure Quality", f"{structure_score}%")
                            
                            with col3:
                                improvements_count = len(automatic_qa.get('improvements_applied', []))
                                st.metric("Improvements Applied", improvements_count)
                            
                            with col4:
                                final_score = automatic_qa.get('final_verification', {}).get('overall_readiness', 85)
                                st.metric("Overall Quality", f"{final_score}%")
                            
                            # Show applied improvements
                            if automatic_qa.get('improvements_applied'):
                                st.markdown("### ✅ Applied Improvements")
                                for improvement in automatic_qa['improvements_applied']:
                                    # Handle dictionary format with type, description, and details
                                    if isinstance(improvement, dict):
                                        st.success(f"✓ {improvement.get('description', 'Improvement applied')}")
                                        if improvement.get('details'):
                                            with st.expander("View details", expanded=False):
                                                for detail in improvement['details']:
                                                    st.write(f"• {detail}")
                                    else:
                                        # Fallback for string format
                                        st.success(f"✓ {improvement}")
                            
                            # Show QA timestamp
                            qa_time = datetime.fromisoformat(automatic_qa['timestamp']).strftime("%Y-%m-%d %H:%M:%S")
                            st.caption(f"QA completed at: {qa_time}")
                        else:
                            st.error(f"❌ Automatic QA failed: {automatic_qa.get('error', 'Unknown error')}")
                    
                    # Show metadata if available
                    if metadata:
                        st.divider()
                        st.markdown("### 📊 Report Metadata")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Generated At", metadata.get('generated_at', 'Unknown'))
                        with col2:
                            st.metric("Subtasks Completed", metadata.get('subtasks_completed', 0))
                        with col3:
                            st.metric("Documents Analyzed", metadata.get('documents_analyzed', 0))
                else:
                    st.error("❌ No report found in completed workflow")
                    st.info("The workflow was marked as complete but no report content was found.")
                
                # Option to start a new research
                st.divider()
                if st.button("🔄 Start New Research", type="primary"):
                    # Clear workflow state
                    workflow_keys_to_clear = [
                        'workflow_state',
                        'research_workflow',
                        'workflow_tracking',
                        'editable_decomposition',
                        'pending_tasks',
                        'completed_tasks'
                    ]
                    
                    for key in workflow_keys_to_clear:
                        if key in st.session_state:
                            del st.session_state[key]
                    
                    # Reset workflow persistence
                    workflow_persistence.current_session_dir = None
                    
                    st.rerun()
            else:
                st.error("❌ Invalid workflow state data")
                st.write("Debug - Workflow state:", workflow_state)

else:
    # Quick Search Interface (existing functionality)
    query = st.text_input(
        "Enter your search query:",
        value=st.session_state.get('query_rerun', ''),
        placeholder="Search for concepts, topics, or ask questions..."
    )
    
    # Clear query_rerun after use
    if 'query_rerun' in st.session_state:
        del st.session_state.query_rerun
    
    col1, col2 = st.columns([1, 5])
    with col1:
        search_button = st.button("🔍 Search", type="primary")
    with col2:
        if st.session_state.current_results:
            if st.button("🔄 Clear Results"):
                st.session_state.current_results = None
                st.rerun()
    
    if search_button and query:
        with st.spinner("Searching intelligently..."):
            # Check thesaurus settings
            use_thesaurus = st.session_state.get('use_thesaurus', True)
            expansion_weight = st.session_state.get('expansion_weight', 0.7)
            max_synonyms = st.session_state.get('max_synonyms', 3)
            
            # Perform enhanced search with optional thesaurus expansion
            if use_thesaurus and hasattr(search_engine, 'search_with_expansion'):
                # Use thesaurus-enhanced search
                thesaurus_results = search_engine.search_with_expansion(
                    query,
                    use_synonyms=True,
                    expansion_weight=expansion_weight,
                    max_synonyms_per_word=max_synonyms
                )
                # Convert to expected format
                results_list = []
                for result in thesaurus_results:
                    if hasattr(result, 'to_dict'):
                        results_list.append(result.to_dict())
                    else:
                        results_list.append(result)
            else:
                # Use standard search
                results_list = search_engine.search_content(query)
            
            # Parse query intent for additional info
            query_intent = search_engine.parse_query_intent(query)
            
            # Generate synthesized answer with QA if results found
            answer_data = None
            if results_list:
                # Check if QA is enabled in settings
                enable_qa = st.session_state.get('enable_qa_improvement', True)
                answer_data = search_engine.synthesize_answer_with_qa(
                    query, results_list, 
                    use_structured_report=True,
                    enable_qa_improvement=enable_qa
                )
            
            # Get synonym expansions for display
            thesaurus_expansions = {}
            if use_thesaurus and hasattr(search_engine, 'explain_expansions'):
                expansion_info = search_engine.explain_expansions(query)
                thesaurus_expansions = expansion_info.get('expansions', {})
            
            # Format results in expected structure
            results = {
                'results': results_list,
                'query_analysis': {
                    'intent': query_intent.get('intent_type', 'information_seeking'),
                    'entities': query_intent.get('key_entities', []),
                    'search_type': query_intent.get('expected_answer_type', 'synthesized_answer'),
                    'expanded_terms': query_intent.get('expanded_query', {}).get('expanded_tokens', []),
                    'thesaurus_expansions': thesaurus_expansions,
                    'expansion_used': use_thesaurus
                },
                'answer': answer_data.get('answer') if answer_data else None,
                'answer_confidence': answer_data.get('confidence', 0) if answer_data else 0,
                'total_clusters': answer_data.get('clusters_found', 0) if answer_data else 0,
                'related_queries': []  # Could be enhanced with query suggestions
            }
            
            # Store in session state
            st.session_state.current_results = results
            st.session_state.search_history.append({
                'query': query,
                'timestamp': datetime.now(),
                'results_count': len(results_list)
            })
    
    # Display results
    if st.session_state.current_results:
        results = st.session_state.current_results
        
        # Query analysis (if enabled)
        if st.session_state.show_analysis and 'query_analysis' in results:
            with st.expander("🔍 Query Analysis", expanded=True):
                analysis = results['query_analysis']
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.markdown("**Intent:**")
                    st.info(analysis.get('intent', 'General search'))
                
                with col2:
                    st.markdown("**Key Entities:**")
                    entities = analysis.get('entities', [])
                    if entities:
                        for entity in entities[:5]:
                            st.write(f"• {entity}")
                    else:
                        st.write("No specific entities")
                
                with col3:
                    st.markdown("**Expanded Terms:**")
                    expanded = analysis.get('expanded_terms', [])
                    if expanded:
                        for term in expanded[:5]:
                            st.write(f"• {term}")
                    else:
                        st.write("No expansions")
                
                with col4:
                    st.markdown("**Search Strategy:**")
                    st.success(analysis.get('search_type', 'Keyword search'))
                
                # Add thesaurus expansion display
                if analysis.get('expansion_used') and analysis.get('thesaurus_expansions'):
                    st.divider()
                    st.markdown("**🔤 Synonym Expansions Used:**")
                    expansions = analysis['thesaurus_expansions']
                    
                    if expansions:
                        cols = st.columns(min(len(expansions), 4))
                        for i, (word, synonyms) in enumerate(expansions.items()):
                            with cols[i % len(cols)]:
                                st.markdown(f"**{word}:**")
                                for syn in synonyms[:3]:  # Show top 3 synonyms
                                    st.write(f"• {syn}")
                    else:
                        st.info("No synonyms found for query terms")
        
        # Results summary with enhanced info
        total_results = len(results['results'])
        unique_clusters = len(set(r.get('cluster_id', i) for i, r in enumerate(results['results'])))
        st.markdown(f"### Found {total_results} relevant results in {unique_clusters} topic clusters")
        
        if results.get('answer'):
            st.markdown("#### 💡 AI-Generated Answer")
            col1, col2 = st.columns([5, 1])
            with col1:
                st.info(results['answer'])
            with col2:
                confidence = results.get('answer_confidence', 0) * 100
                st.metric("Confidence", f"{confidence:.0f}%")
            
            # Display QA feedback if available
            if st.session_state.get('enable_qa_improvement') and 'qa_results' in results:
                with st.expander("🔍 Quality Assessment & Improvements", expanded=False):
                    qa_results = results['qa_results']
                    
                    # Overall QA metrics
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        overall_score = qa_results.get('overall_score', 0) * 100
                        st.metric("Overall Quality", f"{overall_score:.0f}%")
                    with col2:
                        qa_confidence = qa_results.get('confidence', 0) * 100
                        st.metric("QA Confidence", f"{qa_confidence:.0f}%")
                    with col3:
                        trust_score = qa_results.get('trust_score', 0) * 100
                        st.metric("Trust Score", f"{trust_score:.0f}%")
                    with col4:
                        improvements_made = len(results.get('improvements_made', []))
                        st.metric("Improvements Made", improvements_made)
                    
                    # Show trust/fix decision information if available
                    if qa_results.get('fix_decision_reasoning'):
                        st.markdown("**QA Decision Analysis:**")
                        
                        # Display fix recommendation status
                        if qa_results.get('auto_fix_recommended'):
                            st.success("✅ **Auto-fix Recommended** - High confidence fixes applied automatically")
                        elif qa_results.get('suggest_review'):
                            st.info("⚠️ **Suggest Review** - Moderate confidence, suitable for review")
                        elif qa_results.get('manual_review_required'):
                            st.warning("🔍 **Manual Review Required** - Complex issues need human attention")
                        
                        # Show reasoning
                        with st.expander("Decision Reasoning", expanded=False):
                            for reason in qa_results['fix_decision_reasoning']:
                                st.write(f"• {reason}")
                    
                    # Layer scores
                    if qa_results.get('layer_scores'):
                        st.markdown("**Quality by Category:**")
                        layer_cols = st.columns(len(qa_results['layer_scores']))
                        for i, (layer, layer_data) in enumerate(qa_results['layer_scores'].items()):
                            with layer_cols[i]:
                                score = layer_data.get('score', 0) * 100
                                st.metric(layer.title(), f"{score:.0f}%")
                    
                    # Show improvements made
                    if results.get('improvements_made'):
                        st.markdown("**Improvements Applied:**")
                        for improvement in results['improvements_made']:
                            with st.container():
                                st.markdown(f"**{improvement['section']}**")
                                st.write("Issues addressed:")
                                for issue in improvement['issues_addressed']:
                                    st.write(f"• {issue}")
                    
                    # Show original vs improved toggle
                    if results.get('original_answer') and results.get('qa_status') == 'improved':
                        show_comparison = st.checkbox("Show Before/After Comparison")
                        if show_comparison:
                            st.markdown("**Original Answer:**")
                            st.text_area("", value=results['original_answer'], height=200, disabled=True)
                            st.markdown("**Improved Answer:**")
                            st.text_area("", value=results['answer'], height=200, disabled=True)
                            
                            score_improvement = results.get('score_improvement', 0) * 100
                            if score_improvement > 0:
                                st.success(f"Quality improved by {score_improvement:.1f} points")
            
            st.divider()
        
        # Display results
        if results['results']:
            st.markdown("#### 📄 Relevant Documents")
            
            for i, result in enumerate(results['results']):
                # Extract content data from nested structure
                content_data = result.get('content', {})
                title = content_data.get('title', 'Untitled')
                category = content_data.get('category', 'Uncategorized')
                
                # Show cluster indicator for non-primary results
                cluster_info = ""
                if result.get('cluster_size', 1) > 1 and not result.get('is_cluster_primary'):
                    cluster_info = " 🔗"
                
                with st.expander(f"**{title}**{cluster_info} - {category}", expanded=(i < 3)):
                    # Result metadata
                    col1, col2, col3 = st.columns([2, 1, 1])
                    with col1:
                        if content_data.get('author'):
                            st.write(f"**Author:** {content_data['author']}")
                        st.write(f"**Match Type:** {result.get('match_type', 'keyword')}")
                        
                        # Show matched terms
                        if result.get('matched_terms'):
                            matched = ", ".join(result['matched_terms'][:5])
                            st.write(f"**Matched:** {matched}")
                    with col2:
                        score = result.get('final_score', result.get('score', 0))
                        st.metric("Relevance", f"{score:.2f}")
                    with col3:
                        if result.get('cluster_size', 1) > 1:
                            st.metric("Similar Docs", result['cluster_size'] - 1)
                    
                    # Key concepts and entities
                    if content_data.get('entities') or content_data.get('concepts'):
                        col1, col2 = st.columns(2)
                        with col1:
                            if content_data.get('entities'):
                                st.markdown("**Key Entities:**")
                                for entity in content_data['entities'][:5]:
                                    st.write(f"• {entity}")
                        with col2:
                            if content_data.get('concepts'):
                                st.markdown("**Key Concepts:**")
                                for concept in content_data['concepts'][:5]:
                                    st.write(f"• {concept}")
                    
                    # Content preview
                    st.markdown("**Content Preview:**")
                    body = content_data.get('body', '')
                    preview_length = 500
                    if len(body) > preview_length:
                        st.write(body[:preview_length] + "...")
                        if st.button(f"Read more", key=f"more_{i}"):
                            st.write(body)
                    else:
                        st.write(body)
                    
                    # Related topics
                    if content_data.get('related_topics'):
                        st.markdown("**Related Topics:**")
                        related = ", ".join(content_data['related_topics'][:5])
                        st.write(related)
                    
                    # File path
                    st.caption(f"📁 {result.get('file_key', 'Unknown path')}")
        
        # Related searches
        if results.get('related_queries'):
            st.divider()
            st.markdown("#### 🔗 Related Searches")
            cols = st.columns(3)
            for i, related_query in enumerate(results['related_queries'][:6]):
                with cols[i % 3]:
                    if st.button(related_query, key=f"related_{i}"):
                        st.session_state.query_rerun = related_query
                        st.rerun()
        
        else:
            st.warning("No results found. Try rephrasing your query or using different keywords.")

# Footer
st.divider()
st.caption("Intelligent Search powered by AI - Continuously learning from your knowledge base")