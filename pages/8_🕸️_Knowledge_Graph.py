import streamlit as st
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import yaml
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Page configuration
st.set_page_config(
    page_title="Knowledge Graph - Local Knowledgebase", 
    page_icon="🕸️",
    layout="wide"
)

# Check if required dependencies are available
try:
    import networkx as nx
    import plotly.graph_objects as go
    import plotly.express as px
    import pandas as pd
    GRAPH_AVAILABLE = True
except ImportError:
    GRAPH_AVAILABLE = False

st.title("🕸️ Knowledge Graph")

if not GRAPH_AVAILABLE:
    st.error("🚨 Missing Dependencies for Graph Visualization")
    st.write("The Knowledge Graph requires additional dependencies for full functionality.")
    
    st.subheader("📦 Required Installation")
    st.code("""
# Install required packages for Knowledge Graph
pip install networkx>=3.2.1
pip install plotly>=5.17.0  
pip install pandas>=2.1.4

# Or install all requirements
pip install -r requirements.txt
    """)
    
    st.subheader("🕸️ Knowledge Graph Features")
    st.write("""
    **What you'll get with full dependencies:**
    - Interactive network visualization of your knowledge
    - Document relationships based on shared entities and concepts
    - Dynamic filtering by category, time period, and content type
    - Entity and concept clustering
    - Path finding between related documents
    - Intelligent content discovery
    """)
    
    st.stop()

