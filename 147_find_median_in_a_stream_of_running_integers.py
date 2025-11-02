"""
Running Median

Find median of stream of integers using two heaps.

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
        if len(max_heap) == 0:
            heapq.heappush(max_heap, -num)
        elif num > -max_heap[0]:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -num)
        
        # Balance heaps
        if len(max_heap) - len(min_heap) == 2:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) - len(max_heap) == 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        # Calculate median
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) // 2
        else:
            median = -max_heap[0]
        
        medians.append(median)
    
    return medians

