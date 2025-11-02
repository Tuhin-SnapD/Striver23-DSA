"""
Is Height Balanced Binary Tree

Check if binary tree is height-balanced (difference in heights of left
and right subtrees <= 1 for all nodes).

Time Complexity: O(n)
Space Complexity: O(n) for recursion stack
"""

from typing import Optional, Tuple


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


def check(root: Optional[TreeNode]) -> Tuple[int, bool]:
    """
    Check if tree is balanced and return height.
    
    Args:
        root: Current node
        
    Returns:
        Tuple of (height, is_balanced)
    """
    if root is None:
        return (0, True)
    
    left_height, left_balanced = check(root.left)
    right_height, right_balanced = check(root.right)
    
    height_diff = abs(left_height - right_height) <= 1
    is_balanced = left_balanced and right_balanced and height_diff
    
    height = 1 + max(left_height, right_height)
    
    return (height, is_balanced)


def is_balanced_bt(root: Optional[TreeNode]) -> bool:
    """
    Check if binary tree is height-balanced.
    
    Args:
        root: Root of binary tree
        
    Returns:
        True if balanced, False otherwise
    """
    _, balanced = check(root)
    return balanced

