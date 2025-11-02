"""
Reverse Words in a String

Reverse order of words in string.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def reverse_string(s: str) -> str:
    """
    Reverse words in string.
    
    Args:
        s: Input string with words separated by spaces
        
    Returns:
        String with words in reverse order
    """
    stack = []
    word = ""
    
    for char in s:
        if word and char == ' ':
            stack.append(word)
            word = ""
        elif char != ' ':
            word += char
    
    # Add last word if exists
    if word:
        stack.append(word)
    
    # Build result by popping from stack
    result = ""
    while stack:
        result += stack.pop()
        if stack:
            result += " "
    
    return result

