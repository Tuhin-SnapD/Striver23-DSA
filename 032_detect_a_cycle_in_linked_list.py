"""
Delete Node in a Linked List

Delete a node (except tail) from a singly linked list, given only access to that node.

Time Complexity: O(1)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def delete_node(node: ListNode) -> None:
    """
    Delete node by copying next node's data and updating pointer.
    
    Note: This method cannot delete the tail node.
    
    Args:
        node: Node to be deleted (not the tail)
    """
    # Copy next node's value
    node.val = node.next.val
    # Skip next node
    node.next = node.next.next

