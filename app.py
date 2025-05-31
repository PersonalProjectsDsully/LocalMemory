import streamlit as st
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.session_state_manager import initialize_session_state

# Page configuration
st.set_page_config(
    page_title="Local Knowledgebase",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state from saved settings
initialize_session_state()

# Redirect to home page (pages/0_🏠_Home.py)
st.switch_page("pages/0_🏠_Home.py")