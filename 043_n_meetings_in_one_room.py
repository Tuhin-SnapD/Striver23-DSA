"""
Maximum Meetings

Find maximum number of meetings that can be scheduled without conflicts.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n)
"""

from typing import List


def maximum_meetings(start: List[int], end: List[int]) -> List[int]:
    """
    Find maximum number of non-overlapping meetings.
    
    Uses greedy algorithm: sort by end time and always pick earliest ending meeting.
    
    Args:
        start: Start times of meetings
        end: End times of meetings
        
    Returns:
        List of meeting indices (1-indexed) that can be scheduled
    """
    n = len(start)
    
    # Create list of [end_time, index (1-indexed), start_time]
    meetings = []
    for i in range(n):
        meetings.append([end[i], i + 1, start[i]])
    
    # Sort by end time
    meetings.sort()
    
    result = []
    finish_time = meetings[0][0]
    result.append(meetings[0][1])
    
    # Select meetings that don't conflict
    for i in range(1, n):
        if meetings[i][2] > finish_time:
            finish_time = meetings[i][0]
            result.append(meetings[i][1])
    
    return result

