"""
Check Bipartite Graph

Check if graph is bipartite (can be colored with 2 colors).

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List


def dfs(
    node: int,
    adj: List[List[int]],
    color: List[int]
) -> bool:
    """
    DFS to check bipartite property.
    
    Args:
        node: Current node
        adj: Adjacency list
        color: Color array (-1 = uncolored, 0/1 = colors)
        
    Returns:
        True if bipartite, False otherwise
    """
    for neighbour in adj[node]:
        if color[neighbour] == -1:
            color[neighbour] = 1 - color[node]
            if not dfs(neighbour, adj, color):
                return False
        elif color[neighbour] == color[node]:
            return False
    
    return True


def is_graph_bipartite(edges: List[List[int]]) -> bool:
    """
    Check if graph is bipartite.
    
    Args:
        edges: Adjacency matrix
        
    Returns:
        True if bipartite, False otherwise
    """
    n = len(edges)
    
    # Build adjacency list
    adj: List[List[int]] = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if edges[i][j] == 1:
                adj[i].append(j)
                adj[j].append(i)
    
    color = [-1] * n
    
    # Check each component
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            if not dfs(i, adj, color):
                return False
    
    return True

