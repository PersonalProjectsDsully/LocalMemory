#!/usr/bin/env python3
"""
Setup script for Moby Thesaurus integration

This script downloads, processes, and tests the Moby Thesaurus integration.
Run this once to set up the thesaurus for your knowledgebase system.
"""

import sys
import os
from pathlib import Path
import time

# Add the current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from utils.thesaurus_maintenance import (
        update_thesaurus, create_fallback, health_check_thesaurus,
        get_thesaurus_stats
    )
    from utils.moby_thesaurus import RobustMobyThesaurus
    IMPORTS_AVAILABLE = True
except ImportError as e:
    print(f"Some imports failed: {e}")
    print("Will create basic fallback only...")
    IMPORTS_AVAILABLE = False

def print_banner():
    """Print setup banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                   Moby Thesaurus Setup                       ║
    ║                                                              ║
    ║  Setting up synonym expansion for your knowledge base        ║
    ║  This may take a few minutes on first run...                ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def step_1_create_fallback():
    """Step 1: Create emergency fallback"""
    print("\n📋 Step 1: Creating emergency fallback thesaurus...")
    
    if not IMPORTS_AVAILABLE:
        # Create basic fallback manually
        return _create_basic_fallback()
    
    try:
        success = create_fallback()
        if success:
            print("✅ Emergency fallback created successfully!")
            return True
        else:
            print("❌ Failed to create fallback")
            return False
    except Exception as e:
        print(f"❌ Error creating fallback: {e}")
        return _create_basic_fallback()

def _create_basic_fallback():
    """Create basic fallback without dependencies"""
    import json
    
    try:
        # Create directory
        fallback_dir = Path("data/thesaurus")
        fallback_dir.mkdir(parents=True, exist_ok=True)
        
        # Basic synonyms
        basic_synonyms = {
            'search': ['find', 'look', 'seek', 'query'],
            'create': ['make', 'build', 'generate', 'produce'],
            'debug': ['troubleshoot', 'fix', 'repair', 'solve'],
            'code': ['program', 'script', 'software'],
            'error': ['bug', 'problem', 'issue', 'fault'],
            'analyze': ['examine', 'study', 'evaluate'],
            'update': ['modify', 'change', 'revise', 'edit']
        }
        
        # Create reverse index
        reverse_index = {}
        for root, syns in basic_synonyms.items():
            for syn in syns:
                if syn not in reverse_index:
                    reverse_index[syn] = []
                reverse_index[syn].append(root)
        
        fallback_data = {
            'thesaurus': basic_synonyms,
            'reverse_index': reverse_index,
            'version': 'basic-fallback-1.0'
        }
        
        fallback_path = fallback_dir / "emergency_fallback.json"
        with open(fallback_path, 'w') as f:
            json.dump(fallback_data, f, indent=2)
        
        print(f"✅ Basic fallback created at {fallback_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to create basic fallback: {e}")
        return False

def step_2_download_thesaurus():
    """Step 2: Download and process thesaurus"""
    print("\n📥 Step 2: Downloading and processing Moby Thesaurus...")
    
    if not IMPORTS_AVAILABLE:
        print("⚠️  Cannot download full thesaurus - missing dependencies")
        print("   Please install: pip install requests")
        print("   Using basic fallback for now...")
        return False
    
    print("   This may take several minutes for the first download...")
    
    try:
        start_time = time.time()
        success = update_thesaurus(force_download=False)
        end_time = time.time()
        
        if success:
            print(f"✅ Thesaurus downloaded and processed in {end_time - start_time:.1f} seconds!")
            return True
        else:
            print("❌ Failed to download thesaurus")
            return False
    except Exception as e:
        print(f"❌ Error downloading thesaurus: {e}")
        return False

def step_3_test_integration():
    """Step 3: Test the integration"""
    print("\n🧪 Step 3: Testing thesaurus integration...")
    
    if not IMPORTS_AVAILABLE:
        print("⚠️  Cannot test full integration - using basic fallback test")
        return _test_basic_fallback()
    
    try:
        # Test basic thesaurus functionality
        thesaurus = RobustMobyThesaurus(
            fallback_file="data/thesaurus/emergency_fallback.json"
        )
        thesaurus.initialize()
        
        # Test sample words
        test_words = ['search', 'code', 'debug', 'create', 'analyze']
        print("   Testing synonym lookup for sample words:")
        
        all_tests_passed = True
        for word in test_words:
            synonyms = thesaurus.get_synonyms(word, max_results=3)
            if synonyms:
                print(f"   ✅ {word}: {', '.join(synonyms[:3])}")
            else:
                print(f"   ⚠️  {word}: No synonyms found")
                all_tests_passed = False
        
        return all_tests_passed
    
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return _test_basic_fallback()

def _test_basic_fallback():
    """Test basic fallback functionality"""
    import json
    
    try:
        fallback_path = Path("data/thesaurus/emergency_fallback.json")
        if not fallback_path.exists():
            print("   ❌ Fallback file not found")
            return False
        
        with open(fallback_path, 'r') as f:
            fallback_data = json.load(f)
        
        thesaurus = fallback_data.get('thesaurus', {})
        test_words = ['search', 'code', 'debug']
        
        print("   Testing basic fallback:")
        all_passed = True
        for word in test_words:
            if word in thesaurus:
                synonyms = thesaurus[word][:3]
                print(f"   ✅ {word}: {', '.join(synonyms)}")
            else:
                print(f"   ⚠️  {word}: Not in fallback")
                all_passed = False
        
        return all_passed
    
    except Exception as e:
        print(f"   ❌ Fallback test failed: {e}")
        return False

def step_4_display_stats():
    """Step 4: Display statistics"""
    print("\n📊 Step 4: Displaying thesaurus statistics...")
    
    if not IMPORTS_AVAILABLE:
        print("⚠️  Cannot get full statistics - showing basic info")
        return _show_basic_stats()
    
    try:
        stats = get_thesaurus_stats()
        if 'error' in stats:
            print(f"❌ Could not get stats: {stats['error']}")
            return _show_basic_stats()
        
        print("   📈 Thesaurus Statistics:")
        print(f"   • Total root words: {stats.get('total_root_words', 0):,}")
        print(f"   • Total synonyms: {stats.get('total_synonyms', 0):,}")
        print(f"   • Average synonyms per word: {stats.get('average_synonyms_per_word', 0)}")
        print(f"   • Word with most synonyms: {stats.get('word_with_most_synonyms', 'N/A')} ({stats.get('max_synonyms', 0)} synonyms)")
        print(f"   • Data size: {stats.get('data_size_mb', 0)} MB")
        
        return True
    
    except Exception as e:
        print(f"❌ Error getting statistics: {e}")
        return _show_basic_stats()

def _show_basic_stats():
    """Show basic statistics from fallback"""
    import json
    
    try:
        fallback_path = Path("data/thesaurus/emergency_fallback.json")
        if fallback_path.exists():
            with open(fallback_path, 'r') as f:
                data = json.load(f)
            
            thesaurus = data.get('thesaurus', {})
            total_synonyms = sum(len(syns) for syns in thesaurus.values())
            
            print("   📈 Basic Fallback Statistics:")
            print(f"   • Root words: {len(thesaurus)}")
            print(f"   • Total synonyms: {total_synonyms}")
            print(f"   • Version: {data.get('version', 'unknown')}")
            return True
        else:
            print("   ❌ No statistics available")
            return False
    except Exception as e:
        print(f"   ❌ Error showing stats: {e}")
        return False

def step_5_health_check():
    """Step 5: Final health check"""
    print("\n🏥 Step 5: Performing comprehensive health check...")
    
    if not IMPORTS_AVAILABLE:
        print("⚠️  Cannot perform full health check - basic validation only")
        return _basic_health_check()
    
    try:
        health = health_check_thesaurus()
        
        if health.get('system_status') == 'healthy':
            print("   ✅ All systems healthy!")
            
            # Show test results
            if 'test_results' in health:
                print("   🔤 Sample synonym tests:")
                for word, result in health['test_results'].items():
                    synonyms = result.get('synonyms', [])
                    if synonyms:
                        print(f"   • {word}: {', '.join(synonyms)}")
            
            return True
        
        elif health.get('system_status') == 'unhealthy':
            print("   ⚠️  System initialized but with warnings")
            if 'recent_errors' in health and health['recent_errors']:
                print("   Recent errors:")
                for error in health['recent_errors'][-3:]:
                    print(f"   • {error}")
            return False
        
        else:
            print(f"   ❌ System status: {health.get('system_status', 'unknown')}")
            if 'error' in health:
                print(f"   Error: {health['error']}")
            return False
    
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return _basic_health_check()

def _basic_health_check():
    """Basic health check without full dependencies"""
    try:
        # Check if fallback exists
        fallback_path = Path("data/thesaurus/emergency_fallback.json")
        
        if fallback_path.exists():
            print("   ✅ Emergency fallback available")
            
            # Check if Streamlit integration is in place
            search_page = Path("pages/7_🧠_Intelligent_Search.py")
            if search_page.exists():
                content = search_page.read_text(encoding='utf-8', errors='ignore')
                if 'enhanced_search_thesaurus' in content:
                    print("   ✅ Streamlit integration installed")
                    print("   ⚠️  Install 'requests' package for full functionality")
                    return True
                else:
                    print("   ❌ Streamlit integration missing")
                    return False
            else:
                print("   ❌ Streamlit search page not found")
                return False
        else:
            print("   ❌ No fallback thesaurus available")
            return False
    
    except Exception as e:
        print(f"   ❌ Basic health check failed: {e}")
        return False

def main():
    """Main setup function"""
    print_banner()
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        sys.exit(1)
    
    # Create data directory
    data_dir = Path("data/thesaurus")
    data_dir.mkdir(parents=True, exist_ok=True)
    
    success_steps = 0
    total_steps = 5
    
    # Run setup steps
    if step_1_create_fallback():
        success_steps += 1
    
    if step_2_download_thesaurus():
        success_steps += 1
    
    if step_3_test_integration():
        success_steps += 1
    
    if step_4_display_stats():
        success_steps += 1
    
    if step_5_health_check():
        success_steps += 1
    
    # Final summary
    print("\n" + "="*60)
    print("🏁 SETUP COMPLETE")
    print("="*60)
    
    if success_steps >= 3:  # At least basic functionality working
        print("✅ Basic thesaurus integration is ready!")
        print("\n🎉 Your synonym expansion is set up!")
        print("\nNext steps:")
        print("1. Install missing packages: pip install requests")
        print("2. Run this script again for full functionality")
        print("3. Restart your Streamlit app")
        print("4. Go to the Intelligent Search page")
        print("5. Enable 'Thesaurus Expansion' in the settings")
        print("6. Try searching with synonym expansion!")
        
        if success_steps == total_steps:
            print("\n✨ Full thesaurus functionality available!")
    else:
        print(f"⚠️  {success_steps}/{total_steps} setup steps completed")
        print("\nSome features may have limited functionality.")
        print("You can run this script again to retry failed steps.")
    
    print("\n📝 About the setup file:")
    print("   • Keep setup_thesaurus.py for future updates and maintenance")
    print("   • Run it again after installing missing packages")
    print("   • Use it to re-download thesaurus data if needed")
    print("   • Safe to move to a 'scripts' folder if you prefer")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    main()