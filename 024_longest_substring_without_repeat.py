"""
Longest Palindromic Substring

Find the longest palindromic substring in a string.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def longest_palin_substring(s: str) -> str:
    """
    Find longest palindromic substring using expansion around centers.
    
    Checks both even and odd length palindromes.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    n = len(s)
    start = 0
    max_length = 1
    
    for i in range(1, n):
        # Check for even length palindrome (center between i-1 and i)
        left = i - 1
        right = i
        
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1
        
        # Check for odd length palindrome (center at i)
        left = i - 1
        right = i + 1
        
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1
    
    return s[start:start + max_length]

