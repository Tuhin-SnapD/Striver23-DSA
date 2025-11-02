"""
Maximum Activities

Find maximum number of activities that can be performed.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n)
"""

from typing import List, Tuple


def maximum_activities(start: List[int], finish: List[int]) -> int:
    """
    Find maximum non-overlapping activities using greedy algorithm.
    
    Sort by finish time and always pick activity with earliest finish time.
    
    Args:
        start: Start times of activities
        finish: Finish times of activities
        
    Returns:
        Maximum number of activities that can be performed
    """
    n = len(start)
    
    # Create pairs of (finish, start)
    activities = [(finish[i], start[i]) for i in range(n)]
    
    # Sort by finish time
    activities.sort()
    
    count = 1
    end_limit = activities[0][0]
    
    for i in range(1, n):
        start_time, finish_time = activities[i][1], activities[i][0]
        
        # If activity starts after previous ends, include it
        if start_time >= end_limit:
            count += 1
            end_limit = finish_time
    
    return count

