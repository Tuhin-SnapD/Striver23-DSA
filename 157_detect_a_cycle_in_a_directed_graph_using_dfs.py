"""
Clone Graph

Create deep copy of graph with same structure and values.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import Optional, Dict, List


class GraphNode:
    """Definition for graph node."""
    
    def __init__(self, data: int = 0, neighbours: Optional[List['GraphNode']] = None):
        self.data = data
        self.neighbours = neighbours if neighbours is not None else []


node_map: Dict[GraphNode, GraphNode] = {}


def dfs(node: GraphNode) -> None:
    """
    DFS to clone graph nodes.
    
    Args:
        node: Current node to clone
    """
    copy_node = GraphNode(node.data)
    node_map[node] = copy_node
    
    for neighbour in node.neighbours:
        if neighbour in node_map:
            copy_node.neighbours.append(node_map[neighbour])
        else:
            dfs(neighbour)
            copy_node.neighbours.append(node_map[neighbour])


def clone_graph(node: Optional[GraphNode]) -> Optional[GraphNode]:
    """
    Clone graph starting from given node.
    
    Args:
        node: Starting node of graph
        
    Returns:
        Cloned starting node
    """
    if node is None:
        return None
    
    node_map.clear()
    dfs(node)
    return node_map[node]

