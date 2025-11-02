"""
DFS (Depth First Search)

Depth first search traversal of a graph.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List

def dfs(graph: List[List[int]], start: int) -> List[int]:
    """
    DFS traversal starting from start node.
    
    Args:
        graph: Adjacency list representation
        start: Starting vertex
        
    Returns:
        List of vertices in DFS order
    """
    visited = [False] * len(graph)
    result = []
    
    def dfs_helper(node: int) -> None:
        """Recursive DFS helper."""
        visited[node] = True
        result.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs_helper(neighbor)
    
    dfs_helper(start)
    return result
