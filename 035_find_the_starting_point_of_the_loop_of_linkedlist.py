"""
Linked List Cycle II

Find the first node where the cycle begins in a linked list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def first_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find first node of cycle using Floyd's cycle detection.
    
    After detecting cycle, reset slow to head and move both one step at a time.
    Where they meet is the cycle start.
    
    Args:
        head: Head of linked list
        
    Returns:
        First node of cycle, or None if no cycle
    """
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            # Cycle detected, find entry point
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    
    return None

