"""
Vertical Order Traversal

Traverse binary tree vertically (from top to bottom for each horizontal distance).

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List, Optional, Dict, Tuple
from collections import deque, defaultdict


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


def vertical_order_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Get vertical order traversal of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of nodes in vertical order
    """
    if root is None:
        return []
    
    # Map: vertical -> {level -> [nodes]}
    vertical_map: Dict[int, Dict[int, List[int]]] = defaultdict(
        lambda: defaultdict(list)
    )
    
    queue = deque([(root, 0, 0)])  # (node, vertical, level)
    
    while queue:
        node, v, h = queue.popleft()
        vertical_map[v][h].append(node.val)
        
        if node.left:
            queue.append((node.left, v - 1, h + 1))
        if node.right:
            queue.append((node.right, v + 1, h + 1))
    
    # Extract nodes in vertical order
    result = []
    for v in sorted(vertical_map.keys()):
        for h in sorted(vertical_map[v].keys()):
            result.extend(vertical_map[v][h])
    
    return result

