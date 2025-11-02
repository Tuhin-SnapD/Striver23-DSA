"""
Symmetric Tree

Check if binary tree is symmetric (mirror of itself).

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


def solve(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    """
    Check if two subtrees are symmetric.
    
    Args:
        root1: Root of first subtree
        root2: Root of second subtree
        
    Returns:
        True if symmetric, False otherwise
    """
    if root1 is None and root2 is None:
        return True
    
    if root1 is None or root2 is None:
        return False
    
    if root1.val != root2.val:
        return False
    
    return (solve(root1.left, root2.right) and
            solve(root1.right, root2.left))


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    Check if binary tree is symmetric.
    
    Args:
        root: Root of binary tree
        
    Returns:
        True if symmetric, False otherwise
    """
    if root is None:
        return True
    
    return solve(root.left, root.right)

