"""
Maximum Product Subarray

Find maximum product of contiguous subarray.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List
import sys


def maximum_product(arr: List[int], n: int) -> int:
    """
    Find maximum product subarray.
    
    Traverse from both ends to handle negative numbers.
    
    Args:
        arr: Array of integers
        n: Length of array
        
    Returns:
        Maximum product of subarray
    """
    max_product = -sys.maxsize - 1
    product = 1
    
    # Traverse left to right
    for i in range(n):
        product *= arr[i]
        max_product = max(max_product, product)
        if product == 0:
            product = 1
    
    product = 1
    
    # Traverse right to left
    for i in range(n - 1, -1, -1):
        product *= arr[i]
        max_product = max(max_product, product)
        if product == 0:
            product = 1
    
    return max_product

