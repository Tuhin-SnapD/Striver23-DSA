"""
Cut Logs (Egg Dropping Problem)

Find minimum attempts to find critical floor with k eggs and n floors.

Time Complexity: O(k * n * log n)
Space Complexity: O(k * n)
"""

from typing import List
import sys


def helper(e: int, f: int, dp: List[List[int]]) -> int:
    """
    Recursive helper with memoization and binary search optimization.
    
    Args:
        e: Number of eggs
        f: Number of floors
        dp: Memoization table
        
    Returns:
        Minimum attempts needed
    """
    if f <= 1 or e == 1:
        dp[e][f] = f
        return f
    
    if dp[e][f] != -1:
        return dp[e][f]
    
    ans = 10**6
    start, end = 1, f
    
    # Binary search for optimal floor to drop from
    while start <= end:
        mid = start + (end - start) // 2
        
        # Egg breaks
        if dp[e - 1][mid - 1] == -1:
            dp[e - 1][mid - 1] = helper(e - 1, mid - 1, dp)
        break_case = dp[e - 1][mid - 1]
        
        # Egg doesn't break
        if dp[e][f - mid] == -1:
            dp[e][f - mid] = helper(e, f - mid, dp)
        survive_case = dp[e][f - mid]
        
        ans = min(ans, 1 + max(break_case, survive_case))
        
        # Binary search optimization
        if break_case < survive_case:
            start = mid + 1
        else:
            end = mid - 1
    
    dp[e][f] = ans
    return ans


def cut_logs(k: int, n: int) -> int:
    """
    Find minimum attempts to find critical floor.
    
    Args:
        k: Number of eggs (logs)
        n: Number of floors
        
    Returns:
        Minimum attempts needed
    """
    dp = [[-1] * (n + 1) for _ in range(k + 1)]
    return helper(k, n, dp)

