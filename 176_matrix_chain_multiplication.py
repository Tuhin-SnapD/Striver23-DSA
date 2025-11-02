"""
Matrix Chain Multiplication

Find minimum cost to multiply chain of matrices.

Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

from typing import List
import sys


def helper(
    arr: List[int],
    start: int,
    end: int,
    dp: List[List[int]]
) -> int:
    """
    Recursive helper with memoization.
    
    Args:
        arr: Array of matrix dimensions
        start: Start index
        end: End index
        dp: Memoization table
        
    Returns:
        Minimum operations needed
    """
    if start == end - 1:
        dp[start][end] = 0
        return 0
    
    if dp[start][end] != -1:
        return dp[start][end]
    
    min_ops = sys.maxsize
    
    # Try all possible partition points
    for i in range(start + 1, end):
        if dp[start][i] == -1:
            dp[start][i] = helper(arr, start, i, dp)
        if dp[i][end] == -1:
            dp[i][end] = helper(arr, i, end, dp)
        
        ops = (dp[start][i] + dp[i][end] +
               arr[start] * arr[i] * arr[end])
        min_ops = min(min_ops, ops)
    
    dp[start][end] = min_ops
    return min_ops


def matrix_chain_multiplication(arr: List[int]) -> int:
    """
    Find minimum cost to multiply matrices.
    
    Args:
        arr: Array of matrix dimensions (n-1 matrices)
        
    Returns:
        Minimum operations needed
    """
    n = len(arr)
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    return helper(arr, 0, n - 1, dp)
