"""
Construct BST from Preorder Traversal

Build BST from preorder traversal using bounds.

Time Complexity: O(n)
Space Complexity: O(n) for recursion stack
"""

from typing import List, Optional
import sys


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


def solve(
    preorder: List[int],
    index: List[int],
    bound: int,
    n: int
) -> Optional[TreeNode]:
    """
    Recursively build BST from preorder.
    
    Args:
        preorder: Preorder traversal array
        index: Current index (list to modify)
        bound: Upper bound for current subtree
        n: Length of array
        
    Returns:
        Root of constructed BST
    """
    if index[0] >= n or preorder[index[0]] > bound:
        return None
    
    root = TreeNode(preorder[index[0]])
    index[0] += 1
    
    root.left = solve(preorder, index, root.val, n)
    root.right = solve(preorder, index, bound, n)
    
    return root


def preorder_tree(preorder: List[int]) -> Optional[TreeNode]:
    """
    Build BST from preorder traversal.
    
    Args:
        preorder: Preorder traversal array
        
    Returns:
        Root of constructed BST
    """
    index = [0]
    n = len(preorder)
    return solve(preorder, index, sys.maxsize, n)

