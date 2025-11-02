"""
Rotate Linked List

Rotate linked list to the right by k places.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def rotate(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Rotate linked list to the right by k places.
    
    Args:
        head: Head of linked list
        k: Number of places to rotate
        
    Returns:
        Head of rotated linked list
    """
    if head is None or head.next is None or k == 0:
        return head
    
    # Find length and last node
    length = 1
    curr = head
    while curr.next is not None:
        curr = curr.next
        length += 1
    
    # Form a circle
    curr.next = head
    
    # Calculate effective rotation
    k = k % length
    
    # Move to new head position
    for _ in range(length - k):
        curr = curr.next
    
    # Break the circle
    head = curr.next
    curr.next = None
    
    return head

