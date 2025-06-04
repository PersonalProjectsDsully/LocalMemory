#!/usr/bin/env python3
"""
Verify that the key fixes are in place
"""

from pathlib import Path

def check_cached_thesaurus_fix():
    """Check if CachedMobyThesaurus has initialize method"""
    try:
        with open('utils/moby_thesaurus.py', 'r') as f:
            content = f.read()
        
        checks = [
            'def initialize(self, **kwargs):' in content,
            'def get_synonyms(self, word: str, max_results: int = 10)' in content,
            'def health_check(self):' in content,
            'self.initialized = False' in content
        ]
        
        if all(checks):
            print('✅ CachedMobyThesaurus fixes applied successfully')
            return True
        else:
            print('⚠️  Some CachedMobyThesaurus fixes missing')
            return False
    except Exception as e:
        print(f'❌ Error checking CachedMobyThesaurus: {e}')
        return False

def check_enhanced_search_fix():
    """Check if EnhancedIntelligentSearchEngine has required methods"""
    try:
        with open('utils/enhanced_search_thesaurus.py', 'r') as f:
            content = f.read()
        
        checks = [
            'def configure_qa_system(self, qa_config: str):' in content,
            'def search_content(self, query: str):' in content,
            'def parse_query_intent(self, query: str):' in content,
            'def synthesize_answer_with_qa(self, query, results, **kwargs):' in content,
            'def explain_expansions(self, query: str)' in content
        ]
        
        if all(checks):
            print('✅ EnhancedIntelligentSearchEngine fixes applied successfully')
            return True
        else:
            print('⚠️  Some EnhancedIntelligentSearchEngine fixes missing')
            return False
    except Exception as e:
        print(f'❌ Error checking EnhancedIntelligentSearchEngine: {e}')
        return False

def check_streamlit_integration():
    """Check if Streamlit integration is properly set up"""
    try:
        search_page = Path('pages/7_🧠_Intelligent_Search.py')
        if not search_page.exists():
            print('❌ Intelligent Search page not found')
            return False
        
        with open(search_page, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        checks = [
            'enhanced_search_thesaurus' in content,
            'use_thesaurus' in content,
            'expansion_weight' in content,
            'thesaurus_expansions' in content,
            'search_with_expansion' in content
        ]
        
        if all(checks):
            print('✅ Streamlit integration properly configured')
            return True
        else:
            print('⚠️  Some Streamlit integration elements missing')
            return False
    except Exception as e:
        print(f'❌ Error checking Streamlit integration: {e}')
        return False

def check_fallback_exists():
    """Check if emergency fallback exists"""
    fallback_path = Path('data/thesaurus/emergency_fallback.json')
    if fallback_path.exists():
        print('✅ Emergency fallback thesaurus exists')
        return True
    else:
        print('⚠️  Emergency fallback missing - run setup_thesaurus.py')
        return False

def main():
    print('🔧 Verifying Thesaurus Integration Fixes')
    print('='*50)
    
    fixes = [
        check_cached_thesaurus_fix(),
        check_enhanced_search_fix(), 
        check_streamlit_integration(),
        check_fallback_exists()
    ]
    
    passed = sum(fixes)
    total = len(fixes)
    
    print('\n' + '='*50)
    print(f'🏁 Verification Results: {passed}/{total} checks passed')
    
    if passed == total:
        print('🎉 All fixes verified! The thesaurus integration should work now.')
        print('\nTo use:')
        print('1. Restart your Streamlit app')
        print('2. Go to the Intelligent Search page')
        print('3. Enable "Thesaurus Expansion" in the settings')
        print('4. Try searching with synonyms!')
    else:
        print('⚠️  Some issues remain. Please check the output above.')
    
    print('='*50)

if __name__ == "__main__":
    main()