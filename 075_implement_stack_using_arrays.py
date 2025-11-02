"""
Stack Implementation Using Array

Implement stack data structure using array.

Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""


class Stack:
    """Stack implementation using array."""
    
    def __init__(self, capacity: int):
        """
        Initialize stack with given capacity.
        
        Args:
            capacity: Maximum size of stack
        """
        self.arr = [0] * capacity
        self.tail = 0
        self.max_size = capacity
    
    def push(self, num: int) -> None:
        """
        Push element onto stack.
        
        Args:
            num: Element to push
        """
        if self.tail != self.max_size:
            self.arr[self.tail] = num
            self.tail += 1
    
    def pop(self) -> int:
        """
        Pop element from stack.
        
        Returns:
            Popped element, or -1 if stack is empty
        """
        if self.tail != 0:
            self.tail -= 1
            return self.arr[self.tail]
        return -1
    
    def top(self) -> int:
        """
        Get top element without removing it.
        
        Returns:
            Top element, or -1 if stack is empty
        """
        return self.arr[self.tail - 1] if self.tail != 0 else -1
    
    def is_empty(self) -> int:
        """
        Check if stack is empty.
        
        Returns:
            1 if empty, 0 otherwise
        """
        return 1 if self.tail == 0 else 0
    
    def is_full(self) -> int:
        """
        Check if stack is full.
        
        Returns:
            1 if full, 0 otherwise
        """
        return 1 if self.tail == self.max_size else 0

