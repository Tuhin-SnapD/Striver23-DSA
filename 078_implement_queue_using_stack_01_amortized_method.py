"""
Stack Using Queue

Implement stack using a single queue.

Time Complexity: O(n) for push, O(1) for pop
Space Complexity: O(n)
"""

from collections import deque


class Stack:
    """Stack implementation using a single queue."""
    
    def __init__(self):
        """Initialize empty stack."""
        self.queue = deque()
    
    def get_size(self) -> int:
        """
        Get size of stack.
        
        Returns:
            Number of elements in stack
        """
        return len(self.queue)
    
    def is_empty(self) -> bool:
        """
        Check if stack is empty.
        
        Returns:
            True if empty, False otherwise
        """
        return len(self.queue) == 0
    
    def push(self, element: int) -> None:
        """
        Push element onto stack.
        
        Args:
            element: Element to push
        """
        self.queue.append(element)
        # Rotate queue to maintain stack order
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self) -> int:
        """
        Pop element from stack.
        
        Returns:
            Top element, or -1 if empty
        """
        if not self.is_empty():
            return self.queue.popleft()
        return -1
    
    def top(self) -> int:
        """
        Get top element without removing.
        
        Returns:
            Top element, or -1 if empty
        """
        if not self.is_empty():
            return self.queue[0]
        return -1

