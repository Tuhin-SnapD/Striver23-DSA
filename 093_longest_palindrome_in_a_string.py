"""
Longest Palindrome in a String

Find the longest palindromic substring in a string.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def longest_palindrome(s: str) -> str:
    """
    Find longest palindromic substring.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    # Expand around center approach
    def expand_around_center(left: int, right: int) -> tuple:
        """Expand around center and return start and length."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1
    
    # Check for odd-length palindromes
    for i in range(len(s)):
        start_temp, len_temp = expand_around_center(i, i)
        if len_temp > max_len:
            max_len = len_temp
            start = start_temp
        
        # Check for even-length palindromes
        start_temp, len_temp = expand_around_center(i, i + 1)
        if len_temp > max_len:
            max_len = len_temp
            start = start_temp
    
    return s[start:start + max_len]
