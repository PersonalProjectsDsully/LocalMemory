import streamlit as st
import networkx as nx
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import yaml
import re
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import math
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.session_state_manager import initialize_session_state
from utils.graph_utils import (
    calculate_centrality_metrics, 
    analyze_graph_structure, 
    detect_influential_documents,
    generate_graph_recommendations
)

# Page configuration
st.set_page_config(
    page_title="Knowledge Graph - Local Knowledgebase",
    page_icon="🕸️",
    layout="wide"
)

# Initialize session state
initialize_session_state()

def parse_markdown_frontmatter(file_path: Path):
    """Parse YAML frontmatter from markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if content.startswith('---'):
            # Split frontmatter from content
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter_yaml = parts[1].strip()
                if frontmatter_yaml:
                    return yaml.safe_load(frontmatter_yaml)
    except Exception as e:
        pass
    return None

def extract_tags_from_content(content: str):
    """Extract hashtags from markdown content"""
    # Find hashtags in content (e.g., #tag, #machine-learning)
    hashtags = re.findall(r'#([a-zA-Z0-9_-]+)', content)
    return list(set(hashtags))  # Remove duplicates

def get_documents_in_timeframe(start_date, end_date, categories=None):
    """Get documents within specified timeframe and categories"""
    documents = []
    kb_path = Path("knowledgebase")
    
    if not kb_path.exists():
        return documents
    
    # Get all categories or specific ones
    if categories is None or "All Categories" in categories:
        category_dirs = [d for d in kb_path.iterdir() if d.is_dir() and d.name != "settings.json"]
    else:
        category_dirs = [kb_path / cat.replace("/", "_").replace(" ", "_") for cat in categories if (kb_path / cat.replace("/", "_").replace(" ", "_")).exists()]
    
    for category_dir in category_dirs:
        for md_file in category_dir.glob("*.md"):
            try:
                # Check file modification time
                file_time = datetime.fromtimestamp(md_file.stat().st_mtime)
                
                if start_date <= file_time <= end_date:
                    # Parse frontmatter
                    frontmatter = parse_markdown_frontmatter(md_file)
                    
                    # Read content for hashtag extraction
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Get tags from frontmatter and content
                    tags = []
                    if frontmatter and 'tags' in frontmatter:
                        if isinstance(frontmatter['tags'], list):
                            tags.extend(frontmatter['tags'])
                        elif isinstance(frontmatter['tags'], str):
                            tags.append(frontmatter['tags'])
                    
                    # Add hashtags from content
                    content_tags = extract_tags_from_content(content)
                    tags.extend(content_tags)
                    
                    # Remove duplicates and clean tags
                    tags = list(set([tag.strip().lower() for tag in tags if tag.strip()]))
                    
                    doc_info = {
                        'path': md_file,
                        'name': md_file.stem,
                        'title': frontmatter.get('title', md_file.stem) if frontmatter else md_file.stem,
                        'category': category_dir.name,
                        'tags': tags,
                        'type': frontmatter.get('type', 'document') if frontmatter else 'document',
                        'author': frontmatter.get('author', 'Unknown') if frontmatter else 'Unknown',
                        'date_added': frontmatter.get('date_added', file_time.strftime('%Y-%m-%d')) if frontmatter else file_time.strftime('%Y-%m-%d'),
                        'file_time': file_time
                    }
                    
                    documents.append(doc_info)
                    
            except Exception as e:
                continue
    
    return documents

def create_knowledge_graph(documents, min_connections=1):
    """Create a network graph from documents based on shared tags"""
    G = nx.Graph()
    
    # Add document nodes
    for doc in documents:
        node_id = doc['name']
        G.add_node(node_id, 
                  title=doc['title'],
                  category=doc['category'],
                  type=doc['type'],
                  author=doc['author'],
                  tags=doc['tags'],
                  date_added=doc['date_added'],
                  path=str(doc['path']))
    
    # Add edges based on shared tags
    edge_weights = defaultdict(int)
    
    for i, doc1 in enumerate(documents):
        for j, doc2 in enumerate(documents[i+1:], i+1):
            shared_tags = set(doc1['tags']).intersection(set(doc2['tags']))
            if len(shared_tags) >= min_connections:
                edge_weight = len(shared_tags)
                G.add_edge(doc1['name'], doc2['name'], 
                          weight=edge_weight, 
                          shared_tags=list(shared_tags))
                edge_weights[(doc1['name'], doc2['name'])] = edge_weight
    
    return G

def create_plotly_graph(G, layout_type="spring"):
    """Create an interactive Plotly graph visualization"""
    if len(G.nodes()) == 0:
        return None
    
    # Choose layout algorithm
    if layout_type == "spring":
        pos = nx.spring_layout(G, k=3, iterations=50)
    elif layout_type == "circular":
        pos = nx.circular_layout(G)
    elif layout_type == "random":
        pos = nx.random_layout(G)
    else:
        pos = nx.spring_layout(G, k=3, iterations=50)
    
    # Prepare node traces
    node_trace = go.Scatter(
        x=[pos[node][0] for node in G.nodes()],
        y=[pos[node][1] for node in G.nodes()],
        mode='markers+text',
        text=[G.nodes[node].get('title', node)[:30] + ('...' if len(G.nodes[node].get('title', node)) > 30 else '') for node in G.nodes()],
        textposition="middle center",
        textfont=dict(size=10, color="white"),
        hovertemplate='<b>%{customdata[0]}</b><br>' +
                      'Category: %{customdata[1]}<br>' +
                      'Type: %{customdata[2]}<br>' +
                      'Author: %{customdata[3]}<br>' +
                      'Tags: %{customdata[4]}<br>' +
                      'Date: %{customdata[5]}<br>' +
                      '<extra></extra>',
        customdata=[[G.nodes[node].get('title', node),
                     G.nodes[node].get('category', 'Unknown'),
                     G.nodes[node].get('type', 'document'),
                     G.nodes[node].get('author', 'Unknown'),
                     ', '.join(G.nodes[node].get('tags', [])),
                     G.nodes[node].get('date_added', 'Unknown')] for node in G.nodes()],
        marker=dict(
            size=[20 + len(G.nodes[node].get('tags', [])) * 3 for node in G.nodes()],
            color=[hash(G.nodes[node].get('category', 'default')) % 360 for node in G.nodes()],
            colorscale='HSV',
            line=dict(width=2, color='white'),
            opacity=0.8
        )
    )
    
    # Prepare edge traces
    edge_traces = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        weight = G.edges[edge].get('weight', 1)
        shared_tags = G.edges[edge].get('shared_tags', [])
        
        edge_trace = go.Scatter(
            x=[x0, x1, None],
            y=[y0, y1, None],
            mode='lines',
            line=dict(width=weight * 2, color=f'rgba(150, 150, 150, {0.3 + weight * 0.1})'),
            hovertemplate=f'Shared tags: {", ".join(shared_tags)}<br>Connection strength: {weight}<extra></extra>',
            showlegend=False
        )
        edge_traces.append(edge_trace)
    
    # Create figure
    fig = go.Figure(data=[node_trace] + edge_traces)
    
    fig.update_layout(
        title="Knowledge Graph - Documents Connected by Shared Tags",
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20,l=5,r=5,t=40),
        annotations=[ dict(
            text="Hover over nodes to see details. Node size indicates number of tags.",
            showarrow=False,
            xref="paper", yref="paper",
            x=0.005, y=-0.002,
            xanchor='left', yanchor='bottom',
            font=dict(color="gray", size=12)
        )],
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=700
    )
    
    return fig

def display_graph_statistics(G, documents):
    """Display statistics about the graph"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Documents", len(documents))
    
    with col2:
        st.metric("Connected Documents", len([n for n in G.nodes() if G.degree(n) > 0]))
    
    with col3:
        st.metric("Total Connections", G.number_of_edges())
    
    with col4:
        # Most connected document
        if G.nodes():
            most_connected = max(G.nodes(), key=lambda x: G.degree(x))
            st.metric("Most Connected", f"{G.nodes[most_connected].get('title', most_connected)[:20]}...")

