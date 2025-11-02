"""
Tree Traversals

Get inorder, preorder, and postorder traversals in single pass using stack.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Optional, Tuple


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


def get_tree_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Get all three traversals (inorder, preorder, postorder) in one pass.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of [inorder, preorder, postorder] traversals
    """
    result = [[], [], []]  # [inorder, preorder, postorder]
    
    if root is None:
        return result
    
    # Stack: (node, state) where state: 1=pre, 2=in, 3=post
    stack = [(root, 1)]
    
    while stack:
        node, state = stack.pop()
        
        if state == 1:
            # Preorder: visit root
            result[1].append(node.val)
            state += 1
            stack.append((node, state))
            
            if node.left:
                stack.append((node.left, 1))
        
        elif state == 2:
            # Inorder: visit root
            result[0].append(node.val)
            state += 1
            stack.append((node, state))
            
            if node.right:
                stack.append((node.right, 1))
        
        else:
            # Postorder: visit root
            result[2].append(node.val)
    
    return result

