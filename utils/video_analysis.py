"""
Video Analysis Module
This module contains functions for analyzing YouTube videos including
classification, summarization, and tag recommendation.
"""

import json
from typing import Any, Dict, List, Optional

from .llm_client import call_llm


def classify_youtube_video(summary: str, video_title: str, video_author: str, knowledgebase_categories: List[str] = None) -> Dict[str, Any]:
    """
    Classify a YouTube video into the appropriate category using LLM.
    
    Args:
        summary: Concise summary of the video content
        video_title: Title of the video
        video_author: Channel/author name
        knowledgebase_categories: List of available categories in the knowledge base
        
    Returns:
        Dict with 'category', 'confidence', and optionally 'reasoning' keys
    """
    # Default categories if none provided
    if knowledgebase_categories is None:
        knowledgebase_categories = [
            "Programming", "AI/ML", "DevOps", "Web Development", 
            "Database", "Security", "Unclassified"
        ]
    
    # Create the system prompt with category descriptions
    system_prompt = """You are an expert content classifier for a technical knowledge base. Your task is to analyze YouTube video content and assign it to the most appropriate category.

Available Categories:
- Programming: Software development, coding tutorials, programming languages, algorithms, design patterns
- AI/ML: Artificial intelligence, machine learning, deep learning, neural networks, data science
- DevOps: CI/CD, cloud computing, infrastructure, deployment, containers, Kubernetes, monitoring
- Web Development: Frontend, backend, web frameworks, HTML/CSS/JavaScript, APIs, web services
- Database: SQL, NoSQL, database design, data modeling, database administration
- Security: Cybersecurity, encryption, security best practices, penetration testing, vulnerabilities
- Unclassified: Content that doesn't clearly fit into any of the above categories

Guidelines:
1. Choose the single most relevant category based on the primary focus of the content
2. Consider the video title, author expertise, and content summary
3. If content spans multiple categories, choose the dominant theme
4. Only use "Unclassified" if the content truly doesn't fit any category
5. Base your decision on the actual content, not just keywords"""

    # Create the user prompt
    user_prompt = f"""Classify the following YouTube video into one of these categories: {', '.join(knowledgebase_categories)}

Video Title: {video_title}
Channel/Author: {video_author}
Content Summary: {summary}

Respond with ONLY the category name, nothing else."""

    # Call the LLM
    llm_response = call_llm(system_prompt + "\n\n" + user_prompt, operation_name="video_classification")
    
    if llm_response:
        # Clean and validate the response
        category = llm_response.strip().strip('"').strip("'")
        
        # Validate category
        if category in knowledgebase_categories:
            return {
                "category": category,
                "confidence": "high",
                "method": "llm_classification"
            }
        else:
            # Try to find closest match
            category_lower = category.lower()
            for valid_category in knowledgebase_categories:
                if valid_category.lower() in category_lower or category_lower in valid_category.lower():
                    return {
                        "category": valid_category,
                        "confidence": "medium",
                        "method": "llm_classification_fuzzy"
                    }
            
            # Default to Unclassified if no match
            return {
                "category": "Unclassified",
                "confidence": "low",
                "original_response": category,
                "method": "llm_classification_failed"
            }
    else:
        # Fallback classification based on keywords
        return fallback_classification(video_title, summary, knowledgebase_categories)


def fallback_classification(title: str, summary: str, categories: List[str]) -> Dict[str, Any]:
    """
    Fallback classification using keyword matching when LLM fails.
    """
    text = (title + " " + summary).lower()
    
    # Keyword mappings
    category_keywords = {
        "Programming": ["programming", "coding", "code", "algorithm", "function", "class", "python", "java", "javascript", "c++"],
        "AI/ML": ["ai", "artificial intelligence", "machine learning", "ml", "neural", "deep learning", "model", "training"],
        "DevOps": ["devops", "docker", "kubernetes", "ci/cd", "deployment", "cloud", "aws", "azure", "infrastructure"],
        "Web Development": ["web", "frontend", "backend", "html", "css", "react", "angular", "api", "rest", "website"],
        "Database": ["database", "sql", "nosql", "mongodb", "postgresql", "mysql", "query", "data model"],
        "Security": ["security", "cybersecurity", "encryption", "vulnerability", "penetration", "firewall", "authentication"]
    }
    
    # Count keyword matches
    scores = {}
    for category, keywords in category_keywords.items():
        if category in categories:
            score = sum(1 for keyword in keywords if keyword in text)
            if score > 0:
                scores[category] = score
    
    if scores:
        # Return the category with highest score
        best_category = max(scores, key=scores.get)
        return {
            "category": best_category,
            "confidence": "low",
            "method": "keyword_fallback",
            "score": scores[best_category]
        }
    
    return {
        "category": "Unclassified",
        "confidence": "low",
        "method": "no_match"
    }


