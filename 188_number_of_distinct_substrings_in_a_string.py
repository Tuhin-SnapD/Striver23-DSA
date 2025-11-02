"""
Number Of Distinct Substring

Count number of distinct substrings in a string.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""


def distinct_substring(word: str) -> int:
    """
    Count distinct substrings using set.
    
    Args:
        word: Input string
        
    Returns:
        Number of distinct substrings
    """
    distinct = set()
    n = len(word)
    
    # Generate all substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = word[i:j]
            distinct.add(substring)
    
    return len(distinct)

