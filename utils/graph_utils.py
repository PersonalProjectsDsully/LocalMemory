"""
UNUSED MODULE - CANDIDATE FOR REMOVAL

Utility functions for knowledge graph creation and analysis.

STATUS: This module appears to be unused in the current codebase.
- No imports found in any pages or other utility modules
- The Knowledge Graph page (8_🕸️_Knowledge_Graph.py) does not import this module
- Functions appear to be well-implemented but orphaned

RECOMMENDATION: Consider removing this module unless:
1. It's intended for future Knowledge Graph enhancements
2. It's used by external scripts not in the main codebase
3. It provides functionality that should be integrated into the current Knowledge Graph page

If keeping, consider integrating these functions into the Knowledge Graph page:
- calculate_centrality_metrics() could enhance node importance visualization
- find_communities() could provide clustering features
- suggest_connections() could power recommendation features
- detect_influential_documents() could highlight key content
"""
import networkx as nx
import numpy as np
from collections import defaultdict, Counter
from typing import List, Dict, Tuple, Set
import math

def calculate_centrality_metrics(G: nx.Graph) -> Dict[str, Dict[str, float]]:
    """Calculate various centrality metrics for nodes in the graph"""
    if len(G.nodes()) == 0:
        return {}
    
    metrics = {}
    
    # Degree centrality
    degree_centrality = nx.degree_centrality(G)
    
    # Betweenness centrality (for connected components)
    try:
        betweenness_centrality = nx.betweenness_centrality(G)
    except:
        betweenness_centrality = {node: 0.0 for node in G.nodes()}
    
    # Closeness centrality (for connected components)
    try:
        closeness_centrality = nx.closeness_centrality(G)
    except:
        closeness_centrality = {node: 0.0 for node in G.nodes()}
    
    # Eigenvector centrality (for connected components)
    try:
        eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)
    except:
        eigenvector_centrality = {node: 0.0 for node in G.nodes()}
    
    # Combine all metrics
    for node in G.nodes():
        metrics[node] = {
            'degree': degree_centrality.get(node, 0.0),
            'betweenness': betweenness_centrality.get(node, 0.0),
            'closeness': closeness_centrality.get(node, 0.0),
            'eigenvector': eigenvector_centrality.get(node, 0.0)
        }
    
    return metrics

def find_communities(G: nx.Graph) -> Dict[str, int]:
    """Find communities in the graph using the Louvain algorithm"""
    try:
        import community as community_louvain
        communities = community_louvain.best_partition(G)
        return communities
    except ImportError:
        # Fallback to simple connected components
        communities = {}
        for i, component in enumerate(nx.connected_components(G)):
            for node in component:
                communities[node] = i
        return communities

def suggest_connections(documents: List[Dict], threshold: float = 0.3) -> List[Tuple[str, str, float]]:
    """Suggest potential connections between documents based on content similarity"""
    suggestions = []
    
    for i, doc1 in enumerate(documents):
        for j, doc2 in enumerate(documents[i+1:], i+1):
            similarity = calculate_document_similarity(doc1, doc2)
            if similarity > threshold:
                suggestions.append((doc1['name'], doc2['name'], similarity))
    
    return sorted(suggestions, key=lambda x: x[2], reverse=True)

def calculate_document_similarity(doc1: Dict, doc2: Dict) -> float:
    """Calculate similarity between two documents based on various factors"""
    similarity_score = 0.0
    factors = 0
    
    # Tag similarity (Jaccard coefficient)
    tags1 = set(doc1.get('tags', []))
    tags2 = set(doc2.get('tags', []))
    if tags1 or tags2:
        tag_similarity = len(tags1.intersection(tags2)) / len(tags1.union(tags2)) if tags1.union(tags2) else 0
        similarity_score += tag_similarity * 0.6  # Weight for tags
        factors += 0.6
    
    # Category similarity
    if doc1.get('category') == doc2.get('category'):
        similarity_score += 0.2
        factors += 0.2
    
    # Type similarity
    if doc1.get('type') == doc2.get('type'):
        similarity_score += 0.1
        factors += 0.1
    
    # Author similarity
    if doc1.get('author') == doc2.get('author') and doc1.get('author') != 'Unknown':
        similarity_score += 0.1
        factors += 0.1
    
    return similarity_score / factors if factors > 0 else 0.0

def get_path_between_nodes(G: nx.Graph, source: str, target: str) -> List[str]:
    """Find the shortest path between two nodes"""
    try:
        return nx.shortest_path(G, source, target)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return []

