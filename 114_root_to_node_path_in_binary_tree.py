"""
Left View Of Binary Tree

Find leftmost node at each level of binary tree.

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


def get_left_view(root: Optional[TreeNode]) -> List[int]:
    """
    Get left view of binary tree using level order traversal.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of leftmost nodes at each level
    """
    if root is None:
        return []
    
    result = []
    queue = deque([root, None])
    result.append(root.val)
    
    while queue:
        node = queue.popleft()
        
        if node is None:
            if queue:
                queue.append(None)
                result.append(queue[0].val)
        else:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

