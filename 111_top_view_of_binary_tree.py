"""
Construct Binary Tree from Inorder and Postorder Traversal

Build binary tree from inorder and postorder traversal arrays.

Time Complexity: O(n) with hash map
Space Complexity: O(n)
"""

from typing import List, Optional, Dict


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


def solver(
    inorder: List[int],
    postorder: List[int],
    hash_map: Dict[int, int],
    index: List[int],
    start: int,
    end: int
) -> Optional[TreeNode]:
    """
    Recursive helper to build tree.
    
    Args:
        inorder: Inorder traversal array
        postorder: Postorder traversal array
        hash_map: Map from value to index in inorder
        index: Current index in postorder (list to modify)
        start: Start index in inorder
        end: End index in inorder
        
    Returns:
        Root of constructed subtree
    """
    # Base case
    if start == end:
        root = TreeNode(postorder[index[0]])
        index[0] -= 1
        return root
    
    if start > end or end < 0:
        return None
    
    # Build node from postorder
    root = TreeNode(postorder[index[0]])
    mid = hash_map[postorder[index[0]]]
    index[0] -= 1
    
    # Build right subtree first (postorder: left, right, root)
    root.right = solver(inorder, postorder, hash_map, index, mid + 1, end)
    
    # Build left subtree
    root.left = solver(inorder, postorder, hash_map, index, start, mid - 1)
    
    return root


def build_binary_tree(
    inorder: List[int],
    postorder: List[int]
) -> Optional[TreeNode]:
    """
    Build binary tree from inorder and postorder traversals.
    
    Args:
        inorder: Inorder traversal array
        postorder: Postorder traversal array
        
    Returns:
        Root of constructed binary tree
    """
    n = len(postorder)
    hash_map = {inorder[i]: i for i in range(n)}
    index = [n - 1]  # Start from last element in postorder
    
    return solver(inorder, postorder, hash_map, index, 0, n - 1)

