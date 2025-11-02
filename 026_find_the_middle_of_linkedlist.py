"""
Middle of Linked List

Find the middle node of a linked list using two pointers.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find middle node using slow and fast pointers (tortoise and hare).
    
    When fast pointer reaches end, slow pointer is at middle.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Middle node of the linked list
    """
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next       # Move one step
        fast = fast.next.next  # Move two steps
    
    return slow

