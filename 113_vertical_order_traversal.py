"""
Vertical Order Traversal

Traverse binary tree in vertical order.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List, Optional, Dict
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Vertical order traversal.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of lists, each containing nodes at same vertical level
    """
    if root is None:
        return []
    
    # Dictionary to store nodes by their vertical level
    vertical_map: Dict[int, List[int]] = defaultdict(list)
    
    # DFS to assign vertical levels
    def dfs(node: Optional[TreeNode], level: int) -> None:
        if node is None:
            return
        
        vertical_map[level].append(node.val)
        dfs(node.left, level - 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    
    # Sort by level and return
    return [vertical_map[key] for key in sorted(vertical_map.keys())]
