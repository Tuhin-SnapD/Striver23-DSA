"""
Path In A Tree

Find path from root to given node in binary tree.

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


def solve(root: Optional[TreeNode], x: int, result: List[int]) -> None:
    """
    Recursive helper to find path to node.
    
    Args:
        root: Current node
        x: Target value
        result: Path list (modified in-place)
    """
    if root is None:
        return
    
    # Found target
    if root.val == x:
        result.append(root.val)
        return
    
    result.append(root.val)
    
    # Search in left and right subtrees
    solve(root.left, x, result)
    solve(root.right, x, result)
    
    # Backtrack if not found in this path
    if result[-1] != x:
        result.pop()


def path_in_tree(root: Optional[TreeNode], x: int) -> List[int]:
    """
    Find path from root to node with value x.
    
    Args:
        root: Root of binary tree
        x: Target value
        
    Returns:
        Path from root to target node
    """
    result = []
    solve(root, x, result)
    return result

