"""
Size of Largest BST in Binary Tree

Find size of largest BST subtree in binary tree.

Time Complexity: O(n)
Space Complexity: O(n) for recursion stack
"""

from typing import Optional, Tuple


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


def get_largest_bst(root: Optional[TreeNode]) -> Tuple[int, Tuple[int, int]]:
    """
    Get size and range of largest BST subtree.
    
    Returns: (size, (min_val, max_val))
    If invalid BST, returns (size, (-1, -1))
    
    Args:
        root: Current node
        
    Returns:
        Tuple of (size, (min, max))
    """
    if root is None:
        return (0, (0, 0))
    
    left_result = get_largest_bst(root.left)
    right_result = get_largest_bst(root.right)
    
    # Leaf node
    if left_result[0] == 0 and right_result[0] == 0:
        return (1, (root.val, root.val))
    
    # Only right subtree
    elif left_result[0] == 0:
        if right_result[1][0] == -1:
            return (right_result[0], (-1, -1))
        elif root.val < right_result[1][1]:  # root < min of right
            return (1 + right_result[0], (right_result[1][0], root.val))
        return (right_result[0], (-1, -1))
    
    # Only left subtree
    elif right_result[0] == 0:
        if left_result[1][0] == -1:
            return (left_result[0], (-1, -1))
        elif root.val > left_result[1][0]:  # root > max of left
            return (1 + left_result[0], (root.val, left_result[1][1]))
        return (left_result[0], (-1, -1))
    
    # Both subtrees exist
    if left_result[1][0] == -1 or right_result[1][0] == -1:
        return (max(left_result[0], right_result[0]), (-1, -1))
    
    # Check if valid BST
    if (root.val > left_result[1][0] and  # root > max of left
            root.val < right_result[1][1]):  # root < min of right
        return (left_result[0] + right_result[0] + 1,
                (right_result[1][0], left_result[1][1]))
    
    return (max(left_result[0], right_result[0]), (-1, -1))


def largest_bst(root: Optional[TreeNode]) -> int:
    """
    Find size of largest BST in binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Size of largest BST subtree
    """
    return get_largest_bst(root)[0]

