"""
Single Element in a Sorted Array

Find single element in sorted array where all other elements appear twice.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


def single_non_duplicate(arr: List[int]) -> int:
    """
    Find single non-duplicate element using binary search.
    
    Args:
        arr: Sorted array with all elements appearing twice except one
        
    Returns:
        Single non-duplicate element
    """
    n = len(arr)
    start = 0
    end = n - 1
    
    # Edge cases
    if end == 0:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[end] != arr[end - 1]:
        return arr[end]
    
    while start <= end:
        mid = start + (end - start) // 2
        
        # Check if mid is the single element
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]
        
        # Check pattern to decide which half to search
        if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or \
           (mid % 2 == 1 and arr[mid] == arr[mid - 1]):
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

