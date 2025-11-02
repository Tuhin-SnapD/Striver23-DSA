"""
Unique Paths

Count the number of unique paths from top-left to bottom-right of a grid.
Can only move right or down.

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""


def unique_paths(m: int, n: int) -> int:
    """
    Count unique paths using dynamic programming.
    
    dp[i][j] represents number of ways to reach cell (i, j).
    Base case: first row and column have only 1 way to reach.
    Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    Args:
        m: Number of rows
        n: Number of columns
        
    Returns:
        Number of unique paths
    """
    # Initialize DP table
    dp = [[0] * n for _ in range(m)]
    
    # First row and column have only 1 way to reach
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
    
    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]

