"""
Search in a 2D Matrix

Search for a target value in a 2D matrix where each row and column is sorted.

Time Complexity: O(log(m * n))
Space Complexity: O(1)
"""

from typing import List


def search_matrix(mat: List[List[int]], target: int) -> bool:
    """
    Search for target in a sorted 2D matrix using binary search.
    
    Treats the 2D matrix as a 1D sorted array.
    
    Args:
        mat: 2D sorted matrix (each row and column is sorted)
        target: Value to search for
        
    Returns:
        True if target is found, False otherwise
    """
    n = len(mat)
    m = len(mat[0])
    
    start = 0
    end = (n * m) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        # Convert 1D index to 2D coordinates
        row = mid // m
        col = mid % m
        
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return False

