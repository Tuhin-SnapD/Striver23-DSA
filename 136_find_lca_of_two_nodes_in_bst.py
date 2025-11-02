"""
Diameter Of Binary Tree

Find diameter of binary tree (longest path between any two nodes).

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


def solve(root: Optional[TreeNode], max_diameter: List[int]) -> int:
    """
    Recursive helper to calculate diameter.
    
    Args:
        root: Current node
        max_diameter: List to store maximum diameter found
        
    Returns:
        Height of subtree
    """
    if root is None:
        return 0
    
    left_height = solve(root.left, max_diameter)
    right_height = solve(root.right, max_diameter)
    
    # Diameter passing through current node
    max_diameter[0] = max(max_diameter[0], left_height + right_height)
    
    return max(left_height, right_height) + 1


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Find diameter of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Diameter (longest path length)
    """
    max_diameter = [0]
    solve(root, max_diameter)
    return max_diameter[0]

