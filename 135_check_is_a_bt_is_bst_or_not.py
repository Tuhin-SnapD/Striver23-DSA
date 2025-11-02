"""
Search in Rotated Sorted Array

Search for element in rotated sorted array.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


def search(arr: List[int], n: int, key: int) -> int:
    """
    Search for key in rotated sorted array using binary search.
    
    Args:
        arr: Rotated sorted array
        n: Length of array
        key: Element to search
        
    Returns:
        Index of key if found, -1 otherwise
    """
    start = 0
    end = n - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if arr[mid] == key:
            return mid
        
        # Check which half is sorted
        if arr[start] <= arr[mid]:
            # Left half is sorted
            if arr[start] <= key <= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            # Right half is sorted
            if arr[mid] <= key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    return -1

