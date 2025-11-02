"""
Set Matrix Zeros

Given an m x n matrix, if an element is 0, set its entire row and column to 0.

Time Complexity: O(n * m * (n + m))
Space Complexity: O(n * m)
"""

from typing import List


def set_zeros(matrix: List[List[int]]) -> None:
    """
    Set entire row and column to zero if an element is zero.
    
    Args:
        matrix: 2D list of integers to modify in-place
    """
    n = len(matrix)
    m = len(matrix[0])
    # Create a copy to track which cells should be zero
    visited = [row[:] for row in matrix]
    
    # Mark rows with zeros
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                for k in range(m):
                    visited[i][k] = 0
    
    # Mark columns with zeros
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                for k in range(n):
                    visited[k][j] = 0
    
    # Update the original matrix
    for i in range(n):
        for j in range(m):
            matrix[i][j] = visited[i][j]

