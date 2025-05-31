import streamlit as st
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.comprehensive_duplicate_detector import DuplicateDetector, show_duplicate_report

# Page configuration
st.set_page_config(
    page_title="Duplicate Detector - Local Knowledgebase",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Knowledge Base Duplicate Detector")
st.markdown("Scan your knowledge base for duplicate files based on content, titles, and metadata")

# Add some helpful information
st.info("""
This tool will detect:
- 📄 **Exact content duplicates** - Files with identical content
- 📝 **Similar titles** - Files with very similar names (e.g., "file_1.md" and "file_2.md")
- 📺 **YouTube duplicates** - Multiple files for the same video ID
- 🔤 **Exact title matches** - Files with the same title in metadata
""")

# Create detector instance
detector = DuplicateDetector()

# Show the duplicate report
show_duplicate_report(detector)

# Additional options
st.divider()
st.subheader("ℹ️ About Duplicate Detection")

with st.expander("How it works"):
    st.write("""
    **Detection Methods:**
    
    1. **Content Hash Comparison**: Each file's content is hashed using MD5. Files with identical hashes have exactly the same content.
    
    2. **Title Similarity**: Titles are cleaned (removing numbers, special characters) and compared using sequence matching. 
       - Exact matches after cleaning are flagged
       - Titles with >85% similarity are grouped as potential duplicates
    
    3. **YouTube Video ID**: For YouTube transcripts, files with the same video_id are considered duplicates.
    
    4. **Smart Grouping**: Files are grouped by their duplicate type, making it easy to review and clean up.
    
    **Safe Cleanup**: When removing duplicates, the oldest file (by path) is kept to preserve any manual edits or historical data.
    """)

with st.expander("Best Practices"):
    st.write("""
    **Before Cleaning Up:**
    
    - 📋 Export the duplicate report for reference
    - 🔍 Review similar titles - they might be intentionally different versions
    - 💾 Consider backing up your knowledge base before bulk deletions
    - 📝 Check if duplicates have different metadata that should be merged
    
    **Common Duplicate Patterns:**
    
    - Files ending in `_1`, `_2`, etc. are often unintentional duplicates
    - YouTube videos saved multiple times
    - Files copied between categories
    - Auto-generated variations from different sources
    """)

st.caption("💡 Tip: Run this periodically to keep your knowledge base clean and organized!")