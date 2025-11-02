"""
Next Greater Element

Find next greater element for each element in array.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


def next_greater(arr: List[int], n: int) -> List[int]:
    """
    Find next greater element for each element.
    
    Args:
        arr: Array of integers
        n: Length of array
        
    Returns:
        Array with next greater elements
    """
    stack = [-1]
    
    for i in range(n - 1, -1, -1):
        curr = arr[i]
        
        # Pop elements smaller than or equal to current
        while stack and stack[-1] != -1 and stack[-1] <= curr:
            stack.pop()
        
        # Set next greater element
        if stack and stack[-1] != -1:
            arr[i] = stack[-1]
        else:
            arr[i] = -1
        
        stack.append(curr)
    
    return arr

