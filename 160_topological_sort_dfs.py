"""
Topological Sort

Find topological ordering of directed acyclic graph using DFS.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from typing import List


def dfs_topo_sort(
    adj: List[List[int]],
    visited: List[bool],
    stack: List[int],
    node: int
) -> None:
    """
    DFS helper for topological sort.
    
    Args:
        adj: Adjacency list
        visited: Visited array
        stack: Stack to store topological order
        node: Current node
    """
    if visited[node]:
        return
    
    visited[node] = True
    
    for neighbour in adj[node]:
        if not visited[neighbour]:
            dfs_topo_sort(adj, visited, stack, neighbour)
    
    # Push to stack after processing all neighbors
    stack.append(node)


def topological_sort(
    edges: List[List[int]],
    v: int,
    e: int
) -> List[int]:
    """
    Find topological ordering of DAG.
    
    Args:
        edges: List of edges [u, v]
        v: Number of vertices
        e: Number of edges
        
    Returns:
        Topological ordering
    """
    # Build adjacency list
    adj: List[List[int]] = [[] for _ in range(v)]
    for edge in edges:
        u, w = edge
        adj[u].append(w)
    
    visited = [False] * v
    stack = []
    
    # Process all components
    for i in range(v):
        if not visited[i]:
            dfs_topo_sort(adj, visited, stack, i)
    
    # Reverse stack to get topological order
    return stack[::-1]

