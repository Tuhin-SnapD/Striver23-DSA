"""
Minimum Sum Path in Matrix

Find minimum sum path from top-left to bottom-right in matrix.
Can only move down or right.

Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""

from typing import List


def min_path_sum(matrix: List[List[int]]) -> int:
    """
    Find minimum sum path from top-left to bottom-right.
    
    Args:
        matrix: 2D matrix of integers
        
    Returns:
        Minimum sum of path
    """
    n = len(matrix)
    m = len(matrix[0])
    
    # Create DP table
    dp = [[0] * m for _ in range(n)]
    
    # Base case: starting point
    dp[0][0] = matrix[0][0]
    
    # Fill first row: can only come from left
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    
    # Fill first column: can only come from top
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    
    # Fill rest of the table: can come from top or left
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    return dp[n-1][m-1]

