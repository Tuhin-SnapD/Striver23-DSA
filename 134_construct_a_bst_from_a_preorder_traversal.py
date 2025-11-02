"""
Construct Binary Tree From Inorder and Preorder Traversal

Build binary tree from inorder and preorder traversal arrays.

Time Complexity: O(n^2) worst case, O(n log n) average
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


def find_pos(inorder: List[int], element: int, n: int) -> int:
    """Find position of element in inorder array."""
    for i in range(n):
        if inorder[i] == element:
            return i
    return -1


def solve(
    inorder: List[int],
    preorder: List[int],
    index: List[int],
    inorder_start: int,
    inorder_end: int,
    n: int
) -> Optional[TreeNode]:
    """
    Recursive helper to build tree.
    
    Args:
        inorder: Inorder traversal array
        preorder: Preorder traversal array
        index: Current index in preorder (list to modify)
        inorder_start: Start index in inorder
        inorder_end: End index in inorder
        n: Total number of nodes
        
    Returns:
        Root of constructed subtree
    """
    if index[0] >= n or inorder_start > inorder_end:
        return None
    
    element = preorder[index[0]]
    index[0] += 1
    root = TreeNode(element)
    pos = find_pos(inorder, element, n)
    
    root.left = solve(
        inorder, preorder, index,
        inorder_start, pos - 1, n
    )
    root.right = solve(
        inorder, preorder, index,
        pos + 1, inorder_end, n
    )
    
    return root


def build_binary_tree(inorder: List[int], preorder: List[int]) -> Optional[TreeNode]:
    """
    Build binary tree from inorder and preorder traversals.
    
    Args:
        inorder: Inorder traversal array
        preorder: Preorder traversal array
        
    Returns:
        Root of constructed binary tree
    """
    n = len(preorder)
    preorder_index = [0]
    return solve(inorder, preorder, preorder_index, 0, n - 1, n)

