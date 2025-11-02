"""
Kth Element of Two Sorted Arrays

Find kth element when two sorted arrays are merged.

Time Complexity: O(log(min(n, m)))
Space Complexity: O(1)
"""

from typing import List
import sys


def ninja_and_ladoos(
    arr1: List[int],
    arr2: List[int],
    n: int,
    m: int,
    k: int
) -> int:
    """
    Find kth element using binary search on partition.
    
    Args:
        arr1: First sorted array
        arr2: Second sorted array
        n: Length of arr1
        m: Length of arr2
        k: Kth position (1-indexed)
        
    Returns:
        Kth element
    """
    # Ensure arr1 is shorter
    if m < n:
        return ninja_and_ladoos(arr2, arr1, m, n, k)
    
    low = max(0, k - m)
    high = min(k, n)
    
    while low <= high:
        p1 = (low + high) // 2
        p2 = k - p1
        
        l1 = -sys.maxsize - 1 if p1 == 0 else arr1[p1 - 1]
        l2 = -sys.maxsize - 1 if p2 == 0 else arr2[p2 - 1]
        r1 = sys.maxsize if p1 == n else arr1[p1]
        r2 = sys.maxsize if p2 == m else arr2[p2]
        
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = p1 - 1
        else:
            low = p1 + 1
    
    return 1

