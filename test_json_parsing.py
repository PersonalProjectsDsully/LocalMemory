#!/usr/bin/env python3
"""Test JSON parsing to debug the issue"""

import json

# The actual response from the saved file
test_response = '''
{
  "original_query": "I Would like to understand when to use AI Agents, vs other AI systems.",
  "query_analysis": {
    "main_topic": "Differences and use cases of AI Agents versus other AI systems",
    "implicit_needs": [
      "Examples or scenarios illustrating when to choose AI Agents",
      "Comparison criteria between AI Agents and other AI systems",
      "Understanding of specific types of AI systems"
    ],
    "ambiguities": [
      "What specific AI systems are being compared (e.g., machine learning models, rule-based systems)?",
      "Level of detail desired (overview, in-depth analysis, case studies)?",
      "Intended application or industry context"
    ]
  },
  "clarifying_questions": [
    {
      "question": "Are you interested in understanding the use cases of AI Agents in particular industries or general applications?",
      "purpose": "To tailor examples and explanations to relevant contexts",
      "options": ["Industry-specific (e.g., healthcare, finance)", "General AI applications"]
    },
    {
      "question": "Would you like detailed case studies or high-level overviews of when to use AI Agents versus other AI systems?",
      "purpose": "To determine the depth of information needed",
      "options": ["Case studies", "High-level summaries"]
    },
    {
      "question": "Are you comparing AI Agents mainly to other autonomous AI systems, or to traditional AI models like supervised learning?",
      "purpose": "To clarify the scope of comparison",
      "options": ["Other autonomous AI systems", "Traditional AI models", "Both"]
    },
    {
      "question": "Do you have specific constraints or preferences, such as focusing on ethical considerations, performance, or implementation complexity?",
      "purpose": "To provide insights aligned with your priorities",
      "options": ["Ethics", "Performance", "Ease of implementation", "Cost"]
    }
  ],
  "suggested_refinement": "Specify the context or industry you are interested in, and whether you prefer high-level explanations or detailed case studies to better tailor the information."
}
'''

# Test parsing
try:
    parsed = json.loads(test_response.strip())
    print("✓ JSON parsing successful!")
    print(f"Number of clarifying questions: {len(parsed['clarifying_questions'])}")
    print(f"Main topic: {parsed['query_analysis']['main_topic']}")
    print("\nQuestions:")
    for i, q in enumerate(parsed['clarifying_questions'], 1):
        print(f"{i}. {q['question']}")
except json.JSONDecodeError as e:
    print(f"✗ JSON parsing failed: {e}")
    print(f"Error at line {e.lineno}, column {e.colno}")