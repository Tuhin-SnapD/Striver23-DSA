"""
Count Inversions

Count the number of inversions in an array using merge sort.

An inversion is a pair (i, j) where i < j and arr[i] > arr[j].

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List


def merge(
    arr: List[int],
    begin: int,
    middle: int,
    end: int,
    count: List[int]
) -> None:
    """
    Merge two sorted subarrays and count inversions.
    
    Args:
        arr: Array being sorted
        begin: Start index of first subarray
        middle: End index of first subarray
        end: End index of second subarray
        count: List containing count (using list to pass by reference)
    """
    merged = []
    i = begin
    j = middle + 1
    
    while i <= middle and j <= end:
        if arr[i] > arr[j]:
            merged.append(arr[j])
            # Count inversions: all elements from i to middle form inversions
            count[0] += middle - i + 1
            j += 1
        elif arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[i])
            i += 1
    
    # Add remaining elements
    while i <= middle:
        merged.append(arr[i])
        i += 1
    
    while j <= end:
        merged.append(arr[j])
        j += 1
    
    # Copy merged array back to original
    for k in range(len(merged)):
        arr[begin + k] = merged[k]


def merge_sort(
    arr: List[int],
    start: int,
    stop: int,
    count: List[int]
) -> None:
    """
    Merge sort with inversion counting.
    
    Args:
        arr: Array to sort
        start: Start index
        stop: End index
        count: List containing count (using list to pass by reference)
    """
    if start >= stop:
        return
    
    mid = (start + stop) // 2
    merge_sort(arr, start, mid, count)
    merge_sort(arr, mid + 1, stop, count)
    merge(arr, start, mid, stop, count)


def get_inversions(arr: List[int], n: int) -> int:
    """
    Count inversions in an array.
    
    Args:
        arr: Array of integers
        n: Length of the array
        
    Returns:
        Number of inversions
    """
    count = [0]  # Use list to simulate pass by reference
    arr_copy = arr[:]
    merge_sort(arr_copy, 0, n - 1, count)
    return count[0]

