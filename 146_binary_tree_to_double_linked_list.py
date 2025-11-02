"""
Top View Of Binary Tree

Find topmost node at each horizontal distance.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Optional, Dict
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


def get_top_view(root: Optional[TreeNode]) -> List[int]:
    """
    Get top view of binary tree using level order traversal.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of topmost nodes at each horizontal distance
    """
    if root is None:
        return []
    
    distance_map: Dict[int, int] = {}
    queue = deque([(root, 0)])
    
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node, hd = queue.popleft()
            
            # Only add first node at each horizontal distance
            if hd not in distance_map:
                distance_map[hd] = node.val
            
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
    
    # Extract values in order of horizontal distance
    result = [distance_map[hd] for hd in sorted(distance_map.keys())]
    return result

