"""
Print Permutations - String

Generate all permutations of a string.

Time Complexity: O(n! * n)
Space Complexity: O(n!)
"""

from typing import List


def helper(index: int, s: List[str], result: List[str]) -> None:
    """
    Recursive helper to generate all permutations.
    
    Args:
        index: Current index
        s: String as list of characters
        result: List to store all permutations
    """
    if index >= len(s):
        result.append(''.join(s))
        return
    
    # Try each character at current position
    for i in range(index, len(s)):
        # Swap characters
        s[index], s[i] = s[i], s[index]
        helper(index + 1, s, result)
        # Backtrack
        s[index], s[i] = s[i], s[index]


def find_permutations(s: str) -> List[str]:
    """
    Find all permutations of string.
    
    Args:
        s: Input string
        
    Returns:
        List of all permutations
    """
    result = []
    s_list = list(s)
    helper(0, s_list, result)
    return result

