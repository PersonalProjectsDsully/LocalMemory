"""
Quick Search UI Module

Handles the quick search interface and results display.
"""

import streamlit as st
from datetime import datetime
import json
from pathlib import Path
from .session_management import get_unique_key
from .report_processing import is_report_incomplete
from .qa_quality import safe_improvement_pipeline_call


def render_quick_search(search_engine, workflow_orchestrator):
    """Render the quick search interface"""
    st.header("🔍 Quick Search")
    
    query = st.text_input(
        "Search Query:",
        placeholder="Enter your search terms or question...",
        help="Use natural language to describe what you're looking for"
    )
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("🔍 Search", type="primary", disabled=not query):
            perform_search(query, search_engine)
    
    with col2:
        if st.button("🧠 Generate Report"):
            if query:
                generate_intelligent_report(query, search_engine)
    
    # Display current results
    if st.session_state.current_results:
        display_search_results(st.session_state.current_results, search_engine, workflow_orchestrator)


def perform_search(query, search_engine):
    """Perform the actual search operation"""
    with st.spinner("Searching..."):
        try:
            # Configure search parameters based on session state
            search_params = {
                'query': query,
                'max_results': 20,
                'use_thesaurus': st.session_state.get('use_thesaurus', True),
            }
            
            if st.session_state.get('use_thesaurus', True):
                search_params.update({
                    'expansion_weight': st.session_state.get('expansion_weight', 0.7),
                    'max_synonyms': st.session_state.get('max_synonyms', 3)
                })
            
            results = search_engine.search(**search_params)
            
            if results:
                # Store in session state
                st.session_state.current_results = {
                    'query': query,
                    'results': results.get('results', []),
                    'metadata': results.get('metadata', {}),
                    'timestamp': datetime.now().isoformat()
                }
                
                # Add to search history
                st.session_state.search_history.append({
                    'query': query,
                    'results': st.session_state.current_results,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'num_results': len(results.get('results', []))
                })
                
                st.success(f"Found {len(results.get('results', []))} results")
                st.rerun()
            else:
                st.warning("No results found")
                
        except Exception as e:
            st.error(f"Search failed: {str(e)}")


def generate_intelligent_report(query, search_engine):
    """Generate an intelligent report from search results"""
    with st.spinner("Generating intelligent report..."):
        try:
            # Check if QA is enabled
            enable_qa = st.session_state.get('enable_qa_improvement', True)
            qa_config = st.session_state.get('qa_config', 'comprehensive')
            
            if enable_qa:
                search_engine.configure_qa_system(qa_config)
            
            # Generate report with QA
            result = search_engine.generate_report(query, enable_qa=enable_qa)
            
            if result:
                st.session_state.current_results = {
                    'query': query,
                    'generated_report': result.get('report', ''),
                    'qa_analysis': result.get('qa_analysis', {}),
                    'sources': result.get('sources', []),
                    'metadata': result.get('metadata', {}),
                    'timestamp': datetime.now().isoformat(),
                    'type': 'report'
                }
                
                st.success("Report generated successfully!")
                st.rerun()
            else:
                st.error("Failed to generate report")
                
        except Exception as e:
            st.error(f"Report generation failed: {str(e)}")


def display_search_results(results, search_engine, workflow_orchestrator):
    """Display search results with various formats"""
    if results.get('type') == 'report':
        display_generated_report(results, search_engine, workflow_orchestrator)
    else:
        display_search_list_results(results)


def display_generated_report(results, search_engine, workflow_orchestrator):
    """Display a generated report with QA features"""
    st.markdown("---")
    st.subheader("📄 Generated Report")
    
    report = results.get('generated_report', '')
    qa_analysis = results.get('qa_analysis', {})
    sources = results.get('sources', [])
    
    # Check if report is incomplete
    is_incomplete = is_report_incomplete(report)
    
    if is_incomplete:
        st.warning("⚠️ This report appears to be incomplete. You may want to regenerate it.")
    
    # Display metadata
    metadata = results.get('metadata', {})
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Sources Used", len(sources))
    with col2:
        st.metric("Generated", metadata.get('generated_at', 'Unknown')[:10])
    with col3:
        if qa_analysis:
            overall_score = qa_analysis.get('overall_score', 0)
            st.metric("Quality Score", f"{overall_score:.1%}")
    
    # Display the report content
    st.markdown("### Report Content")
    st.markdown(report)
    
    # QA Analysis section
    if qa_analysis and st.session_state.get('enable_qa_improvement', True):
        display_qa_improvements(qa_analysis, report, sources, results.get('query', ''), search_engine)
    
    # Sources section
    if sources:
        with st.expander(f"📚 Sources ({len(sources)})", expanded=False):
            for i, source in enumerate(sources[:10]):  # Limit to first 10
                st.markdown(f"**{i+1}. {source.get('title', 'Untitled')}**")
                st.caption(f"Category: {source.get('category', 'Unknown')} | Author: {source.get('author', 'Unknown')}")
                if source.get('content', {}).get('body'):
                    preview = source['content']['body'][:200] + "..." if len(source['content']['body']) > 200 else source['content']['body']
                    st.markdown(preview)
                st.divider()


