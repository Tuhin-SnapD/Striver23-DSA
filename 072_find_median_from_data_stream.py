"""
Median in a Stream

Find median after each element is added using two heaps.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List
import heapq


def find_median(arr: List[int], n: int) -> List[int]:
    """
    Find median for each position in stream.
    
    Uses max heap for lower half and min heap for upper half.
    
    Args:
        arr: Array of integers
        n: Length of array
        
    Returns:
        List of medians at each position
    """
    max_heap = []  # Max heap (negated values)
    min_heap = []  # Min heap
    medians = []
    
    for num in arr:
        # Add to max heap
        heapq.heappush(max_heap, -num)
        
        # Transfer top element
        temp = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, temp)
        
        # Balance heaps
        if len(min_heap) > len(max_heap):
            temp = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -temp)
        
        # Calculate median
        if len(max_heap) != len(min_heap):
            medians.append(-max_heap[0])
        else:
            medians.append((-max_heap[0] + min_heap[0]) // 2)
    
    return medians

