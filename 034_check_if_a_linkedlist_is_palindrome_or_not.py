"""
Palindrome Linked List

Check if a linked list is a palindrome.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a linked list.
    
    Args:
        head: Head of linked list
        
    Returns:
        Head of reversed linked list
    """
    prev = None
    curr = head
    
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev


def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is palindrome using two pointers and reversing.
    
    Finds middle, reverses second half, then compares both halves.
    
    Args:
        head: Head of linked list
        
    Returns:
        True if palindrome, False otherwise
    """
    if head is None or head.next is None:
        return True
    
    # Find middle using slow and fast pointers
    slow = head
    fast = head
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    slow.next = reverse(slow.next)
    slow = slow.next
    
    # Compare both halves
    curr = head
    while slow is not None:
        if curr.val != slow.val:
            return False
        curr = curr.next
        slow = slow.next
    
    return True

