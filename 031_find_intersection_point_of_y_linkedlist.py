"""
Intersection of Two Linked Lists

Find the intersection node of two linked lists.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def find_intersection(
    first_head: Optional[ListNode],
    second_head: Optional[ListNode]
) -> int:
    """
    Find intersection node by aligning lengths and then comparing.
    
    Args:
        first_head: Head of first linked list
        second_head: Head of second linked list
        
    Returns:
        Value of intersection node, or -1 if no intersection
    """
    # Calculate lengths
    len1 = 0
    curr1 = first_head
    while curr1 is not None:
        len1 += 1
        curr1 = curr1.next
    
    len2 = 0
    curr2 = second_head
    while curr2 is not None:
        len2 += 1
        curr2 = curr2.next
    
    # Reset pointers
    curr1 = first_head
    curr2 = second_head
    
    # Align pointers to same starting position
    if len1 > len2:
        for _ in range(len1 - len2):
            curr1 = curr1.next
    elif len2 > len1:
        for _ in range(len2 - len1):
            curr2 = curr2.next
    
    # Find intersection
    while curr1 is not None and curr2 is not None:
        if curr1 == curr2:
            return curr1.val
        curr1 = curr1.next
        curr2 = curr2.next
    
    return -1

