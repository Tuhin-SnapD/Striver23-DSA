"""
Roman Numeral To Integer

Convert Roman numeral string to integer.

Time Complexity: O(n) where n is length of string
Space Complexity: O(1)
"""


def roman_to_int(s: str) -> int:
    """
    Convert Roman numeral to integer.
    
    Args:
        s: Roman numeral string
        
    Returns:
        Integer value
    """
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    n = len(s)
    
    for i in range(n):
        curr_val = values[s[i]]
        
        # Check if next character exists and is greater
        if i + 1 < n and values[s[i + 1]] > curr_val:
            total -= curr_val
        else:
            total += curr_val
    
    return total

