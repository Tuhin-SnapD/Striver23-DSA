"""
Find Four Elements That Sum to a Given Value

Check if there exist four elements in array that sum to target.

Time Complexity: O(n^3)
Space Complexity: O(1)
"""

from typing import List


def four_sum(arr: List[int], target: int, n: int) -> str:
    """
    Check if four elements exist that sum to target.
    
    Uses sorting and two-pointer technique.
    
    Args:
        arr: Array of integers
        target: Target sum
        n: Length of array
        
    Returns:
        "Yes" if four elements exist, "No" otherwise
    """
    arr.sort()
    
    # Fix first two elements and use two-pointer for remaining two
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            k = j + 1
            l = n - 1
            
            while k < l:
                current_sum = arr[i] + arr[j] + arr[k] + arr[l]
                
                if current_sum == target:
                    return "Yes"
                elif current_sum > target:
                    l -= 1
                else:
                    k += 1
    
    return "No"

