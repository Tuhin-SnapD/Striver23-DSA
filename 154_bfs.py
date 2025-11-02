"""
BFS (Breadth First Search)

Breadth first search traversal of a graph.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List
from collections import deque

def bfs(graph: List[List[int]], start: int) -> List[int]:
    """
    BFS traversal starting from start node.
    
    Args:
        graph: Adjacency list representation
        start: Starting vertex
        
    Returns:
        List of vertices in BFS order
    """
    if not graph or start >= len(graph):
        return []
    
    visited = [False] * len(graph)
    queue = deque([start])
    result = []
    
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result
