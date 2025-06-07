"""
Report Processing Module

Handles report completeness detection and completion functionality.
"""

def is_report_incomplete(report_text: str) -> bool:
    """Detect if a report is incomplete based on various indicators"""
    if not report_text or len(report_text.strip()) < 500:
        return True
    
    stripped_text = report_text.strip()
    
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
    
    return any(incomplete_indicators)


def complete_incomplete_report(partial_report: str, workflow_orchestrator=None, workflow_state_data=None) -> str:
    """Complete an incomplete report by calling the LLM to continue generation"""
    try:
        from utils.llm.llm_utils import call_llm
        
        print(f"DEBUG: Starting report completion. Original length: {len(partial_report)}")
        
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