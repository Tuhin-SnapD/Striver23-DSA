"""
Convert Binary Tree To Doubly Linked List

Convert binary tree to doubly linked list using inorder traversal.

Time Complexity: O(n)
Space Complexity: O(n)
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


def inorder(root: Optional[TreeNode], result: List[int]) -> None:
    """Perform inorder traversal."""
    if root is None:
        return
    
    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)


def bt_to_dll(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Convert binary tree to doubly linked list.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Head of doubly linked list
    """
    values = []
    inorder(root, values)
    
    # Create DLL
    head = TreeNode(-1)
    curr = head
    prev = None
    
    for val in values:
        node = TreeNode(val)
        curr.right = node
        curr.left = prev
        prev = curr
        curr = curr.right
    
    curr.right = None
    
    # Update first node's left pointer
    if head.right:
        head.right.left = None
    
    return head.right

