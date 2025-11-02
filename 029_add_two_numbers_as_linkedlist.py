"""
Add Two Numbers

Add two numbers represented as linked lists (digits stored in reverse order).

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def add_two_numbers(
    num1: Optional[ListNode],
    num2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Add two numbers represented as linked lists.
    
    Args:
        num1: Head of first number (digits in reverse)
        num2: Head of second number (digits in reverse)
        
    Returns:
        Head of result linked list (digits in reverse)
    """
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    
    while num1 is not None or num2 is not None or carry == 1:
        total = carry
        
        if num1 is not None:
            total += num1.val
            num1 = num1.next
        
        if num2 is not None:
            total += num2.val
            num2 = num2.next
        
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
    
    return dummy.next

