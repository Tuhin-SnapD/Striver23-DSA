"""
Valid Parentheses

Check if parentheses in string are balanced and properly nested.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def is_valid_parenthesis(expression: str) -> bool:
    """
    Check if parentheses are valid using stack.
    
    Args:
        expression: String containing parentheses
        
    Returns:
        True if valid, False otherwise
    """
    # Odd length cannot be valid
    if len(expression) % 2 == 1:
        return False
    
    stack = []
    mapping = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    for char in expression:
        if char in mapping:  # Opening bracket
            stack.append(char)
        else:  # Closing bracket
            if not stack:
                return False
            if mapping[stack[-1]] != char:
                return False
            stack.pop()
    
    return len(stack) == 0

