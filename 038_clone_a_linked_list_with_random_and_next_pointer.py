"""
Cycle Detection in a Singly Linked List

Detect if a linked list has a cycle using Floyd's cycle detection algorithm.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def detect_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect cycle using Floyd's cycle detection (tortoise and hare).
    
    If slow and fast pointers meet, there's a cycle.
    
    Args:
        head: Head of the linked list
        
    Returns:
        True if cycle exists, False otherwise
    """
    if head is None:
        return False
    
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next       # Move one step
        fast = fast.next.next  # Move two steps
        
        if slow == fast:
            return True
    
    return False

