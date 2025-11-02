"""
Height of Binary Tree From Inorder and Level Order Traversal

Find height of binary tree given inorder and level order traversals.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List
from collections import deque


class Temp:
    """Temporary class to store subtree information."""
    
    def __init__(self, height: int, left_index: int, right_index: int):
        self.height = height
        self.left_index = left_index
        self.right_index = right_index


def height_of_tree(inorder: List[int], level_order: List[int], n: int) -> int:
    """
    Find height of tree using inorder and level order.
    
    Args:
        inorder: Inorder traversal
        level_order: Level order traversal
        n: Number of nodes
        
    Returns:
        Height of tree
    """
    if n == 0:
        return 0
    
    queue = deque()
    queue.append(Temp(0, 0, n - 1))
    
    # Map value to index in inorder
    value_to_index = {inorder[i]: i for i in range(n)}
    
    max_height = 0
    
    for i in range(n):
        temp = queue.popleft()
        max_height = max(max_height, temp.height)
        
        root_val = level_order[i]
        root_index = value_to_index[root_val]
        
        # Add left subtree if exists
        if root_index - 1 >= temp.left_index:
            queue.append(Temp(
                temp.height + 1,
                temp.left_index,
                root_index - 1
            ))
        
        # Add right subtree if exists
        if root_index + 1 <= temp.right_index:
            queue.append(Temp(
                temp.height + 1,
                root_index + 1,
                temp.right_index
            ))
    
    return max_height

