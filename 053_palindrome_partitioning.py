"""
Palindrome Partitioning

Partition string such that every substring is a palindrome.

Time Complexity: O(2^n * n)
Space Complexity: O(n)
"""

from typing import List


def is_safe(s: str, start: int, end: int) -> bool:
    """
    Check if substring is palindrome.
    
    Args:
        s: Input string
        start: Start index
        end: End index
        
    Returns:
        True if palindrome, False otherwise
    """
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def solve(
    index: int,
    s: str,
    current: List[str],
    result: List[List[str]]
) -> None:
    """
    Recursive helper to generate all palindrome partitions.
    
    Args:
        index: Current index
        s: Input string
        current: Current partition being built
        result: List to store all partitions
    """
    # Base case: processed entire string
    if index == len(s):
        result.append(current[:])
        return
    
    # Try all possible substrings starting at index
    for i in range(index, len(s)):
        if is_safe(s, index, i):
            current.append(s[index:i + 1])
            solve(i + 1, s, current, result)
            current.pop()


def partition(s: str) -> List[List[str]]:
    """
    Partition string into all possible palindrome substrings.
    
    Args:
        s: Input string
        
    Returns:
        List of all palindrome partitions
    """
    result = []
    current = []
    solve(0, s, current, result)
    return result

