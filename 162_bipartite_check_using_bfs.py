"""
Bipartite Check Using BFS

Check if graph is bipartite using BFS.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List

def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Check if graph is bipartite.
    
    Args:
        graph: Adjacency list representation
        
    Returns:
        True if bipartite, False otherwise
    """
    from collections import deque
    
    n = len(graph)
    color = [-1] * n
    
    # BFS for each connected component
    for start in range(n):
        if color[start] != -1:
            continue
        
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
    
    return True
