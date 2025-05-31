import streamlit as st
from pathlib import Path
import datetime

# Page configuration
st.set_page_config(
    page_title="Favorites - Local Knowledgebase",
    page_icon="⭐",
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
    .favorite-item {
        background-color: #1a1a1a;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border: 1px solid #333;
    }
    .favorite-item h4 {
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .favorite-item p {
        color: #cccccc;
        margin-bottom: 0.5rem;
    }
    .favorite-item .metadata {
        color: #888;
        font-size: 0.9rem;
    }
    .empty-state {
        text-align: center;
        padding: 3rem;
        color: #666;
    }
    .empty-state h3 {
        color: #888;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("⭐ Favorites")
st.write("Your bookmarked articles for quick access")

# Initialize favorites in session state
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# Function to get favorite file info
def get_favorite_info(file_path_str):
    """Get information about a favorite file"""
    file_path = Path(file_path_str)
    if file_path.exists():
        stat = file_path.stat()
        return {
            'title': file_path.name,
            'path': file_path,
            'category': file_path.parent.name,
            'modified': datetime.datetime.fromtimestamp(stat.st_mtime),
            'size': stat.st_size / 1024,  # Size in KB
            'exists': True
        }
    else:
        # File has been deleted
        return {
            'title': file_path.name,
            'path': file_path,
            'category': 'Unknown',
            'modified': None,
            'size': 0,
            'exists': False
        }

# Sort options
sort_by = st.selectbox("Sort by:", ["Recently Added", "Name", "Category"])

# Get favorite files info
favorite_files = []
for fav_path in st.session_state.favorites:
    file_info = get_favorite_info(fav_path)
    favorite_files.append(file_info)

# Sort favorites based on selection
if sort_by == "Name":
    favorite_files.sort(key=lambda x: x['title'].lower())
elif sort_by == "Category":
    favorite_files.sort(key=lambda x: x['category'])
# Default is "Recently Added" which maintains the order in session state

# Display favorites
if favorite_files:
    st.subheader(f"{len(favorite_files)} favorite articles")
    
    # Clean up non-existent files
    non_existent = [f for f in favorite_files if not f['exists']]
    if non_existent:
        st.warning(f"{len(non_existent)} favorite(s) no longer exist and will be removed.")
        # Remove non-existent files from favorites
        st.session_state.favorites = [str(f['path']) for f in favorite_files if f['exists']]
        favorite_files = [f for f in favorite_files if f['exists']]
    
    for file_info in favorite_files:
        if file_info['exists']:
            # Calculate time since modified
            now = datetime.datetime.now()
            time_diff = now - file_info['modified']
            if time_diff.days > 0:
                time_ago = f"{time_diff.days} days ago"
            elif time_diff.seconds > 3600:
                time_ago = f"{time_diff.seconds // 3600} hours ago"
            else:
                time_ago = f"{time_diff.seconds // 60} minutes ago"
            
            st.markdown(f"""
            <div class="favorite-item">
                <h4>⭐ {file_info['title']}</h4>
                <p class="metadata">
                    Category: {file_info['category']} | 
                    Modified: {time_ago} | 
                    Size: {file_info['size']:.1f} KB
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 1, 4])
            with col1:
                if st.button("Open", key=f"open_{file_info['path']}"):
                    with open(file_info['path'], 'r', encoding='utf-8') as f:
                        content = f.read()
                    st.text_area(f"Content of {file_info['title']}", content, height=400)
            
            with col2:
                if st.button("Remove", key=f"remove_{file_info['path']}"):
                    st.session_state.favorites.remove(str(file_info['path']))
                    st.rerun()
else:
    # Empty state
    st.markdown("""
    <div class="empty-state">
        <h3>No favorites yet</h3>
        <p>Start marking articles as favorites to see them here!</p>
        <p>You can favorite articles from:</p>
        <ul style="text-align: left; display: inline-block;">
            <li>📁 Categories - when browsing articles</li>
            <li>🔍 Search - from search results</li>
            <li>📝 Recent - from recently accessed files</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Quick actions
st.divider()
st.subheader("Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📁 Browse Categories", use_container_width=True):
        st.switch_page("pages/1_📁_Categories.py")

with col2:
    if st.button("🔍 Search Articles", use_container_width=True):
        st.switch_page("pages/2_🔍_Search.py")

with col3:
    if st.button("📝 View Recent", use_container_width=True):
        st.switch_page("pages/3_📝_Recent.py")

# Sidebar footer
with st.sidebar:
    st.divider()
    st.caption("Local Knowledgebase v1.0")
    st.caption("© 2025 Your Organization")