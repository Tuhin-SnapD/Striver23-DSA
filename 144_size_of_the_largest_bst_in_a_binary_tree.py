"""
Invert Binary Tree

Invert binary tree such that leaf becomes new root.

Time Complexity: O(n)
Space Complexity: O(n)
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


def helper(
    root: Optional[TreeNode],
    leaf: TreeNode,
    stack: list
) -> bool:
    """
    Helper to find path to leaf and store in stack.
    
    Args:
        root: Current node
        leaf: Target leaf node
        stack: Stack to store path
        
    Returns:
        True if path found, False otherwise
    """
    if root is None:
        return False
    
    stack.append(root)
    
    if root.left is None and root.right is None:
        if root.val == leaf.val:
            return True
        else:
            stack.pop()
            return False
    
    if root.left and helper(root.left, leaf, stack):
        return True
    
    if root.right and helper(root.right, leaf, stack):
        return True
    
    stack.pop()
    return False


def invert_binary_tree(root: Optional[TreeNode], leaf: TreeNode) -> Optional[TreeNode]:
    """
    Invert tree so that leaf becomes new root.
    
    Args:
        root: Root of binary tree
        leaf: Leaf node that should become new root
        
    Returns:
        New root node
    """
    if root is None:
        return None
    
    stack = []
    helper(root, leaf, stack)
    
    new_root = stack.pop()
    parent = new_root
    
    while stack:
        current = stack.pop()
        
        if current.left == parent:
            current.left = None
            parent.left = current
        else:
            current.right = current.left
            current.left = None
            parent.left = current
        
        parent = current
    
    return new_root

