"""
Remove Duplicates from Sorted Array

Remove duplicates in-place and return new length.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def remove_duplicates(arr: List[int], n: int) -> int:
    """
    Remove duplicates from sorted array in-place.
    
    Args:
        arr: Sorted array (modified in-place)
        n: Length of array
        
    Returns:
        New length after removing duplicates
    """
    if n == 0:
        return 0
    
    count = 1  # Count of unique elements
    
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[count] = arr[i]
            count += 1
    
    return count

