"""
Kth Smallest Node in BST

Find kth smallest element in BST using inorder traversal.

Time Complexity: O(h + k) where h is height
Space Complexity: O(h) for recursion stack
"""

from typing import Optional, List


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


def kth_smallest(root: Optional[TreeNode], k: List[int]) -> int:
    """
    Find kth smallest element using inorder traversal.
    
    Args:
        root: Root of BST
        k: K value (list to modify) - 1-indexed
        
    Returns:
        Kth smallest value, or -1 if not found
    """
    if root is None:
        return -1
    
    # Left subtree
    left_result = kth_smallest(root.left, k)
    if left_result != -1:
        return left_result
    
    # Current node
    k[0] -= 1
    if k[0] == 0:
        return root.val
    
    # Right subtree
    right_result = kth_smallest(root.right, k)
    if right_result != -1:
        return right_result
    
    return -1

