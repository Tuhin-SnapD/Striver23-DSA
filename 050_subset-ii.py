"""
Subsets II

Find all unique subsets of array (may contain duplicates).

Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

from typing import List


def help(
    i: int,
    arr: List[int],
    n: int,
    subset: List[int],
    powerset: List[List[int]]
) -> None:
    """
    Recursive helper to generate unique subsets.
    
    Args:
        i: Current index
        arr: Input array
        n: Length of array
        subset: Current subset being built
        powerset: List to store all subsets
    """
    if i == n:
        powerset.append(subset[:])
        return
    
    # Include current element
    subset.append(arr[i])
    help(i + 1, arr, n, subset, powerset)
    subset.pop()
    
    # Skip duplicates
    while i + 1 < len(arr) and arr[i] == arr[i + 1]:
        i += 1
    
    # Exclude current element (and duplicates)
    help(i + 1, arr, n, subset, powerset)


def unique_subsets(n: int, arr: List[int]) -> List[List[int]]:
    """
    Find all unique subsets of array.
    
    Args:
        n: Length of array
        arr: Array of integers (may contain duplicates)
        
    Returns:
        List of all unique subsets
    """
    arr.sort()
    powerset = []
    subset = []
    help(0, arr, n, subset, powerset)
    powerset.sort()
    return powerset

