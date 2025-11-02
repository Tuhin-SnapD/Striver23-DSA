"""
Majority Element II

Find all elements that appear more than n/3 times in an array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def majority_element_ii(arr: List[int]) -> List[int]:
    """
    Find all majority elements (appearing more than n/3 times) using Boyer-Moore algorithm.
    
    Uses extended Boyer-Moore voting algorithm for two candidates.
    
    Args:
        arr: Array of integers
        
    Returns:
        List of majority elements
    """
    n = len(arr)
    
    # Candidates for majority elements
    num1 = -1
    num2 = -1
    count1 = 0
    count2 = 0
    
    # Phase 1: Find potential candidates
    for num in arr:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1
        elif count1 == 0:
            num1 = num
            count1 = 1
        elif count2 == 0:
            num2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    # Phase 2: Verify candidates
    ans = []
    count1 = count2 = 0
    
    for num in arr:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1
    
    if count1 > n // 3:
        ans.append(num1)
    if count2 > n // 3:
        ans.append(num2)
    
    return ans

