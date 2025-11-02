"""
Next Permutation

Find the next lexicographically greater permutation of the given array.
If no such permutation exists, rearrange to the lowest possible order.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def next_permutation(arr: List[int]) -> List[int]:
    """
    Find the next lexicographically greater permutation.
    
    Args:
        arr: List of integers
        
    Returns:
        Next permutation in lexicographic order
    """
    n = len(arr)
    i = n - 2
    
    # Find the largest index i such that arr[i] < arr[i + 1]
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i >= 0:
        # Find the largest index j such that arr[j] > arr[i]
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]
    
    # Reverse the suffix starting at arr[i + 1]
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr

