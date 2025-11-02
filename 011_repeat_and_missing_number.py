"""
Missing and Repeating Numbers

Find the missing and repeating numbers in an array containing numbers from 1 to n.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Tuple


def missing_and_repeating(arr: List[int], n: int) -> Tuple[int, int]:
    """
    Find missing and repeating numbers in array.
    
    Args:
        arr: List containing n integers (one missing, one repeating)
        n: Expected range (1 to n)
        
    Returns:
        Tuple of (missing_number, repeating_number)
    """
    # Create a frequency array
    freq = [0] * (n + 1)
    freq[0] = 1  # Mark 0 as visited (won't be used)
    
    repeating = -1
    missing = -1
    
    # Find the repeating number
    for num in arr:
        if freq[num] == 1:
            repeating = num
        freq[num] = 1
    
    # Find the missing number
    for i in range(1, n + 1):
        if freq[i] == 0:
            missing = i
            break
    
    return (missing, repeating)

