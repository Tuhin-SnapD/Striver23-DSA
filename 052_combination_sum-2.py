"""
Combination Sum II

Find all unique combinations that sum to target (each number used once).

Time Complexity: O(2^n)
Space Complexity: O(target)
"""

from typing import List


def combination_sum_helper(
    index: int,
    result: List[List[int]],
    current: List[int],
    arr: List[int],
    n: int,
    target: int
) -> None:
    """
    Recursive helper to find combinations summing to target.
    
    Args:
        index: Current index
        result: List to store valid combinations
        current: Current combination being built
        arr: Input array
        n: Length of array
        target: Target sum
    """
    if target == 0:
        result.append(current[:])
        return
    
    for i in range(index, n):
        # Skip duplicates
        if i > index and arr[i] == arr[i - 1]:
            continue
        # Prune if element exceeds target
        if arr[i] > target:
            break
        
        current.append(arr[i])
        combination_sum_helper(
            i + 1, result, current, arr, n, target - arr[i]
        )
        current.pop()


def combination_sum_2(arr: List[int], n: int, target: int) -> List[List[int]]:
    """
    Find all unique combinations that sum to target.
    
    Args:
        arr: Array of integers (may contain duplicates)
        n: Length of array
        target: Target sum
        
    Returns:
        List of unique combinations
    """
    arr.sort()
    result = []
    current = []
    combination_sum_helper(0, result, current, arr, n, target)
    return result

