"""
Subset Sum

Find all possible subset sums of array elements.

Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

from typing import List


def subset_sum_recursive(
    index: int,
    current_sum: int,
    arr: List[int],
    result: List[int]
) -> None:
    """
    Recursive helper to generate all subset sums.
    
    Args:
        index: Current index
        current_sum: Current sum of subset
        arr: Input array
        result: List to store all subset sums
    """
    # Base case: processed all elements
    if index == len(arr):
        result.append(current_sum)
        return
    
    # Include current element
    subset_sum_recursive(index + 1, current_sum + arr[index], arr, result)
    
    # Exclude current element
    subset_sum_recursive(index + 1, current_sum, arr, result)


def subset_sum(num: List[int]) -> List[int]:
    """
    Find all possible subset sums.
    
    Args:
        num: Array of integers
        
    Returns:
        Sorted list of all possible subset sums
    """
    result = []
    subset_sum_recursive(0, 0, num, result)
    result.sort()
    return result

