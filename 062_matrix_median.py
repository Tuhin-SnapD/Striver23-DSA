"""
Matrix Median

Find median of row-wise sorted matrix using binary search.

Time Complexity: O(32 * n * log(m)) where n is rows, m is columns
Space Complexity: O(1)
"""

from typing import List
import sys


def get_median(matrix: List[List[int]]) -> int:
    """
    Find median using binary search on answer.
    
    Args:
        matrix: Row-wise sorted matrix
        
    Returns:
        Median value
    """
    n = len(matrix)
    m = len(matrix[0])
    
    # Find min and max values
    start = sys.maxsize
    end = -sys.maxsize - 1
    
    for i in range(n):
        start = min(start, matrix[i][0])
        end = max(end, matrix[i][m - 1])
    
    # Position of median
    mid_pos = (n * m + 1) // 2
    
    while start <= end:
        mid = start + (end - start) // 2
        count = 0
        
        # Count elements <= mid
        for i in range(n):
            # Binary search for upper bound
            left, right = 0, m
            while left < right:
                middle = (left + right) // 2
                if matrix[i][middle] <= mid:
                    left = middle + 1
                else:
                    right = middle
            count += left
        
        if count < mid_pos:
            start = mid + 1
        else:
            end = mid - 1
    
    return start

