"""
Subset Sum Equal To K

Check if any subset of array sums to given value k.

Time Complexity: O(n * k)
Space Complexity: O(n * k)
"""

from typing import List


def subset_sum_to_k(n: int, sum_val: int, arr: List[int]) -> bool:
    """
    Check if any subset sums to k.
    
    Args:
        n: Number of elements
        sum_val: Target sum
        arr: Array of integers
        
    Returns:
        True if subset exists, False otherwise
    """
    # DP table: dp[i][j] = can we make sum j using first i elements
    dp = [[False] * (sum_val + 1) for _ in range(n + 1)]
    
    # Initialize: sum 0 is always possible (empty subset)
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, sum_val + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][sum_val]

