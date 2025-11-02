"""
Rotate Matrix

Rotate a matrix by 90 degrees in-place (clockwise).

Time Complexity: O(n * m)
Space Complexity: O(1)
"""

from typing import List


def rotate_matrix(mat: List[List[int]], n: int, m: int) -> None:
    """
    Rotate matrix by 90 degrees clockwise in-place.
    
    Args:
        mat: 2D list representing the matrix
        n: Number of rows
        m: Number of columns
    """
    if n == 1 or m == 1:
        return
    
    top, bottom = 0, n - 1
    left, right = 0, m - 1
    
    while top < bottom and left < right:
        # Store the top-left element
        temp = mat[top][left]
        
        # Rotate top column (move elements up)
        for i in range(top, bottom):
            mat[i][left] = mat[i + 1][left]
        
        # Rotate right row (move elements right)
        for i in range(left, right):
            mat[bottom][i] = mat[bottom][i + 1]
        
        # Rotate bottom column (move elements down)
        for i in range(bottom, top, -1):
            mat[i][right] = mat[i - 1][right]
        
        # Rotate left row (move elements left)
        for i in range(right, left + 1, -1):
            mat[top][i] = mat[top][i - 1]
        
        # Place the stored element
        mat[top][left + 1] = temp
        
        # Move to inner layer
        top += 1
        bottom -= 1
        left += 1
        right -= 1

