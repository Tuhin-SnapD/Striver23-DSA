"""
Kth Largest Element In A Stream

Maintain kth largest element in stream using min heap.

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

from typing import List
import heapq


class KthLargest:
    """Class to maintain kth largest element in stream."""
    
    def __init__(self, k: int, arr: List[int]):
        """
        Initialize with k and initial array.
        
        Args:
            k: K value
            arr: Initial array
        """
        self.k = k
        self.heap = []
        
        for num in arr:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)
    
    def add(self, num: int) -> None:
        """
        Add new number to stream.
        
        Args:
            num: Number to add
        """
        heapq.heappush(self.heap, num)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
    
    def get_kth_largest(self) -> int:
        """
        Get kth largest element.
        
        Returns:
            Kth largest element
        """
        return self.heap[0]

