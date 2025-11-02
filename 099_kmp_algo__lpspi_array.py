"""
Find Pattern in String - KMP Algorithm

Check if pattern exists in string (simplified version).

Time Complexity: O(n + m)
Space Complexity: O(m)
"""


def find_pattern(pattern: str, text: str) -> bool:
    """
    Check if pattern exists in string.
    
    Args:
        pattern: Pattern to search
        text: Input string
        
    Returns:
        True if pattern found, False otherwise
    """
    return pattern in text

