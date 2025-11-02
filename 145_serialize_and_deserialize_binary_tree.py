"""
K-th Largest Number BST

Find kth largest element in BST.

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


def inorder_helper(root: Optional[TreeNode], result: List[int]) -> None:
    """Perform inorder traversal to get sorted values."""
    if root is None:
        return
    
    inorder_helper(root.left, result)
    result.append(root.val)
    inorder_helper(root.right, result)


def kth_largest_number(root: Optional[TreeNode], k: int) -> int:
    """
    Find kth largest element in BST.
    
    Args:
        root: Root of BST
        k: Kth position (1-indexed)
        
    Returns:
        Kth largest value, or -1 if k > number of nodes
    """
    result = []
    inorder_helper(root, result)
    n = len(result)
    
    if k > n:
        return -1
    
    # Kth largest = (n-k)th element from start
    return result[n - k]

