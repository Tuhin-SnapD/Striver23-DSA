"""
K Max Sum Combinations

Find k maximum sum combinations from two arrays.

Time Complexity: O(n log n + k log k)
Space Complexity: O(k)
"""

from typing import List, Set, Tuple
import heapq


def k_max_sum_combination(
    a: List[int],
    b: List[int],
    n: int,
    k: int
) -> List[int]:
    """
    Find k maximum sum combinations using max heap.
    
    Args:
        a: First array
        b: Second array
        n: Length of arrays
        k: Number of combinations needed
        
    Returns:
        List of k maximum sums
    """
    # Sort both arrays in descending order
    a.sort(reverse=True)
    b.sort(reverse=True)
    
    # Max heap: (-sum, (i, j))
    heap = []
    # Set to track visited pairs
    visited: Set[Tuple[int, int]] = set()
    
    # Push first combination
    heapq.heappush(heap, (-(a[0] + b[0]), (0, 0)))
    visited.add((0, 0))
    
    result = []
    
    for _ in range(k):
        neg_sum, (i, j) = heapq.heappop(heap)
        result.append(-neg_sum)
        
        # Try next combinations
        if i + 1 < n and (i + 1, j) not in visited:
            heapq.heappush(heap, (-(a[i + 1] + b[j]), (i + 1, j)))
            visited.add((i + 1, j))
        
        if j + 1 < n and (i, j + 1) not in visited:
            heapq.heappush(heap, (-(a[i] + b[j + 1]), (i, j + 1)))
            visited.add((i, j + 1))
    
    return result

