"""
Reverse Nodes in k-Group

Reverse nodes in groups of k. Skip groups of size 0.

Time Complexity: O(n)
Space Complexity: O(k) for recursion
"""

from typing import Optional, List


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def reversal(
    head: Optional[ListNode],
    n: int,
    b: List[int],
    i: int
) -> Optional[ListNode]:
    """
    Recursively reverse nodes in groups specified by array b.
    
    Args:
        head: Head of linked list
        n: Length of array b
        b: Array specifying group sizes
        i: Current index in array b
        
    Returns:
        Head of modified linked list
    """
    # Skip zero-size groups
    while i < n and b[i] == 0:
        i += 1
    
    # Base case: empty list or end of array
    if head is None or head.next is None or i == n:
        return head
    
    # Reverse current group of size b[i]
    counter = b[i]
    prev = None
    curr = head
    
    while curr is not None and counter > 0:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        counter -= 1
    
    # Recursively process remaining nodes
    head.next = reversal(curr, n, b, i + 1)
    
    return prev


def get_list_after_reverse_operation(
    head: Optional[ListNode],
    n: int,
    b: List[int]
) -> Optional[ListNode]:
    """
    Reverse linked list in groups as specified by array b.
    
    Args:
        head: Head of linked list
        n: Length of array b
        b: Array specifying sizes of groups to reverse
        
    Returns:
        Head of modified linked list
    """
    if head is None:
        return None
    
    return reversal(head, n, b, 0)

