import streamlit as st
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.session_state_manager import initialize_session_state

# Page configuration
st.set_page_config(
    page_title="Home - Local Knowledgebase",
    page_icon="🏠",
    layout="wide"
)

# Initialize session state from saved settings
initialize_session_state()

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        padding: 2rem 0;
    }
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
</style>
""", unsafe_allow_html=True)

# Home page content
st.markdown('<h1 class="main-header">Welcome to Your Knowledgebase</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.subheader("📚 Organized Content")
    st.write("Access your knowledge organized by categories for easy navigation.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.subheader("🔍 Quick Search")
    st.write("Find what you need instantly with powerful search capabilities.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.subheader("📺 YouTube Integration")
    st.write("Extract and save transcripts from YouTube videos with metadata.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.subheader("🤖 AI Summarization")
    st.write("Generate intelligent summaries from YouTube videos using AI.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.subheader("💬 AI Chat Assistant")
    st.write("Chat with an AI that can access your entire knowledge base.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.subheader("📊 Analytics")
    st.write("Track your knowledge growth and usage patterns over time.")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# Quick stats
st.subheader("Quick Stats")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Articles", "0")
with col2:
    st.metric("Categories", "6")
with col3:
    st.metric("This Week", "0")
with col4:
    st.metric("Favorites", "0")

st.divider()

# Getting started section
st.subheader("Getting Started")
st.write("1. Navigate to **Categories** to browse and organize your documents")
st.write("2. **Drag and drop** markdown files into any category to add them")
st.write("3. Use **Search** to quickly find specific documents")
st.write("4. Mark important documents as **Favorites** for quick access")
st.write("5. Extract and summarize **YouTube** video transcripts with AI")
st.write("6. **Chat** with an AI assistant that can reference your knowledge base")
st.write("7. Configure AI/LLM settings in **Settings** page")

# Sidebar footer
with st.sidebar:
    st.divider()
    st.caption("Local Knowledgebase v1.0")
    st.caption("© 2025 Your Organization")