# Custom CSS for graph styling
st.markdown("""
<style>
    .graph-container {
        background-color: #0e1117;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .node-info {
        background-color: #1a1a1a;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border: 1px solid #333;
    }
    .entity-tag {
        background-color: #2c5282;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        margin: 0.2rem;
        display: inline-block;
    }
    .concept-tag {
        background-color: #38a169;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        margin: 0.2rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_documents():
    """Load all documents from the knowledgebase with enhanced metadata"""
    documents = []
    kb_path = Path("knowledgebase")
    
    if not kb_path.exists():
        return documents
    
    for md_file in kb_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse YAML frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    try:
                        frontmatter = yaml.safe_load(parts[1]) or {}
                        body = parts[2].strip()
                    except yaml.YAMLError:
                        frontmatter = {}
                        body = content
                else:
                    frontmatter = {}
                    body = content
            else:
                frontmatter = {}
                body = content
            
            # Extract document info with new intelligent fields
            doc = {
                'name': md_file.stem,
                'title': frontmatter.get('title', md_file.stem),
                'category': frontmatter.get('category', 'General'),
                'author': frontmatter.get('author', 'Unknown'),
                'date_added': frontmatter.get('date_added', ''),
                'content_type': frontmatter.get('type', 'document'),
                'file_path': str(md_file),
                'relative_path': str(md_file.relative_to(kb_path)),
                
                # Enhanced intelligent metadata
                'entities': frontmatter.get('entities', []),
                'concepts': frontmatter.get('concepts', []),
                'content_structure': frontmatter.get('content_structure', 'unknown'),
                'difficulty_level': frontmatter.get('difficulty_level', 'unknown'),
                'prerequisites': frontmatter.get('prerequisites', []),
                'related_topics': frontmatter.get('related_topics', []),
                'authority_signals': frontmatter.get('authority_signals', []),
                'confidence_score': frontmatter.get('confidence_score', 0.5),
                
                # Legacy fields for backward compatibility
                'tags': frontmatter.get('tags', []),
                'body': body[:500],  # Preview
                'word_count': len(body.split())
            }
            
            documents.append(doc)
            
        except Exception as e:
            st.error(f"Error loading {md_file}: {e}")
            continue
    
    return documents

def create_enhanced_knowledge_graph(documents, min_connections=1, connection_type="entities"):
    """
    Create enhanced knowledge graph based on intelligent metadata
    """
    G = nx.Graph()
    
    # Add document nodes
    for doc in documents:
        node_id = doc['name']
        G.add_node(node_id, **doc)
    
    # Create connections based on shared entities, concepts, or topics
    for i, doc1 in enumerate(documents):
        for j, doc2 in enumerate(documents[i+1:], i+1):
            if connection_type == "entities":
                shared_items = set(doc1['entities']).intersection(set(doc2['entities']))
            elif connection_type == "concepts":
                shared_items = set(doc1['concepts']).intersection(set(doc2['concepts']))
            elif connection_type == "topics":
                shared_items = set(doc1['related_topics']).intersection(set(doc2['related_topics']))
            else:  # combined
                shared_entities = set(doc1['entities']).intersection(set(doc2['entities']))
                shared_concepts = set(doc1['concepts']).intersection(set(doc2['concepts']))
                shared_items = shared_entities.union(shared_concepts)
            
            if len(shared_items) >= min_connections:
                weight = len(shared_items)
                G.add_edge(doc1['name'], doc2['name'], 
                          weight=weight, 
                          shared_items=list(shared_items),
                          connection_type=connection_type)
    
    return G

def create_interactive_graph(G, layout_type="spring"):
    """Create interactive plotly graph"""
    if len(G.nodes()) == 0:
        return None
    
    # Choose layout
    if layout_type == "spring":
        pos = nx.spring_layout(G, k=3, iterations=50)
    elif layout_type == "circular":
        pos = nx.circular_layout(G)
    elif layout_type == "shell":
        pos = nx.shell_layout(G)
    else:
        pos = nx.random_layout(G)
    
    # Extract node information
    node_trace = go.Scatter(
        x=[pos[node][0] for node in G.nodes()],
        y=[pos[node][1] for node in G.nodes()],
        mode='markers+text',
        text=[G.nodes[node].get('title', node)[:20] for node in G.nodes()],
        textposition="middle center",
        hovertemplate='<b>%{text}</b><br>' +
                     'Category: %{customdata[0]}<br>' +
                     'Author: %{customdata[1]}<br>' +
                     'Connections: %{customdata[2]}<br>' +
                     'Confidence: %{customdata[3]:.1%}<br>' +
                     '<extra></extra>',
        customdata=[[G.nodes[node].get('category', 'Unknown'),
                    G.nodes[node].get('author', 'Unknown'),
                    len(list(G.neighbors(node))),
                    G.nodes[node].get('confidence_score', 0.5)] for node in G.nodes()],
        marker=dict(
            size=[15 + len(list(G.neighbors(node))) * 2 for node in G.nodes()],
            color=[hash(G.nodes[node].get('category', 'Unknown')) % 10 for node in G.nodes()],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Category", tickmode="array"),
            line=dict(width=2, color='white')
        )
    )
    
    # Extract edge information
    edge_x = []
    edge_y = []
    edge_info = []
    
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        
        edge_data = G.edges[edge]
        shared_items = edge_data.get('shared_items', [])
        edge_info.append(f"Shared: {', '.join(shared_items[:3])}")
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='rgba(136, 136, 136, 0.5)'),
        hoverinfo='none',
        mode='lines'
    )
    
    # Create figure
    fig = go.Figure(data=[edge_trace, node_trace],
                   layout=go.Layout(
                       title='Knowledge Graph - Interactive Network Visualization',
                       titlefont_size=16,
                       showlegend=False,
                       hovermode='closest',
                       margin=dict(b=20,l=5,r=5,t=40),
                       annotations=[ dict(
                           text="Nodes represent documents. Size indicates connections. Hover for details.",
                           showarrow=False,
                           xref="paper", yref="paper",
                           x=0.005, y=-0.002,
                           xanchor="left", yanchor="bottom",
                           font=dict(color="white", size=12)
                       )],
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       plot_bgcolor='rgba(0,0,0,0)',
                       paper_bgcolor='rgba(0,0,0,0)'
                   ))
    
    return fig

# Main interface
st.write("Explore relationships between documents based on shared entities, concepts, and topics.")

# Load documents
with st.spinner("Loading documents..."):
    documents = load_documents()

if not documents:
    st.warning("No documents found in the knowledgebase. Import some content first!")
    st.stop()

st.success(f"✅ Loaded {len(documents)} documents")

# Display statistics
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_entities = len(set(entity for doc in documents for entity in doc['entities']))
    st.metric("Unique Entities", total_entities)

with col2:
    total_concepts = len(set(concept for doc in documents for concept in doc['concepts']))
    st.metric("Unique Concepts", total_concepts)

with col3:
    categories = set(doc['category'] for doc in documents)
    st.metric("Categories", len(categories))

with col4:
    avg_confidence = sum(doc['confidence_score'] for doc in documents) / len(documents)
    st.metric("Avg Confidence", f"{avg_confidence:.1%}")

# Filtering options
st.subheader("🔧 Graph Configuration")

col1, col2, col3 = st.columns(3)

with col1:
    # Connection type
    connection_type = st.selectbox(
        "Connection Basis:",
        ["entities", "concepts", "topics", "combined"],
        help="What should link documents together?"
    )

with col2:
    # Minimum connections
    min_connections = st.slider(
        "Minimum Shared Items:",
        min_value=1,
        max_value=5,
        value=1,
        help="How many shared items needed to create a connection?"
    )

with col3:
    # Layout type
    layout_type = st.selectbox(
        "Layout Algorithm:",
        ["spring", "circular", "shell", "random"],
        help="How to arrange the nodes"
    )

# Additional filters
col1, col2, col3 = st.columns(3)

with col1:
    # Category filter
    selected_categories = st.multiselect(
        "Filter by Categories:",
        sorted(categories),
        default=list(categories)
    )

with col2:
    # Content type filter
    content_types = set(doc['content_type'] for doc in documents)
    selected_content_types = st.multiselect(
        "Filter by Content Type:",
        sorted(content_types),
        default=list(content_types)
    )

with col3:
    # Difficulty filter
    difficulty_levels = set(doc['difficulty_level'] for doc in documents if doc['difficulty_level'] != 'unknown')
    if difficulty_levels:
        selected_difficulties = st.multiselect(
            "Filter by Difficulty:",
            sorted(difficulty_levels),
            default=list(difficulty_levels)
        )
    else:
        selected_difficulties = []

# Apply filters
filtered_documents = [
    doc for doc in documents
    if doc['category'] in selected_categories
    and doc['content_type'] in selected_content_types
    and (not selected_difficulties or doc['difficulty_level'] in selected_difficulties)
]

st.info(f"📊 Showing {len(filtered_documents)} of {len(documents)} documents")

# Generate and display graph
if filtered_documents:
    with st.spinner("Generating knowledge graph..."):
        G = create_enhanced_knowledge_graph(filtered_documents, min_connections, connection_type)
        
        if len(G.nodes()) == 0:
            st.warning("No documents to display with current filters.")
        elif len(G.edges()) == 0:
            st.warning(f"No connections found with {min_connections} minimum shared {connection_type}. Try lowering the threshold.")
        else:
            st.subheader("🕸️ Interactive Knowledge Graph")
            
            # Graph statistics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Nodes", len(G.nodes()))
            with col2:
                st.metric("Connections", len(G.edges()))
            with col3:
                st.metric("Density", f"{nx.density(G):.3f}")
            with col4:
                components = nx.number_connected_components(G)
                st.metric("Components", components)
            
            # Create and display interactive graph
            fig = create_interactive_graph(G, layout_type)
            if fig:
                st.plotly_chart(fig, use_container_width=True, height=600)
            
            # Entity and concept analysis
            st.divider()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🏷️ Top Entities")
                entity_counts = Counter(entity for doc in filtered_documents for entity in doc['entities'])
                if entity_counts:
                    for entity, count in entity_counts.most_common(10):
                        st.markdown(f"<span class='entity-tag'>{entity} ({count})</span>", unsafe_allow_html=True)
                else:
                    st.info("No entities found in filtered documents")
            
            with col2:
                st.subheader("💡 Top Concepts")
                concept_counts = Counter(concept for doc in filtered_documents for concept in doc['concepts'])
                if concept_counts:
                    for concept, count in concept_counts.most_common(10):
                        st.markdown(f"<span class='concept-tag'>{concept} ({count})</span>", unsafe_allow_html=True)
                else:
                    st.info("No concepts found in filtered documents")
            
            # Node details
            if st.checkbox("🔍 Show Node Details"):
                st.subheader("📋 Document Details")
                
                # Most connected nodes
                degree_centrality = nx.degree_centrality(G)
                most_connected = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
                
                st.write("**Most Connected Documents:**")
                for node_id, centrality in most_connected:
                    doc = next(doc for doc in filtered_documents if doc['name'] == node_id)
                    
                    with st.container():
                        st.markdown(f"""
                        <div class="node-info">
                            <strong>{doc['title']}</strong><br>
                            <em>by {doc['author']} | {doc['category']} | {doc['content_type']}</em><br>
                            <small>Connections: {G.degree[node_id]} | Centrality: {centrality:.3f}</small><br>
                            <small>Entities: {', '.join(doc['entities'][:5])}</small><br>
                            <small>Concepts: {', '.join(doc['concepts'][:5])}</small>
                        </div>
                        """, unsafe_allow_html=True)

else:
    st.warning("No documents match the selected filters.")

# Sidebar - Graph Analytics
with st.sidebar:
    st.subheader("📊 Graph Analytics")
    
    if 'G' in locals() and len(G.nodes()) > 0:
        # Basic graph metrics
        st.metric("Graph Density", f"{nx.density(G):.3f}")
        
        if nx.is_connected(G):
            diameter = nx.diameter(G)
            st.metric("Graph Diameter", diameter)
            
            avg_path_length = nx.average_shortest_path_length(G)
            st.metric("Avg Path Length", f"{avg_path_length:.2f}")
        
        # Centrality measures
        st.write("**Most Central Documents:**")
        betweenness = nx.betweenness_centrality(G)
        top_betweenness = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:3]
        
        for node_id, score in top_betweenness:
            doc = next(doc for doc in filtered_documents if doc['name'] == node_id)
            st.caption(f"{doc['title'][:30]}... ({score:.3f})")
    
    st.divider()
    
    # Export options
    st.subheader("📤 Export Options")
    
    if st.button("📊 Export Graph Data"):
        if 'G' in locals():
            # Create downloadable data
            nodes_data = []
            for node in G.nodes(data=True):
                nodes_data.append({
                    'id': node[0],
                    'title': node[1].get('title', ''),
                    'category': node[1].get('category', ''),
                    'connections': G.degree[node[0]]
                })
            
            edges_data = []
            for edge in G.edges(data=True):
                edges_data.append({
                    'source': edge[0],
                    'target': edge[1],
                    'weight': edge[2].get('weight', 1),
                    'shared_items': ', '.join(edge[2].get('shared_items', []))
                })
            
            # Convert to CSV format
            import pandas as pd
            nodes_df = pd.DataFrame(nodes_data)
            edges_df = pd.DataFrame(edges_data)
            
            st.download_button(
                "📥 Download Nodes CSV",
                nodes_df.to_csv(index=False),
                file_name=f"knowledge_graph_nodes_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv"
            )
            
            st.download_button(
                "📥 Download Edges CSV",
                edges_df.to_csv(index=False),
                file_name=f"knowledge_graph_edges_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv"
            )
    
    st.divider()
    st.caption("🕸️ Knowledge Graph v2.0")
    st.caption("Enhanced with Intelligent Metadata")