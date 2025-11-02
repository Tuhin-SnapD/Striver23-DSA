"""
Edit Distance

Find minimum operations (insert, delete, replace) to convert one string to another.

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""


def edit_distance(word1: str, word2: str) -> int:
    """
    Find minimum edit distance between two strings.
    
    Args:
        word1: First string
        word2: Second string
        
    Returns:
        Minimum edit distance
    """
    m = len(word1)
    n = len(word2)
    
    # DP table: dp[i][j] = edit distance of word1[0:i] and word2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                insert_op = dp[i][j - 1]
                delete_op = dp[i - 1][j]
                replace_op = dp[i - 1][j - 1]
                dp[i][j] = 1 + min(insert_op, delete_op, replace_op)
    
    return dp[m][n]

