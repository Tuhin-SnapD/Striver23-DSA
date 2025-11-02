"""
Binary Tree Zigzag Traversal

Traverse binary tree in zigzag order (alternate left-to-right and right-to-left).

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Optional
from collections import deque


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


def zigzag_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Traverse binary tree in zigzag order.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of node values in zigzag order
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level = [0] * level_size
        
        for i in range(level_size):
            node = queue.popleft()
            
            # Fill level array based on direction
            index = i if left_to_right else level_size - 1 - i
            level[index] = node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.extend(level)
        left_to_right = not left_to_right
    
    return result

