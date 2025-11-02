"""
Postorder Traversal

Perform postorder traversal of binary tree (Left, Right, Root).

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


def postorder(root: Optional[TreeNode], result: List[int]) -> None:
    """
    Perform postorder traversal recursively.
    
    Args:
        root: Root of binary tree
        result: List to store traversal result
    """
    if root is None:
        return
    
    postorder(root.left, result)   # Traverse left subtree
    postorder(root.right, result)  # Traverse right subtree
    result.append(root.val)        # Visit root


def get_postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Get postorder traversal of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List containing postorder traversal
    """
    result = []
    postorder(root, result)
    return result

