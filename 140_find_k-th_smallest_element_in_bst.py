"""
Partial BST (Validate BST)

Check if binary tree is a valid BST.

Time Complexity: O(n)
Space Complexity: O(n)
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
    """Perform inorder traversal."""
    if root is None:
        return
    
    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)


def validate_bst(root: Optional[TreeNode]) -> bool:
    """
    Validate if tree is a BST using inorder traversal.
    
    BST inorder traversal is always sorted.
    
    Args:
        root: Root of binary tree
        
    Returns:
        True if valid BST, False otherwise
    """
    result = []
    inorder(root, result)
    
    # Check if sorted
    for i in range(1, len(result)):
        if result[i] <= result[i - 1]:
            return False
    
    return True

