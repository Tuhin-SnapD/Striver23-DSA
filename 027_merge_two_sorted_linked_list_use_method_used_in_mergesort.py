"""
Merge Two Sorted Linked Lists

Merge two sorted linked lists into one sorted linked list.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def sort_two_lists(
    first: Optional[ListNode],
    second: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Merge two sorted linked lists recursively.
    
    Args:
        first: Head of first sorted linked list
        second: Head of second sorted linked list
        
    Returns:
        Head of merged sorted linked list
    """
    # Base cases
    if first is None:
        return second
    if second is None:
        return first
    
    # Choose smaller value and recurse
    if first.val <= second.val:
        first.next = sort_two_lists(first.next, second)
        return first
    else:
        second.next = sort_two_lists(first, second.next)
        return second