def display_tag_analysis(documents):
    """Display tag frequency analysis"""
    st.subheader("📊 Tag Analysis")
    
    # Count tag frequencies
    all_tags = []
    for doc in documents:
        all_tags.extend(doc['tags'])
    
    tag_counts = Counter(all_tags)
    
    if tag_counts:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Create tag frequency chart
            top_tags = dict(tag_counts.most_common(20))
            fig_tags = px.bar(
                x=list(top_tags.values()),
                y=list(top_tags.keys()),
                orientation='h',
                title="Top 20 Most Common Tags",
                labels={'x': 'Frequency', 'y': 'Tags'}
            )
            fig_tags.update_layout(height=500, yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_tags, use_container_width=True)
        
        with col2:
            st.write("**Tag Statistics:**")
            st.write(f"Total unique tags: {len(tag_counts)}")
            st.write(f"Most common tag: **{tag_counts.most_common(1)[0][0]}** ({tag_counts.most_common(1)[0][1]} docs)")
            
            st.write("**Top 10 Tags:**")
            for tag, count in tag_counts.most_common(10):
                st.write(f"• {tag}: {count}")
    else:
        st.info("No tags found in the selected documents.")

# Custom CSS for the graph page
st.markdown("""
<style>
    .stSelectbox > div > div > div {
        background-color: #1a1a1a;
    }
    .graph-container {
        border: 1px solid #333;
        border-radius: 10px;
        padding: 1rem;
        background-color: #0e1117;
    }
    .metric-card {
        background-color: #1a1a1a;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #333;
    }
    .stSlider > div > div > div > div {
        background-color: #1e3a5f;
    }
</style>
""", unsafe_allow_html=True)

