"""
BFS in Graph

Perform BFS traversal on graph (may be disconnected).

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List, Set, Tuple
from collections import deque


def bfs(vertex: int, edges: List[Tuple[int, int]]) -> List[int]:
    """
    Perform BFS traversal on graph.
    
    Args:
        vertex: Number of vertices
        edges: List of edges as tuples (u, v)
        
    Returns:
        BFS traversal order
    """
    # Build adjacency list using sets for sorted neighbors
    adj: List[Set[int]] = [set() for _ in range(vertex)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    visited = [False] * vertex
    bfs_order = []
    
    # Process each component
    for i in range(vertex):
        if not visited[i]:
            queue = deque([i])
            
            while queue:
                curr = queue.popleft()
                
                if visited[curr]:
                    continue
                
                visited[curr] = True
                bfs_order.append(curr)
                
                # Visit neighbors in sorted order
                for neighbour in sorted(adj[curr]):
                    if not visited[neighbour]:
                        queue.append(neighbour)
    
    return bfs_order

