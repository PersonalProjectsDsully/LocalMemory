"""
Workflow Persistence Manager
Handles saving and loading research workflow state to files
"""

import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List
import streamlit as st
import threading
import time


class WorkflowPersistence:
    """Manages persistent storage of research workflow state"""
    
    def __init__(self, workspace_dir: str = "research_workspace"):
        self.workspace_dir = Path(workspace_dir)
        self.workspace_dir.mkdir(exist_ok=True)
        self.current_session_dir = None
        self._session_lock = threading.Lock()
        
    def create_session(self, query: str) -> Path:
        """Create a new research session directory with thread safety"""
        with self._session_lock:
            # Check if we already have an active session
            if self.current_session_dir and self.current_session_dir.exists():
                # Verify it's still valid
                metadata_file = self.current_session_dir / "metadata.json"
                if metadata_file.exists():
                    try:
                        with open(metadata_file, 'r') as f:
                            metadata = json.load(f)
                        if metadata.get('status') == 'active':
                            return self.current_session_dir
                    except Exception:
                        pass
            
            # Create timestamp-based session name with microseconds for uniqueness
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S%f")[:-3]  # Include milliseconds
            # Clean query for directory name
            clean_query = "".join(c for c in query[:50] if c.isalnum() or c in " -_").strip()
            clean_query = clean_query.replace(" ", "_")
            
            session_name = f"{timestamp}_{clean_query}" if clean_query else timestamp
            session_dir = self.workspace_dir / session_name
            
            # Ensure unique directory name
            attempt = 0
            while session_dir.exists() and attempt < 10:
                attempt += 1
                session_name = f"{timestamp}_{clean_query}_{attempt}" if clean_query else f"{timestamp}_{attempt}"
                session_dir = self.workspace_dir / session_name
            
            session_dir.mkdir(exist_ok=True)
            self.current_session_dir = session_dir
            
            # Initialize session metadata
            metadata = {
                'session_id': session_name,
                'created_at': datetime.now().isoformat(),
                'original_query': query,
                'status': 'active'
            }
            
            self._save_json(session_dir / "metadata.json", metadata)
            
            return session_dir
    
    def save_workflow_state(self, state: Dict[str, Any]) -> bool:
        """Save the complete workflow state"""
        if not self.current_session_dir:
            print("Error: No current session directory set")
            # Try to create a session if we have the original query
            if 'original_query' in state:
                self.create_session(state['original_query'])
            else:
                raise ValueError("Cannot save workflow state without a session directory")
        
        try:
            print(f"Saving workflow state to: {self.current_session_dir}")
            
            # Save main workflow state
            self._save_json(
                self.current_session_dir / "workflow_state.json",
                state
            )
            
            # Save individual components
            if 'clarified_request' in state and state['clarified_request']:
                print(f"Saving clarified request")
                self._save_text(
                    self.current_session_dir / "01_clarified_request.md",
                    f"# Clarified Research Request\n\n{state['clarified_request']}"
                )
            
            if 'subtasks' in state and state['subtasks']:
                print(f"Saving {len(state['subtasks'])} tasks")
                self._save_tasks(
                    self.current_session_dir / "02_research_tasks.md",
                    state['subtasks']
                )
            
            if 'scratchpads' in state and state['scratchpads']:
                print(f"Saving {len(state['scratchpads'])} scratchpads")
                self._save_scratchpads(state['scratchpads'])
            
            if 'document_analysis' in state and state['document_analysis']:
                print(f"Saving {len(state['document_analysis'])} document analyses")
                self._save_document_analysis(state['document_analysis'])
            
            if 'final_report' in state and state['final_report']:
                print(f"Saving final report")
                self._save_text(
                    self.current_session_dir / "05_final_report.md",
                    state['final_report']
                )
            
            # Update session status
            self._update_session_status(state)
            
            print(f"Successfully saved workflow state")
            
            # List files created
            if self.current_session_dir.exists():
                files = list(self.current_session_dir.rglob("*"))
                print(f"Files in session directory: {len(files)}")
                for f in files:
                    if f.is_file():
                        print(f"  - {f.relative_to(self.current_session_dir)}")
            
            return True
            
        except Exception as e:
            print(f"Error saving workflow state: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def load_workflow_state(self, session_dir: str) -> Optional[Dict[str, Any]]:
        """Load workflow state from a session directory"""
        session_path = self.workspace_dir / session_dir
        
        if not session_path.exists():
            return None
        
        try:
            state_file = session_path / "workflow_state.json"
            if state_file.exists():
                with open(state_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading workflow state: {e}")
        
        return None
    
    def list_sessions(self) -> List[Dict[str, Any]]:
        """List all research sessions"""
        sessions = []
        
        for session_dir in self.workspace_dir.iterdir():
            if session_dir.is_dir():
                metadata_file = session_dir / "metadata.json"
                if metadata_file.exists():
                    try:
                        with open(metadata_file, 'r', encoding='utf-8') as f:
                            metadata = json.load(f)
                            metadata['session_dir'] = session_dir.name
                            sessions.append(metadata)
                    except:
                        continue
        
        # Sort by creation date (newest first)
        sessions.sort(key=lambda x: x.get('created_at', ''), reverse=True)
        
        return sessions
    
    def _save_json(self, filepath: Path, data: Dict[str, Any]):
        """Save data as JSON with error handling"""
        try:
            # Ensure parent directory exists
            filepath.parent.mkdir(parents=True, exist_ok=True)
            
            # Write to temporary file first
            temp_filepath = filepath.with_suffix('.tmp')
            with open(temp_filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Move temp file to final location (atomic operation)
            temp_filepath.replace(filepath)
            
        except PermissionError as e:
            print(f"Permission denied while saving to {filepath}: {e}")
            raise
        except OSError as e:
            if e.errno == 28:  # ENOSPC - No space left on device
                print(f"Disk full while saving to {filepath}: {e}")
            else:
                print(f"OS error while saving to {filepath}: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error while saving JSON to {filepath}: {e}")
            raise
    
    def _save_text(self, filepath: Path, content: str):
        """Save text content with error handling"""
        try:
            # Ensure parent directory exists
            filepath.parent.mkdir(parents=True, exist_ok=True)
            
            # Write to temporary file first
            temp_filepath = filepath.with_suffix('.tmp')
            with open(temp_filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Move temp file to final location (atomic operation)
            temp_filepath.replace(filepath)
            
        except PermissionError as e:
            print(f"Permission denied while saving to {filepath}: {e}")
            raise
        except OSError as e:
            if e.errno == 28:  # ENOSPC - No space left on device
                print(f"Disk full while saving to {filepath}: {e}")
            else:
                print(f"OS error while saving to {filepath}: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error while saving text to {filepath}: {e}")
            raise
    
    def _save_tasks(self, filepath: Path, tasks: List[Dict[str, Any]]):
        """Save research tasks in markdown format"""
        content = ["# Research Tasks\n"]
        
        for i, task in enumerate(tasks, 1):
            content.append(f"## Task {i}: {task.get('title', 'Untitled')}")
            content.append(f"**ID:** {task.get('id', 'unknown')}")
            content.append(f"**Objective:** {task.get('objective', 'Not specified')}")
            content.append(f"**Scope:** {task.get('scope', 'Not specified')}")
            content.append(f"**Complexity:** {task.get('complexity', 'unknown')}")
            content.append(f"**Estimated Documents:** {task.get('estimated_documents', 0)}")
            
            if task.get('dependencies'):
                content.append(f"**Dependencies:** {', '.join(task['dependencies'])}")
            
            content.append("\n---\n")
        
        self._save_text(filepath, '\n'.join(content))
    
    def _save_scratchpads(self, scratchpads: Dict[str, Any]):
        """Save scratchpad contents for each subtask"""
        scratchpad_dir = self.current_session_dir / "03_scratchpads"
        scratchpad_dir.mkdir(exist_ok=True)
        
        for task_id, scratchpad in scratchpads.items():
            content = [f"# Scratchpad: {task_id}\n"]
            
            # Add metadata
            content.append(f"**Created:** {scratchpad.get('created_at', 'Unknown')}")
            content.append(f"**Iteration Count:** {scratchpad.get('iteration_count', 0)}")
            content.append(f"**Documents Analyzed:** {len(scratchpad.get('documents_analyzed', []))}\n")
            
            if 'documents_analyzed' in scratchpad:
                content.append("## Documents Analyzed")
                for doc in scratchpad['documents_analyzed']:
                    content.append(f"- {doc}")
                content.append("")
            
            if 'high_value_findings' in scratchpad:
                content.append("## High Value Findings")
                for i, finding in enumerate(scratchpad['high_value_findings'], 1):
                    content.append(f"{i}. {finding}")
                content.append("")
            
            if 'insights' in scratchpad:
                content.append("## Insights")
                for i, insight in enumerate(scratchpad['insights'], 1):
                    content.append(f"{i}. {insight}")
                content.append("")
            
            if 'quotes' in scratchpad:
                content.append("## Notable Quotes")
                for quote in scratchpad['quotes']:
                    content.append(f"> {quote}")
                    content.append("")
            
            if 'notes' in scratchpad:
                content.append("## Additional Notes")
                content.append(scratchpad['notes'])
            
            file_path = scratchpad_dir / f"{task_id}_scratchpad.md"
            self._save_text(file_path, '\n'.join(content))
            print(f"  Saved scratchpad: {file_path.name}")
    
    def _save_document_analysis(self, analyses: Dict[str, Any]):
        """Save document analysis results"""
        analysis_dir = self.current_session_dir / "04_document_analysis"
        analysis_dir.mkdir(exist_ok=True)
        
        for task_id, analysis in analyses.items():
            content = [f"# Document Analysis: {task_id}\n"]
            
            if 'document_analyses' in analysis:
                for doc in analysis['document_analyses']:
                    content.append(f"## {doc.get('document_title', 'Unknown Document')}")
                    content.append(f"**Relevance Score:** {doc.get('relevance_score', 0)}/10")
                    
                    if doc.get('key_information'):
                        content.append("\n### Key Information")
                        for info in doc['key_information']:
                            content.append(f"- {info}")
                    
                    if doc.get('insights'):
                        content.append("\n### Insights")
                        for insight in doc['insights']:
                            content.append(f"- {insight}")
                    
                    if doc.get('quotes'):
                        content.append("\n### Notable Quotes")
                        for quote in doc['quotes']:
                            content.append(f"> {quote}")
                    
                    content.append("\n---\n")
            
            if 'synthesis' in analysis:
                content.append("## Synthesis")
                content.append(analysis['synthesis'])
            
            if 'sufficiency' in analysis:
                content.append(f"\n**Sufficiency Status:** {analysis['sufficiency']}")
            
            if 'missing_information' in analysis:
                content.append("\n**Missing Information:**")
                for missing in analysis['missing_information']:
                    content.append(f"- {missing}")
            
            self._save_text(
                analysis_dir / f"{task_id}_analysis.md",
                '\n'.join(content)
            )
    
    def _update_session_status(self, state: Dict[str, Any]):
        """Update session metadata with current status"""
        if not self.current_session_dir:
            return
        
        metadata_file = self.current_session_dir / "metadata.json"
        if metadata_file.exists():
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                
                # Determine current stage
                if state.get('final_report'):
                    metadata['status'] = 'completed'
                elif state.get('document_analysis'):
                    metadata['status'] = 'researching'
                elif state.get('subtasks'):
                    metadata['status'] = 'planning'
                else:
                    metadata['status'] = 'initializing'
                
                metadata['last_updated'] = datetime.now().isoformat()
                metadata['progress'] = {
                    'clarified': bool(state.get('clarified_request')),
                    'tasks_defined': bool(state.get('subtasks')),
                    'research_complete': bool(state.get('scratchpads')),
                    'report_generated': bool(state.get('final_report'))
                }
                
                self._save_json(metadata_file, metadata)
                
            except Exception as e:
                print(f"Error updating session metadata: {e}")
    
    def get_current_session_dir(self) -> Optional[Path]:
        """Get the current session directory"""
        return self.current_session_dir
    
    def set_current_session(self, session_dir: str):
        """Set the current session directory with thread safety"""
        with self._session_lock:
            # Handle both full paths and just directory names
            if isinstance(session_dir, str) and session_dir.startswith(str(self.workspace_dir)):
                # Full path provided
                session_path = Path(session_dir)
            else:
                # Just directory name provided
                session_path = self.workspace_dir / session_dir
                
            if session_path.exists():
                self.current_session_dir = session_path
                print(f"Set current session directory to: {self.current_session_dir}")
                return True
            else:
                print(f"Session directory not found: {session_path}")
                return False


# Global persistence manager instance
workflow_persistence = WorkflowPersistence()