"""
Find Duplicate in Array

Find the duplicate number in an array using Floyd's cycle detection algorithm.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def find_duplicate(arr: List[int], n: int) -> int:
    """
    Find duplicate number in array using Floyd's cycle detection.
    
    The array contains n+1 integers from 1 to n, with one duplicate.
    This problem is similar to finding the start of a cycle in a linked list.
    
    Args:
        arr: List containing n+1 integers from 1 to n with one duplicate
        n: Range of numbers (1 to n)
        
    Returns:
        The duplicate number
    """
    slow = arr[0]
    fast = arr[0]
    
    # Phase 1: Detect the cycle
    while True:
        slow = arr[slow]  # Move one step
        fast = arr[arr[fast]]  # Move two steps
        if slow == fast:
            break
    
    # Phase 2: Find the entry point of the cycle (duplicate)
    fast = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return fast