def display_qa_improvements(qa_analysis, report, sources, query, search_engine):
    """Display QA analysis and improvement options"""
    st.markdown("---")
    st.subheader("🔍 Quality Analysis & Improvements")
    
    # Overall metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        overall_score = qa_analysis.get('overall_score', 0)
        st.metric("Overall Score", f"{overall_score:.1%}")
    
    with col2:
        trust_score = qa_analysis.get('trust_score', overall_score)
        st.metric("Trust Score", f"{trust_score:.1%}")
    
    with col3:
        confidence = qa_analysis.get('confidence', overall_score)
        st.metric("Confidence", f"{confidence:.1%}")
    
    # Issues found
    issues = qa_analysis.get('inaccurate_or_confusing_sections', [])
    
    if issues:
        st.markdown(f"### 🚨 Issues Found ({len(issues)})")
        
        # Batch improvement options
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔧 Apply All Improvements", type="primary"):
                apply_all_improvements(issues, report, sources, query, search_engine)
        
        with col2:
            if st.button("🧠 Smart Fix Selection"):
                apply_smart_improvements(issues, report, sources, query, search_engine)
        
        # Individual issues
        st.markdown("#### Individual Issues")
        
        for i, issue in enumerate(issues):
            with st.expander(f"Issue {i+1}: {issue.get('section_title', 'Unknown Section')}", expanded=False):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**Problem:** {issue.get('issue', 'No description')}")
                    st.markdown(f"**Suggested Fix:** {issue.get('suggested_fix', 'No suggestion')}")
                    
                    # Custom instruction
                    custom_instruction = st.text_area(
                        "Custom instruction (optional):",
                        placeholder="Provide specific guidance for fixing this issue...",
                        key=get_unique_key(f"custom_instruction_{i}"),
                        height=70
                    )
                
                with col2:
                    confidence = issue.get('confidence', 0)
                    st.metric("Confidence", f"{confidence:.1%}")
                    
                    # Action buttons
                    if st.button(f"🔧 Apply Fix", key=get_unique_key(f"apply_fix_{i}")):
                        apply_individual_fix(issue, report, sources, query, search_engine, custom_instruction)
                    
                    if st.button(f"❌ Ignore", key=get_unique_key(f"ignore_{i}")):
                        st.success("Issue ignored")
    
    # General suggestions
    suggestions = qa_analysis.get('suggestions', [])
    if suggestions:
        with st.expander("💡 General Suggestions", expanded=False):
            for suggestion in suggestions:
                st.markdown(f"- {suggestion}")
    
    # Show improvement history
    if 'manual_improvement_applied' in st.session_state:
        display_improvement_history()


def apply_all_improvements(issues, report, sources, query, search_engine):
    """Apply all suggested improvements at once"""
    with st.spinner("Applying all improvements..."):
        try:
            improved_report, improvements_made = safe_improvement_pipeline_call(
                search_engine, report, issues, sources, query
            )
            
            if improved_report and improved_report != report:
                from .session_management import update_improvement_session_state
                update_improvement_session_state(
                    report, 
                    improved_report, 
                    improvements_made,
                    fix_type='batch',
                    fix_details={'issues_count': len(issues)}
                )
                
                st.success(f"✅ Applied {len(improvements_made)} improvements!")
                st.rerun()
            else:
                st.warning("No improvements were made")
                
        except Exception as e:
            st.error(f"Failed to apply improvements: {str(e)}")


def apply_smart_improvements(issues, report, sources, query, search_engine):
    """Apply improvements using smart selection criteria"""
    with st.spinner("Analyzing and applying smart improvements..."):
        try:
            # Filter issues by confidence and type
            high_confidence_issues = [
                issue for issue in issues 
                if issue.get('confidence', 0) > 0.7
            ]
            
            if high_confidence_issues:
                improved_report, improvements_made = safe_improvement_pipeline_call(
                    search_engine, report, high_confidence_issues, sources, query
                )
                
                if improved_report and improved_report != report:
                    from .session_management import update_improvement_session_state
                    update_improvement_session_state(
                        report, 
                        improved_report, 
                        improvements_made,
                        fix_type='smart',
                        fix_details={'high_confidence_issues': len(high_confidence_issues)}
                    )
                    
                    st.success(f"✅ Applied {len(improvements_made)} high-confidence improvements!")
                    st.rerun()
                else:
                    st.warning("No high-confidence improvements could be applied")
            else:
                st.info("No high-confidence issues found for smart fixing")
                
        except Exception as e:
            st.error(f"Failed to apply smart improvements: {str(e)}")


