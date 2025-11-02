"""
Sort 0s, 1s, and 2s (Dutch National Flag Problem)

Sort an array containing only 0s, 1s, and 2s in-place.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def sort_012(arr: List[int], n: int) -> None:
    """
    Sort array containing 0s, 1s, and 2s using Dutch National Flag algorithm.
    
    Args:
        arr: List containing only 0s, 1s, and 2s
        n: Length of the array
    """
    start = 0  # Points to position where next 0 should be placed
    mid = 0    # Current element being examined
    end = n - 1  # Points to position where next 2 should be placed
    
    while mid <= end:
        if arr[mid] == 0:
            # Move 0 to the beginning
            arr[start], arr[mid] = arr[mid], arr[start]
            start += 1
            mid += 1
        elif arr[mid] == 1:
            # 1 is in correct position, just move forward
            mid += 1
        else:  # arr[mid] == 2
            # Move 2 to the end
            arr[mid], arr[end] = arr[end], arr[mid]
            end -= 1
            # Don't increment mid as we need to check the swapped element

