"""
Preorder Inorder Postorder in a Single Traversal

Traverse binary tree in all three orders simultaneously.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def all_traversals(root: Optional[TreeNode]) -> Tuple[List[int], List[int], List[int]]:
    """
    Get preorder, inorder, and postorder in one traversal.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Tuple of (preorder, inorder, postorder) lists
    """
    preorder, inorder, postorder = [], [], []
    stack = []
    
    if root is None:
        return preorder, inorder, postorder
    
    stack.append((root, 1))
    
    while stack:
        node, num = stack.pop()
        
        if num == 1:
            preorder.append(node.val)
            stack.append((node, 2))
            if node.left:
                stack.append((node.left, 1))
        
        elif num == 2:
            inorder.append(node.val)
            stack.append((node, 3))
            if node.right:
                stack.append((node.right, 1))
        
        else:
            postorder.append(node.val)
    
    return preorder, inorder, postorder
