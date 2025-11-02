"""
Detect Cycle In A Directed Graph

Detect cycle in directed graph using DFS with recursion stack.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List, Tuple


def dfs_is_cycle(
    adj: List[List[int]],
    visited: List[bool],
    dfs_visited: List[bool],
    node: int
) -> bool:
    """
    Check for cycle using DFS with recursion stack tracking.
    
    Args:
        adj: Adjacency list
        visited: Visited array
        dfs_visited: DFS recursion stack array
        node: Current node
        
    Returns:
        True if cycle found, False otherwise
    """
    if visited[node]:
        return False
    
    visited[node] = True
    
    for neighbour in adj[node]:
        if visited[neighbour]:
            if dfs_visited[neighbour]:
                return True
            else:
                continue
        else:
            dfs_visited[neighbour] = True
            if dfs_is_cycle(adj, visited, dfs_visited, neighbour):
                return True
            dfs_visited[neighbour] = False
    
    return False


def detect_cycle_in_directed_graph(
    n: int,
    edges: List[Tuple[int, int]]
) -> int:
    """
    Detect cycle in directed graph.
    
    Args:
        n: Number of vertices
        edges: List of edges as tuples (u, v)
        
    Returns:
        1 if cycle exists, 0 otherwise
    """
    # Build adjacency list
    adj: List[List[int]] = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
    
    visited = [False] * (n + 1)
    dfs_visited = [False] * (n + 1)
    
    # Check each component
    for i in range(1, n + 1):
        if not visited[i]:
            dfs_visited[i] = True
            if dfs_is_cycle(adj, visited, dfs_visited, i):
                return 1
            dfs_visited[i] = False
    
    return 0

