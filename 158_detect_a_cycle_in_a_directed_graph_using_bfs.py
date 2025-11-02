"""
DFS Traversal

Perform DFS traversal on graph, return connected components.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from typing import List, Set, Callable


def depth_first_search(
    v: int,
    e: int,
    edges: List[List[int]]
) -> List[List[int]]:
    """
    Perform DFS and return all connected components.
    
    Args:
        v: Number of vertices
        e: Number of edges
        edges: List of edges [u, v]
        
    Returns:
        List of connected components (each component is list of vertices)
    """
    # Build adjacency list
    graph: List[List[int]] = [[] for _ in range(v)]
    for edge in edges:
        u, w = edge
        graph[u].append(w)
        graph[w].append(u)
    
    visited = [False] * v
    result = []
    
    def dfs(vertex: int, component: List[int]) -> None:
        """DFS helper function."""
        if visited[vertex]:
            return
        
        visited[vertex] = True
        component.append(vertex)
        
        for neighbour in graph[vertex]:
            dfs(neighbour, component)
    
    # Process all components
    for i in range(v):
        if not visited[i]:
            component = []
            dfs(i, component)
            result.append(component)
    
    return result

