"""
Count And Say

Generate nth term of count-and-say sequence.

Time Complexity: O(2^n) approximately
Space Complexity: O(2^n)
"""


def generate(n: int) -> str:
    """
    Recursively generate nth term of count-and-say sequence.
    
    Args:
        n: Term number
        
    Returns:
        nth term as string
    """
    if n == 1:
        return "1"
    
    prev = generate(n - 1)
    result = ""
    i = 0
    
    while i < len(prev):
        count = 1
        # Count consecutive same characters
        while i < len(prev) - 1 and prev[i] == prev[i + 1]:
            count += 1
            i += 1
        
        result += str(count) + prev[i]
        i += 1
    
    return result


def write_as_you_speak(n: int) -> str:
    """
    Get nth term of count-and-say sequence.
    
    Args:
        n: Term number
        
    Returns:
        nth term as string
    """
    return generate(n)

