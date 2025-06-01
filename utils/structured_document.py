"""
Structured Document Management System

This module provides functionality to store documents as markdown content + JSON metadata,
enabling precise section identification and modification for QA improvements.
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import hashlib

class DocumentSection:
    """Represents a section within a structured document."""
    
    def __init__(self, id: str, title: str, level: int, start_line: int, end_line: int, 
                 char_start: int, char_end: int, parent: Optional[str] = None):
        self.id = id
        self.title = title
        self.level = level
        self.start_line = start_line
        self.end_line = end_line
        self.char_start = char_start
        self.char_end = char_end
        self.parent = parent
        self.subsections: List[str] = []
        self.metadata: Dict[str, Any] = {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert section to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "level": self.level,
            "start_line": self.start_line,
            "end_line": self.end_line,
            "char_start": self.char_start,
            "char_end": self.char_end,
            "parent": self.parent,
            "subsections": self.subsections,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DocumentSection':
        """Create section from dictionary."""
        section = cls(
            data["id"], data["title"], data["level"],
            data["start_line"], data["end_line"],
            data["char_start"], data["char_end"],
            data.get("parent")
        )
        section.subsections = data.get("subsections", [])
        section.metadata = data.get("metadata", {})
        return section

class QAIssue:
    """Represents a QA issue linked to a specific document section."""
    
    def __init__(self, id: str, section_id: str, issue_type: str, description: str,
                 suggested_fix: str, status: str = "open"):
        self.id = id
        self.section_id = section_id
        self.type = issue_type
        self.description = description
        self.suggested_fix = suggested_fix
        self.status = status
        self.created = datetime.now().isoformat()
        self.custom_instruction: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert issue to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "section_id": self.section_id,
            "type": self.type,
            "description": self.description,
            "suggested_fix": self.suggested_fix,
            "status": self.status,
            "created": self.created,
            "custom_instruction": self.custom_instruction
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QAIssue':
        """Create issue from dictionary."""
        issue = cls(
            data["id"], data["section_id"], data["type"],
            data["description"], data["suggested_fix"], data.get("status", "open")
        )
        issue.created = data.get("created", datetime.now().isoformat())
        issue.custom_instruction = data.get("custom_instruction")
        return issue

class StructuredDocument:
    """Manages a document with separate markdown content and JSON structure metadata."""
    
    def __init__(self, document_id: str, base_path: Path):
        self.document_id = document_id
        self.base_path = Path(base_path)
        self.version = "1.0"
        self.created = datetime.now().isoformat()
        self.last_modified = datetime.now().isoformat()
        
        self.sections: Dict[str, DocumentSection] = {}
        self.qa_issues: Dict[str, QAIssue] = {}
        self.content_hash = ""
        
        # File paths
        self.content_file = self.base_path / f"{document_id}.md"
        self.structure_file = self.base_path / f"{document_id}_structure.json"
        self.versions_file = self.base_path / f"{document_id}_versions.json"
    
    def parse_markdown_content(self, content: str) -> None:
        """Parse markdown content and extract section structure."""
        lines = content.split('\n')
        sections = {}
        current_sections = []  # Stack to track nested sections
        
        char_pos = 0
        for line_num, line in enumerate(lines, 1):
            # Check for markdown headers
            if line.strip().startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                title = line.lstrip('#').strip()
                
                # Close sections that are at the same level or deeper
                while current_sections and current_sections[-1].level >= level:
                    closing_section = current_sections.pop()
                    closing_section.end_line = line_num - 1
                    closing_section.char_end = char_pos
                
                # Create new section
                section_id = self._generate_section_id(title, level)
                parent_id = current_sections[-1].id if current_sections else None
                
                section = DocumentSection(
                    id=section_id,
                    title=title,
                    level=level,
                    start_line=line_num,
                    end_line=len(lines),  # Will be updated when next section starts
                    char_start=char_pos,
                    char_end=len(content),  # Will be updated
                    parent=parent_id
                )
                
                sections[section_id] = section
                current_sections.append(section)
                
                # Update parent's subsections
                if parent_id and parent_id in sections:
                    sections[parent_id].subsections.append(section_id)
            
            char_pos += len(line) + 1  # +1 for newline
        
        # Close remaining sections
        for section in current_sections:
            section.end_line = len(lines)
            section.char_end = len(content)
        
        self.sections = sections
        self.content_hash = hashlib.md5(content.encode()).hexdigest()
    
    def _generate_section_id(self, title: str, level: int) -> str:
        """Generate a unique section ID based on title and level."""
        # Clean title for ID
        clean_title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
        clean_title = re.sub(r'\s+', '_', clean_title.strip()).lower()
        
        # Add level prefix
        level_prefix = f"h{level}"
        
        # Ensure uniqueness
        base_id = f"{level_prefix}_{clean_title}"
        counter = 1
        section_id = base_id
        
        while section_id in self.sections:
            section_id = f"{base_id}_{counter}"
            counter += 1
        
        return section_id
    
    def get_section_content(self, section_id: str, content: str) -> str:
        """Extract content for a specific section."""
        if section_id not in self.sections:
            return ""
        
        section = self.sections[section_id]
        
        # Validate section boundaries
        if section.char_start < 0 or section.char_end > len(content) or section.char_start > section.char_end:
            print(f"Warning: Invalid section boundaries for {section_id}")
            return ""
            
        return content[section.char_start:section.char_end]
    
    def replace_section_content(self, section_id: str, content: str, new_content: str) -> str:
        """Replace content for a specific section and return updated document."""
        if section_id not in self.sections:
            print(f"Warning: Section {section_id} not found")
            return content
        
        section = self.sections[section_id]
        
        # Validate section boundaries
        if section.char_start < 0 or section.char_end > len(content) or section.char_start > section.char_end:
            print(f"Warning: Invalid section boundaries for {section_id}")
            return content
        
        # Replace the section content
        before = content[:section.char_start]
        after = content[section.char_end:]
        updated_content = before + new_content + after
        
        # Update section boundaries for this and subsequent sections
        char_diff = len(new_content) - (section.char_end - section.char_start)
        
        # Calculate line difference for updating line numbers
        old_lines = content[section.char_start:section.char_end].count('\n')
        new_lines = new_content.count('\n')
        line_diff = new_lines - old_lines
        
        for other_section in self.sections.values():
            if other_section.char_start > section.char_end:
                other_section.char_start += char_diff
                other_section.char_end += char_diff
                other_section.start_line += line_diff
                other_section.end_line += line_diff
        
        section.char_end = section.char_start + len(new_content)
        section.end_line = section.start_line + new_lines
        
        return updated_content
    
    def add_qa_issue(self, section_id: str, issue_type: str, description: str, 
                     suggested_fix: str) -> str:
        """Add a QA issue for a specific section."""
        issue_id = f"issue_{len(self.qa_issues) + 1}"
        
        issue = QAIssue(
            id=issue_id,
            section_id=section_id,
            issue_type=issue_type,
            description=description,
            suggested_fix=suggested_fix
        )
        
        self.qa_issues[issue_id] = issue
        
        # Update section metadata
        if section_id in self.sections:
            if "qa_issues" not in self.sections[section_id].metadata:
                self.sections[section_id].metadata["qa_issues"] = []
            self.sections[section_id].metadata["qa_issues"].append(issue_id)
        
        return issue_id
    
    def get_issues_for_section(self, section_id: str) -> List[QAIssue]:
        """Get all QA issues for a specific section."""
        return [issue for issue in self.qa_issues.values() if issue.section_id == section_id]
    
    def save_structure(self) -> None:
        """Save document structure to JSON file."""
        structure_data = {
            "document_id": self.document_id,
            "version": self.version,
            "created": self.created,
            "last_modified": datetime.now().isoformat(),
            "content_hash": self.content_hash,
            "sections": [section.to_dict() for section in self.sections.values()],
            "qa_issues": [issue.to_dict() for issue in self.qa_issues.values()]
        }
        
        with open(self.structure_file, 'w', encoding='utf-8') as f:
            json.dump(structure_data, f, indent=2, ensure_ascii=False)
    
    def load_structure(self) -> bool:
        """Load document structure from JSON file."""
        if not self.structure_file.exists():
            return False
        
        try:
            with open(self.structure_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.version = data.get("version", "1.0")
            self.created = data.get("created", datetime.now().isoformat())
            self.last_modified = data.get("last_modified", datetime.now().isoformat())
            self.content_hash = data.get("content_hash", "")
            
            # Load sections
            self.sections = {}
            for section_data in data.get("sections", []):
                section = DocumentSection.from_dict(section_data)
                self.sections[section.id] = section
            
            # Load QA issues
            self.qa_issues = {}
            for issue_data in data.get("qa_issues", []):
                issue = QAIssue.from_dict(issue_data)
                self.qa_issues[issue.id] = issue
            
            return True
        except Exception as e:
            print(f"Error loading structure: {e}")
            return False
    
    def save_content(self, content: str) -> None:
        """Save markdown content to file."""
        with open(self.content_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def load_content(self) -> str:
        """Load markdown content from file."""
        if not self.content_file.exists():
            return ""
        
        with open(self.content_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def create_version_snapshot(self, content: str, description: str = "") -> None:
        """Create a version snapshot of the current document state."""
        version_data = {
            "version": self.version,
            "timestamp": datetime.now().isoformat(),
            "description": description,
            "content_hash": self.content_hash,
            "sections_count": len(self.sections),
            "qa_issues_count": len(self.qa_issues)
        }
        
        # Load existing versions
        versions = []
        if self.versions_file.exists():
            try:
                with open(self.versions_file, 'r', encoding='utf-8') as f:
                    versions = json.load(f)
            except:
                versions = []
        
        versions.append(version_data)
        
        # Keep only last 10 versions
        versions = versions[-10:]
        
        with open(self.versions_file, 'w', encoding='utf-8') as f:
            json.dump(versions, f, indent=2)

def create_structured_document_from_markdown(content: str, document_id: str, 
                                           base_path: Path) -> StructuredDocument:
    """Create a structured document from existing markdown content."""
    doc = StructuredDocument(document_id, base_path)
    doc.parse_markdown_content(content)
    doc.save_content(content)
    doc.save_structure()
    return doc

def load_or_create_structured_document(document_id: str, base_path: Path, 
                                     markdown_content: str = "") -> StructuredDocument:
    """Load existing structured document or create new one from markdown."""
    doc = StructuredDocument(document_id, base_path)
    
    if doc.load_structure() and doc.content_file.exists():
        # Verify content hasn't changed
        current_content = doc.load_content()
        current_hash = hashlib.md5(current_content.encode()).hexdigest()
        
        if current_hash != doc.content_hash:
            # Content changed, reparse
            doc.parse_markdown_content(current_content)
            doc.save_structure()
    else:
        # Create new structured document
        if markdown_content:
            doc.parse_markdown_content(markdown_content)
            doc.save_content(markdown_content)
            doc.save_structure()
    
    return doc