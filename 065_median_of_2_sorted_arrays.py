"""
Median of Two Sorted Arrays

Find median of two sorted arrays of potentially different sizes.

Time Complexity: O(log(min(n, m)))
Space Complexity: O(1)
"""

from typing import List
import sys


def median(a: List[int], b: List[int]) -> float:
    """
    Find median using binary search on partition.
    
    Args:
        a: First sorted array
        b: Second sorted array
        
    Returns:
        Median value
    """
    n1 = len(a)
    n2 = len(b)
    
    # Ensure a is shorter array
    if n1 < n2:
        return median(b, a)
    
    lo = 0
    hi = n2 * 2
    
    while lo <= hi:
        mid2 = (lo + hi) // 2  # Cut in array b
        mid1 = n1 + n2 - mid2  # Cut in array a
        
        # Get left and right values
        l1 = -sys.maxsize - 1 if mid1 == 0 else a[(mid1 - 1) // 2]
        l2 = -sys.maxsize - 1 if mid2 == 0 else b[(mid2 - 1) // 2]
        r1 = sys.maxsize if mid1 == n1 * 2 else a[mid1 // 2]
        r2 = sys.maxsize if mid2 == n2 * 2 else b[mid2 // 2]
        
        if l1 > r2:
            lo = mid2 + 1
        elif l2 > r1:
            hi = mid2 - 1
        else:
            return (max(l1, l2) + min(r1, r2)) / 2.0
    
    return -1

