"""
0/1 Knapsack Problem

Find maximum profit that can be obtained by selecting items with given weights
and values, without exceeding weight capacity.

Time Complexity: O(n * w) where n is number of items, w is capacity
Space Complexity: O(n * w)
"""

from typing import List


def solve(
    i: int,
    values: List[int],
    weights: List[int],
    n: int,
    w: int,
    dp: List[List[int]]
) -> int:
    """
    Recursive function with memoization to solve knapsack.
    
    Args:
        i: Current index
        values: Array of item values
        weights: Array of item weights
        n: Number of items remaining
        w: Remaining weight capacity
        dp: Memoization table
        
    Returns:
        Maximum profit achievable
    """
    if n == 0 or w == 0:
        return 0
    
    if dp[i][w] != -1:
        return dp[i][w]
    
    # If current item can be included
    if weights[n - 1] <= w:
        dp[i][w] = max(
            values[n - 1] + solve(
                i + 1, values, weights, n - 1, w - weights[n - 1], dp
            ),
            solve(i + 1, values, weights, n - 1, w, dp)
        )
    else:
        # Cannot include current item
        dp[i][w] = solve(i + 1, values, weights, n - 1, w, dp)
    
    return dp[i][w]


def max_profit(
    values: List[int],
    weights: List[int],
    n: int,
    w: int
) -> int:
    """
    Find maximum profit for 0/1 knapsack problem.
    
    Args:
        values: Array of item values
        weights: Array of item weights
        n: Number of items
        w: Weight capacity
        
    Returns:
        Maximum profit achievable
    """
    # Initialize DP table with -1
    dp = [[-1 for _ in range(w + 1)] for _ in range(n + 1)]
    
    return solve(0, values, weights, n, w, dp)

