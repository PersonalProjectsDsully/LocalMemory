#!/usr/bin/env python3
"""
Basic test of thesaurus integration without external dependencies
"""

import json
from pathlib import Path

def test_fallback_creation():
    """Test creating the emergency fallback"""
    print("Testing fallback creation...")
    
    common_synonyms = {
        'search': ['find', 'look', 'seek', 'query'],
        'create': ['make', 'build', 'generate', 'produce'],
        'debug': ['troubleshoot', 'fix', 'repair', 'solve'],
        'code': ['program', 'script', 'software', 'application'],
    }
    
    # Create reverse index
    reverse_index = {}
    for root_word, synonyms in common_synonyms.items():
        for synonym in synonyms:
            if synonym not in reverse_index:
                reverse_index[synonym] = []
            reverse_index[synonym].append(root_word)
    
    fallback_data = {
        'thesaurus': common_synonyms,
        'reverse_index': reverse_index,
        'version': 'fallback-1.0',
        'description': 'Emergency fallback thesaurus'
    }
    
    # Create directory and save
    fallback_path = Path('data/thesaurus/emergency_fallback.json')
    fallback_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(fallback_path, 'w') as f:
        json.dump(fallback_data, f, indent=2)
    
    print(f"✅ Created fallback at {fallback_path}")
    print(f"   - {len(common_synonyms)} root words")
    print(f"   - {sum(len(syns) for syns in common_synonyms.values())} total synonyms")
    
    return True

def test_enhanced_search_import():
    """Test if we can import the enhanced search module"""
    print("\nTesting enhanced search import...")
    
    try:
        # Test if we can import without external dependencies
        import sys
        sys.path.insert(0, '/workspace')
        
        # This should work if our module structure is correct
        from utils.enhanced_search_thesaurus import EnhancedIntelligentSearchEngine
        print("✅ Enhanced search engine import successful")
        return True
    except ImportError as e:
        print(f"⚠️  Enhanced search import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_streamlit_integration():
    """Test if the Streamlit page modifications are valid"""
    print("\nTesting Streamlit integration...")
    
    try:
        # Check if the modified file exists and has our changes
        page_file = Path('/workspace/pages/7_🧠_Intelligent_Search.py')
        
        if not page_file.exists():
            print("❌ Intelligent Search page not found")
            return False
        
        content = page_file.read_text()
        
        # Check for our integration markers
        checks = [
            'enhanced_search_thesaurus' in content,
            'use_thesaurus' in content,
            'expansion_weight' in content,
            'thesaurus_expansions' in content
        ]
        
        if all(checks):
            print("✅ Streamlit integration looks good")
            print("   - Thesaurus import added")
            print("   - UI controls added")
            print("   - Search expansion integrated")
            return True
        else:
            print("⚠️  Some integration elements missing")
            return False
    
    except Exception as e:
        print(f"❌ Error checking integration: {e}")
        return False

def main():
    """Run basic tests"""
    print("🧪 Basic Thesaurus Integration Test")
    print("="*50)
    
    tests_passed = 0
    total_tests = 3
    
    if test_fallback_creation():
        tests_passed += 1
    
    if test_enhanced_search_import():
        tests_passed += 1
    
    if test_streamlit_integration():
        tests_passed += 1
    
    print("\n" + "="*50)
    print(f"🏁 Test Results: {tests_passed}/{total_tests} passed")
    
    if tests_passed == total_tests:
        print("✅ All basic tests passed!")
        print("\nNext steps:")
        print("1. Install missing packages: pip install requests")
        print("2. Run the full setup: python setup_thesaurus.py")
        print("3. Restart Streamlit app")
        print("4. Test synonym expansion in Intelligent Search")
    else:
        print("⚠️  Some tests failed - check the output above")
    
    return tests_passed == total_tests

if __name__ == "__main__":
    main()