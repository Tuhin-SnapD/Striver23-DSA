"""
Sort a Stack

Sort stack using recursion without using extra space (except recursion stack).

Time Complexity: O(n^2)
Space Complexity: O(n) for recursion stack
"""

from typing import List


def insert(s: List[int], temp: int) -> None:
    """
    Insert element in sorted position in stack.
    
    Args:
        s: Stack (list)
        temp: Element to insert
    """
    if not s or s[-1] <= temp:
        s.append(temp)
        return
    
    val = s.pop()
    insert(s, temp)
    s.append(val)


def sort_stack(s: List[int]) -> None:
    """
    Sort stack using recursion.
    
    Args:
        s: Stack to sort (modified in-place)
    """
    if len(s) == 1:
        return
    
    temp = s.pop()
    sort_stack(s)
    insert(s, temp)

