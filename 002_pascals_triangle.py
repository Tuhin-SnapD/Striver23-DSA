"""
Pascal's Triangle

Generate the first n rows of Pascal's triangle.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

from typing import List


def print_pascal(n: int) -> List[List[int]]:
    """
    Generate Pascal's triangle with n rows.
    
    Args:
        n: Number of rows in Pascal's triangle
        
    Returns:
        2D list representing Pascal's triangle
    """
    ans = [[] for _ in range(n)]
    
    for i in range(1, n + 1):
        c = 1
        for j in range(1, i + 1):
            ans[i - 1].append(c)
            # Calculate next value using the formula:
            # C(n, k+1) = C(n, k) * (n - k) / (k + 1)
            c = c * (i - j) // j
    
    return ans

