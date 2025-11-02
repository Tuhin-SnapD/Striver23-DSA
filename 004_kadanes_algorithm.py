"""
Maximum Subarray Sum (Kadane's Algorithm)

Find the maximum sum of a contiguous subarray.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def max_subarray_sum(arr: List[int], n: int) -> int:
    """
    Find the maximum sum of contiguous subarray using Kadane's algorithm.
    
    Args:
        arr: List of integers
        n: Length of the array
        
    Returns:
        Maximum sum of contiguous subarray
    """
    current_sum = 0
    max_sum = float('-inf')
    
    for i in range(n):
        current_sum += arr[i]
        
        # Reset current_sum to 0 if it becomes negative
        if current_sum < 0:
            current_sum = 0
        
        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum

