"""
Pair Sum

Find all pairs in array that sum to target value.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) excluding output
"""

from typing import List


def bin_search(
    arr: List[int],
    target: int,
    low: int,
    high: int,
    find_right: bool
) -> int:
    """
    Binary search to find first or last occurrence of target.
    
    Args:
        arr: Sorted array
        target: Value to search
        low: Start index
        high: End index
        find_right: If True, find rightmost occurrence, else leftmost
        
    Returns:
        Index of occurrence, -1 if not found
    """
    l = low
    h = high
    occ = -1
    
    while h >= l:
        mid = (l + h) // 2
        
        if arr[mid] == target:
            occ = mid
            if find_right:
                l = mid + 1
                h = high
            else:
                h = mid - 1
                l = low
        elif arr[mid] > target:
            h = mid - 1
        else:
            l = mid + 1
    
    return occ


def pair_sum(arr: List[int], s: int) -> List[List[int]]:
    """
    Find all pairs that sum to target value.
    
    Args:
        arr: Array of integers
        s: Target sum
        
    Returns:
        List of pairs that sum to target
    """
    arr.sort()
    ans = []
    n = len(arr)
    
    for i in range(n - 1):
        elem = arr[i]
        complement = s - elem
        
        # Find range of complement values
        right = bin_search(arr, complement, i + 1, n - 1, True)
        left = bin_search(arr, complement, i + 1, n - 1, False)
        
        # Add all pairs with this element and complement
        while right != -1 and left <= right:
            ans.append([elem, complement])
            left += 1
    
    return ans

