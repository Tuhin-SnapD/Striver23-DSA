"""
Delete Node In A BST

Delete a node with given value from binary search tree.

Time Complexity: O(h) where h is height, O(log n) for balanced BST
Space Complexity: O(h) for recursion stack
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


def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """
    Delete node with given key from BST.
    
    Args:
        root: Root of BST
        key: Value to delete
        
    Returns:
        Root of modified BST
    """
    if root is None:
        return None
    
    # Search for the node to delete
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Node to delete found
        # Case 1: Node has no children
        if root.left is None and root.right is None:
            return None
        
        # Case 2: Node has one child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        # Case 3: Node has two children
        # Find inorder successor (smallest in right subtree)
        successor = root.right
        while successor.left is not None:
            successor = successor.left
        
        # Replace node value with successor value
        root.val = successor.val
        
        # Delete the successor
        root.right = delete_node(root.right, successor.val)
    
    return root