def apply_individual_fix(issue, report, sources, query, search_engine, custom_instruction=None):
    """Apply a fix for an individual issue"""
    with st.spinner(f"Applying fix for: {issue.get('section_title', 'Unknown')}..."):
        try:
            # Create a modified issue with custom instruction if provided
            if custom_instruction and custom_instruction.strip():
                modified_issue = issue.copy()
                modified_issue['suggested_fix'] = custom_instruction.strip()
                issues_to_fix = [modified_issue]
            else:
                issues_to_fix = [issue]
            
            improved_report, improvements_made = safe_improvement_pipeline_call(
                search_engine, report, issues_to_fix, sources, query
            )
            
            if improved_report and improved_report != report:
                from .session_management import update_improvement_session_state
                update_improvement_session_state(
                    report, 
                    improved_report, 
                    improvements_made,
                    fix_type='individual',
                    fix_details={
                        'section': issue.get('section_title', 'Unknown'),
                        'issue': issue.get('issue', ''),
                        'custom_instruction': bool(custom_instruction)
                    }
                )
                
                st.success(f"✅ Applied fix for {issue.get('section_title', 'Unknown')}!")
                st.rerun()
            else:
                st.warning("No changes were made")
                
        except Exception as e:
            st.error(f"Failed to apply individual fix: {str(e)}")


def display_improvement_history():
    """Display the history of improvements made"""
    improvement_data = st.session_state.manual_improvement_applied
    
    with st.expander("📈 Improvement History", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Improvements Made", len(improvement_data.get('improvements_made', [])))
        
        with col2:
            timestamp = improvement_data.get('timestamp', datetime.now())
            if hasattr(timestamp, 'strftime'):
                time_str = timestamp.strftime('%H:%M:%S')
            else:
                time_str = str(timestamp)[:8]
            st.metric("Last Updated", time_str)
        
        with col3:
            method = improvement_data.get('method', 'unknown')
            st.metric("Method", method.title())
        
        # Show improvements
        improvements = improvement_data.get('improvements_made', [])
        if improvements:
            st.markdown("**Changes Made:**")
            for improvement in improvements[:5]:  # Show first 5
                st.markdown(f"- {improvement}")
        
        # Option to revert
        if st.button("🔄 Revert to Original"):
            if 'current_results' in st.session_state and 'generated_report' in st.session_state.current_results:
                original_report = improvement_data.get('original_report', '')
                st.session_state.current_results['generated_report'] = original_report
                del st.session_state.manual_improvement_applied
                st.success("Reverted to original report")
                st.rerun()


def display_search_list_results(results):
    """Display traditional search results as a list"""
    st.markdown("---")
    st.subheader("🔍 Search Results")
    
    search_results = results.get('results', [])
    metadata = results.get('metadata', {})
    
    # Display metadata
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Results", len(search_results))
    with col2:
        st.metric("Search Time", f"{metadata.get('search_time', 0):.2f}s")
    with col3:
        if metadata.get('thesaurus_expanded'):
            st.metric("Synonyms Used", "✅")
        else:
            st.metric("Synonyms Used", "❌")
    
    # Display results
    if search_results:
        for i, result in enumerate(search_results):
            render_search_result_item(result, i)
    else:
        st.info("No results found")


def render_search_result_item(result, idx):
    """Render a single search result item"""
    with st.expander(f"{idx+1}. {result.get('title', 'Untitled')}", expanded=(idx < 3)):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**Category:** {result.get('category', 'Unknown')}")
            if result.get('author'):
                st.caption(f"Author: {result['author']}")
            if result.get('created_at'):
                st.caption(f"Created: {result['created_at']}")
            
            # Content preview
            content = result.get('content', {})
            if isinstance(content, dict) and 'body' in content:
                preview = content['body'][:500] + "..." if len(content['body']) > 500 else content['body']
                st.markdown(preview)
        
        with col2:
            score = result.get('similarity_score', 0)
            st.metric("Relevance", f"{score:.1%}")
            
            # Show reasoning if available
            if result.get('reasoning'):
                with st.popover("📊 Scoring Details"):
                    st.json(result['reasoning'])
        
        # Highlights
        if result.get('highlights'):
            st.markdown("**Key Highlights:**")
            for highlight in result['highlights'][:3]:
                st.markdown(f"- {highlight}")
        
        # Show intelligent features if available
        if result.get('ai_summary'):
            with st.expander("🤖 AI Summary"):
                st.markdown(result['ai_summary'])
        
        if result.get('key_topics'):
            st.markdown("**Key Topics:** " + ", ".join(result['key_topics']))