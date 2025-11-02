"""
Maximum Consecutive Ones

Find longest subarray with at most k zeros.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def longest_subseg(arr: List[int], n: int, k: int) -> int:
    """
    Find longest subarray with at most k zeros using sliding window.
    
    Args:
        arr: Array of 0s and 1s
        n: Length of array
        k: Maximum allowed zeros
        
    Returns:
        Length of longest subarray with at most k zeros
    """
    i = 0
    j = 0
    
    for i in range(n):
        if arr[i] == 0:
            k -= 1
        
        # Shrink window if k becomes negative
        if k < 0:
            if arr[j] == 0:
                k += 1
            j += 1
    
    return i - j + 1

