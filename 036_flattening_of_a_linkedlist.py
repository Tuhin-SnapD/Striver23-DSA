"""
Flatten a Linked List

Flatten a multilevel linked list where nodes have next and child pointers.

Time Complexity: O(n) where n is total nodes
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    """Definition for multilevel linked list node."""
    
    def __init__(
        self,
        val: int = 0,
        next: Optional['ListNode'] = None,
        child: Optional['ListNode'] = None
    ):
        self.val = val
        self.next = next
        self.child = child


def merge_lists(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists.
    
    Args:
        head1: Head of first sorted list
        head2: Head of second sorted list
        
    Returns:
        Head of merged sorted list
    """
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    # Choose smaller head as root
    root = head2 if head1.val > head2.val else head1
    prev = root
    first = root.child
    second = head2 if root == head1 else head1
    
    # Merge while both lists have nodes
    while first is not None and second is not None:
        if first.val < second.val:
            prev.child = first
            prev = first
            first = first.child
        else:
            prev.child = second
            prev = second
            second = second.child
    
    # Append remaining nodes
    if first is not None:
        prev.child = first
    elif second is not None:
        prev.child = second
    
    return root


def flatten_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Flatten multilevel linked list recursively.
    
    Args:
        head: Head of multilevel linked list
        
    Returns:
        Head of flattened linked list
    """
    # Base case
    if head is None or head.next is None:
        return head
    
    # Flatten remaining list
    root = head.next
    head.next = None
    root = flatten_linked_list(root)
    
    # Merge current level with flattened list
    head = merge_lists(head, root)
    return head