def recommend_category_and_tags(transcript: str, video_title: str, video_author: str) -> Dict[str, Any]:
    """
    Recommend a category and suggest tags for a YouTube video.
    
    Args:
        transcript: The full transcript text
        video_title: Title of the video
        video_author: Channel/author name
        
    Returns:
        Dict with 'category' and 'tags' keys, or None if failed
    """
    prompt = f"""Based on the following YouTube video information, please recommend a category and suggest relevant tags.

Video Title: {video_title}
Channel/Author: {video_author}

Transcript excerpt:
{transcript[:3000]}...

Available categories:
- Programming: Software development, coding tutorials, programming languages
- AI/ML: Artificial intelligence, machine learning, deep learning, neural networks
- DevOps: CI/CD, cloud computing, infrastructure, deployment, containers
- Web Development: Frontend, backend, web frameworks, HTML/CSS/JavaScript
- Database: SQL, NoSQL, database design, data modeling
- Security: Cybersecurity, encryption, security best practices

Please respond in the following JSON format ONLY (no additional text):
{{
    "category": "One of the categories listed above",
    "tags": ["tag1", "tag2", "tag3", "tag4", "tag5"],
    "category_reasoning": "Brief explanation of why this category was chosen"
}}

Provide 5-7 relevant tags that describe the content. Tags should be lowercase and concise."""

    response = call_llm(prompt, "category and tag recommendation")
    if not response:
        return {"category": "Programming", "tags": [], "category_reasoning": "Failed to get recommendation"}
    
    try:
        # Try to parse as JSON
        result = json.loads(response)
        
        # Validate category
        valid_categories = ["Programming", "AI/ML", "DevOps", "Web Development", "Database", "Security"]
        if result.get("category") not in valid_categories:
            result["category"] = "Programming"  # Default
            
        # Ensure tags is a list
        if not isinstance(result.get("tags"), list):
            result["tags"] = []
            
        return result
    except json.JSONDecodeError:
        # If JSON parsing fails, try to extract information manually
        category = "Programming"  # Default
        tags = []
        
        # Simple pattern matching for category
        response_lower = response.lower()
        if "ai/ml" in response_lower or "artificial intelligence" in response_lower or "machine learning" in response_lower:
            category = "AI/ML"
        elif "devops" in response_lower or "deployment" in response_lower or "cloud" in response_lower:
            category = "DevOps"
        elif "web development" in response_lower or "frontend" in response_lower or "backend" in response_lower:
            category = "Web Development"
        elif "database" in response_lower or "sql" in response_lower:
            category = "Database"
        elif "security" in response_lower or "cybersecurity" in response_lower:
            category = "Security"
            
        return {"category": category, "tags": tags, "category_reasoning": "Extracted from response"}


def summarize_youtube_transcript(transcript: str, video_title: str, video_author: str) -> Optional[str]:
    """
    Summarize a YouTube video transcript using the configured LLM.
    
    Args:
        transcript: The full transcript text
        video_title: Title of the video
        video_author: Channel/author name
        
    Returns:
        A summary with key points, or None if failed
    """
    prompt = f"""Please provide a comprehensive summary of the following YouTube video transcript.

Video Title: {video_title}
Channel/Author: {video_author}

Instructions:
1. Start with a brief overview (2-3 sentences)
2. List the main key points or topics covered (use bullet points)
3. Include any important quotes or insights
4. If there are actionable items or recommendations, list them separately
5. Keep the summary concise but informative

Transcript:
{transcript[:8000]}...  # Limiting to avoid token limits

Please format your response in markdown."""

    return call_llm(prompt, "YouTube video summarization")