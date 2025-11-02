"""
Predecessor And Successor In BST

Find inorder predecessor and successor of a key in BST.

Time Complexity: O(h) where h is height
Space Complexity: O(1)
"""

from typing import Optional, Tuple


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


def predecessor_successor(root: Optional[TreeNode], key: int) -> Tuple[int, int]:
    """
    Find predecessor and successor of key in BST.
    
    Args:
        root: Root of BST
        key: Key to find predecessor and successor for
        
    Returns:
        Tuple of (predecessor, successor), -1 if not found
    """
    pred = -1
    succ = -1
    curr = root
    
    # Find key and track pred/succ during search
    while curr is not None:
        if curr.val == key:
            break
        elif curr.val > key:
            succ = curr.val
            curr = curr.left
        else:
            pred = curr.val
            curr = curr.right
    
    # Find predecessor (rightmost in left subtree)
    if curr is not None:
        temp = curr.left
        while temp is not None:
            pred = temp.val
            temp = temp.right
    
    # Find successor (leftmost in right subtree)
    if curr is not None:
        temp = curr.right
        while temp is not None:
            succ = temp.val
            temp = temp.left
    
    return (pred, succ)

