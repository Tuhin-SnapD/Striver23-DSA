"""
Morris Inorder Traversal

Inorder traversal using Morris algorithm (without stack/recursion).

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def morris_inorder(root: Optional[TreeNode]) -> List[int]:
    """
    Morris inorder traversal.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of node values in inorder
    """
    result = []
    current = root
    
    while current:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right
    
    return result
