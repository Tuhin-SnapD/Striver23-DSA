"""
Longest Consecutive Sequence

Find the length of the longest consecutive sequence in an unsorted array.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1)
"""

from typing import List


def length_of_longest_consecutive_sequence(arr: List[int], n: int) -> int:
    """
    Find length of longest consecutive sequence using sorting.
    
    Args:
        arr: Array of integers
        n: Length of array
        
    Returns:
        Length of longest consecutive sequence
    """
    if n == 0:
        return 0
    
    arr.sort()
    max_length = 0
    count = 1
    
    for i in range(1, n):
        # Skip duplicates
        if arr[i] == arr[i - 1]:
            continue
        # Check if consecutive
        elif arr[i] == arr[i - 1] + 1:
            count += 1
        else:
            # Update max and reset count
            max_length = max(max_length, count)
            count = 1
    
    # Update max for last sequence
    max_length = max(max_length, count)
    
    return max_length

