"""
Kth Largest Element in the Unsorted Array

Find kth largest element using min heap of size k.

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

from typing import List
import heapq


def kth_largest(nums: List[int], n: int, k: int) -> int:
    """
    Find kth largest element using min heap.
    
    Args:
        nums: Array of integers
        n: Length of array
        k: Kth position (1-indexed)
        
    Returns:
        Kth largest element
    """
    heap = []
    
    for i in range(n):
        if i < k:
            heapq.heappush(heap, nums[i])
        else:
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
    
    return heap[0]

