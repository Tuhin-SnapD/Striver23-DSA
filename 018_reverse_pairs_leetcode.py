"""
Reverse Pairs

Count reverse pairs: pairs (i, j) where i < j and arr[i] > 2 * arr[j].

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List


def merge(arr: List[int], low: int, mid: int, high: int) -> None:
    """
    Merge two sorted subarrays.
    
    Args:
        arr: Array to merge
        low: Start index
        mid: Middle index
        high: End index
    """
    left = low
    right = mid + 1
    temp = []
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    # Add remaining elements
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    # Copy back to original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def count_pairs(arr: List[int], low: int, mid: int, high: int) -> int:
    """
    Count reverse pairs between two sorted subarrays.
    
    Args:
        arr: Array
        low: Start of left subarray
        mid: End of left subarray
        high: End of right subarray
        
    Returns:
        Number of reverse pairs
    """
    count = 0
    right = mid + 1
    
    for i in range(low, mid + 1):
        # Count elements in right subarray where arr[i] > 2 * arr[right]
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        count += right - mid - 1
    
    return count


def merges(arr: List[int], low: int, high: int) -> int:
    """
    Merge sort with reverse pair counting.
    
    Args:
        arr: Array to sort
        low: Start index
        high: End index
        
    Returns:
        Number of reverse pairs
    """
    count = 0
    
    if low >= high:
        return count
    
    mid = (low + high) // 2
    
    count += merges(arr, low, mid)
    count += merges(arr, mid + 1, high)
    count += count_pairs(arr, low, mid, high)
    merge(arr, low, mid, high)
    
    return count


def reverse_pairs(arr: List[int], n: int) -> int:
    """
    Count reverse pairs in array.
    
    Args:
        arr: Array of integers
        n: Length of array
        
    Returns:
        Number of reverse pairs
    """
    return merges(arr, 0, n - 1)

