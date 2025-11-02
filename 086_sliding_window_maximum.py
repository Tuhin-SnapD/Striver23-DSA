"""
Maximum in Sliding Windows of Size K

Find maximum element in each sliding window of size k.

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

from typing import List
import heapq


def sliding_window_maximum(arr: List[int], k: int) -> List[int]:
    """
    Find maximum in each sliding window using max heap.
    
    Args:
        arr: Array of integers
        k: Window size
        
    Returns:
        List of maximum elements in each window
    """
    n = len(arr)
    result = []
    # Max heap: (-value, index)
    heap = []
    
    # Initialize first window
    for i in range(k):
        heapq.heappush(heap, (-arr[i], i))
    
    result.append(-heap[0][0])
    
    # Process remaining windows
    for i in range(k, n):
        heapq.heappush(heap, (-arr[i], i))
        
        # Remove elements outside current window
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        
        result.append(-heap[0][0])
    
    return result

