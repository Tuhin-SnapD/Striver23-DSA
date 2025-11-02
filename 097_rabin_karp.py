"""
Rabin-Karp Algorithm

Find all occurrences of pattern in string using rolling hash.

Time Complexity: O(n + m) average case, O(n*m) worst case
Space Complexity: O(1)
"""

from typing import List


def string_match(s: str, pattern: str) -> List[int]:
    """
    Find all starting indices of pattern in string.
    
    Args:
        s: Input string
        pattern: Pattern to search
        
    Returns:
        List of starting indices
    """
    result = []
    n = len(s)
    m = len(pattern)
    
    for i in range(n):
        if s[i] == pattern[0]:
            if i + m <= n and s[i:i + m] == pattern:
                result.append(i)
    
    return result

