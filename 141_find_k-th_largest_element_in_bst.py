"""
Floor in BST

Find floor value (largest value <= key) in BST.

Time Complexity: O(h) where h is height
Space Complexity: O(h) for recursion stack
"""

from typing import Optional


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


def floor_in_bst(root: Optional[TreeNode], x: int) -> int:
    """
    Find floor value in BST.
    
    Args:
        root: Root of BST
        x: Key to find floor for
        
    Returns:
        Floor value, or -1 if not found
    """
    if root is None:
        return -1
    
    left_floor = floor_in_bst(root.left, x)
    
    # If current node is greater than key, return left result
    if root.val > x:
        return left_floor
    
    # Current node <= key, check right subtree
    right_floor = floor_in_bst(root.right, x)
    
    return max(root.val, right_floor)

