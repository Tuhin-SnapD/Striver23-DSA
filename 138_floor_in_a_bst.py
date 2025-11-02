"""
Convert Sorted Array to BST

Build height-balanced BST from sorted array.

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


def solve(arr: List[int], end: int, start: int) -> Optional[TreeNode]:
    """
    Recursively build BST from sorted array.
    
    Args:
        arr: Sorted array
        end: End index
        start: Start index
        
    Returns:
        Root of constructed BST
    """
    if start > end:
        return None
    
    mid = (start + end) // 2
    root = TreeNode(arr[mid])
    root.left = solve(arr, mid - 1, start)
    root.right = solve(arr, end, mid + 1)
    return root


def sorted_arr_to_bst(arr: List[int], n: int) -> Optional[TreeNode]:
    """
    Convert sorted array to height-balanced BST.
    
    Args:
        arr: Sorted array
        n: Length of array
        
    Returns:
        Root of BST
    """
    return solve(arr, n - 1, 0)