# Main page content
st.title("🕸️ Knowledge Graph")
st.write("Visualize connections between your documents based on shared tags and metadata")

# Sidebar controls
with st.sidebar:
    st.subheader("🔧 Graph Controls")
    
    # Category selection
    categories = ["Programming", "AI/ML", "DevOps", "Web Development", "Database", "Security"]
    selected_categories = st.multiselect(
        "Select Categories",
        ["All Categories"] + categories,
        default=["All Categories"],
        help="Choose which categories to include in the graph"
    )
    
    # Time frame selection
    st.subheader("📅 Time Frame")
    time_preset = st.selectbox(
        "Quick Select",
        ["All Time", "Last 7 days", "Last 30 days", "Last 90 days", "Custom Range"]
    )
    
    if time_preset == "Custom Range":
        start_date = st.date_input("Start Date", value=datetime.now() - timedelta(days=30))
        end_date = st.date_input("End Date", value=datetime.now())
    else:
        end_date = datetime.now()
        if time_preset == "Last 7 days":
            start_date = end_date - timedelta(days=7)
        elif time_preset == "Last 30 days":
            start_date = end_date - timedelta(days=30)
        elif time_preset == "Last 90 days":
            start_date = end_date - timedelta(days=90)
        else:  # All Time
            start_date = datetime.now() - timedelta(days=365 * 10)  # 10 years ago
        
        # Convert to date objects for consistency
        start_date = start_date.date() if hasattr(start_date, 'date') else start_date
        end_date = end_date.date() if hasattr(end_date, 'date') else end_date
    
    # Convert back to datetime for comparison
    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.max.time())
    
    # Graph settings
    st.subheader("🎨 Graph Settings")
    layout_type = st.selectbox(
        "Layout Algorithm",
        ["spring", "circular", "random"],
        help="Choose how nodes are positioned"
    )
    
    min_connections = st.slider(
        "Minimum Shared Tags",
        min_value=1,
        max_value=5,
        value=1,
        help="Minimum number of shared tags required to create a connection"
    )
    
    # Additional options
    st.subheader("📊 Export & Analysis")
    
    show_node_details = st.checkbox(
        "Show Node Details Panel",
        help="Display detailed information about graph nodes"
    )
    
    # Refresh button
    if st.button("🔄 Refresh Graph", type="primary"):
        st.rerun()

# Main content area
# Get documents based on filters
with st.spinner("Analyzing documents and building graph..."):
    documents = get_documents_in_timeframe(
        start_datetime, 
        end_datetime, 
        selected_categories if "All Categories" not in selected_categories else None
    )

if not documents:
    st.warning("No documents found in the selected time frame and categories.")
    st.info("Try adjusting your filters or adding some documents to your knowledge base.")
