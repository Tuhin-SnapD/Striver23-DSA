"""
Ways To Make Coin Change

Count number of ways to make change using given denominations.

Time Complexity: O(n * value)
Space Complexity: O(value)
"""

from typing import List


def count_ways_to_make_change(denominations: List[int], n: int, value: int) -> int:
    """
    Count ways to make change using dynamic programming.
    
    Args:
        denominations: Array of coin denominations
        n: Number of denominations
        value: Target value
        
    Returns:
        Number of ways to make change
    """
    # Space-optimized DP
    after = [0] * (value + 1)
    cur = [0] * (value + 1)
    
    # Base case: one way to make 0
    for i in range(n):
        cur[0] = 1
    
    for i in range(n - 1, -1, -1):
        for t in range(1, value + 1):
            pick = 0
            not_pick = 0
            
            if denominations[i] <= t:
                pick = cur[t - denominations[i]]
            
            if i < n - 1:
                not_pick = after[t]
            
            cur[t] = pick + not_pick
        
        after = cur[:]
    
    return cur[value]

