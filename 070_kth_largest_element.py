"""
Kth Smallest and Largest Element of Array

Find kth smallest and kth largest elements in array.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1)
"""

from typing import List


def kth_small_large(arr: List[int], n: int, k: int) -> List[int]:
    """
    Find kth smallest and kth largest elements.
    
    Args:
        arr: Array of integers
        n: Length of array
        k: Kth position (1-indexed)
        
    Returns:
        [kth smallest, kth largest]
    """
    arr.sort()
    result = [arr[k - 1], arr[n - k]]
    return result

