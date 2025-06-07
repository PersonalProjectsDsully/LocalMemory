# LocalMemory - Intelligent Knowledge Management System

A comprehensive Streamlit-based application for managing, searching, and interacting with your personal knowledge repository. Features AI-powered chat, YouTube integration, intelligent search, and advanced document management capabilities with sophisticated research workflows.

## 🚀 Features

### Core Features
- **📚 Document Management**: Organize documents by categories with drag-and-drop functionality
- **🔍 Advanced Search**: Full-text search across your entire knowledge base with AI enhancement
- **⭐ Favorites System**: Mark and quickly access important documents
- **📝 Recent Activity**: Track recently accessed and modified documents
- **🔍 Duplicate Detection**: Intelligent duplicate document detection and management

### AI-Powered Features
- **💬 AI Chat Assistant**: Interactive chat with your knowledge base using multiple LLM providers
- **🧠 Intelligent Search**: AI-enhanced search with context understanding and synonym expansion
- **📺 YouTube Integration**: Extract, summarize, and analyze YouTube video transcripts
- **🤖 Content Intelligence**: AI-powered content analysis and categorization
- **📊 Research Workflows**: Multi-stage research process with iterative refinement

### Advanced Features
- **🕸️ Knowledge Graph**: Visualize relationships between documents and concepts
- **📈 Analytics**: Track usage patterns and knowledge growth
- **⚙️ Flexible Settings**: Configure AI providers, search parameters, and more
- **🔬 Automatic QA**: Quality assurance for generated reports with automatic improvements

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
8. Use **Intelligent Search** for AI-enhanced research workflows

### AI Configuration
The application supports multiple LLM providers:
- **Ollama (Local)**: Run models locally using Ollama
- **OpenAI**: Use OpenAI's cloud-based models (requires API key)
- **LM Studio (Local)**: Use LM Studio for local model inference

Configure your preferred provider in the Settings page.

