"""
LCA Of Binary Tree

Find lowest common ancestor of two nodes in binary tree.

Time Complexity: O(n)
Space Complexity: O(n) for recursion stack
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


def lowest_common_ancestor(root: Optional[TreeNode], x: int, y: int) -> int:
    """
    Find lowest common ancestor of nodes with values x and y.
    
    Args:
        root: Root of binary tree
        x: Value of first node
        y: Value of second node
        
    Returns:
        Value of LCA, or -1 if not found
    """
    if root is None:
        return -1
    
    if root.val == x or root.val == y:
        return root.val
    
    left_result = lowest_common_ancestor(root.left, x, y)
    right_result = lowest_common_ancestor(root.right, x, y)
    
    if left_result != -1 and right_result != -1:
        # Current node is LCA
        return root.val
    elif left_result != -1:
        return left_result
    elif right_result != -1:
        return right_result
    else:
        return -1

