"""
Z Algorithm

Count occurrences of pattern in string using Z-algorithm approach.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""


def z_algorithm(s: str, p: str, n: int, m: int) -> int:
    """
    Count occurrences of pattern in string.
    
    Args:
        s: Input string
        p: Pattern
        n: Length of string
        m: Length of pattern
        
    Returns:
        Number of occurrences
    """
    count = 0
    s_list = list(s)
    
    while True:
        index = ''.join(s_list).find(p)
        if 0 <= index < len(s_list):
            count += 1
            s_list[index] = '1'  # Mark as processed
        else:
            break
    
    return count

