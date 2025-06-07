"""
Content Intelligence and Analysis Module
This module contains functions for analyzing content using LLMs to extract
entities, concepts, relationships, and metadata across any domain.
"""

import json
from typing import Dict, Any

from .llm_client import call_llm


def extract_content_intelligence(content_text: str, title: str, author: str = "Unknown", content_type: str = "general") -> dict:
    """
    Universal content analysis using LLM to extract entities, concepts, relationships, and metadata
    Works across any domain - Azure, movies, cooking, survival, etc.
    """
    if not content_text or not content_text.strip():
        return {
            'entities': [],
            'concepts': [],
            'content_structure': 'unknown',
            'difficulty_level': 'unknown',
            'prerequisites': [],
            'related_topics': [],
            'authority_signals': [],
            'category': 'General',
            'tags': [],
            'confidence_score': 0.1
        }
    
    # Create universal content analysis prompt
    prompt = f"""Analyze this content and extract structured information. Be domain-agnostic and work for any topic (tech, entertainment, cooking, survival, etc.).

CONTENT TITLE: {title}
AUTHOR/CREATOR: {author}
CONTENT TYPE: {content_type}

CONTENT TEXT:
{content_text[:8000]}

Please extract the following information in a structured format:

1. ENTITIES (specific people, places, tools, technologies, movies, etc.):
   - List 5-10 most important specific entities mentioned

2. CONCEPTS (abstract ideas, methodologies, genres, skills, etc.):
   - List 5-10 key concepts or topics covered

3. CONTENT STRUCTURE (what type of content this is):
   - tutorial/how-to, overview/explanation, comparison/review, troubleshooting/problem-solving, list/compilation, or discussion/opinion

4. DIFFICULTY LEVEL:
   - beginner, intermediate, advanced, or expert

5. PREREQUISITES (what someone should know/have before this content):
   - List 3-5 prerequisites if any are mentioned or implied

6. RELATED TOPICS (what naturally connects to this content):
   - List 5-8 related topics someone might want to learn about

7. AUTHORITY SIGNALS (indicators of expertise or confidence):
   - Quote specific phrases that show authority/experience
   - Rate confidence: high/medium/low

8. CATEGORY RECOMMENDATION:
   - Suggest the best high-level category for this content

9. DESCRIPTIVE TAGS:
   - List 8-12 descriptive tags that would help find this content

Please format your response as a valid JSON object with these exact keys:
{{
  "entities": ["entity1", "entity2"],
  "concepts": ["concept1", "concept2"],
  "content_structure": "tutorial",
  "difficulty_level": "intermediate",
  "prerequisites": ["prereq1", "prereq2"],
  "related_topics": ["topic1", "topic2"],
  "authority_signals": ["quote1", "quote2"],
  "category": "Category Name",
  "tags": ["tag1", "tag2"],
  "confidence_score": 0.8
}}"""

    try:
        response = call_llm(prompt, "content intelligence extraction")
        
        if not response:
            return _fallback_content_analysis(title, content_text)
        
        # Parse JSON response
        try:
            # Clean up response to extract JSON
            if '```json' in response:
                response = response.split('```json')[1].split('```')[0]
            elif '```' in response:
                response = response.split('```')[1].split('```')[0]
            
            result = json.loads(response)
            
            # Validate required fields
            required_fields = ['entities', 'concepts', 'content_structure', 'difficulty_level', 
                             'prerequisites', 'related_topics', 'authority_signals', 'category', 'tags']
            
            for field in required_fields:
                if field not in result:
                    result[field] = []
            
            # Ensure confidence score exists
            if 'confidence_score' not in result:
                result['confidence_score'] = 0.7
            
            return result
            
        except json.JSONDecodeError:
            # If JSON parsing fails, try to extract information manually
            return _parse_unstructured_response(response, title)
            
    except Exception as e:
        print(f"Error in content intelligence extraction: {str(e)}")
        return _fallback_content_analysis(title, content_text)


def _fallback_content_analysis(title: str, content_text: str) -> dict:
    """Fallback analysis when LLM is unavailable"""
    # Simple keyword-based analysis
    words = content_text.lower().split()
    
    # Detect some basic patterns
    has_steps = any(word in content_text.lower() for word in ['step', 'first', 'second', 'then', 'next', 'finally'])
    has_comparison = any(word in content_text.lower() for word in ['versus', 'vs', 'better', 'worse', 'compare'])
    has_tutorial = any(word in content_text.lower() for word in ['how to', 'tutorial', 'guide', 'instruction'])
    
    if has_tutorial or has_steps:
        structure = 'tutorial'
    elif has_comparison:
        structure = 'comparison'
    else:
        structure = 'overview'
    
    # Basic category detection
    category = "General"
    if any(word in title.lower() for word in ['azure', 'cloud', 'microsoft', 'aws', 'tech']):
        category = "Technology"
    elif any(word in title.lower() for word in ['movie', 'film', 'actor', 'director']):
        category = "Entertainment"
    elif any(word in title.lower() for word in ['cook', 'recipe', 'food', 'kitchen']):
        category = "Cooking"
    elif any(word in title.lower() for word in ['survival', 'outdoor', 'camping', 'wilderness']):
        category = "Outdoor"
    
    return {
        'entities': [title],
        'concepts': [],
        'content_structure': structure,
        'difficulty_level': 'intermediate',
        'prerequisites': [],
        'related_topics': [],
        'authority_signals': [],
        'category': category,
        'tags': [structure, category.lower()],
        'confidence_score': 0.3
    }


def _parse_unstructured_response(response_text: str, title: str) -> dict:
    """Parse LLM response when JSON parsing fails"""
    # Try to extract information from unstructured text
    lines = response_text.split('\n')
    
    result = {
        'entities': [],
        'concepts': [],
        'content_structure': 'unknown',
        'difficulty_level': 'unknown',
        'prerequisites': [],
        'related_topics': [],
        'authority_signals': [],
        'category': 'General',
        'tags': [],
        'confidence_score': 0.5
    }
    
    current_section = None
    for line in lines:
        line = line.strip()
        if 'entities' in line.lower():
            current_section = 'entities'
        elif 'concepts' in line.lower():
            current_section = 'concepts'
        elif 'tags' in line.lower():
            current_section = 'tags'
        elif 'category' in line.lower() and ':' in line:
            result['category'] = line.split(':')[1].strip()
        elif current_section and line.startswith('-'):
            item = line[1:].strip()
            if current_section in result and isinstance(result[current_section], list):
                result[current_section].append(item)
    
    return result