### Research Workflows
The system provides comprehensive research capabilities:
- **Multi-stage Research**: Inquiry clarification → Task decomposition → Document research → Report generation
- **Intelligent Document Search**: Uses lexical search enhanced with Moby Thesaurus synonym expansion
- **Iterative Validation**: Ensures research quality through automatic validation loops
- **Automatic QA**: Quality assurance with automatic improvements for generated reports

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
├── app.py                              # Main application entry point
├── pages/                              # Streamlit pages
│   ├── 0_🏠_Home.py                   # Home page
│   ├── 1_📁_Categories.py             # Document categories
│   ├── 2_🔍_Search.py                 # Search functionality
│   ├── 3_📝_Recent.py                 # Recent documents
│   ├── 4_⭐_Favorites.py              # Favorited documents
│   ├── 5_⚙️_Settings.py               # Application settings
│   ├── 6_📺_YouTube.py                # YouTube integration (original)
│   ├── 6_📺_YouTube_Refactored.py     # YouTube integration (refactored)
│   ├── 7_💬_Chat.py                   # AI chat interface
│   ├── 7_🧠_Intelligent_Search.py     # AI-enhanced search (original)
│   ├── 7_🧠_Intelligent_Search_Refactored.py # AI-enhanced search (refactored)
│   ├── 8_🕸️_Knowledge_Graph.py       # Knowledge graph visualization
│   ├── 9_🔍_Duplicate_Detector.py     # Duplicate detection
│   ├── intelligent_search_modules/    # Intelligent Search refactored components
│   │   ├── __init__.py               # Module exports
│   │   ├── report_processing.py      # Report completeness and generation
│   │   ├── qa_quality.py             # QA response parsing and improvements
│   │   ├── session_management.py     # Session state management
│   │   ├── ui_components.py          # Reusable UI components
│   │   ├── workflow_ui.py            # Research workflow interface
│   │   └── quick_search_ui.py        # Quick search interface
│   └── youtube_modules/               # YouTube page refactored components
│       ├── __init__.py               # Module exports
│       ├── youtube_page_utils.py     # Common utilities and styling
│       ├── single_video_handler.py   # Single video processing
│       ├── channel_explorer_handler.py # Channel exploration and bulk processing
│       └── llm_settings_manager.py   # LLM configuration interface
├── utils/                              # Utility modules (organized by function)
│   ├── llm/                           # Language model utilities
│   │   ├── llm_utils.py              # Core LLM functionality
│   │   ├── llm_client.py             # LLM client wrapper
│   │   ├── llm_providers.py          # Multiple LLM provider support
│   │   ├── openai_specialized.py     # OpenAI-specific functionality
│   │   └── robust_json_parser.py     # JSON parsing for LLM responses
│   ├── search/                        # Search and retrieval
│   │   ├── intelligent_search.py     # Core search engine
│   │   ├── intelligent_search_enhanced.py # Enhanced search features
│   │   ├── intelligent_search_refined.py  # Refined scoring algorithms
│   │   ├── enhanced_search_thesaurus.py   # Thesaurus integration
│   │   ├── moby_thesaurus.py         # Moby Thesaurus implementation
│   │   ├── thesaurus_maintenance.py  # Thesaurus utilities
│   │   └── search_config.py          # Search configuration
│   ├── content/                       # Content analysis and intelligence
│   │   ├── content_intelligence.py   # AI-powered content analysis
│   │   ├── batch_intelligence_processor.py # Batch processing
│   │   ├── duplicate_detection.py    # Basic duplicate detection
│   │   └── comprehensive_duplicate_detector.py # Advanced duplicate detection
│   ├── research/                      # Research workflow components
│   │   ├── workflow_orchestrator.py  # Main workflow coordination
│   │   ├── workflow_steps.py         # Individual workflow steps
│   │   ├── document_analysis.py      # Document search and analysis
│   │   ├── validation.py             # Research validation
│   │   ├── report_generation.py      # Report generation
│   │   ├── llm_provider.py           # Research-specific LLM wrapper
│   │   └── workflow_tracker.py       # Progress tracking
│   ├── qa/                           # Quality assurance and report enhancement
│   │   ├── automatic_qa_system.py    # Automatic quality assurance
│   │   ├── enhanced_report_generator.py # Enhanced report generation
│   │   └── report_depth_enhancer.py  # Report depth improvement
│   ├── session/                       # Session and state management
│   │   ├── session_state_manager.py  # Session state management
│   │   ├── settings_manager.py       # Application settings
│   │   ├── workflow_persistence.py   # Workflow state persistence
│   │   ├── progress_reporter.py      # Progress reporting
│   │   └── classification_logger.py  # Classification logging
│   ├── youtube/                       # YouTube integration
│   │   ├── youtube_utils.py          # Core YouTube functionality
│   │   ├── youtube_channel_utils.py  # Channel-specific utilities
│   │   └── video_analysis.py         # Video content analysis
│   └── graph/                        # Graph utilities
│       └── graph_utils.py            # Knowledge graph creation
├── knowledgebase/                     # Document storage
├── research_workspace/                # Research project workspace
├── data/                             # Application data
│   └── thesaurus/                    # Thesaurus data files
└── requirements.txt                   # Python dependencies
```

## 🔧 Architecture

### Search Engine Architecture
The LocalMemory search system operates without vector embeddings, using:

1. **Lexical Search**: Full-text search with TF-IDF-style scoring
2. **Synonym Expansion**: Moby Thesaurus integration with 30,000+ root words and 2.5M synonyms
3. **Phrase Matching**: Bigram and trigram matching with proximity scoring
4. **Entity Recognition**: Metadata-based entity and concept matching
5. **Intent Analysis**: Query intent detection for better result ranking

### Report Generation Pipeline
Multi-stage report generation ensures high-quality output:

1. **Outline Generation**: Creates detailed report structure
2. **Section Generation**: Generates narrative sections with minimum word counts
3. **Depth Enhancement**: Automatically expands shallow content
4. **Quality Assurance**: Two-stage QA with automatic improvements
5. **Citation Management**: Maintains source citations throughout

### Research Workflow
Comprehensive research process with validation:

1. **Inquiry Clarification**: Generates clarifying questions for user queries
2. **Task Decomposition**: Breaks complex queries into manageable subtasks
3. **Document Research**: Searches and analyzes relevant documents iteratively
4. **Validation**: Ensures research quality and completeness
5. **Report Generation**: Creates comprehensive markdown reports

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (if using OpenAI provider)
- `ANTHROPIC_API_KEY`: Your Anthropic API key (if using Claude)

### Settings File
Application settings are automatically saved and loaded from the session state. Configure:
- Default LLM provider and model
- Search parameters and scoring weights
- Research workflow settings
- UI preferences
- API endpoints

### Research Workspace
Research sessions are automatically saved with:
- Session metadata and workflow state
- Document analysis results
- Research findings and insights
- Generated reports in markdown format
- Quality assurance results

## 🧠 Key Features Deep Dive

### Intelligent Search
- **No Vector Embeddings**: Uses sophisticated lexical search with intelligent scoring
- **Synonym Expansion**: Context-aware synonym matching using Moby Thesaurus
- **Intent Detection**: Automatically detects query type (information seeking, comparison, etc.)
- **Proximity Scoring**: Rewards documents where query terms appear close together
- **Smart Ranking**: Balances relevance, recency, and content quality

### Research Workflow
- **Multi-Stage Process**: Systematic approach from query clarification to report generation
- **Iterative Refinement**: Continues research until sufficient findings are collected
- **Automatic Validation**: Quality checks at each stage ensure comprehensive results
- **Evidence Citation**: Maintains source attribution throughout the research process
- **Report Enhancement**: Automatic QA improves report depth and quality

### Content Intelligence
- **Domain Agnostic**: Works across any content domain (technology, entertainment, etc.)
- **Entity Extraction**: Identifies people, places, tools, technologies automatically
- **Concept Recognition**: Extracts abstract ideas, methodologies, skills
- **Relationship Mapping**: Identifies connections between different content pieces
- **Quality Assessment**: Evaluates content authority and reliability

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

#### Code Organization
- Keep modules under 1000 lines
- Organize code by functionality (llm/, search/, content/, etc.)
- Use clear, descriptive naming conventions
- Include comprehensive docstrings

#### Refactored Components
The project has undergone significant refactoring to improve maintainability:

**Large Page Refactoring:**
- `7_🧠_Intelligent_Search.py` (4056 lines) → Split into 6 focused modules
- `6_📺_YouTube.py` (1544 lines) → Split into 4 focused modules

**Benefits of Refactoring:**
- **Maintainability**: Smaller, focused modules are easier to understand and modify
- **Reusability**: Components can be reused across different parts of the application
- **Testability**: Individual modules can be tested in isolation
- **Performance**: Reduced memory footprint and faster load times
- **Collaboration**: Multiple developers can work on different modules simultaneously

#### File Structure Rules
- **utils/llm/**: All language model related functionality
- **utils/search/**: Search engines, thesaurus, and retrieval logic
- **utils/content/**: Content analysis and intelligence features
- **utils/research/**: Research workflow components
- **utils/qa/**: Quality assurance and report generation
- **utils/session/**: Session management and persistence
- **utils/youtube/**: YouTube integration features
- **utils/graph/**: Knowledge graph utilities

#### Import Guidelines
- Use relative imports within module folders
- Import from __init__.py for external access
- Maintain clean dependency hierarchies

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the Settings page for configuration issues
2. Ensure all dependencies are properly installed
3. Verify your LLM provider is correctly configured
4. Check the console for error messages
5. Review research workspace logs for workflow issues

## 🔮 Future Enhancements

### Planned Features
- **Additional LLM Providers**: Support for more local and cloud-based models
- **Enhanced Knowledge Graph**: More sophisticated relationship detection
- **Advanced Analytics**: Deeper insights into knowledge patterns and usage
- **Mobile Support**: Responsive design improvements for mobile devices
- **Collaborative Features**: Multi-user support and shared knowledge bases

### Performance Improvements
- **Caching Optimization**: Better caching strategies for search and analysis
- **Parallel Processing**: Concurrent research task execution
- **Memory Management**: Improved handling of large knowledge bases
- **Search Optimization**: Further refinements to search accuracy and speed

### Integration Enhancements
- **Export/Import**: Knowledge base backup and migration tools
- **API Access**: RESTful API for external integrations
- **Plugin System**: Extensible architecture for custom functionality
- **Database Support**: Optional database backend for large-scale deployments