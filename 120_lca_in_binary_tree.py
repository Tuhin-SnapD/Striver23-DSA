"""
Maximum Width In Binary Tree

Find maximum width (number of nodes) at any level of binary tree.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional
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


def get_max_width(root: Optional[TreeNode]) -> int:
    """
    Find maximum width using level order traversal.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Maximum width (number of nodes at widest level)
    """
    if not root:
        return 0
    
    max_width = 0
    count = 0
    queue = deque([root, None])
    
    while queue:
        node = queue.popleft()
        
        if node is None:
            max_width = max(max_width, count)
            if len(queue) == 0:
                break
            queue.append(None)
            count = 0
            continue
        
        count += 1
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return max_width

