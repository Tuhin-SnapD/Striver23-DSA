"""
MST Using Kruskal's Algorithm

Find minimum spanning tree using Kruskal's algorithm.

Time Complexity: O(E log E)
Space Complexity: O(V)
"""

from typing import List


class DisjointSet:
    """Union-Find data structure with union by size."""
    
    def __init__(self, n: int):
        """
        Initialize disjoint set.
        
        Args:
            n: Number of elements
        """
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, node: int) -> int:
        """
        Find root with path compression.
        
        Args:
            node: Node to find root for
            
        Returns:
            Root of the set
        """
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]
    
    def union_by_size(self, u: int, v: int) -> None:
        """
        Union two sets by size.
        
        Args:
            u: First element
            v: Second element
        """
        pu = self.find(u)
        pv = self.find(v)
        
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]


def kruskal_mst(n: int, m: int, graph: List[List[int]]) -> int:
    """
    Find MST using Kruskal's algorithm.
    
    Algorithm:
    1. Sort edges by weight
    2. Process edges in order, add if doesn't form cycle
    3. Use Union-Find to detect cycles
    
    Args:
        n: Number of vertices
        m: Number of edges
        graph: List of edges [u, v, weight]
        
    Returns:
        Sum of weights in MST
    """
    # Build edge list with weights
    edges = []
    for edge in graph:
        u, v, wt = edge
        edges.append((wt, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # Initialize disjoint set
    ds = DisjointSet(n)
    mst_sum = 0
    
    # Process edges
    for wt, u, v in edges:
        if ds.find(u) != ds.find(v):
            mst_sum += wt
            ds.union_by_size(u, v)
    
    return mst_sum

