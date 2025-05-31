import streamlit as st
from pathlib import Path
import yaml
import re
import os
import sys
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.session_state_manager import initialize_session_state

# Helper function to parse markdown frontmatter
def parse_markdown_frontmatter(file_path):
    """Parse YAML frontmatter from markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if file has frontmatter
        if content.startswith('---'):
            # Find the end of frontmatter
            match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if match:
                frontmatter_text = match.group(1)
                try:
                    return yaml.safe_load(frontmatter_text)
                except:
                    return None
    except:
        pass
    return None

# Page configuration
st.set_page_config(
    page_title="Categories - Local Knowledgebase",
    page_icon="📁",
    layout="wide"
)

# Initialize session state from saved settings
initialize_session_state()

# Initialize session state
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None
if 'editing_file' not in st.session_state:
    st.session_state.editing_file = None

# Function to parse YAML frontmatter from markdown files
def parse_markdown_frontmatter(file_path):
    """Extract YAML frontmatter from a markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has frontmatter
        if content.startswith('---'):
            # Find the closing ---
            match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL | re.MULTILINE)
            if match:
                frontmatter_text = match.group(1)
                try:
                    frontmatter = yaml.safe_load(frontmatter_text)
                    return frontmatter
                except:
                    return None
        return None
    except:
        return None

