"""
Search In BST

Search for a value in binary search tree.

Time Complexity: O(h) where h is height, O(log n) for balanced BST
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


def search_in_bst(root: Optional[TreeNode], x: int) -> bool:
    """
    Search for value x in BST.
    
    Args:
        root: Root of BST
        x: Value to search
        
    Returns:
        True if found, False otherwise
    """
    if root is None:
        return False
    
    if root.val == x:
        return True
    elif root.val > x:
        return search_in_bst(root.left, x)
    else:
        return search_in_bst(root.right, x)

