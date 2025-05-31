import streamlit as st
from pathlib import Path
import re

# Page configuration
st.set_page_config(
    page_title="Search - Local Knowledgebase",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    /* Style all buttons with dark blue theme */
    .stButton>button {
        width: 100%;
        background-color: #1e3a5f !important;
        color: white !important;
        border: none !important;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #2c5282 !important;
        color: white !important;
    }
    .search-result {
        background-color: #1a1a1a;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border: 1px solid #333;
    }
    .search-result h4 {
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .search-result p {
        color: #cccccc;
        margin-bottom: 0.5rem;
    }
    .search-result .category {
        color: #1f77b4;
        font-size: 0.9rem;
    }
    .highlight {
        background-color: #ffeb3b;
        color: #000;
        padding: 0 2px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔍 Search")

# Search interface
search_query = st.text_input("Search your knowledgebase", placeholder="Enter keywords...")

col1, col2 = st.columns([1, 4])
with col1:
    search_type = st.selectbox("Search in:", ["All", "Title", "Content", "Tags"])

def search_files(query, search_type="All"):
    """Search for files in the knowledgebase"""
    results = []
    kb_path = Path("knowledgebase")
    
    if not kb_path.exists():
        return results
    
    # Search through all markdown files
    for md_file in kb_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine if file matches search criteria
            matches = False
            title = md_file.name
            category = md_file.parent.name
            
            if search_type == "All":
                if query.lower() in title.lower() or query.lower() in content.lower():
                    matches = True
            elif search_type == "Title":
                if query.lower() in title.lower():
                    matches = True
            elif search_type == "Content":
                if query.lower() in content.lower():
                    matches = True
            elif search_type == "Tags":
                # Look for tags in content (assuming tags are marked with #)
                tags = re.findall(r'#\w+', content)
                if any(query.lower() in tag.lower() for tag in tags):
                    matches = True
            
            if matches:
                # Extract snippet around the match
                snippet = ""
                if query.lower() in content.lower():
                    index = content.lower().find(query.lower())
                    start = max(0, index - 50)
                    end = min(len(content), index + len(query) + 50)
                    snippet = "..." + content[start:end] + "..."
                    # Highlight the match
                    snippet = snippet.replace(query, f'<span class="highlight">{query}</span>')
                
                results.append({
                    'title': title,
                    'path': md_file,
                    'category': category,
                    'snippet': snippet,
                    'size': md_file.stat().st_size / 1024  # Size in KB
                })
        except Exception as e:
            continue
    
    return results

if st.button("Search", type="primary"):
    if search_query:
        with st.spinner("Searching..."):
            results = search_files(search_query, search_type)
        
        if results:
            st.subheader(f"Search Results ({len(results)} found)")
            
            for result in results:
                st.markdown(f"""
                <div class="search-result">
                    <h4>📄 {result['title']}</h4>
                    <p class="category">Category: {result['category']} | Size: {result['size']:.1f} KB</p>
                    {f'<p>{result["snippet"]}</p>' if result['snippet'] else ''}
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns([1, 5])
                with col1:
                    if st.button("Open", key=f"open_{result['path']}"):
                        with open(result['path'], 'r', encoding='utf-8') as f:
                            content = f.read()
                        st.text_area(f"Content of {result['title']}", content, height=400)
        else:
            st.info(f"No results found for '{search_query}'")
    else:
        st.warning("Please enter a search query")

# Recent searches (stored in session state)
if 'recent_searches' not in st.session_state:
    st.session_state.recent_searches = []

if search_query and st.button("Search", type="primary", key="search_btn2"):
    if search_query not in st.session_state.recent_searches:
        st.session_state.recent_searches.insert(0, search_query)
        # Keep only last 5 searches
        st.session_state.recent_searches = st.session_state.recent_searches[:5]

if st.session_state.recent_searches:
    st.divider()
    st.subheader("Recent Searches")
    for recent in st.session_state.recent_searches:
        if st.button(f"🔍 {recent}", key=f"recent_{recent}"):
            st.session_state.search_query = recent
            st.rerun()

# Sidebar footer
with st.sidebar:
    st.divider()
    st.caption("Local Knowledgebase v1.0")
    st.caption("© 2025 Your Organization")