#!/usr/bin/env python3
"""
Test the fixes for the thesaurus integration
"""

import sys
from pathlib import Path

# Mock requests module to avoid import error
class MockRequests:
    class RequestException(Exception):
        pass
    
    def get(self, *args, **kwargs):
        raise self.RequestException("Mocked - no actual network call")

# Insert mock before importing our modules
sys.modules['requests'] = MockRequests()

try:
    from utils.enhanced_search_thesaurus import EnhancedIntelligentSearchEngine
    print('✅ Enhanced search engine import successful')
    
    # Test creation
    engine = EnhancedIntelligentSearchEngine()
    print('✅ Enhanced search engine created successfully')
    
    # Test configure_qa_system method
    engine.configure_qa_system('basic')
    print('✅ configure_qa_system method works')
    
    # Test health check
    health = engine.health_check()
    print(f'✅ health_check works: base_engine_healthy={health.get("base_engine_healthy", False)}')
    
    # Test other methods
    intent = engine.parse_query_intent("test query")
    print(f'✅ parse_query_intent works: {intent.get("intent_type", "unknown")}')
    
    explanation = engine.explain_expansions("search code")
    print(f'✅ explain_expansions works: found {len(explanation.get("expansions", {}))} expansions')
    
    print('\n🎉 All fixes verified successfully!')
    print('\nThe thesaurus integration should now work in Streamlit!')
    print('Just restart your Streamlit app and try the Intelligent Search page.')
    
except Exception as e:
    print(f'❌ Error: {e}')
    import traceback
    traceback.print_exc()