"""
Longest Common Subsequence

Find length of longest common subsequence between two strings.

Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""


def lcs(s: str, t: str) -> int:
    """
    Find length of longest common subsequence.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        Length of LCS
    """
    n = len(s)
    m = len(t)
    
    # DP table: dp[i][j] = LCS of s[0:i] and t[0:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][m]

