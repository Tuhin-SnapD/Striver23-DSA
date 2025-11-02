"""
Trapping Rain Water

Calculate how much rainwater can be trapped between bars.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def get_trapped_water(arr: List[int], n: int) -> int:
    """
    Calculate trapped rainwater using two-pointer approach.
    
    Args:
        arr: Array representing heights of bars
        n: Length of array
        
    Returns:
        Total amount of trapped rainwater
    """
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    total_water = 0
    
    while left <= right:
        if arr[left] <= arr[right]:
            # Process left side
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                total_water += left_max - arr[left]
            left += 1
        else:
            # Process right side
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                total_water += right_max - arr[right]
            right -= 1
    
    return total_water

