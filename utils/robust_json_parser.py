"""
Robust JSON Parser for LLM Responses
Handles various response formats and provides fallback extraction
"""

import json
import re
from typing import Dict, Any, Optional, List, Union
from pathlib import Path
from datetime import datetime


class RobustJSONParser:
    """A robust parser for extracting JSON from LLM responses"""
    
    def __init__(self, debug_mode: bool = True):
        self.debug_mode = debug_mode
        self.debug_file = Path("research_workspace/json_parser_debug.log")
        if debug_mode:
            self.debug_file.parent.mkdir(exist_ok=True)
    
    def parse(self, response: str, expected_structure: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Parse JSON from LLM response with multiple fallback strategies
        
        Args:
            response: The raw LLM response
            expected_structure: Optional dict describing expected JSON structure
            
        Returns:
            Parsed JSON as dict, with parse_error flag if parsing failed
        """
        if not response:
            return {'error': 'Empty response', 'parse_error': True}
        
        self._debug_log(f"Parsing response of length: {len(response)}")
        
        # Try multiple parsing strategies in order
        strategies = [
            ("clean_json", self._try_clean_json),
            ("markdown_blocks", self._try_markdown_blocks),
            ("find_json_object", self._try_find_json_object),
            ("relaxed_json", self._try_relaxed_json),
            ("extract_structure", self._try_extract_structure),
        ]
        
        for strategy_name, strategy_func in strategies:
            try:
                result = strategy_func(response)
                if result and isinstance(result, dict):
                    self._debug_log(f"Success with strategy: {strategy_name}")
                    # Validate against expected structure if provided
                    if expected_structure:
                        self._fill_missing_fields(result, expected_structure)
                    return result
            except Exception as e:
                self._debug_log(f"Strategy {strategy_name} failed: {str(e)}")
                continue
        
        # All strategies failed - return with parse error
        self._debug_log("All parsing strategies failed")
        return {
            'raw_response': response,
            'parse_error': True,
            'error': 'Failed to parse JSON from response'
        }
    
    def _try_clean_json(self, response: str) -> Optional[Dict]:
        """Try to parse clean JSON directly"""
        response = response.strip()
        
        # Remove common prefixes/suffixes
        prefixes_to_remove = [
            "Here is the JSON response:",
            "Here's the JSON:",
            "JSON:",
            "Response:",
            "Output:",
        ]
        
        for prefix in prefixes_to_remove:
            if response.lower().startswith(prefix.lower()):
                response = response[len(prefix):].strip()
        
        # Try direct parsing
        return json.loads(response)
    
    def _try_markdown_blocks(self, response: str) -> Optional[Dict]:
        """Extract JSON from markdown code blocks"""
        # Look for ```json blocks
        json_block_pattern = r'```(?:json)?\s*\n?(.*?)\n?```'
        matches = re.findall(json_block_pattern, response, re.DOTALL)
        
        for match in matches:
            try:
                return json.loads(match.strip())
            except:
                continue
        
        # Look for ``` blocks without json tag
        code_block_pattern = r'```\s*\n?(.*?)\n?```'
        matches = re.findall(code_block_pattern, response, re.DOTALL)
        
        for match in matches:
            match = match.strip()
            if match.startswith('{') and match.endswith('}'):
                try:
                    return json.loads(match)
                except:
                    continue
        
        return None
    
    def _try_find_json_object(self, response: str) -> Optional[Dict]:
        """Find and extract JSON object using brace matching"""
        # Find the first { and match it with its closing }
        start_idx = response.find('{')
        if start_idx == -1:
            return None
        
        brace_count = 0
        in_string = False
        escape_next = False
        
        for i in range(start_idx, len(response)):
            char = response[i]
            
            if escape_next:
                escape_next = False
                continue
                
            if char == '\\':
                escape_next = True
                continue
                
            if char == '"' and not escape_next:
                in_string = not in_string
                continue
            
            if not in_string:
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        json_str = response[start_idx:i+1]
                        return json.loads(json_str)
        
        return None
    
    def _try_relaxed_json(self, response: str) -> Optional[Dict]:
        """Try parsing with relaxed JSON rules"""
        # This handles common issues like trailing commas, single quotes, etc.
        
        # Extract potential JSON content
        json_match = re.search(r'\{[^{}]*\}', response, re.DOTALL)
        if not json_match:
            return None
        
        json_str = json_match.group(0)
        
        # Fix common issues
        # Replace single quotes with double quotes (careful with apostrophes)
        json_str = re.sub(r"(?<!\\)'([^']*)'(?=\s*:)", r'"\1"', json_str)
        json_str = re.sub(r":\s*'([^']*)'", r': "\1"', json_str)
        
        # Remove trailing commas
        json_str = re.sub(r',\s*}', '}', json_str)
        json_str = re.sub(r',\s*]', ']', json_str)
        
        # Try to parse
        return json.loads(json_str)
    
    def _try_extract_structure(self, response: str) -> Optional[Dict]:
        """Extract structure using pattern matching as last resort"""
        result = {}
        
        # Extract query analysis if present
        query_analysis_match = re.search(
            r'"query_analysis"\s*:\s*\{([^}]+)\}', 
            response, 
            re.DOTALL
        )
        if query_analysis_match:
            result['query_analysis'] = self._extract_query_analysis(query_analysis_match.group(1))
        
        # Extract clarifying questions
        questions = self._extract_clarifying_questions(response)
        if questions:
            result['clarifying_questions'] = questions
        
        # Extract other common fields
        fields_patterns = [
            (r'"original_query"\s*:\s*"([^"]+)"', 'original_query'),
            (r'"suggested_refinement"\s*:\s*"([^"]+)"', 'suggested_refinement'),
            (r'"request_summary"\s*:\s*"([^"]+)"', 'request_summary'),
        ]
        
        for pattern, field_name in fields_patterns:
            match = re.search(pattern, response)
            if match:
                result[field_name] = match.group(1)
        
        return result if result else None
    
    def _extract_query_analysis(self, content: str) -> Dict[str, Any]:
        """Extract query analysis structure"""
        analysis = {}
        
        # Extract main topic
        topic_match = re.search(r'"main_topic"\s*:\s*"([^"]+)"', content)
        if topic_match:
            analysis['main_topic'] = topic_match.group(1)
        
        # Extract implicit needs
        needs_match = re.search(r'"implicit_needs"\s*:\s*\[([^\]]+)\]', content)
        if needs_match:
            needs = re.findall(r'"([^"]+)"', needs_match.group(1))
            analysis['implicit_needs'] = needs
        
        # Extract ambiguities
        ambig_match = re.search(r'"ambiguities"\s*:\s*\[([^\]]+)\]', content)
        if ambig_match:
            ambiguities = re.findall(r'"([^"]+)"', ambig_match.group(1))
            analysis['ambiguities'] = ambiguities
        
        return analysis
    
    def _extract_clarifying_questions(self, response: str) -> List[Dict[str, Any]]:
        """Extract clarifying questions from response"""
        questions = []
        
        # Look for question patterns
        question_pattern = r'\{[^{}]*"question"\s*:\s*"([^"]+)"[^{}]*\}'
        matches = re.finditer(question_pattern, response, re.DOTALL)
        
        for match in matches:
            question_block = match.group(0)
            question_obj = {'question': match.group(1)}
            
            # Extract purpose
            purpose_match = re.search(r'"purpose"\s*:\s*"([^"]+)"', question_block)
            if purpose_match:
                question_obj['purpose'] = purpose_match.group(1)
            
            # Extract options
            options_match = re.search(r'"options"\s*:\s*\[([^\]]+)\]', question_block)
            if options_match:
                options = re.findall(r'"([^"]+)"', options_match.group(1))
                question_obj['options'] = options
            
            questions.append(question_obj)
        
        return questions
    
    def _fill_missing_fields(self, result: Dict, expected: Dict) -> None:
        """Fill in missing fields with defaults based on expected structure"""
        for key, value in expected.items():
            if key not in result:
                if isinstance(value, dict):
                    result[key] = {}
                elif isinstance(value, list):
                    result[key] = []
                elif isinstance(value, str):
                    result[key] = ""
                elif isinstance(value, (int, float)):
                    result[key] = 0
                elif isinstance(value, bool):
                    result[key] = False
    
    def _debug_log(self, message: str) -> None:
        """Log debug information"""
        if self.debug_mode:
            with open(self.debug_file, 'a', encoding='utf-8') as f:
                timestamp = datetime.now().isoformat()
                f.write(f"[{timestamp}] {message}\n")


# Expected structures for different workflow stages
EXPECTED_STRUCTURES = {
    'inquiry_clarification': {
        'original_query': '',
        'query_analysis': {
            'main_topic': '',
            'implicit_needs': [],
            'ambiguities': []
        },
        'clarifying_questions': [],
        'suggested_refinement': ''
    },
    'task_decomposition': {
        'request_summary': '',
        'subtasks': [],
        'execution_order': [],
        'success_criteria': ''
    },
    'document_analysis': {
        'document_analyses': [],
        'synthesis': '',
        'sufficiency': '',
        'missing_information': []
    }
}


def parse_llm_json(response: str, stage: Optional[str] = None) -> Dict[str, Any]:
    """
    Convenience function to parse LLM JSON responses
    
    Args:
        response: The raw LLM response
        stage: Optional workflow stage to get expected structure
        
    Returns:
        Parsed JSON dictionary
    """
    parser = RobustJSONParser()
    expected = EXPECTED_STRUCTURES.get(stage) if stage else None
    return parser.parse(response, expected)


# Test the parser with various formats
if __name__ == "__main__":
    test_responses = [
        # Clean JSON
        '{"test": "value"}',
        
        # JSON in markdown
        '```json\n{"test": "value"}\n```',
        
        # JSON with text before/after
        'Here is the response:\n{"test": "value"}\nThat\'s all!',
        
        # Malformed JSON with single quotes
        "{'test': 'value'}",
        
        # JSON with trailing comma
        '{"test": "value",}',
        
        # Complex nested structure
        '''
        ```json
        {
            "query_analysis": {
                "main_topic": "AI Agents",
                "implicit_needs": ["comparison", "use cases"],
                "ambiguities": ["scope", "detail level"]
            },
            "clarifying_questions": [
                {
                    "question": "What industries?",
                    "purpose": "To focus examples",
                    "options": ["Healthcare", "Finance", "General"]
                }
            ]
        }
        ```
        '''
    ]
    
    parser = RobustJSONParser(debug_mode=True)
    
    for i, response in enumerate(test_responses):
        print(f"\nTest {i+1}:")
        result = parser.parse(response)
        if 'parse_error' in result:
            print("  ❌ Parse failed")
        else:
            print("  ✅ Parse successful")
            print(f"  Result: {json.dumps(result, indent=2)}")