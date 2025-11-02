"""
2Sum Problem

Find two numbers in array that add up to target.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target.
    
    Args:
        nums: Array of integers
        target: Target sum
        
    Returns:
        Indices of the two numbers
    """
    # Use hashmap to store seen values and their indices
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []
