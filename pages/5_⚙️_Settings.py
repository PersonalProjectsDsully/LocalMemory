import streamlit as st
from pathlib import Path
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.llm_utils import test_llm_connection, get_available_ollama_models, get_available_openai_models, get_available_lmstudio_models, OPENAI_AVAILABLE
from utils.settings_manager import settings_manager
from utils.session_state_manager import initialize_session_state, sync_session_state_to_settings, auto_save_settings

# Page configuration
st.set_page_config(
    page_title="Settings - Local Knowledgebase",
    page_icon="⚙️",
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
    .settings-section {
        background-color: #1a1a1a;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #333;
    }
    .settings-section h3 {
        color: #ffffff;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚙️ Settings")

# Initialize session state from saved settings
initialize_session_state()

# Show success message if settings were just saved
if 'settings_saved' in st.session_state and st.session_state.settings_saved:
    st.success("✅ Settings saved successfully!")
    st.session_state.settings_saved = False

# Auto-save toggle
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.subheader("💾 Auto-Save Settings")
with col2:
    auto_save_enabled = st.checkbox(
        "Enable Auto-Save",
        value=st.session_state.get('auto_save_enabled', True),
        key="auto_save_toggle",
        help="Automatically save settings when they change"
    )
    st.session_state.auto_save_enabled = auto_save_enabled
with col3:
    if st.session_state.get('auto_save_enabled', True):
        st.info("🔄 Auto-save enabled")
    else:
        st.warning("⚠️ Auto-save disabled")

# Settings sections
st.markdown('<div class="settings-section">', unsafe_allow_html=True)
st.subheader("Display Settings")

col1, col2 = st.columns(2)

with col1:
    def on_theme_change():
        st.session_state.theme = st.session_state.settings_theme
        auto_save_settings()
    
    theme = st.selectbox(
        "Theme",
        ["Light", "Dark", "Auto"],
        index=["Light", "Dark", "Auto"].index(st.session_state.get('theme', 'Dark')),
        key="settings_theme",
        on_change=on_theme_change
    )

with col2:
    def on_items_per_page_change():
        st.session_state.items_per_page = st.session_state.settings_items_per_page
        auto_save_settings()
    
    items_per_page = st.slider(
        "Items per page",
        min_value=10,
        max_value=50,
        value=st.session_state.get('items_per_page', 20),
        step=5,
        key="settings_items_per_page",
        on_change=on_items_per_page_change
    )

def on_show_previews_change():
    st.session_state.show_previews = st.session_state.settings_show_previews
    auto_save_settings()

show_previews = st.checkbox(
    "Show article previews in lists",
    value=st.session_state.get('show_previews', True),
    key="settings_show_previews",
    on_change=on_show_previews_change
)

st.markdown('</div>', unsafe_allow_html=True)

# Content Management Settings
st.markdown('<div class="settings-section">', unsafe_allow_html=True)
st.subheader("Content Management")

col1, col2 = st.columns(2)

with col1:
    auto_save = st.checkbox(
        "Auto-save uploads",
        value=st.session_state.get('auto_save', True),
        help="Automatically save uploaded files without confirmation",
        key="settings_auto_save"
    )
    st.session_state.auto_save = auto_save

with col2:
    categories = ["Programming", "AI/ML", "DevOps", "Web Development", "Database", "Security"]
    default_category = st.selectbox(
        "Default category for uploads",
        categories,
        index=categories.index(st.session_state.get('default_category', 'Programming')),
        key="settings_default_category"
    )
    st.session_state.default_category = default_category

st.markdown('</div>', unsafe_allow_html=True)

# YouTube Settings
st.markdown('<div class="settings-section">', unsafe_allow_html=True)
st.subheader("YouTube Transcript Settings")

col1, col2 = st.columns(2)

with col1:
    youtube_language = st.selectbox(
        "Preferred transcript language",
        ["en", "es", "fr", "de", "it", "pt", "ru", "ja", "ko", "zh"],
        index=["en", "es", "fr", "de", "it", "pt", "ru", "ja", "ko", "zh"].index(
            st.session_state.get('youtube_language', 'en')
        ),
        help="Preferred language for YouTube transcripts",
        key="settings_youtube_language"
    )
    st.session_state.youtube_language = youtube_language

with col2:
    export_format = st.selectbox(
        "Default export format",
        ["Markdown", "Plain Text", "JSON"],
        index=["Markdown", "Plain Text", "JSON"].index(st.session_state.get('export_format', 'Markdown')),
        key="settings_export_format"
    )
    st.session_state.export_format = export_format

st.markdown('</div>', unsafe_allow_html=True)

# LLM Settings
st.markdown('<div class="settings-section">', unsafe_allow_html=True)
st.subheader("AI/LLM Configuration")

col1, col2 = st.columns(2)

with col1:
    def on_provider_change():
        provider_map = {
            "Ollama (Local)": "ollama",
            "OpenAI": "openai",
            "LM Studio (Local)": "lmstudio"
        }
        st.session_state.llm_provider = provider_map.get(st.session_state.settings_llm_provider, "ollama")
        auto_save_settings()
    
    # Map current provider to display name
    current_provider = st.session_state.get('llm_provider', 'ollama')
    provider_display_map = {
        "ollama": "Ollama (Local)",
        "openai": "OpenAI",
        "lmstudio": "LM Studio (Local)"
    }
    current_display = provider_display_map.get(current_provider, "Ollama (Local)")
    
    provider = st.selectbox(
        "LLM Provider",
        ["Ollama (Local)", "OpenAI", "LM Studio (Local)"],
        index=["Ollama (Local)", "OpenAI", "LM Studio (Local)"].index(current_display),
        help="Choose between local Ollama, cloud-based OpenAI, or local LM Studio",
        key="settings_llm_provider",
        on_change=on_provider_change
    )
    
    if provider == "OpenAI":
        def on_api_key_change():
            st.session_state.openai_api_key = st.session_state.settings_openai_api_key
            auto_save_settings()
        
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            value=st.session_state.get('openai_api_key', ''),
            help="Your OpenAI API key",
            key="settings_openai_api_key",
            on_change=on_api_key_change
        )
    elif provider == "LM Studio (Local)":
        def on_lmstudio_url_change():
            st.session_state.lmstudio_api_url = st.session_state.settings_lmstudio_api_url
            auto_save_settings()
        
        api_url = st.text_input(
            "LM Studio API URL",
            value=st.session_state.get('lmstudio_api_url', 'http://localhost:1234'),
            help="URL for your local LM Studio instance (default: http://localhost:1234)",
            key="settings_lmstudio_api_url",
            on_change=on_lmstudio_url_change
        )
    else:  # Ollama
        def on_ollama_url_change():
            st.session_state.ollama_api_url = st.session_state.settings_ollama_api_url
            auto_save_settings()
        
        api_url = st.text_input(
            "Ollama API URL",
            value=st.session_state.get('ollama_api_url', 'http://localhost:11434/api/generate'),
            help="URL for your local Ollama instance",
            key="settings_ollama_api_url",
            on_change=on_ollama_url_change
        )

with col2:
    if provider == "OpenAI":
        # Debug information
        api_key_present = bool(st.session_state.get('openai_api_key'))
        
        if not OPENAI_AVAILABLE:
            st.error("❌ OpenAI library not available. Please install: `pip install openai`")
        elif not api_key_present:
            st.info("💡 Enter your OpenAI API key to see available models")
        else:
            # Show models
            try:
                model_options = get_available_openai_models(st.session_state.get('openai_api_key'))
                def on_openai_model_change():
                    st.session_state.openai_model = st.session_state.settings_openai_model
                    auto_save_settings()
                
                selected_model = st.selectbox(
                    "OpenAI Model",
                    model_options,
                    index=model_options.index(st.session_state.get('openai_model', 'gpt-3.5-turbo')) if st.session_state.get('openai_model', 'gpt-3.5-turbo') in model_options else 0,
                    key="settings_openai_model",
                    on_change=on_openai_model_change
                )
                
                # Test connection button
                if st.button("🔌 Test Connection", type="secondary"):
                    with st.spinner("Testing OpenAI connection..."):
                        success, message = test_llm_connection()
                        if success:
                            st.success(message)
                        else:
                            st.error(message)
                            
            except Exception as e:
                st.error(f"Error loading OpenAI models: {e}")
        
        # Debug info (can be removed later)
        with st.expander("🔧 Debug Info", expanded=False):
            st.write(f"OpenAI Available: {OPENAI_AVAILABLE}")
            st.write(f"API Key Present: {api_key_present}")
            if api_key_present:
                api_key = st.session_state.get('openai_api_key', '')
                st.write(f"API Key Length: {len(api_key)}")
                st.write(f"API Key Preview: {api_key[:8]}..." if len(api_key) > 8 else "Too short")
    elif provider == "LM Studio (Local)":
        models = get_available_lmstudio_models(st.session_state.get('lmstudio_api_url', 'http://localhost:1234'))
        if models:
            current_model = st.session_state.get('lmstudio_model', 'granite-3.0-2b-instruct')
            def on_lmstudio_model_change():
                # Debug logging
                print(f"LM Studio model changed to: {st.session_state.settings_lmstudio_model}")
                st.session_state.lmstudio_model = st.session_state.settings_lmstudio_model
                # Force immediate save
                result = auto_save_settings()
                print(f"Auto-save result: {result}")
                # Verify the change
                print(f"Session state lmstudio_model after change: {st.session_state.get('lmstudio_model')}")
            
            selected_model = st.selectbox(
                "LM Studio Model",
                models,
                index=models.index(current_model) if current_model in models else 0,
                key="settings_lmstudio_model",
                on_change=on_lmstudio_model_change
            )
            
            # Force update if the selectbox value differs from session state
            if st.session_state.get('settings_lmstudio_model') != st.session_state.get('lmstudio_model'):
                st.session_state.lmstudio_model = st.session_state.settings_lmstudio_model
                print(f"Force updating lmstudio_model to: {st.session_state.settings_lmstudio_model}")
                auto_save_settings()
        else:
            st.warning("No LM Studio models found. Is LM Studio server running? (lms server start)")
        
        # Debug display
        if provider == "LM Studio (Local)":
            with st.expander("Debug Info"):
                st.write(f"Current lmstudio_model: {st.session_state.get('lmstudio_model', 'NOT SET')}")
                st.write(f"Settings widget value: {st.session_state.get('settings_lmstudio_model', 'NOT SET')}")
    else:  # Ollama
        models, model_info = get_available_ollama_models(st.session_state.get('ollama_api_url', 'http://localhost:11434/api/generate'))
        if models:
            current_model = st.session_state.get('ollama_model', 'llama3.1:8b')
            def on_ollama_model_change():
                st.session_state.ollama_model = st.session_state.settings_ollama_model
                auto_save_settings()
            
            selected_model = st.selectbox(
                "Ollama Model",
                models,
                format_func=lambda x: f"{x} {model_info.get(x, '')}",
                index=models.index(current_model) if current_model in models else 0,
                key="settings_ollama_model",
                on_change=on_ollama_model_change
            )
        else:
            st.warning("No Ollama models found. Is Ollama running?")

# Test LLM connection button
col1, col2 = st.columns(2)
with col1:
    if st.button("Test LLM Connection", use_container_width=True):
        with st.spinner("Testing connection..."):
            success, message = test_llm_connection()
            if success:
                st.success(message)
            else:
                st.error(message)

with col2:
    if st.button("💾 Save LLM Settings", type="primary", use_container_width=True):
        # Debug current state
        print(f"Before save - LM Studio model in session state: {st.session_state.get('lmstudio_model')}")
        print(f"Settings key value: {st.session_state.get('settings_lmstudio_model')}")
        
        # Force save current settings
        current_settings = sync_session_state_to_settings()
        print(f"Settings to save: lmstudio_model = {current_settings.get('lmstudio_model')}")
        
        if settings_manager.save_settings(current_settings):
            st.success("LLM settings saved successfully!")
            # Display current model for confirmation
            if st.session_state.get('llm_provider') == 'lmstudio':
                st.info(f"LM Studio model: {st.session_state.get('lmstudio_model', 'Not set')}")
                # Re-read settings to verify
                saved_settings = settings_manager.load_settings()
                print(f"Verified saved settings: lmstudio_model = {saved_settings.get('lmstudio_model')}")
        else:
            st.error("Failed to save settings")

st.markdown('</div>', unsafe_allow_html=True)

# Privacy & Analytics
st.markdown('<div class="settings-section">', unsafe_allow_html=True)
st.subheader("Privacy & Analytics")

enable_analytics = st.checkbox(
    "Enable usage analytics (Coming Soon)",
    value=st.session_state.get('enable_analytics', True),
    help="Future feature: Track usage patterns to improve the application. Currently non-functional.",
    key="settings_enable_analytics"
)
st.session_state.enable_analytics = enable_analytics

st.info("📝 **Note**: Analytics feature is planned but not yet implemented. When available, analytics data will be stored locally and never shared with third parties.")
st.info("🔮 **Future Analytics Features**: Usage patterns, performance metrics, popular content categories, and feature utilization tracking.")

st.markdown('</div>', unsafe_allow_html=True)

# Data Management
st.markdown('<div class="settings-section">', unsafe_allow_html=True)
st.subheader("Data Management")

col1, col2, col3 = st.columns(3)

with col1:
    # Export settings
    current_settings = sync_session_state_to_settings()
    settings_json = json.dumps(current_settings, indent=2)
    st.download_button(
        label="Export Settings",
        data=settings_json,
        file_name="knowledgebase_settings.json",
        mime="application/json",
        use_container_width=True
    )

with col2:
    if st.button("Backup Settings", use_container_width=True):
        # Sync and save current settings
        current_settings = sync_session_state_to_settings()
        settings_manager.save_settings(current_settings)
        st.success("Settings backed up successfully!")

with col3:
    if st.button("Clear All Favorites", use_container_width=True):
        if st.checkbox("Confirm clear all favorites"):
            st.session_state.favorites = []
            st.success("All favorites cleared!")
            st.rerun()

# Import settings
st.subheader("Import Settings")
uploaded_file = st.file_uploader("Choose a settings JSON file", type="json")
if uploaded_file is not None:
    try:
        # Read the uploaded file
        imported_settings = json.load(uploaded_file)
        
        # Validate it has expected structure
        if isinstance(imported_settings, dict):
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("Apply Imported Settings"):
                    # Save the imported settings
                    settings_manager.save_settings(imported_settings)
                    # Clear session state to force reload
                    for key in list(st.session_state.keys()):
                        del st.session_state[key]
                    st.success("Settings imported successfully! The page will reload.")
                    st.rerun()
            
            with col2:
                with st.expander("Preview imported settings"):
                    st.json(imported_settings)
        else:
            st.error("Invalid settings file format")
    except Exception as e:
        st.error(f"Error reading settings file: {e}")

st.markdown('</div>', unsafe_allow_html=True)

# Storage Information
st.markdown('<div class="settings-section">', unsafe_allow_html=True)
st.subheader("Storage Information")

kb_path = Path("knowledgebase")
if kb_path.exists():
    total_files = len(list(kb_path.rglob("*.md")))
    total_size = sum(f.stat().st_size for f in kb_path.rglob("*.md")) / (1024 * 1024)  # Size in MB
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Documents", total_files)
    
    with col2:
        st.metric("Storage Used", f"{total_size:.2f} MB")
    
    with col3:
        st.metric("Average File Size", f"{(total_size / total_files * 1024):.1f} KB" if total_files > 0 else "0 KB")
else:
    st.info("No knowledgebase data found yet.")

st.markdown('</div>', unsafe_allow_html=True)

# Save Settings Button
st.divider()

if st.button("Save All Settings", type="primary", use_container_width=True):
    # Sync current session state to settings
    current_settings = sync_session_state_to_settings()
    
    # Save settings using the settings manager
    if settings_manager.save_settings(current_settings):
        st.session_state.settings_saved = True
        st.rerun()
    else:
        st.error("Failed to save settings")

# Reset to defaults button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Reset to Defaults", use_container_width=True):
        if st.checkbox("Confirm reset all settings to defaults"):
            settings_manager.reset_to_defaults()
            # Clear session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# Settings File Location
st.divider()
st.subheader("Settings Storage")
st.info(f"""**Settings are stored locally at:** `knowledgebase/settings.json`

Your settings are automatically saved and will persist across application restarts.
API keys are stored locally and never transmitted anywhere.
""")

# About Section
st.divider()
st.subheader("About")
st.info("""
**Local Knowledgebase v1.0**

A powerful document management system for organizing and accessing your markdown files.

Features:
- 📁 Category-based organization
- 🔍 Full-text search
- ⭐ Favorites system
- 📺 YouTube transcript extraction
- 🤖 AI-powered summarization
- 💬 Chat with your knowledge base
- 📊 Usage analytics

© 2025 Your Organization
""")

# Sidebar footer
with st.sidebar:
    st.divider()
    st.caption("Local Knowledgebase v1.0")
    st.caption("© 2025 Your Organization")