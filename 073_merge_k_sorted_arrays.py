"""
Merge K Sorted Arrays

Merge k sorted arrays into one sorted array.

Time Complexity: O(nk log(nk)) where n is average array size
Space Complexity: O(nk)
"""

from typing import List
import heapq


def merge_k_sorted_arrays(k_arrays: List[List[int]], k: int) -> List[int]:
    """
    Merge k sorted arrays using min heap.
    
    Args:
        k_arrays: List of k sorted arrays
        k: Number of arrays
        
    Returns:
        Merged sorted array
    """
    # Push all elements into min heap
    heap = []
    for arr in k_arrays:
        for val in arr:
            heapq.heappush(heap, val)
    
    # Pop all elements to get sorted order
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    
    return result

