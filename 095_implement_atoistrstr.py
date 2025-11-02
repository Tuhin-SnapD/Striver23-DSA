"""
Implement Atoi Function

Convert string to integer (atoi function).

Time Complexity: O(n) where n is length of string
Space Complexity: O(1)
"""


def atoi(s: str) -> int:
    """
    Convert string to integer.
    
    Handles leading whitespace, optional sign, and digits.
    
    Args:
        s: Input string
        
    Returns:
        Integer value
    """
    n = len(s)
    if n == 0:
        return 0
    
    # Skip leading whitespace
    i = 0
    while i < n and s[i] == ' ':
        i += 1
    
    if i == n:
        return 0
    
    # Check sign
    sign = 1
    if s[i] == '-':
        sign = -1
    
    # Move past sign if present
    i = i + 1 if (s[i] == '+' or s[i] == '-') else i
    
    result = 0
    
    # Process digits
    while i < n:
        if s[i].isdigit():
            result = result * 10 + int(s[i])
        i += 1
    
    return sign * result

