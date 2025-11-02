"""
Prim's MST

Find minimum spanning tree using Prim's algorithm.

Time Complexity: O(V^2) for dense graphs
Space Complexity: O(V + E)
"""

from typing import List, Tuple, Dict
import sys


def calculate_prims_mst(
    n: int,
    m: int,
    g: List[Tuple[Tuple[int, int], int]]
) -> List[Tuple[Tuple[int, int], int]]:
    """
    Find MST using Prim's algorithm.
    
    Args:
        n: Number of vertices
        m: Number of edges
        g: List of edges as ((u, v), weight)
        
    Returns:
        List of MST edges as ((u, v), weight)
    """
    # Build adjacency list
    adj: Dict[int, List[Tuple[int, int]]] = {}
    for edge in g:
        u, v = edge[0]
        w = edge[1]
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Initialize arrays
    key = [sys.maxsize] * (n + 1)
    mst = [False] * (n + 1)
    parent = [-1] * (n + 1)
    
    # Start from vertex 1
    key[1] = 0
    parent[1] = -1
    
    # Build MST
    for _ in range(n - 1):
        # Find minimum key vertex not in MST
        min_key = sys.maxsize
        curr = -1
        
        for i in range(1, n + 1):
            if not mst[i] and key[i] < min_key:
                min_key = key[i]
                curr = i
        
        # Add to MST
        mst[curr] = True
        
        # Update keys of adjacent vertices
        if curr in adj:
            for neighbour, weight in adj[curr]:
                if not mst[neighbour] and weight < key[neighbour]:
                    parent[neighbour] = curr
                    key[neighbour] = weight
    
    # Build result
    result = []
    for i in range(2, n + 1):
        result.append(((parent[i], i), key[i]))
    
    return result

