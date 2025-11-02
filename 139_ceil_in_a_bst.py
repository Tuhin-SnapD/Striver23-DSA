"""
Ceil from BST

Find ceil value (smallest value >= key) in BST using Morris traversal.

Time Complexity: O(n)
Space Complexity: O(1)
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


def find_ceil(root: Optional[TreeNode], x: int) -> int:
    """
    Find ceil value using Morris traversal.
    
    Args:
        root: Root of BST
        x: Key to find ceil for
        
    Returns:
        Ceil value, or -1 if not found
    """
    ans = -1
    found = False
    curr = root
    
    while curr is not None:
        if curr.left is None:
            if curr.val >= x and not found:
                ans = curr.val
                found = True
            curr = curr.right
        else:
            # Find inorder predecessor
            pred = curr.left
            while pred.right is not None and pred.right != curr:
                pred = pred.right
            
            if pred.right is None:
                pred.right = curr
                curr = curr.left
            else:
                if curr.val >= x and not found:
                    ans = curr.val
                    found = True
                pred.right = None
                curr = curr.right
    
    return ans

