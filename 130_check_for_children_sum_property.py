"""
Children Sum Property

Ensure node value equals sum of its children's values.

Time Complexity: O(n)
Space Complexity: O(n) for recursion stack
"""

from typing import Optional
import sys


max_val = [-sys.maxsize - 1]


def dfs(root: Optional['TreeNode']) -> None:
    """Find maximum value in tree."""
    if root is None or root.val == -1:
        return
    
    max_val[0] = max(max_val[0], root.val)
    dfs(root.right)
    dfs(root.left)


def edit(root: Optional['TreeNode']) -> int:
    """
    Edit tree to satisfy children sum property.
    
    Args:
        root: Current node
        
    Returns:
        Updated value of node
    """
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        root.val = max_val[0]
        return max_val[0]
    
    root.val = edit(root.right) + edit(root.left)
    return root.val


def change_tree(root: Optional['TreeNode']) -> None:
    """
    Change tree to satisfy children sum property.
    
    Args:
        root: Root of binary tree
    """
    dfs(root)
    edit(root)

