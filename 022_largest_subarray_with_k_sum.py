"""
Longest Subarray Zero Sum

Find the length of the longest subarray with zero sum.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


def longest_subset_with_zero_sum(arr: List[int]) -> int:
    """
    Find length of longest subarray with zero sum using hash map.
    
    Uses prefix sum technique: if prefix_sum[i] == prefix_sum[j],
    then sum from i+1 to j is zero.
    
    Args:
        arr: Array of integers
        
    Returns:
        Length of longest subarray with zero sum
    """
    prefix_sum = {}  # Map prefix sum to first occurrence index
    current_sum = 0
    max_length = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        # If current sum is zero, subarray from start to i has zero sum
        if current_sum == 0:
            max_length = i + 1
        
        # If prefix sum seen before, there's a zero-sum subarray
        if current_sum in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum])
        else:
            # Store first occurrence of this prefix sum
            prefix_sum[current_sum] = i
    
    return max_length

