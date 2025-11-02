"""
Maximum Sum Increasing Subsequence

Find maximum sum of increasing subsequence.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

from typing import List


def max_increasing_dumbbells_sum(a: List[int], n: int) -> int:
    """
    Find maximum sum of increasing subsequence.
    
    Args:
        a: Array of integers
        n: Length of array
        
    Returns:
        Maximum sum of increasing subsequence
    """
    if n == 1:
        return a[0]
    
    # DP: dp[i][prev_ind+1] = max sum starting from i with previous index prev_ind
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n - 1, -1, -1):
        for prev_ind in range(i - 1, -2, -1):
            # Not take
            sum1 = dp[i + 1][prev_ind + 1] if i + 1 < n else 0
            
            # Take
            sum2 = 0
            if prev_ind == -1 or (i < n and a[i] > a[prev_ind]):
                sum2 = a[i] + (dp[i + 1][i] if i + 1 < n else 0)
            
            dp[i][prev_ind + 1] = max(sum1, sum2)
    
    return dp[0][0]

