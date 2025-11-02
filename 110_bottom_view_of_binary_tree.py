"""
Boundary Traversal of Binary Tree

Traverse boundary of binary tree in anti-clockwise direction:
left boundary, leaves, right boundary (reverse).

Time Complexity: O(n)
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


def is_leaf(root: Optional[TreeNode]) -> bool:
    """Check if node is leaf."""
    if root is None:
        return False
    return root.left is None and root.right is None


def left_boundary(root: Optional[TreeNode], result: List[int]) -> None:
    """Add left boundary nodes."""
    if root is None or is_leaf(root):
        return
    
    result.append(root.val)
    if root.left:
        left_boundary(root.left, result)
    else:
        left_boundary(root.right, result)


def leaves(root: Optional[TreeNode], result: List[int]) -> None:
    """Add leaf nodes."""
    if root is None:
        return
    
    if is_leaf(root):
        result.append(root.val)
        return
    
    leaves(root.left, result)
    leaves(root.right, result)


def right_boundary(root: Optional[TreeNode], result: List[int]) -> None:
    """Add right boundary nodes in reverse."""
    if root is None or is_leaf(root):
        return
    
    temp = []
    node = root
    while node:
        if not is_leaf(node):
            temp.append(node.val)
        if node.right:
            node = node.right
        else:
            node = node.left
    
    # Add in reverse order
    result.extend(reversed(temp))


def traverse_boundary(root: Optional[TreeNode]) -> List[int]:
    """
    Traverse boundary of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of boundary nodes in anti-clockwise order
    """
    if root is None:
        return []
    
    result = []
    
    if not is_leaf(root):
        result.append(root.val)
    
    left_boundary(root.left, result)
    leaves(root, result)
    right_boundary(root.right, result)
    
    return result

