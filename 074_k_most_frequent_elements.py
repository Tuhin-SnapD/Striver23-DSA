"""
K Most Frequent Elements

Find k most frequent elements in array.

Time Complexity: O(n + m log k) where m is number of unique elements
Space Complexity: O(m)
"""

from typing import List, Dict
import heapq


def k_most_frequent(n: int, k: int, arr: List[int]) -> List[int]:
    """
    Find k most frequent elements using min heap.
    
    Args:
        n: Length of array
        k: Number of most frequent elements needed
        arr: Array of integers
        
    Returns:
        List of k most frequent elements (sorted)
    """
    # Count frequencies
    freq: Dict[int, int] = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    # Use min heap of size k
    heap = []
    
    for num, count in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, num))
        else:
            if heap[0][0] < count:
                heapq.heapreplace(heap, (count, num))
    
    # Extract elements
    result = [num for _, num in heap]
    result.sort()
    return result

