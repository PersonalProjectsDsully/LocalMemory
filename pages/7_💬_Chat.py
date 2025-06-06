import streamlit as st
from pathlib import Path
import yaml
import os
from typing import List, Dict, Optional
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.llm_utils import _call_llm_api, test_llm_connection, get_available_ollama_models, get_available_openai_models, OPENAI_AVAILABLE
from utils.session_state_manager import initialize_session_state, auto_save_settings

# Page configuration
st.set_page_config(
    page_title="Chat - Local Knowledgebase",
    page_icon="💬",
    layout="wide"
)

# Initialize session state from saved settings
initialize_session_state()

# Custom CSS
st.markdown("""
<style>
    .stButton>button {
        background-color: #1e3a5f !important;
        color: white !important;
        border: none !important;
    }
    .stButton>button:hover {
        background-color: #2c5282 !important;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #1e3a5f;
        margin-left: 20%;
    }
    .assistant-message {
        background-color: #2d2d2d;
        margin-right: 20%;
    }
    .kb-context {
        background-color: #1a1a1a;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# Initialize chat-specific session state
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []

def load_knowledge_base_documents(categories: List[str] = None) -> List[Dict]:
    """Load documents from the knowledge base, optionally filtered by categories."""
    kb_path = Path("knowledgebase")
    documents = []
    
    if not kb_path.exists():
        return documents
    
    # If no categories specified, load all
    if not categories:
        categories = [d.name for d in kb_path.iterdir() if d.is_dir()]
    
    for category in categories:
        category_path = kb_path / category
        if category_path.exists():
            for file_path in category_path.glob("*.md"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Parse frontmatter if present
                    metadata = {}
                    if content.startswith('---'):
                        try:
                            parts = content.split('---', 2)
                            if len(parts) >= 3:
                                metadata = yaml.safe_load(parts[1])
                                content = parts[2].strip()
                        except:
                            pass
                    
                    documents.append({
                        'path': str(file_path),
                        'category': category,
                        'filename': file_path.name,
                        'content': content,
                        'metadata': metadata,
                        'title': metadata.get('title', file_path.stem.replace('_', ' '))
                    })
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
    
    return documents

def search_knowledge_base(query: str, documents: List[Dict], limit: int = 5) -> List[Dict]:
    """Simple search function to find relevant documents based on query."""
    # Simple keyword-based search (could be enhanced with embeddings)
    query_lower = query.lower()
    keywords = query_lower.split()
    
    scored_docs = []
    for doc in documents:
        score = 0
        content_lower = doc['content'].lower()
        title_lower = doc['title'].lower()
        
        # Check for keyword matches
        for keyword in keywords:
            score += content_lower.count(keyword) * 1
            score += title_lower.count(keyword) * 3  # Title matches are weighted higher
            
            # Check metadata
            if doc['metadata']:
                for key, value in doc['metadata'].items():
                    if isinstance(value, str) and keyword in value.lower():
                        score += 2
        
        if score > 0:
            scored_docs.append((score, doc))
    
    # Sort by score and return top results
    scored_docs.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in scored_docs[:limit]]

def format_context_for_llm(documents: List[Dict]) -> str:
    """Format relevant documents as context for the LLM."""
    if not documents:
        return ""
    
    context = "Here is relevant information from the knowledge base:\n\n"
    
    for i, doc in enumerate(documents, 1):
        context += f"Document {i}: {doc['title']} (Category: {doc['category']})\n"
        context += "-" * 50 + "\n"
        # Limit content length per document
        content_preview = doc['content'][:1500]
        if len(doc['content']) > 1500:
            content_preview += "..."
        context += content_preview + "\n\n"
    
    return context

# Title and description
st.title("💬 AI Chat Assistant")
st.write("Chat with an AI assistant that can access your knowledge base")

# Sidebar settings
with st.sidebar:
    st.subheader("⚙️ Chat Settings")
    
    # LLM Provider selection
    def on_provider_change():
        st.session_state.llm_provider = "openai" if st.session_state.llm_provider_chat == "OpenAI" else "ollama"
        auto_save_settings()
    
    provider = st.selectbox(
        "LLM Provider",
        ["Ollama (Local)", "OpenAI"],
        index=0 if st.session_state.get('llm_provider', 'ollama') == 'ollama' else 1,
        key="llm_provider_chat",
        on_change=on_provider_change
    )
    
    if provider == "OpenAI":
        def on_api_key_change():
            st.session_state.openai_api_key = st.session_state.openai_api_key_chat
            auto_save_settings()
        
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            value=st.session_state.get('openai_api_key', ''),
            key="openai_api_key_chat",
            help="Enter your OpenAI API key",
            on_change=on_api_key_change
        )
        
        model_options = get_available_openai_models()
        if model_options:
            current_model = st.session_state.get('openai_model', 'gpt-3.5-turbo')
            def on_openai_model_change():
                st.session_state.openai_model = st.session_state.openai_model_chat
                auto_save_settings()
            
            selected_model = st.selectbox(
                "Model",
                model_options,
                index=model_options.index(current_model) if current_model in model_options else 0,
                key="openai_model_chat",
                on_change=on_openai_model_change
            )
    else:
        # Ollama settings
        def on_ollama_url_change():
            st.session_state.ollama_api_url = st.session_state.ollama_api_url_chat
            auto_save_settings()
        
        api_url = st.text_input(
            "Ollama API URL",
            value=st.session_state.get('ollama_api_url', 'http://localhost:11434/api/generate'),
            key="ollama_api_url_chat",
            on_change=on_ollama_url_change
        )
        
        models, model_info = get_available_ollama_models(api_url)
        if models:
            current_model = st.session_state.get('ollama_model', 'llama3.1:8b')
            def on_ollama_model_change():
                st.session_state.ollama_model = st.session_state.ollama_model_chat
                auto_save_settings()
            
            selected_model = st.selectbox(
                "Model",
                models,
                format_func=lambda x: f"{x} {model_info.get(x, '')}",
                index=models.index(current_model) if current_model in models else 0,
                key="ollama_model_chat",
                on_change=on_ollama_model_change
            )
        else:
            st.warning("No Ollama models found. Is Ollama running?")
    
    # Test connection button
    if st.button("Test Connection"):
        with st.spinner("Testing connection..."):
            success, message = test_llm_connection()
            if success:
                st.success(message)
            else:
                st.error(message)
    
    st.divider()
    
    # Knowledge base settings
    st.subheader("📚 Knowledge Base")
    
    def on_kb_toggle():
        st.session_state.chat_use_knowledge_base = st.session_state.use_kb_checkbox
        auto_save_settings()
    
    use_kb = st.checkbox(
        "Use Knowledge Base", 
        value=st.session_state.get('chat_use_knowledge_base', True), 
        key="use_kb_checkbox",
        on_change=on_kb_toggle
    )
    
    if use_kb:
        # Category selection
        kb_path = Path("knowledgebase")
        if kb_path.exists():
            available_categories = [d.name for d in kb_path.iterdir() if d.is_dir()]
            # Get saved selected categories or default to all
            saved_cats = st.session_state.get('chat_selected_categories', [])
            default_cats = saved_cats if saved_cats else available_categories
            
            def on_categories_change():
                st.session_state.chat_selected_categories = st.session_state.category_selector
                auto_save_settings()
            
            selected_cats = st.multiselect(
                "Select Categories",
                available_categories,
                default=default_cats,
                key="category_selector",
                on_change=on_categories_change
            )
            
            # Show document count
            if selected_cats:
                docs = load_knowledge_base_documents(selected_cats)
                st.info(f"📄 {len(docs)} documents available")
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_messages = []
        st.rerun()

# Main chat interface
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.chat_messages:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message user-message">{message["content"]}</div>', unsafe_allow_html=True)
        elif message["role"] == "assistant":
            st.markdown(f'<div class="chat-message assistant-message">{message["content"]}</div>', unsafe_allow_html=True)
        elif message["role"] == "context":
            with st.expander("📚 Knowledge Base Context Used"):
                st.markdown(f'<div class="kb-context">{message["content"]}</div>', unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to chat
    st.session_state.chat_messages.append({"role": "user", "content": user_input})
    
    # Prepare context if using knowledge base
    context = ""
    if st.session_state.get('chat_use_knowledge_base', True) and st.session_state.get('chat_selected_categories', []):
        with st.spinner("Searching knowledge base..."):
            # Load documents from selected categories
            documents = load_knowledge_base_documents(st.session_state.get('chat_selected_categories', []))
            
            # Search for relevant documents
            max_docs = st.session_state.get('chat_max_context_docs', 5)
            relevant_docs = search_knowledge_base(user_input, documents, limit=max_docs)
            
            if relevant_docs:
                context = format_context_for_llm(relevant_docs)
                # Add context to chat for transparency
                st.session_state.chat_messages.append({
                    "role": "context",
                    "content": f"Found {len(relevant_docs)} relevant documents"
                })
    
    # Prepare prompt for LLM
    if context:
        prompt = f"""You are a helpful AI assistant with access to a knowledge base. Use the provided context to answer the user's question accurately.

{context}

User Question: {user_input}

Please provide a helpful and accurate response based on the context provided. If the context doesn't contain relevant information, you can provide a general response but mention that the specific information wasn't found in the knowledge base."""
    else:
        prompt = f"""You are a helpful AI assistant. Please provide a thoughtful and accurate response to the following question:

User Question: {user_input}"""
    
    # Get LLM response
    with st.spinner("Thinking..."):
        response = _call_llm_api(prompt, "chat response")
        
        if response:
            # Add assistant response to chat
            st.session_state.chat_messages.append({"role": "assistant", "content": response})
        else:
            st.session_state.chat_messages.append({
                "role": "assistant", 
                "content": "I'm sorry, I encountered an error while processing your request. Please check the LLM settings and try again."
            })
    
    # Rerun to display new messages
    st.rerun()

# Footer info
with st.sidebar:
    st.divider()
    if st.session_state.get('auto_save_enabled', True):
        st.caption("🔄 Settings auto-save is enabled")
    st.caption("💡 Tips:")
    st.caption("• Enable knowledge base to search your documents")
    st.caption("• Select specific categories to narrow search")
    st.caption("• Test connection before starting chat")
    st.caption("• Clear chat to start fresh")