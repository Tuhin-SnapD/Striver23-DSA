"""
Longest Increasing Subsequence

Find length of longest increasing subsequence using binary search.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List
import bisect


def longest_increasing_subsequence(arr: List[int], n: int) -> int:
    """
    Find length of LIS using patience sorting approach.
    
    Maintains tail array where tail[i] is smallest tail of all increasing
    subsequences of length i+1.
    
    Args:
        arr: Array of integers
        n: Length of array
        
    Returns:
        Length of longest increasing subsequence
    """
    tail = [arr[0]]
    
    for i in range(1, n):
        if arr[i] > tail[-1]:
            tail.append(arr[i])
        else:
            # Find position to replace using binary search
            pos = bisect.bisect_left(tail, arr[i])
            tail[pos] = arr[i]
    
    return len(tail)

