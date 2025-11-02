"""
Level Order Traversal

Traverse binary tree level by level from top to bottom.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    """Definition for binary tree node."""
    
    def __init__(
        self,
        val: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None
    ):
        self.val = val
        self.left = left
        self.right = right


def get_level_order(root: Optional[TreeNode]) -> List[int]:
    """
    Get level order traversal (BFS) of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of node values in level order
    """
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

