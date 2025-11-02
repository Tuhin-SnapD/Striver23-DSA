"""
Word Break II

Find all possible sentences by adding spaces in string using dictionary words.

Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

from typing import List, Set


def helper(
    s: str,
    str_dict: Set[str],
    result: List[str],
    n: int,
    location: int,
    temp: List[str]
) -> None:
    """
    Recursive helper to generate all word break combinations.
    
    Args:
        s: Input string
        str_dict: Set of dictionary words
        result: List to store all sentences
        n: Length of string
        location: Current position in string
        temp: Current sentence being built
    """
    # Base case: processed entire string
    if location == n:
        result.append(' '.join(temp))
        return
    
    # Try all possible substrings starting at location
    for i in range(location, n):
        substring = s[location:i + 1]
        if substring in str_dict:
            temp.append(substring)
            helper(s, str_dict, result, n, i + 1, temp)
            temp.pop()


def word_break(s: str, dictionary: List[str]) -> List[str]:
    """
    Find all possible sentences using dictionary words.
    
    Args:
        s: Input string
        dictionary: List of valid words
        
    Returns:
        List of all possible sentences
    """
    str_dict = set(dictionary)
    result = []
    temp = []
    n = len(s)
    
    helper(s, str_dict, result, n, 0, temp)
    return result

