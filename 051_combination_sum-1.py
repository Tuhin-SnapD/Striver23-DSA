"""
Return Subsets Sum to K

Find all subsets that sum to target value k.

Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

from typing import List


def solve(
    i: int,
    current_sum: int,
    k: int,
    num: List[int],
    result: List[List[int]],
    current_subset: List[int]
) -> None:
    """
    Recursive helper to find subsets summing to k.
    
    Args:
        i: Current index
        current_sum: Current sum of subset
        k: Target sum
        num: Input array
        result: List to store valid subsets
        current_subset: Current subset being built
    """
    # Base case: processed all elements
    if i == len(num):
        if current_sum == k:
            result.append(current_subset[:])
        return
    
    # Exclude current element
    solve(i + 1, current_sum, k, num, result, current_subset)
    
    # Include current element
    current_subset.append(num[i])
    solve(i + 1, current_sum + num[i], k, num, result, current_subset)
    current_subset.pop()


def find_subsets_that_sum_to_k(arr: List[int], n: int, k: int) -> List[List[int]]:
    """
    Find all subsets that sum to k.
    
    Args:
        arr: Array of integers
        n: Length of array
        k: Target sum
        
    Returns:
        List of all subsets that sum to k
    """
    result = []
    current_subset = []
    solve(0, 0, k, arr, result, current_subset)
    return result

