"""
Clone a Graph

Create a deep copy of an undirected graph.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: Optional['Node']) -> Optional['Node']:
    """
    Clone the graph.
    
    Args:
        node: Reference to a node in the graph
        
    Returns:
        Clone of the graph
    """
    if node is None:
        return None
    
    # Dictionary to map old nodes to new nodes
    cloned = {}
    
    # DFS to clone nodes
    def dfs(original: Optional['Node']) -> Optional['Node']:
        if original is None:
            return None
        
        if original in cloned:
            return cloned[original]
        
        # Create new node
        copy = Node(original.val)
        cloned[original] = copy
        
        # Clone neighbors
        for neighbor in original.neighbors:
            copy.neighbors.append(dfs(neighbor))
        
        return copy
    
    return dfs(node)
