import streamlit as st
from pathlib import Path
import datetime
import os

# Page configuration
st.set_page_config(
    page_title="Recent - Local Knowledgebase",
    page_icon="📝",
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
    .recent-item {
        background-color: #1a1a1a;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border: 1px solid #333;
    }
    .recent-item h4 {
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .recent-item p {
        color: #cccccc;
        margin-bottom: 0.5rem;
    }
    .recent-item .metadata {
        color: #888;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("📝 Recent Articles")
st.write("Your recently accessed and added content")

def get_recent_files(limit=20):
    """Get recently modified files from the knowledgebase"""
    recent_files = []
    kb_path = Path("knowledgebase")
    
    if not kb_path.exists():
        return recent_files
    
    # Get all markdown files
    for md_file in kb_path.rglob("*.md"):
        stat = md_file.stat()
        recent_files.append({
            'title': md_file.name,
            'path': md_file,
            'category': md_file.parent.name,
            'modified': datetime.datetime.fromtimestamp(stat.st_mtime),
            'size': stat.st_size / 1024  # Size in KB
        })
    
    # Sort by modification time (newest first)
    recent_files.sort(key=lambda x: x['modified'], reverse=True)
    
    return recent_files[:limit]

# Time filter
time_filter = st.selectbox(
    "Show files from:",
    ["All time", "Today", "This week", "This month"]
)

# Get current time
now = datetime.datetime.now()

# Filter function based on time selection
def should_include_file(file_info, filter_type):
    if filter_type == "All time":
        return True
    elif filter_type == "Today":
        return file_info['modified'].date() == now.date()
    elif filter_type == "This week":
        week_ago = now - datetime.timedelta(days=7)
        return file_info['modified'] >= week_ago
    elif filter_type == "This month":
        month_ago = now - datetime.timedelta(days=30)
        return file_info['modified'] >= month_ago
    return True

# Get and display recent files
recent_files = get_recent_files()

if recent_files:
    # Filter based on time selection
    filtered_files = [f for f in recent_files if should_include_file(f, time_filter)]
    
    if filtered_files:
        st.subheader(f"{len(filtered_files)} recent articles")
        
        for file_info in filtered_files:
            # Calculate time ago
            time_diff = now - file_info['modified']
            if time_diff.days > 0:
                time_ago = f"{time_diff.days} days ago"
            elif time_diff.seconds > 3600:
                time_ago = f"{time_diff.seconds // 3600} hours ago"
            else:
                time_ago = f"{time_diff.seconds // 60} minutes ago"
            
            st.markdown(f"""
            <div class="recent-item">
                <h4>📄 {file_info['title']}</h4>
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
                if 'favorites' not in st.session_state:
                    st.session_state.favorites = []
                
                file_str = str(file_info['path'])
                is_favorite = file_str in st.session_state.favorites
                
                if st.button(
                    "⭐ Unfavorite" if is_favorite else "☆ Favorite", 
                    key=f"fav_{file_info['path']}"
                ):
                    if is_favorite:
                        st.session_state.favorites.remove(file_str)
                    else:
                        st.session_state.favorites.append(file_str)
                    st.rerun()
    else:
        st.info(f"No articles found for the selected time period: {time_filter}")
else:
    st.info("No recent articles found. Start adding documents to your knowledgebase!")

# Quick stats
st.divider()
st.subheader("Activity Overview")

col1, col2, col3, col4 = st.columns(4)

# Calculate stats
today_count = len([f for f in recent_files if f['modified'].date() == now.date()])
week_count = len([f for f in recent_files if f['modified'] >= now - datetime.timedelta(days=7)])
month_count = len([f for f in recent_files if f['modified'] >= now - datetime.timedelta(days=30)])

with col1:
    st.metric("Today", today_count)
with col2:
    st.metric("This Week", week_count)
with col3:
    st.metric("This Month", month_count)
with col4:
    st.metric("Total", len(recent_files))

# Sidebar footer
with st.sidebar:
    st.divider()
    st.caption("Local Knowledgebase v1.0")
    st.caption("© 2025 Your Organization")