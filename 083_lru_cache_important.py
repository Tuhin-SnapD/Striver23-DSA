"""
LRU Cache Implementation

Least Recently Used cache with get and put operations.

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
"""

from typing import Optional, Dict


class ListNode:
    """Doubly linked list node for LRU cache."""
    
    def __init__(self, key: int = -1, val: int = -1):
        self.key = key
        self.val = val
        self.prev: Optional[ListNode] = None
        self.next: Optional[ListNode] = None


class LRUCache:
    """LRU Cache implementation using doubly linked list and hash map."""
    
    def __init__(self, capacity: int):
        """
        Initialize LRU cache.
        
        Args:
            capacity: Maximum capacity of cache
        """
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache: Dict[int, ListNode] = {}
    
    def _delete(self, node: ListNode) -> None:
        """Delete node from doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add(self, node: ListNode) -> None:
        """Add node after head."""
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
    
    def get(self, key: int) -> int:
        """
        Get value for key, updating it to most recently used.
        
        Args:
            key: Key to look up
            
        Returns:
            Value if exists, -1 otherwise
        """
        if key in self.cache:
            node = self.cache[key]
            val = node.val
            # Move to front
            self._delete(node)
            self._add(node)
            self.cache[key] = self.head.next
            return val
        return -1
    
    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.
        
        Args:
            key: Key
            value: Value
        """
        if key in self.cache:
            node = self.cache[key]
            self._delete(node)
        
        if len(self.cache) == self.capacity:
            # Remove least recently used (before tail)
            lru_node = self.tail.prev
            del self.cache[lru_node.key]
            self._delete(lru_node)
        
        # Add new node
        new_node = ListNode(key, value)
        self._add(new_node)
        self.cache[key] = self.head.next

