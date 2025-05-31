# Local Knowledgebase

A comprehensive Streamlit-based application for managing, searching, and interacting with your personal knowledge repository. Features AI-powered chat, YouTube integration, intelligent search, and advanced document management capabilities.

## 🚀 Features

### Core Features
- **📚 Document Management**: Organize documents by categories with drag-and-drop functionality
- **🔍 Advanced Search**: Full-text search across your entire knowledge base
- **⭐ Favorites System**: Mark and quickly access important documents
- **📝 Recent Activity**: Track recently accessed and modified documents
- **🔍 Duplicate Detection**: Intelligent duplicate document detection and management

### AI-Powered Features
- **💬 AI Chat Assistant**: Interactive chat with your knowledge base using multiple LLM providers
- **🧠 Intelligent Search**: AI-enhanced search with context understanding
- **📺 YouTube Integration**: Extract, summarize, and analyze YouTube video transcripts
- **🤖 Content Intelligence**: AI-powered content analysis and categorization

### Advanced Features
- **🕸️ Knowledge Graph**: Visualize relationships between documents and concepts
- **📊 Analytics**: Track usage patterns and knowledge growth
- **⚙️ Flexible Settings**: Configure AI providers, search parameters, and more

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
1. Clone the repository:
```bash
git clone <repository-url>
cd local-knowledgebase
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 📋 Dependencies

The application requires the following packages:
- `streamlit==1.40.2` - Web application framework
- `youtube-transcript-api==0.6.2` - YouTube transcript extraction
- `pytube==15.0.0` - YouTube video information
- `PyYAML==6.0.1` - YAML configuration files
- `requests==2.31.0` - HTTP requests
- `openai==1.35.0` - OpenAI API integration
- `networkx==3.2.1` - Knowledge graph creation
- `plotly==5.17.0` - Interactive visualizations
- `pandas==2.1.4` - Data manipulation
- `selenium==4.15.2` - Web scraping
- `beautifulsoup4==4.12.2` - HTML parsing

## 🎯 Usage

### Getting Started
1. **Navigate to Categories** to browse and organize your documents
2. **Drag and drop** markdown files into any category to add them
3. Use **Search** to quickly find specific documents
4. Mark important documents as **Favorites** for quick access
5. Extract and summarize **YouTube** video transcripts with AI
6. **Chat** with an AI assistant that can reference your knowledge base
7. Configure AI/LLM settings in **Settings** page

### AI Configuration
The application supports multiple LLM providers:
- **Ollama (Local)**: Run models locally using Ollama
- **OpenAI**: Use OpenAI's cloud-based models (requires API key)
- **LM Studio (Local)**: Use LM Studio for local model inference

Configure your preferred provider in the Settings page.

### YouTube Integration
- Extract transcripts from YouTube videos
- Generate AI-powered summaries
- Automatically categorize content
- Handle channel-wide content extraction
- Duplicate detection for existing videos

### Knowledge Graph
Visualize connections between:
- Documents and their relationships
- Topics and concepts
- Authors and content
- Categories and tags

## 📁 Project Structure

```
├── app.py                          # Main application entry point
├── pages/                          # Streamlit pages
│   ├── 0_🏠_Home.py               # Home page
│   ├── 1_📁_Categories.py         # Document categories
│   ├── 2_🔍_Search.py             # Search functionality
│   ├── 3_📝_Recent.py             # Recent documents
│   ├── 4_⭐_Favorites.py          # Favorited documents
│   ├── 5_⚙️_Settings.py           # Application settings
│   ├── 6_📺_YouTube.py            # YouTube integration
│   ├── 7_💬_Chat.py               # AI chat interface
│   ├── 7_🧠_Intelligent_Search.py # AI-enhanced search
│   ├── 8_🕸️_Knowledge_Graph.py   # Knowledge graph visualization
│   └── 9_🔍_Duplicate_Detector.py # Duplicate detection
├── utils/                          # Utility modules
│   ├── llm_utils.py               # LLM integration
│   ├── session_state_manager.py   # Session management
│   ├── youtube_utils.py           # YouTube functionality
│   ├── intelligent_search.py      # AI search capabilities
│   ├── duplicate_detection.py     # Duplicate detection
│   └── graph_utils.py             # Graph visualization
├── knowledgebase/                  # Document storage
├── research_workspace/             # Research projects
└── requirements.txt                # Python dependencies
```

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (if using OpenAI provider)
- `ANTHROPIC_API_KEY`: Your Anthropic API key (if using Claude)

### Settings File
Application settings are automatically saved and loaded from the session state. Configure:
- Default LLM provider and model
- Search parameters
- UI preferences
- API endpoints

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the Settings page for configuration issues
2. Ensure all dependencies are properly installed
3. Verify your LLM provider is correctly configured
4. Check the console for error messages

## 🔮 Future Enhancements

- Additional LLM provider support
- Enhanced knowledge graph features
- Advanced analytics and insights
- Mobile-responsive design improvements
- Collaborative features
- Export/import functionality