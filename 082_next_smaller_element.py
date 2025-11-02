"""
Next Smaller Element

Find next smaller element for each element in array.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


def next_smaller_element(arr: List[int], n: int) -> List[int]:
    """
    Find next smaller element for each element.
    
    Args:
        arr: Array of integers
        n: Length of array
        
    Returns:
        Array with next smaller elements
    """
    stack = [-1]
    result = [0] * n
    
    for i in range(n - 1, -1, -1):
        curr = arr[i]
        
        # Pop elements greater than or equal to current
        while stack[-1] >= curr:
            stack.pop()
        
        result[i] = stack[-1]
        stack.append(curr)
    
    return result

