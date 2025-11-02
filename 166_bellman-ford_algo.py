"""
Bellman Ford Algorithm

Find shortest paths from source to all vertices (handles negative edges).

Time Complexity: O(V * E)
Space Complexity: O(V)
"""

from typing import List


def bellman_ford(
    n: int,
    m: int,
    src: int,
    dest: int,
    edges: List[List[int]]
) -> int:
    """
    Find shortest path using Bellman-Ford algorithm.
    
    Args:
        n: Number of vertices
        m: Number of edges
        src: Source vertex
        dest: Destination vertex
        edges: List of edges [u, v, weight]
        
    Returns:
        Shortest distance, or -1 if negative cycle exists
    """
    INF = 10**9
    dist = [INF] * (n + 1)
    dist[src] = 0
    
    # Relax edges n-1 times
    for _ in range(1, n):
        for edge in edges:
            u, v, w = edge
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # Check for negative cycle
    for edge in edges:
        u, v, w = edge
        if dist[u] != INF and dist[u] + w < dist[v]:
            return -1  # Negative cycle detected
    
    return dist[dest] if dist[dest] != INF else -1
