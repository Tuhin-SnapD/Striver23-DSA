"""
The Celebrity Problem

Find celebrity in party (everyone knows celebrity, celebrity knows no one).

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Callable


def find_celebrity(n: int, knows: Callable[[int, int], bool]) -> int:
    """
    Find celebrity using stack approach.
    
    Args:
        n: Number of people
        knows: Function knows(A, B) returns True if A knows B
        
    Returns:
        Celebrity ID, or -1 if no celebrity exists
    """
    stack = list(range(n))
    
    # Eliminate non-celebrities by comparing pairs
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        
        if knows(a, b):
            # a knows b, so a is not celebrity
            stack.append(b)
        else:
            # a doesn't know b, so b is not celebrity
            stack.append(a)
    
    # Remaining candidate
    candidate = stack[0]
    
    # Verify candidate is celebrity
    for i in range(n):
        if i != candidate:
            # Celebrity should not know anyone
            if knows(candidate, i):
                return -1
            # Everyone should know celebrity
            if not knows(i, candidate):
                return -1
    
    return candidate

