"""
Rod Cutting Problem

Find maximum value by cutting rod of length N into pieces.

Time Complexity: O(n * N)
Space Complexity: O(n * N)
"""

from typing import List


def cut_rod(price: List[int], n: int) -> int:
    """
    Find maximum value from cutting rod.
    
    Args:
        price: Price array where price[i] is price for length i+1
        n: Total length of rod
        
    Returns:
        Maximum value obtainable
    """
    length = len(price)
    lengths = list(range(1, length + 1))
    
    # DP table: dp[i][j] = max value using first i pieces for length j
    dp = [[0] * (n + 1) for _ in range(length + 1)]
    
    # Base case: 0 value for 0 length
    for i in range(length + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    
    # Fill DP table (unbounded knapsack variant)
    for i in range(1, length + 1):
        for j in range(1, n + 1):
            if lengths[i - 1] <= j:
                # Can take multiple pieces of same length
                dp[i][j] = max(
                    price[i - 1] + dp[i][j - lengths[i - 1]],
                    dp[i - 1][j]
                )
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[length][n]

