"""
BST Iterator

Implement iterator for BST with next() and hasNext() operations.

Time Complexity:
    - Constructor: O(n) for inorder traversal
    - next(): O(1)
    - hasNext(): O(1)
Space Complexity: O(n)
"""

from typing import Optional, List


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


class BSTIterator:
    """Iterator for BST using inorder traversal."""
    
    def __init__(self, root: Optional[TreeNode]):
        """
        Initialize BST iterator.
        
        Args:
            root: Root of BST
        """
        self.nodes = []
        self.index = 0
        self._inorder(root, self.nodes)
    
    def _inorder(self, root: Optional[TreeNode], result: List[TreeNode]) -> None:
        """Perform inorder traversal."""
        if root is None:
            return
        
        self._inorder(root.left, result)
        result.append(root)
        self._inorder(root.right, result)
    
    def next(self) -> int:
        """
        Get next element in inorder traversal.
        
        Returns:
            Next value in BST
        """
        if self.index < len(self.nodes):
            val = self.nodes[self.index].val
            self.index += 1
            return val
        return -1
    
    def has_next(self) -> bool:
        """
        Check if there are more elements.
        
        Returns:
            True if more elements exist, False otherwise
        """
        return self.index < len(self.nodes)