# Custom CSS
st.markdown("""
<style>
    .feature-box {
        background-color: #1a1a1a;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #333;
    }
    .feature-box h3 {
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .feature-box p {
        color: #cccccc;
    }
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
    /* Drag and drop styling */
    .category-drop-zone {
        position: relative;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .category-drop-zone:hover {
        border-color: #1e3a5f !important;
        transform: translateY(-2px);
    }
    .drop-indicator {
        font-size: 0.9rem;
        color: #666;
        margin-top: 1rem;
        opacity: 0.7;
    }
    .category-drop-zone:hover .drop-indicator {
        opacity: 1;
        color: #1e3a5f;
    }
    /* Hide the file uploader button but keep functionality */
    .stFileUploader {
        display: none;
    }
    /* Style for drag over effect */
    .category-drop-zone.drag-over {
        background-color: #1e3a5f !important;
        border-color: #2c5282 !important;
    }
    /* YouTube video styling */
    .youtube-card {
        background-color: #1a1a1a;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    .youtube-card:hover {
        border-color: #ff0000;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(255, 0, 0, 0.2);
    }
    .youtube-thumbnail {
        width: 100%;
        border-radius: 8px;
        margin-bottom: 0.5rem;
    }
    .youtube-title {
        color: #ffffff;
        font-weight: bold;
        margin-bottom: 0.25rem;
    }
    .youtube-author {
        color: #aaaaaa;
        font-size: 0.9rem;
    }
    .youtube-badge {
        background-color: #ff0000;
        color: white;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Check if we're in category view mode
if st.session_state.selected_category:
    # Category view page
    category_name = st.session_state.selected_category
    
    # Back button
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back to Categories"):
            st.session_state.selected_category = None
            st.rerun()
    
    # Category header
    category_icons = {
        "Programming": "💻",
        "AI/ML": "🤖",
        "DevOps": "🔧",
        "Web Development": "🌐",
        "Database": "🗄️",
        "Security": "🔒"
    }
    
    icon = category_icons.get(category_name, "📁")
    st.title(f"{icon} {category_name}")
    
    # Category actions
    col1, col2, col3 = st.columns([2, 2, 3])
    with col1:
        sort_by = st.selectbox("Sort by", ["Date Modified", "Name", "Date Added"])
    with col2:
        view_mode = st.radio("View", ["List", "Grid"], horizontal=True)
    
    st.divider()
    
    # File uploader for this category
    uploaded_file = st.file_uploader(
        f"Add files to {category_name}", 
        type=['md'],
        key=f"category_upload_{category_name}"
    )
    
    if uploaded_file is not None:
        # Create knowledgebase directory structure
        kb_path = Path("knowledgebase")
        category_path = kb_path / category_name.replace("/", "_").replace(" ", "_")
        category_path.mkdir(parents=True, exist_ok=True)
        
        # Save the file
        file_path = category_path / uploaded_file.name
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"✅ Added '{uploaded_file.name}' to {category_name}")
        st.rerun()
    
    st.divider()
    
    # Documents in this category
    st.subheader("Documents")
    
    # Check for documents in this category
    kb_path = Path("knowledgebase")
    category_path = kb_path / category_name.replace("/", "_").replace(" ", "_")
    
    if category_path.exists():
        md_files = list(category_path.glob("*.md"))
        if md_files:
            # Sort files based on selected criteria
            if sort_by == "Name":
                md_files.sort(key=lambda x: x.name)
            elif sort_by == "Date Modified":
                md_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            elif sort_by == "Date Added":
                md_files.sort(key=lambda x: x.stat().st_ctime, reverse=True)
            
            if view_mode == "List":
                for doc in md_files:
                    # Parse frontmatter to check if it's a YouTube video
                    frontmatter = parse_markdown_frontmatter(doc)
                    is_youtube = frontmatter and frontmatter.get('type') == 'youtube'
                    
                    if is_youtube:
                        # YouTube video display in list view
                        col1, col2, col3, col4 = st.columns([1, 3, 1, 1])
                        with col1:
                            # Thumbnail in list view
                            video_id = frontmatter.get('video_id', '')
                            thumbnail_url = frontmatter.get('thumbnail_url')
                            
                            # If no thumbnail_url in frontmatter, construct one
                            if not thumbnail_url and video_id:
                                # Try mqdefault first (more reliable), then fallback to maxresdefault
                                thumbnail_url = f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
                            
                            if thumbnail_url:
                                try:
                                    st.image(thumbnail_url, width=120)
                                except:
                                    # Fallback to lower quality thumbnail
                                    try:
                                        fallback_url = f"https://img.youtube.com/vi/{video_id}/default.jpg"
                                        st.image(fallback_url, width=120)
                                    except:
                                        st.markdown("📺")
                            else:
                                st.markdown("📺")
                        with col2:
                            st.markdown(f'<span class="youtube-badge">YouTube</span>', unsafe_allow_html=True)
                            st.write(f"**{frontmatter.get('title', doc.name)}**")
                            st.caption(f"Channel: {frontmatter.get('author', 'Unknown')}")
                        with col3:
                            if st.button("View", key=f"open_{doc.name}"):
                                st.session_state.viewing_file = doc
                                st.rerun()
                        with col4:
                            if st.button("🗑️ Delete", key=f"delete_{doc.name}", help="Delete this document"):
                                try:
                                    doc.unlink()  # Delete the file
                                    st.success(f"Deleted {doc.name}")
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"Error deleting file: {str(e)}")
                    else:
                        # Regular markdown file display
                        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                        with col1:
                            st.write(f"📄 **{doc.name}**")
                        with col2:
                            st.caption(f"{doc.stat().st_size / 1024:.1f} KB")
                        with col3:
                            if st.button("View", key=f"open_{doc.name}"):
                                st.session_state.viewing_file = doc
                                st.rerun()
                        with col4:
                            if st.button("🗑️ Delete", key=f"delete_{doc.name}", help="Delete this document"):
                                try:
                                    doc.unlink()  # Delete the file
                                    st.success(f"Deleted {doc.name}")
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"Error deleting file: {str(e)}")
            else:  # Grid view
                cols = st.columns(3)
                for idx, doc in enumerate(md_files):
                    with cols[idx % 3]:
                        # Parse frontmatter to check if it's a YouTube video
                        frontmatter = parse_markdown_frontmatter(doc)
                        is_youtube = frontmatter and frontmatter.get('type') == 'youtube'
                        
                        if is_youtube:
                            # YouTube video display in grid view
                            with st.container():
                                # YouTube badge
                                st.markdown('<span class="youtube-badge">YouTube</span>', unsafe_allow_html=True)
                                
                                # Thumbnail
                                video_id = frontmatter.get('video_id', '')
                                thumbnail_url = frontmatter.get('thumbnail_url')
                                
                                # If no thumbnail_url in frontmatter, construct one
                                if not thumbnail_url and video_id:
                                    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
                                
                                if thumbnail_url:
                                    try:
                                        st.image(thumbnail_url, use_container_width=True)
                                    except:
                                        # Fallback to lower quality thumbnail
                                        try:
                                            fallback_url = f"https://img.youtube.com/vi/{video_id}/default.jpg"
                                            st.image(fallback_url, use_container_width=True)
                                        except:
                                            st.markdown("📺 *Thumbnail not available*")
                                else:
                                    st.markdown("📺 *No video ID available*")
                                
                                # Title and author
                                st.markdown(f"**{frontmatter.get('title', doc.name)}**")
                                st.caption(f"Channel: {frontmatter.get('author', 'Unknown Channel')}")
                                
                                # Buttons
                                col_btn1, col_btn2 = st.columns(2)
                                with col_btn1:
                                    if st.button("View", key=f"grid_open_{doc.name}"):
                                        st.session_state.viewing_file = doc
                                        st.rerun()
                                with col_btn2:
                                    if st.button("🗑️ Delete", key=f"grid_delete_{doc.name}", help="Delete this document"):
                                        try:
                                            doc.unlink()
                                            st.success(f"Deleted {doc.name}")
                                            st.rerun()
                                        except Exception as e:
                                            st.error(f"Error deleting file: {str(e)}")
                        else:
                            # Regular markdown file display
                            st.markdown(f'''
                            <div class="feature-box">
                                <h4>📄 {doc.name}</h4>
                                <p>{doc.stat().st_size / 1024:.1f} KB</p>
                            </div>
                            ''', unsafe_allow_html=True)
                            col_btn1, col_btn2 = st.columns(2)
                            with col_btn1:
                                if st.button("Open", key=f"grid_open_{doc.name}"):
                                    st.session_state.viewing_file = doc
                                    st.rerun()
                            with col_btn2:
                                if st.button("🗑️ Delete", key=f"grid_delete_{doc.name}", help="Delete this document"):
                                    try:
                                        doc.unlink()
                                        st.success(f"Deleted {doc.name}")
                                        st.rerun()
                                    except Exception as e:
                                        st.error(f"Error deleting file: {str(e)}")
        else:
            st.info(f"No documents in {category_name} yet. Upload .md files above to add them.")
    else:
        st.info(f"No documents in {category_name} yet. Upload .md files above to add them.")
    
    # Edit modal/section
    if st.session_state.editing_file:
        st.divider()
        st.subheader("✏️ Edit YouTube Content")
        
        # Load the file content
        file_path = st.session_state.editing_file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse frontmatter and content
        frontmatter = parse_markdown_frontmatter(file_path)
        if not frontmatter:
            frontmatter = {}
        
        # Extract content without frontmatter
        if content.startswith('---'):
            match = re.search(r'^---\s*\n.*?\n---\s*\n(.*)$', content, re.DOTALL)
            if match:
                main_content = match.group(1)
            else:
                main_content = content
        else:
            main_content = content
        
        # Edit form
        col1, col2 = st.columns(2)
        
        with col1:
            title = st.text_input("Title", value=frontmatter.get('title', ''))
            author = st.text_input("Channel/Author", value=frontmatter.get('author', ''))
            video_id = st.text_input("Video ID", value=frontmatter.get('video_id', ''))
            thumbnail_url = st.text_input("Thumbnail URL", value=frontmatter.get('thumbnail_url', ''))
        
        with col2:
            category = st.selectbox(
                "Category",
                ["Programming", "AI/ML", "DevOps", "Web Development", "Database", "Security"],
                index=["Programming", "AI/ML", "DevOps", "Web Development", "Database", "Security"].index(frontmatter.get('category', 'Programming'))
            )
            
            # Tags handling
            tags_list = frontmatter.get('tags', [])
            if isinstance(tags_list, list):
                tags_str = ', '.join(tags_list)
            else:
                tags_str = str(tags_list)
            
            tags = st.text_input("Tags (comma-separated)", value=tags_str)
            tags_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
        
        # Edit main content
        edited_content = st.text_area("Content (Summary & Transcript)", value=main_content, height=400)
        
        # Save/Cancel buttons
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            if st.button("💾 Save Changes", type="primary"):
                try:
                    # Update frontmatter
                    updated_frontmatter = {
                        'type': 'youtube',
                        'title': title,
                        'author': author,
                        'video_id': video_id,
                        'video_url': f'https://www.youtube.com/watch?v={video_id}',
                        'thumbnail_url': thumbnail_url,
                        'category': category,
                        'tags': tags_list,
                        'date_added': frontmatter.get('date_added', ''),
                        'date_modified': datetime.now().strftime('%Y-%m-%d')
                    }
                    
                    # Reconstruct the file
                    new_content = "---\n"
                    new_content += yaml.dump(updated_frontmatter, default_flow_style=False)
                    new_content += "---\n\n"
                    new_content += edited_content
                    
                    # Save the file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    # Check if category changed
                    if category != st.session_state.selected_category:
                        # Move file to new category
                        kb_path = Path("knowledgebase")
                        new_category_path = kb_path / category.replace("/", "_").replace(" ", "_")
                        new_category_path.mkdir(parents=True, exist_ok=True)
                        
                        new_file_path = new_category_path / file_path.name
                        file_path.rename(new_file_path)
                        
                        st.success(f"Saved and moved to {category} category!")
                    else:
                        st.success("Changes saved successfully!")
                    
                    st.session_state.editing_file = None
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"Error saving changes: {str(e)}")
        
        with col2:
            if st.button("Cancel"):
                st.session_state.editing_file = None
                st.rerun()
    
    # View modal/section for YouTube content
    if st.session_state.get('viewing_file'):
        st.divider()
        
        # Load the file content
        file_path = st.session_state.viewing_file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse frontmatter and content
        frontmatter = parse_markdown_frontmatter(file_path)
        is_youtube = frontmatter and frontmatter.get('type') == 'youtube'
        
        # Extract content without frontmatter
        if content.startswith('---'):
            match = re.search(r'^---\s*\n.*?\n---\s*\n(.*)$', content, re.DOTALL)
            if match:
                main_content = match.group(1)
            else:
                main_content = content
        else:
            main_content = content
        
        if is_youtube and frontmatter:
            # YouTube content viewer
            st.subheader(f"📺 {frontmatter.get('title', 'YouTube Video')}")
            
            # Video info section
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Thumbnail
                thumbnail_url = frontmatter.get('thumbnail_url', '')
                if thumbnail_url:
                    try:
                        st.image(thumbnail_url, use_container_width=True)
                    except:
                        st.markdown("📺 *Thumbnail not available*")
                
                # Video link
                video_id = frontmatter.get('video_id', '')
                if video_id:
                    st.markdown(f"[🎬 Watch on YouTube](https://www.youtube.com/watch?v={video_id})")
            
            with col2:
                # Metadata
                st.markdown(f"**Channel:** {frontmatter.get('author', 'Unknown')}")
                st.markdown(f"**Category:** {frontmatter.get('category', 'Uncategorized')}")
                
                # Tags
                tags = frontmatter.get('tags', [])
                if tags:
                    if isinstance(tags, list):
                        tags_str = ', '.join(tags)
                    else:
                        tags_str = str(tags)
                    st.markdown(f"**Tags:** {tags_str}")
                
                st.markdown(f"**Added:** {frontmatter.get('date_added', 'Unknown')}")
                if frontmatter.get('date_modified'):
                    st.markdown(f"**Modified:** {frontmatter.get('date_modified')}")
            
            # Main content (summary and transcript)
            st.divider()
            
            # Parse the content to separate summary from transcript
            content_parts = main_content.split('## Full Transcript')
            
            if len(content_parts) > 1:
                summary_section = content_parts[0]
                transcript_section = content_parts[1]
                
                # Display summary
                if '## Summary' in summary_section:
                    summary_text = summary_section.split('## Summary')[1].strip()
                    st.markdown("### 📝 Summary")
                    st.markdown(summary_text)
                    st.divider()
                
                # Display transcript in expandable section
                with st.expander("📜 Full Transcript", expanded=False):
                    st.text(transcript_section.strip())
            else:
                # Fallback display
                st.markdown(main_content)
        else:
            # Regular markdown file viewer
            st.subheader(f"📄 {file_path.name}")
            st.markdown(main_content)
        
        # Close button
        if st.button("✖️ Close", type="primary"):
            st.session_state.viewing_file = None
            st.rerun()

else:
    # Main categories page
    st.title("📁 Categories")
    st.write("Browse your knowledge by category - drag and drop .md files to add them")
    
    # Add JavaScript for drag and drop functionality
    st.markdown("""
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        // Make category boxes clickable to trigger file upload
        const categoryBoxes = document.querySelectorAll('.category-drop-zone');
        categoryBoxes.forEach((box, index) => {
            box.addEventListener('click', function() {
                const fileInput = document.querySelectorAll('input[type="file"]')[index];
                if (fileInput) fileInput.click();
            });
            
            // Drag and drop visual feedback
            box.addEventListener('dragover', function(e) {
                e.preventDefault();
                this.classList.add('drag-over');
            });
            
            box.addEventListener('dragleave', function(e) {
                e.preventDefault();
                this.classList.remove('drag-over');
            });
            
            box.addEventListener('drop', function(e) {
                e.preventDefault();
                this.classList.remove('drag-over');
                const fileInput = document.querySelectorAll('input[type="file"]')[index];
                if (fileInput && e.dataTransfer.files.length > 0) {
                    fileInput.files = e.dataTransfer.files;
                    fileInput.dispatchEvent(new Event('change', { bubbles: true }));
                }
            });
        });
    });
    </script>
    """, unsafe_allow_html=True)
    
    # Category grid
    categories = [
        {"name": "Programming", "icon": "💻", "count": 0},
        {"name": "AI/ML", "icon": "🤖", "count": 0},
        {"name": "DevOps", "icon": "🔧", "count": 0},
        {"name": "Web Development", "icon": "🌐", "count": 0},
        {"name": "Database", "icon": "🗄️", "count": 0},
        {"name": "Security", "icon": "🔒", "count": 0},
    ]
    
    # Count documents in each category
    kb_path = Path("knowledgebase")
    for category in categories:
        category_path = kb_path / category['name'].replace("/", "_").replace(" ", "_")
        if category_path.exists():
            category['count'] = len(list(category_path.glob("*.md")))
    
    cols = st.columns(3)
    for idx, category in enumerate(categories):
        with cols[idx % 3]:
            # Create a container for the category with file uploader
            with st.container():
                st.markdown(f'''
                <div class="feature-box category-drop-zone" id="category-{idx}">
                    <h3>{category['icon']} {category['name']}</h3>
                    <p>{category['count']} articles</p>
                    <div class="drop-indicator">📥 Drop .md files here or click to upload</div>
                </div>
                ''', unsafe_allow_html=True)
                
                # File uploader for this category (hidden but functional)
                uploaded_file = st.file_uploader(
                    f"Upload to {category['name']}", 
                    type=['md'],
                    key=f"upload_{category['name']}_{idx}",
                    label_visibility="collapsed"
                )
                
                if uploaded_file is not None:
                    # Create knowledgebase directory structure
                    category_path = kb_path / category['name'].replace("/", "_").replace(" ", "_")
                    category_path.mkdir(parents=True, exist_ok=True)
                    
                    # Save the file
                    file_path = category_path / uploaded_file.name
                    with open(file_path, 'wb') as f:
                        f.write(uploaded_file.getbuffer())
                    
                    st.success(f"✅ Added '{uploaded_file.name}' to {category['name']} category")
                    st.rerun()
                
                if st.button(f"Browse {category['name']}", key=f"cat_{idx}"):
                    st.session_state.selected_category = category['name']
                    st.rerun()

# Sidebar footer
with st.sidebar:
    st.divider()
    st.caption("Local Knowledgebase v1.0")
    st.caption("© 2025 Your Organization")