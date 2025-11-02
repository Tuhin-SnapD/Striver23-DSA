"""
Inorder Traversal

Perform inorder traversal of a binary tree (Left, Root, Right).

Time Complexity: O(n)
Space Complexity: O(n) for recursion stack
"""

from typing import List, Optional


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


def inorder(root: Optional[TreeNode], result: List[int]) -> None:
    """
    Perform inorder traversal recursively.
    
    Args:
        root: Root of binary tree
        result: List to store traversal result
    """
    if root is None:
        return
    
    inorder(root.left, result)  # Traverse left subtree
    result.append(root.val)      # Visit root
    inorder(root.right, result)  # Traverse right subtree


def get_inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Get inorder traversal of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List containing inorder traversal
    """
    result = []
    inorder(root, result)
    return result

