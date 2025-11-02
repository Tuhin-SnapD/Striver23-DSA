"""
Reverse Linked List

Reverse a singly linked list iteratively.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a linked list iteratively using three pointers.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed linked list
    """
    prev = None
    curr = head
    
    while curr is not None:
        next_node = curr.next  # Store next node
        curr.next = prev       # Reverse current node's pointer
        prev = curr            # Move prev forward
        curr = next_node       # Move curr forward
    
    return prev  # prev is the new head

