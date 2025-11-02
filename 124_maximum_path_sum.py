"""
Maximum Path Sum Between Two Leaves

Find maximum path sum between any two leaf nodes in binary tree.

Time Complexity: O(n)
Space Complexity: O(n) for recursion stack
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


def dfs(root: Optional[TreeNode], max_sum: List[int]) -> int:
    """
    DFS to calculate maximum path sum.
    
    Args:
        root: Current node
        max_sum: List to store maximum sum found
        
    Returns:
        Maximum path sum from this node to a leaf
    """
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return root.val
    
    left_sum = dfs(root.left, max_sum)
    right_sum = dfs(root.right, max_sum)
    
    # Update maximum path sum through current node
    max_sum[0] = max(max_sum[0], left_sum + right_sum + root.val)
    
    return root.val + max(left_sum, right_sum)


def find_max_sum_path(root: Optional[TreeNode]) -> int:
    """
    Find maximum path sum between two leaves.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Maximum path sum, or -1 if tree has less than 2 leaves
    """
    if root is None:
        return -1
    
    if root.left is None and root.right is None:
        return -1
    
    if root.left is None or root.right is None:
        return -1
    
    max_sum = [0]
    dfs(root, max_sum)
    return max_sum[0]

