"""
Bottom View Of Binary Tree

Find bottommost node at each horizontal distance.

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


def bottom_view(root: Optional[TreeNode]) -> List[int]:
    """
    Get bottom view of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of bottommost nodes at each horizontal distance
    """
    if root is None:
        return []
    
    # Map: horizontal distance -> node value
    distance_map: Dict[int, int] = {}
    queue = deque([(0, root)])
    
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            hd, node = queue.popleft()
            
            # Update map (bottommost node for each hd)
            distance_map[hd] = node.val
            
            if node.left:
                queue.append((hd - 1, node.left))
            if node.right:
                queue.append((hd + 1, node.right))
    
    # Extract values in order of horizontal distance
    result = [distance_map[hd] for hd in sorted(distance_map.keys())]
    return result

