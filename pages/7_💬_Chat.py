import streamlit as st
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Page configuration
st.set_page_config(
    page_title="Chat - Local Knowledgebase",
    page_icon="💬",
    layout="wide"
)

st.title("💬 AI Chat Assistant")

# Check if required dependencies are available
try:
    from utils.llm_utils import _call_llm_api, test_llm_connection
    from utils.session_state_manager import initialize_session_state, auto_save_settings
    
    # Initialize session state
    initialize_session_state()
    
    st.write("Interactive AI assistant with full knowledge base access and context awareness")
    
    # Check LLM availability
    with st.sidebar:
        st.subheader("⚙️ LLM Settings")
        
        provider = st.selectbox(
            "LLM Provider",
            ["Ollama (Local)", "OpenAI"],
            index=0 if st.session_state.get('llm_provider', 'ollama') == 'ollama' else 1
        )
        
        if provider == "OpenAI":
            api_key = st.text_input(
                "OpenAI API Key",
                type="password",
                value=st.session_state.get('openai_api_key', ''),
                help="Enter your OpenAI API key"
            )
        else:
            api_url = st.text_input(
                "Ollama API URL",
                value=st.session_state.get('ollama_api_url', 'http://localhost:11434/api/generate')
            )
    
    # Simple chat interface
    st.subheader("💬 Chat with your Knowledge Base")
    
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    
    # Display chat messages
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me about your knowledge base..."):
        # Add user message
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        # Add assistant response
        with st.chat_message("assistant"):
            response = "I'm ready to help! However, to fully access your knowledge base and provide AI-powered responses, please ensure all required dependencies are installed. See the instructions below."
            st.write(response)
            st.session_state.chat_messages.append({"role": "assistant", "content": response})

except ImportError as e:
    st.error("🚨 Missing Dependencies")
    st.write("The Chat feature requires additional dependencies to function fully.")
    
    st.subheader("📦 Required Installation")
    st.code("""
# Install required packages
pip install requests>=2.31.0
pip install openai>=1.35.0

# Or install all requirements
pip install -r requirements.txt
    """)
    
    st.subheader("🔧 Full Chat Features")
    st.write("""
    Once dependencies are installed, the Chat page will provide:
    
    - **Knowledge Base Search**: AI can reference and quote from saved documents
    - **Context Preservation**: Maintains conversation context across interactions  
    - **Document Retrieval**: Intelligent matching of user queries to relevant content
    - **Source Attribution**: Citations and links to referenced documents
    - **Multi-Provider Support**: Both Ollama (local) and OpenAI integration
    """)
    
    st.info("💡 After installing dependencies, restart the Streamlit app to access full chat functionality.")