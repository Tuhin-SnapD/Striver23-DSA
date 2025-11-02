"""
Count Distinct Element in Every K Size Window

Count distinct elements in each sliding window of size k.

Time Complexity: O(n)
Space Complexity: O(k)
"""

from typing import List, Dict


def count_distinct_elements(arr: List[int], k: int) -> List[int]:
    """
    Count distinct elements in each window of size k.
    
    Args:
        arr: Array of integers
        k: Window size
        
    Returns:
        List of distinct counts for each window
    """
    n = len(arr)
    prev_index: Dict[int, int] = {}
    seen: Dict[int, bool] = {}
    distinct_count = 0
    result = []
    left = 0
    
    for right in range(n):
        # Add current element
        if arr[right] not in seen or prev_index.get(arr[right], -1) < left:
            distinct_count += 1
        
        seen[arr[right]] = True
        prev_index[arr[right]] = right
        
        # When window size reaches k
        if right >= k - 1:
            result.append(distinct_count)
            
            # Remove leftmost element
            if prev_index.get(arr[left], -1) == left:
                distinct_count -= 1
            left += 1
    
    return result

