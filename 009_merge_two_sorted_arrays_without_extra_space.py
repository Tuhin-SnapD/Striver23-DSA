"""
Merge Two Sorted Arrays

Merge two sorted arrays and return the sorted result.

Time Complexity: O((m + n) log(m + n)) due to sorting
Space Complexity: O(m + n)
"""

from typing import List


def ninja_and_sorted_arrays(
    arr1: List[int], 
    arr2: List[int], 
    m: int, 
    n: int
) -> List[int]:
    """
    Merge two sorted arrays (ignoring zeros in arr1).
    
    Args:
        arr1: First sorted array (may contain zeros to ignore)
        arr2: Second sorted array
        m: Number of non-zero elements in arr1
        n: Length of arr2
        
    Returns:
        Merged sorted array
    """
    merged = []
    
    # Add non-zero elements from arr1
    for num in arr1:
        if num == 0:
            continue
        merged.append(num)
    
    # Add non-zero elements from arr2
    for num in arr2:
        if num == 0:
            continue
        merged.append(num)
    
    # Sort the merged array
    merged.sort()
    return merged

