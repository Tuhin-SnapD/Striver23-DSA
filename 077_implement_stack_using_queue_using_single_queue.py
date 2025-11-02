"""
Implement a Queue

Implement queue data structure using linked list.

Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""

from typing import Optional


class Node:
    """Node for linked list."""
    
    def __init__(self, data: int):
        """
        Initialize node.
        
        Args:
            data: Data value
        """
        self.data = data
        self.next: Optional['Node'] = None


class Queue:
    """Queue implementation using linked list."""
    
    def __init__(self):
        """Initialize empty queue."""
        self.qfront: Optional[Node] = None
        self.rear: Optional[Node] = None
    
    def is_empty(self) -> bool:
        """
        Check if queue is empty.
        
        Returns:
            True if empty, False otherwise
        """
        return self.qfront is None
    
    def enqueue(self, data: int) -> None:
        """
        Add element to rear of queue.
        
        Args:
            data: Element to add
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.qfront = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self) -> int:
        """
        Remove element from front of queue.
        
        Returns:
            Dequeued element, or -1 if queue is empty
        """
        if self.is_empty():
            return -1
        
        ans = self.qfront.data
        temp = self.qfront
        self.qfront = self.qfront.next
        
        if self.qfront is None:
            self.rear = None
        
        return ans
    
    def front(self) -> int:
        """
        Get front element without removing it.
        
        Returns:
            Front element, or -1 if queue is empty
        """
        if self.is_empty():
            return -1
        
        return self.qfront.data

