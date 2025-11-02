"""
Majority Element

Find the majority element in an array (element appearing more than n/2 times).

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1)
"""

from typing import List


def find_majority_element(arr: List[int], n: int) -> int:
    """
    Find majority element using sorting.
    
    After sorting, if a majority element exists, it will be at index n/2.
    
    Args:
        arr: Array of integers
        n: Length of the array
        
    Returns:
        Majority element if exists, -1 otherwise
    """
    arr.sort()
    
    p1 = 0
    p2 = 0
    
    while p2 <= n - 1:
        if arr[p1] == arr[p2]:
            # Check if current element appears more than n/2 times
            if p2 - p1 >= n / 2:
                return arr[p1]
            p2 += 1
        else:
            p1 = p2
    
    return -1

