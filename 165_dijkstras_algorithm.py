"""
Dijkstra's Shortest Path

Find shortest paths from source to all vertices using Dijkstra's algorithm.

Time Complexity: O((V + E) log V)
Space Complexity: O(V + E)
"""

from typing import List, Dict, Tuple, Set
import sys


def dijkstra(
    vec: List[List[int]],
    vertices: int,
    edges: int,
    source: int
) -> List[int]:
    """
    Find shortest distances from source to all vertices.
    
    Args:
        vec: List of edges [u, v, weight]
        vertices: Number of vertices
        edges: Number of edges
        source: Source vertex
        
    Returns:
        Array of shortest distances from source
    """
    # Build adjacency list
    adj: Dict[int, List[Tuple[int, int]]] = {}
    for edge in vec:
        u, v, w = edge
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Initialize distances
    dist = [sys.maxsize] * vertices
    
    # Priority set (distance, node)
    priority_set: Set[Tuple[int, int]] = set()
    
    dist[source] = 0
    priority_set.add((0, source))
    
    while priority_set:
        # Get minimum distance node
        node_distance, top_node = min(priority_set)
        priority_set.remove((node_distance, top_node))
        
        # Update neighbors
        if top_node in adj:
            for neighbour, weight in adj[top_node]:
                new_dist = node_distance + weight
                if new_dist < dist[neighbour]:
                    # Remove old entry if exists
                    old_entry = (dist[neighbour], neighbour)
                    if old_entry in priority_set:
                        priority_set.remove(old_entry)
                    
                    # Update distance and add to set
                    dist[neighbour] = new_dist
                    priority_set.add((new_dist, neighbour))
    
    return dist

