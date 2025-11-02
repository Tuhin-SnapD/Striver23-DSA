"""
Postorder Traversal

Traverse binary tree in postorder (left, right, root).

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Postorder traversal of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of node values in postorder
    """
    result = []
    
    def postorder_helper(node: Optional[TreeNode]) -> None:
        """Recursive helper for postorder traversal."""
        if node is None:
            return
        
        # Visit left, right, then root
        postorder_helper(node.left)
        postorder_helper(node.right)
        result.append(node.val)
    
    postorder_helper(root)
    return result
