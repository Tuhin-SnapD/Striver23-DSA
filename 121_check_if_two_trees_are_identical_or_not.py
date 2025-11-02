"""
Check Identical Trees

Check if two binary trees are identical (same structure and values).

Time Complexity: O(n) where n is number of nodes
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


def identical_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    """
    Check if two trees are identical.
    
    Args:
        root1: Root of first tree
        root2: Root of second tree
        
    Returns:
        True if identical, False otherwise
    """
    if root1 is None or root2 is None:
        return root1 is None and root2 is None
    
    if root1.val != root2.val:
        return False
    
    return (identical_trees(root1.left, root2.left) and
            identical_trees(root1.right, root2.right))

