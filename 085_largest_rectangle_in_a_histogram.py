"""
Largest Rectangle in Histogram

Find largest rectangle area in histogram.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
import sys


def next_smaller(arr: List[int], n: int) -> List[int]:
    """Find next smaller element index for each element."""
    stack = [-1]
    result = [0] * n
    
    for i in range(n - 1, -1, -1):
        curr = arr[i]
        while stack[-1] != -1 and arr[stack[-1]] >= curr:
            stack.pop()
        result[i] = stack[-1]
        stack.append(i)
    
    return result


def prev_smaller(arr: List[int], n: int) -> List[int]:
    """Find previous smaller element index for each element."""
    stack = [-1]
    result = [0] * n
    
    for i in range(n):
        curr = arr[i]
        while stack[-1] != -1 and arr[stack[-1]] >= curr:
            stack.pop()
        result[i] = stack[-1]
        stack.append(i)
    
    return result


def largest_rectangle(heights: List[int]) -> int:
    """
    Find largest rectangle area in histogram.
    
    Args:
        heights: Heights of bars in histogram
        
    Returns:
        Maximum rectangle area
    """
    n = len(heights)
    
    next_small = next_smaller(heights, n)
    prev_small = prev_smaller(heights, n)
    
    max_area = -sys.maxsize - 1
    
    for i in range(n):
        length = heights[i]
        
        if next_small[i] == -1:
            next_small[i] = n
        
        breadth = next_small[i] - prev_small[i] - 1
        area = length * breadth
        max_area = max(max_area, area)
    
    return max_area

