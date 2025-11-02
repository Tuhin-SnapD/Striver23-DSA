"""
Flatten Binary Tree to Linked List

Flatten binary tree to linked list in-place (preorder).

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


def flatten_bt(root: Optional[TreeNode], next_node: List[Optional[TreeNode]]) -> None:
    """
    Recursively flatten binary tree.
    
    Args:
        root: Current node
        next_node: List containing next node in flattened list
    """
    if root is None:
        return
    
    # Process right subtree first
    flatten_bt(root.right, next_node)
    # Process left subtree
    flatten_bt(root.left, next_node)
    
    # Update pointers
    root.left = None
    root.right = next_node[0]
    next_node[0] = root


def flatten_binary_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Flatten binary tree to linked list (preorder).
    
    Args:
        root: Root of binary tree
        
    Returns:
        Root of flattened tree (same as input root)
    """
    next_node = [None]
    flatten_bt(root, next_node)
    return root

