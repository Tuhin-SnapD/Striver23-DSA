"""
Word Break

Check if string can be segmented into words from dictionary.

Time Complexity: O(n^2 * m) where n is string length, m is dict size
Space Complexity: O(n)
"""

from typing import List, Dict


dp: Dict[str, int] = {}


def solve(target: str, arr: List[str]) -> int:
    """
    Recursive helper with memoization.
    
    Args:
        target: Remaining string to check
        arr: Dictionary of words
        
    Returns:
        1 if breakable, -1 otherwise
    """
    size = len(target)
    
    if size == 0:
        return 1
    
    if target in dp:
        return dp[target]
    
    # Try all possible prefixes
    for i in range(1, size + 1):
        prefix = target[:i]
        
        # Check if prefix is in dictionary
        found = False
        for word in arr:
            if prefix == word:
                found = True
                break
        
        # If prefix found, check remaining suffix
        if found and solve(target[i:], arr) == 1:
            dp[target] = 1
            return 1
    
    dp[target] = -1
    return -1


def word_break(arr: List[str], n: int, target: str) -> bool:
    """
    Check if string can be broken into dictionary words.
    
    Args:
        arr: Dictionary of words
        n: Number of words in dictionary
        target: String to check
        
    Returns:
        True if breakable, False otherwise
    """
    dp.clear()
    result = solve(target, arr)
    return result == 1