else:
    # Display statistics
    st.subheader("📈 Graph Overview")
    
    # Create the knowledge graph
    G = create_knowledge_graph(documents, min_connections)
    
    # Display statistics
    display_graph_statistics(G, documents)
    
    st.divider()
    
    # Display the graph
    st.subheader("🕸️ Interactive Graph")
    
    if len(G.nodes()) == 0:
        st.warning("No connections found between documents. Try reducing the 'Minimum Shared Tags' requirement or add more tags to your documents.")
    else:
        fig = create_plotly_graph(G, layout_type)
        if fig:
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': True})
            
            # Export graph data
            col1, col2, col3 = st.columns(3)
            
            with col1:
                # Export nodes as CSV
                if st.button("📊 Export Nodes CSV"):
                    import pandas as pd
                    nodes_data = []
                    for node in G.nodes():
                        node_data = G.nodes[node].copy()
                        node_data['name'] = node
                        node_data['connections'] = G.degree(node)
                        node_data['tags'] = ', '.join(node_data.get('tags', []))
                        nodes_data.append(node_data)
                    
                    df = pd.DataFrame(nodes_data)
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="💾 Download Nodes CSV",
                        data=csv,
                        file_name="knowledge_graph_nodes.csv",
                        mime="text/csv"
                    )
            
            with col2:
                # Export edges as CSV
                if st.button("🔗 Export Edges CSV"):
                    import pandas as pd
                    edges_data = []
                    for edge in G.edges(data=True):
                        edge_data = {
                            'source': edge[0],
                            'target': edge[1],
                            'weight': edge[2].get('weight', 1),
                            'shared_tags': ', '.join(edge[2].get('shared_tags', []))
                        }
                        edges_data.append(edge_data)
                    
                    df = pd.DataFrame(edges_data)
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="💾 Download Edges CSV",
                        data=csv,
                        file_name="knowledge_graph_edges.csv",
                        mime="text/csv"
                    )
            
            with col3:
                # Export graph statistics
                if st.button("📈 Export Statistics"):
                    graph_stats = analyze_graph_structure(G)
                    influential_docs = detect_influential_documents(G, documents)
                    
                    stats_text = f"""# Knowledge Graph Statistics
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Basic Metrics
- Total Documents: {len(documents)}
- Connected Documents: {len([n for n in G.nodes() if G.degree(n) > 0])}
- Total Connections: {G.number_of_edges()}
- Graph Density: {graph_stats.get('density', 0):.3f}
- Connected Components: {graph_stats.get('num_connected_components', 0)}
- Average Clustering: {graph_stats.get('average_clustering', 0):.3f}

## Most Influential Documents
"""
                    for i, doc in enumerate(influential_docs[:10], 1):
                        stats_text += f"{i}. {doc['title']} (Score: {doc.get('influence_score', 0):.3f})\n"
                    
                    st.download_button(
                        label="💾 Download Statistics",
                        data=stats_text,
                        file_name="knowledge_graph_statistics.md",
                        mime="text/markdown"
                    )
            
            # Graph insights
            st.subheader("🔍 Graph Insights")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Most Connected Documents:**")
                # Get top 5 most connected documents
                if G.nodes():
                    most_connected = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)[:5]
                    for i, node in enumerate(most_connected, 1):
                        connections = G.degree(node)
                        if connections > 0:
                            title = G.nodes[node].get('title', node)
                            st.write(f"{i}. **{title[:40]}{'...' if len(title) > 40 else ''}** ({connections} connections)")
            
            with col2:
                st.write("**Isolated Documents:**")
                isolated = [node for node in G.nodes() if G.degree(node) == 0]
                if isolated:
                    for node in isolated[:5]:
                        title = G.nodes[node].get('title', node)
                        st.write(f"• {title[:40]}{'...' if len(title) > 40 else ''}")
                    if len(isolated) > 5:
                        st.write(f"... and {len(isolated) - 5} more")
                else:
                    st.success("All documents are connected!")
    
    st.divider()
    
    # Advanced graph analysis
    st.subheader("🔬 Advanced Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Graph Structure Analysis:**")
        graph_analysis = analyze_graph_structure(G)
        
        st.metric("Graph Density", f"{graph_analysis.get('density', 0):.3f}")
        st.metric("Connected Components", graph_analysis.get('num_connected_components', 0))
        st.metric("Average Clustering", f"{graph_analysis.get('average_clustering', 0):.3f}")
        
        if graph_analysis.get('average_degree'):
            st.metric("Average Connections", f"{graph_analysis.get('average_degree', 0):.1f}")
    
    with col2:
        st.write("**Most Influential Documents:**")
        influential_docs = detect_influential_documents(G, documents)
        
        if influential_docs:
            for i, doc in enumerate(influential_docs[:5], 1):
                influence = doc.get('influence_score', 0)
                st.write(f"{i}. **{doc['title'][:35]}{'...' if len(doc['title']) > 35 else ''}**")
                st.caption(f"Influence Score: {influence:.3f}")
        else:
            st.info("No influential documents detected.")
    
    # Recommendations
    st.subheader("💡 Graph Recommendations")
    recommendations = generate_graph_recommendations(G, documents)
    
    if any(recommendations.values()):
        rec_tabs = st.tabs(["🏷️ Add Tags", "🔗 Create Connections", "⭐ Featured Docs"])
        
        with rec_tabs[0]:
            if recommendations['add_tags']:
                for rec in recommendations['add_tags']:
                    st.write(f"• {rec}")
            else:
                st.success("All documents are well-tagged!")
        
        with rec_tabs[1]:
            if recommendations['create_connections']:
                for rec in recommendations['create_connections']:
                    st.write(f"• {rec}")
            else:
                st.success("Good connection coverage!")
        
        with rec_tabs[2]:
            if recommendations['featured_documents']:
                for rec in recommendations['featured_documents']:
                    st.write(f"• {rec}")
            else:
                st.info("No standout documents detected.")
    
    st.divider()
    
    # Tag analysis
    display_tag_analysis(documents)
    
    st.divider()
    
    # Document list
    st.subheader("📑 Document Details")
    
    # Create expandable sections by category
    categories_with_docs = defaultdict(list)
    for doc in documents:
        categories_with_docs[doc['category']].append(doc)
    
    for category, cat_docs in categories_with_docs.items():
        with st.expander(f"📂 {category} ({len(cat_docs)} documents)"):
            for doc in sorted(cat_docs, key=lambda x: x['file_time'], reverse=True):
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    icon = "📺" if doc['type'] == 'youtube' else "📄"
                    st.write(f"{icon} **{doc['title']}**")
                    if doc['tags']:
                        st.caption(f"Tags: {', '.join(doc['tags'])}")
                
                with col2:
                    st.caption(f"Added: {doc['date_added']}")
                    st.caption(f"Author: {doc['author']}")
                
                with col3:
                    connections = G.degree(doc['name']) if doc['name'] in G else 0
                    st.metric("Connections", connections)
    
    # Node details panel (if enabled)
    if show_node_details and G.nodes():
        st.divider()
        st.subheader("🔍 Node Details Explorer")
        
        # Node selection
        node_names = list(G.nodes())
        node_titles = [G.nodes[node].get('title', node) for node in node_names]
        
        selected_node_idx = st.selectbox(
            "Select a document to explore:",
            range(len(node_names)),
            format_func=lambda x: f"{node_titles[x][:50]}{'...' if len(node_titles[x]) > 50 else ''}"
        )
        
        if selected_node_idx is not None:
            selected_node = node_names[selected_node_idx]
            node_data = G.nodes[selected_node]
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**Title:** {node_data.get('title', 'Unknown')}")
                st.write(f"**Category:** {node_data.get('category', 'Unknown')}")
                st.write(f"**Type:** {node_data.get('type', 'Unknown')}")
                st.write(f"**Author:** {node_data.get('author', 'Unknown')}")
                st.write(f"**Date Added:** {node_data.get('date_added', 'Unknown')}")
                
                if node_data.get('tags'):
                    st.write(f"**Tags:** {', '.join(node_data['tags'])}")
            
            with col2:
                st.metric("Direct Connections", G.degree(selected_node))
                
                # Calculate centrality for this node
                if len(G.nodes()) > 1:
                    centrality_metrics = calculate_centrality_metrics(G)
                    node_centrality = centrality_metrics.get(selected_node, {})
                    
                    st.write("**Centrality Scores:**")
                    st.write(f"Degree: {node_centrality.get('degree', 0):.3f}")
                    st.write(f"Betweenness: {node_centrality.get('betweenness', 0):.3f}")
                    st.write(f"Closeness: {node_centrality.get('closeness', 0):.3f}")
            
            # Show connected nodes
            st.write("**Connected Documents:**")
            neighbors = list(G.neighbors(selected_node))
            
            if neighbors:
                for neighbor in neighbors:
                    neighbor_data = G.nodes[neighbor]
                    edge_data = G.edges[selected_node, neighbor]
                    shared_tags = edge_data.get('shared_tags', [])
                    
                    st.write(f"🔗 **{neighbor_data.get('title', neighbor)}**")
                    st.caption(f"Shared tags: {', '.join(shared_tags)} | Connection strength: {edge_data.get('weight', 1)}")
            else:
                st.info("This document has no connections. Consider adding more tags to connect it with other documents.")

# Footer
st.divider()
st.caption("💡 **Tip**: Documents are connected when they share tags. Add more tags to your documents to create richer connections in the graph.")