def analyze_graph_structure(G: nx.Graph) -> Dict[str, any]:
    """Analyze the overall structure of the graph"""
    analysis = {}
    
    # Basic metrics
    analysis['num_nodes'] = G.number_of_nodes()
    analysis['num_edges'] = G.number_of_edges()
    analysis['density'] = nx.density(G)
    
    # Connected components
    connected_components = list(nx.connected_components(G))
    analysis['num_connected_components'] = len(connected_components)
    analysis['largest_component_size'] = len(max(connected_components, key=len)) if connected_components else 0
    
    # Clustering
    if G.number_of_nodes() > 0:
        analysis['average_clustering'] = nx.average_clustering(G)
        analysis['transitivity'] = nx.transitivity(G)
    
    # Degree statistics
    degrees = [d for n, d in G.degree()]
    if degrees:
        analysis['average_degree'] = sum(degrees) / len(degrees)
        analysis['max_degree'] = max(degrees)
        analysis['min_degree'] = min(degrees)
    
    return analysis

def create_tag_co_occurrence_matrix(documents: List[Dict]) -> Dict[str, Dict[str, int]]:
    """Create a co-occurrence matrix for tags"""
    co_occurrence = defaultdict(lambda: defaultdict(int))
    
    for doc in documents:
        tags = doc.get('tags', [])
        for i, tag1 in enumerate(tags):
            for tag2 in tags[i+1:]:
                co_occurrence[tag1][tag2] += 1
                co_occurrence[tag2][tag1] += 1
    
    return dict(co_occurrence)

def get_hub_and_authority_scores(G: nx.Graph) -> Tuple[Dict[str, float], Dict[str, float]]:
    """Calculate HITS hub and authority scores"""
    try:
        hubs, authorities = nx.hits(G, max_iter=1000)
        return hubs, authorities
    except:
        # Return zeros if calculation fails
        nodes = list(G.nodes())
        return {node: 0.0 for node in nodes}, {node: 0.0 for node in nodes}

def detect_influential_documents(G: nx.Graph, documents: List[Dict]) -> List[Dict]:
    """Detect the most influential documents based on various metrics"""
    if not G.nodes():
        return []
    
    # Calculate centrality metrics
    centrality_metrics = calculate_centrality_metrics(G)
    hubs, authorities = get_hub_and_authority_scores(G)
    
    # Create document info with influence scores
    influential_docs = []
    for doc in documents:
        node_name = doc['name']
        if node_name in G.nodes():
            metrics = centrality_metrics.get(node_name, {})
            
            # Calculate composite influence score
            influence_score = (
                metrics.get('degree', 0) * 0.3 +
                metrics.get('betweenness', 0) * 0.3 +
                metrics.get('eigenvector', 0) * 0.2 +
                hubs.get(node_name, 0) * 0.1 +
                authorities.get(node_name, 0) * 0.1
            )
            
            doc_with_influence = doc.copy()
            doc_with_influence['influence_score'] = influence_score
            doc_with_influence['centrality_metrics'] = metrics
            doc_with_influence['hub_score'] = hubs.get(node_name, 0)
            doc_with_influence['authority_score'] = authorities.get(node_name, 0)
            
            influential_docs.append(doc_with_influence)
    
    # Sort by influence score
    return sorted(influential_docs, key=lambda x: x['influence_score'], reverse=True)

def generate_graph_recommendations(G: nx.Graph, documents: List[Dict]) -> Dict[str, List[str]]:
    """Generate recommendations for improving the knowledge graph"""
    recommendations = {
        'add_tags': [],
        'create_connections': [],
        'organize_clusters': [],
        'featured_documents': []
    }
    
    # Find isolated documents
    isolated_docs = [doc for doc in documents if doc['name'] in G.nodes() and G.degree(doc['name']) == 0]
    if isolated_docs:
        recommendations['add_tags'].extend([
            f"Add more tags to '{doc['title'][:30]}...' to connect it with other documents"
            for doc in isolated_docs[:3]
        ])
    
    # Find potential connections
    suggestions = suggest_connections(documents, threshold=0.2)
    for source, target, similarity in suggestions[:3]:
        source_doc = next((d for d in documents if d['name'] == source), None)
        target_doc = next((d for d in documents if d['name'] == target), None)
        if source_doc and target_doc:
            recommendations['create_connections'].append(
                f"Consider connecting '{source_doc['title'][:25]}...' and '{target_doc['title'][:25]}...' (similarity: {similarity:.2f})"
            )
    
    # Find influential documents
    influential = detect_influential_documents(G, documents)
    if influential:
        recommendations['featured_documents'].extend([
            f"'{doc['title'][:30]}...' is highly influential in your knowledge graph"
            for doc in influential[:3]
        ])
    
    return recommendations