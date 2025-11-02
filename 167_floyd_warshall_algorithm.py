"""
Floyd Warshall Algorithm

Find shortest paths between all pairs of vertices.

Time Complexity: O(V^3)
Space Complexity: O(V^2)
"""

from typing import List


def floyd_warshall(n: int, graph: List[List[int]]) -> List[List[int]]:
    """
    Find shortest distances between all pairs of vertices.
    
    Uses Floyd-Warshall algorithm with dynamic programming approach.
    Handles negative weights but no negative cycles.
    
    Args:
        n: Number of vertices
        graph: n x n adjacency matrix where graph[i][j] = weight of edge (i,j)
               Use 10**9 for unreachable vertices
    
    Returns:
        n x n matrix of shortest distances
    """
    INF = 10**9
    
    # Initialize distance matrix
    dist = [row[:] for row in graph]
    
    # Set unreachable vertices to INF
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == 0:
                dist[i][j] = INF
    
    # Floyd-Warshall: try all intermediate vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Detect negative cycles (dist[i][i] should be 0 for no self-loop)
    for i in range(n):
        if dist[i][i] < 0:
            return []  # Negative cycle detected
    
    return dist

