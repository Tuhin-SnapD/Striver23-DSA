"""
Palindrome Partitioning II

Find minimum cuts needed to partition string into palindromes.

Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

from typing import List
import sys


def helper(
    s: str,
    start: int,
    end: int,
    dp: List[List[int]],
    is_pal: List[List[bool]]
) -> int:
    """
    Recursive helper with memoization.
    
    Args:
        s: Input string
        start: Start index
        end: End index
        dp: Memoization table for cuts
        is_pal: Precomputed palindrome table
        
    Returns:
        Minimum cuts needed
    """
    if start >= end:
        dp[start][end] = 0
        return 0
    
    if is_pal[start][end]:
        dp[start][end] = 0
        return 0
    
    if dp[start][end] != -1:
        return dp[start][end]
    
    min_cuts = 10**6
    
    # Try all partition points
    for i in range(start, end):
        if dp[start][i] == -1:
            dp[start][i] = helper(s, start, i, dp, is_pal)
        if dp[i + 1][end] == -1:
            dp[i + 1][end] = helper(s, i + 1, end, dp, is_pal)
        
        min_cuts = min(min_cuts, 1 + dp[start][i] + dp[i + 1][end])
    
    dp[start][end] = min_cuts
    return min_cuts


def palindrome_partitioning(s: str) -> int:
    """
    Find minimum cuts for palindrome partitioning.
    
    Args:
        s: Input string
        
    Returns:
        Minimum cuts needed
    """
    n = len(s)
    
    # Precompute palindrome table
    is_pal = [[False] * n for _ in range(n)]
    
    # Single characters are palindromes
    for i in range(n):
        is_pal[i][i] = True
        if i + 1 < n:
            is_pal[i][i + 1] = (s[i] == s[i + 1])
    
    # Fill palindrome table
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            is_pal[i][j] = (is_pal[i + 1][j - 1] and s[i] == s[j])
    
    # Compute minimum cuts
    dp = [[-1] * n for _ in range(n)]
    return helper(s, 0, n - 1, dp, is_pal)

