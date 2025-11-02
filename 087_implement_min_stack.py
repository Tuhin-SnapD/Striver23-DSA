"""
Min Stack

Implement stack with O(1) min operation using encoding technique.

Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""


class MinStack:
    """Stack with constant time minimum retrieval."""
    
    def __init__(self):
        """Initialize empty stack."""
        self.stack = []
        self.min_val = None
    
    def push(self, num: int) -> None:
        """
        Push element onto stack.
        
        Args:
            num: Element to push
        """
        if not self.stack:
            self.min_val = num
            self.stack.append(num)
        else:
            if self.min_val <= num:
                self.stack.append(num)
            else:
                # Encode: store modified value
                encoded = 2 * num - self.min_val
                self.min_val = num
                self.stack.append(encoded)
    
    def pop(self) -> int:
        """
        Pop element from stack.
        
        Returns:
            Popped element, or -1 if empty
        """
        if not self.stack:
            return -1
        
        data = self.stack.pop()
        
        if data >= self.min_val:
            return data
        else:
            # Decode: retrieve original minimum
            prev_min = self.min_val
            self.min_val = 2 * self.min_val - data
            return prev_min
    
    def top(self) -> int:
        """
        Get top element without removing.
        
        Returns:
            Top element, or -1 if empty
        """
        if not self.stack:
            return -1
        
        data = self.stack[-1]
        if data >= self.min_val:
            return data
        else:
            return self.min_val
    
    def get_min(self) -> int:
        """
        Get minimum element.
        
        Returns:
            Minimum element, or -1 if empty
        """
        if not self.stack:
            return -1
        return self.min_val

