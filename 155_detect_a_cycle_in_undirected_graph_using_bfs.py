"""
Cycle Detection In Undirected Graph

Detect cycle in undirected graph using BFS.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List, Tuple
from collections import deque


def bfs_cycle_check(
    adj: List[List[int]],
    visited: List[int],
    node: int
) -> bool:
    """
    Check for cycle using BFS.
    
    Args:
        adj: Adjacency list
        visited: Visited array
        node: Starting node
        
    Returns:
        True if cycle found, False otherwise
    """
    queue = deque([(node, -1)])
    visited[node] = 1
    
    while queue:
        curr, parent = queue.popleft()
        
        for neighbour in adj[curr]:
            if not visited[neighbour]:
                visited[neighbour] = 1
                queue.append((neighbour, curr))
            elif neighbour != parent:
                # Back edge to non-parent node indicates cycle
                return True
    
    return False


def cycle_detection(edges: List[List[int]], n: int, m: int) -> str:
    """
    Detect cycle in undirected graph.
    
    Args:
        edges: List of edges [u, v]
        n: Number of vertices
        m: Number of edges
        
    Returns:
        "Yes" if cycle exists, "No" otherwise
    """
    # Build adjacency list
    adj: List[List[int]] = [[] for _ in range(n + 1)]
    for edge in edges:
        u, v = edge
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [0] * (n + 1)
    
    # Check each component
    for i in range(1, n + 1):
        if not visited[i]:
            if bfs_cycle_check(adj, visited, i):
                return "Yes"
    
    return "No"

