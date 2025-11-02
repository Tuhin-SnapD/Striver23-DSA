"""
Minimum Characters For Palindrome

Find minimum characters to add at beginning to make string palindrome.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def is_palindrome(s: str, i: int, j: int) -> bool:
    """
    Check if substring is palindrome.
    
    Args:
        s: String
        i: Start index
        j: End index
        
    Returns:
        True if palindrome, False otherwise
    """
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def min_chars_for_palindrome(s: str) -> int:
    """
    Find minimum characters to add at beginning.
    
    Args:
        s: Input string
        
    Returns:
        Minimum characters needed
    """
    n = len(s)
    i = 0
    j = n - 1
    
    # Find longest suffix that is palindrome
    while i <= j:
        if is_palindrome(s, i, j):
            break
        j -= 1
    
    # Characters needed = length of prefix before palindrome
    return n - j - 1

