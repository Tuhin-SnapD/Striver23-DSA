"""
Minimum Number of Platforms

Find minimum platforms needed so no train waits.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1)
"""

from typing import List


def calculate_min_platforms(at: List[int], dt: List[int], n: int) -> int:
    """
    Calculate minimum platforms needed using greedy approach.
    
    Sort arrivals and departures, track platforms needed at each time.
    
    Args:
        at: Array of arrival times
        dt: Array of departure times
        n: Number of trains
        
    Returns:
        Minimum number of platforms needed
    """
    # Sort arrival and departure arrays
    at.sort()
    dt.sort()
    
    platform_needed = 1
    result = 1
    i = 1  # Pointer for arrivals
    j = 0  # Pointer for departures
    
    while i < n and j < n:
        # If train arrives before another departs, need platform
        if at[i] <= dt[j]:
            platform_needed += 1
            i += 1
        # If train departs before another arrives, free platform
        else:
            platform_needed -= 1
            j += 1
        
        # Update maximum platforms needed
        if platform_needed > result:
            result = platform_needed
    
    return result

