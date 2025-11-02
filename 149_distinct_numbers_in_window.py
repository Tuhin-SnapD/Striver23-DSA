"""
Distinct Numbers in Window

Find count of distinct numbers in every window of size k.

Time Complexity: O(n)
Space Complexity: O(k)
"""

from typing import List

def distinct_in_window(arr: List[int], k: int) -> List[int]:
    """
    Count distinct numbers in each window.
    
    Args:
        arr: Array of integers
        k: Window size
        
    Returns:
        List of distinct counts for each window
    """
    from collections import Counter
    
    if len(arr) < k:
        return []
    
    result = []
    window = Counter(arr[:k])
    result.append(len(window))
    
    for i in range(k, len(arr)):
        # Remove leftmost element
        window[arr[i - k]] -= 1
        if window[arr[i - k]] == 0:
            del window[arr[i - k]]
        
        # Add new element
        window[arr[i]] += 1
        
        result.append(len(window))
    
    return result
