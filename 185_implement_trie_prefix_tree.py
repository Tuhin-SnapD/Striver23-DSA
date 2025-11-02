"""
Serialize and Deserialize Binary Tree

Convert binary tree to string and reconstruct from string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional


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


def serialize_tree(root: Optional[TreeNode]) -> str:
    """
    Serialize binary tree to string (preorder with # for None).
    
    Args:
        root: Root of binary tree
        
    Returns:
        Serialized string
    """
    if root is None:
        return "#"
    
    result = str(root.val) + ","
    left_str = serialize_tree(root.left)
    right_str = serialize_tree(root.right)
    
    return result + left_str + right_str


def helper(serialized: str, index: List[int]) -> Optional[TreeNode]:
    """
    Helper to deserialize tree.
    
    Args:
        serialized: Serialized string
        index: Current index (list to modify)
        
    Returns:
        Root of deserialized tree
    """
    if index[0] >= len(serialized) or serialized[index[0]] == '#':
        index[0] += 1
        return None
    
    # Parse number
    num = 0
    while (index[0] < len(serialized) and
           serialized[index[0]].isdigit()):
        num = num * 10 + int(serialized[index[0]])
        index[0] += 1
    
    root = TreeNode(num)
    index[0] += 1  # Skip comma
    
    root.left = helper(serialized, index)
    root.right = helper(serialized, index)
    
    return root


def deserialize_tree(serialized: str) -> Optional[TreeNode]:
    """
    Deserialize string to binary tree.
    
    Args:
        serialized: Serialized string
        
    Returns:
        Root of binary tree
    """
    index = [0]
    return helper(serialized, index)

