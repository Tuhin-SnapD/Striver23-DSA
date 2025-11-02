"""
Merge Intervals

Merge all overlapping intervals and return an array of non-overlapping intervals.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n)
"""

from typing import List


def merge_intervals(arr: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.
    
    Args:
        arr: List of intervals where each interval is [start, end]
        
    Returns:
        List of merged non-overlapping intervals
    """
    n = len(arr)
    if n == 0:
        return []
    
    # Sort intervals by start time
    arr.sort(key=lambda x: x[0])
    
    ans = []
    curr = arr[0]  # Current interval being built
    
    for i in range(1, n):
        # If current interval overlaps with next interval
        if curr[1] >= arr[i][0]:
            # Merge: update end time to maximum of both
            curr[1] = max(curr[1], arr[i][1])
        else:
            # No overlap, add current interval and start new one
            ans.append(curr)
            curr = arr[i]
    
    # Add the last interval
    ans.append(curr)
    return ans

