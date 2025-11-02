"""
Strongly Connected Components (Kosaraju's Algorithm)

Find all strongly connected components in directed graph.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List
from collections import deque


def topological_sort(adj: List[List[int]], s: int, visited: List[bool], stack: deque) -> None:
    """
    Perform topological sort using DFS.
    
    Args:
        adj: Adjacency list
        s: Current vertex
        visited: Visited array
        stack: Stack to store topological order
    """
    visited[s] = True
    for v in adj[s]:
        if not visited[v]:
            topological_sort(adj, v, visited, stack)
    stack.append(s)


def dfs(adj: List[List[int]], s: int, visited: List[bool], ans: List[int]) -> None:
    """
    Perform DFS to find connected component.
    
    Args:
        adj: Adjacency list (transposed)
        s: Current vertex
        visited: Visited array
        ans: List to store component
    """
    visited[s] = True
    ans.append(s)
    for v in adj[s]:
        if not visited[v]:
            dfs(adj, v, visited, ans)


def strongly_connected_components(n: int, edges: List[List[int]]) -> List[List[int]]:
    """
    Find all strongly connected components using Kosaraju's algorithm.
    
    Algorithm:
    1. Topological sort on original graph
    2. Transpose graph
    3. DFS on transposed graph in reverse topological order
    
    Args:
        n: Number of vertices
        edges: List of edges [u, v]
        
    Returns:
        List of strongly connected components
    """
    # Build original graph
    adj1: List[List[int]] = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge
        adj1[u].append(v)
    
    # Step 1: Topological sort
    visited = [False] * n
    stack = deque()
    
    for i in range(n):
        if not visited[i]:
            topological_sort(adj1, i, visited, stack)
    
    # Step 2: Build transposed graph
    adj2: List[List[int]] = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge
        adj2[v].append(u)
    
    # Step 3: DFS on transposed graph
    visited = [False] * n
    result = []
    
    while stack:
        u = stack.pop()
        if not visited[u]:
            component = []
            dfs(adj2, u, visited, component)
            result.append(component)
    
    return result

