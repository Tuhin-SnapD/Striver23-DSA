"""
M-Coloring Problem

Check if graph can be colored with m colors such that no adjacent nodes
have same color.

Time Complexity: O(m^n)
Space Complexity: O(n)
"""

from typing import List


def can_color(
    mat: List[List[int]],
    paint: List[int],
    n: int,
    color: int,
    m: int,
    node: int
) -> bool:
    """
    Check if node can be colored with given color.
    
    Args:
        mat: Adjacency matrix
        paint: Current color assignment
        n: Number of nodes
        color: Color to assign
        m: Number of colors available
        node: Current node
        
    Returns:
        True if coloring is valid, False otherwise
    """
    # Check if any neighbor has same color
    for i in range(n):
        if i != node and mat[node][i] == 1 and paint[i] == color:
            return False
    return True


def recur(
    mat: List[List[int]],
    paint: List[int],
    n: int,
    m: int,
    start: int
) -> bool:
    """
    Recursive helper to try coloring graph.
    
    Args:
        mat: Adjacency matrix
        paint: Current color assignment
        n: Number of nodes
        m: Number of colors
        start: Current node being colored
        
    Returns:
        True if graph can be colored, False otherwise
    """
    # Base case: colored all nodes
    if start == n:
        return True
    
    # Try each color for current node
    for i in range(1, m + 1):
        if can_color(mat, paint, n, i, m, start):
            paint[start] = i
            if recur(mat, paint, n, m, start + 1):
                return True
            # Backtrack
            paint[start] = 0
    
    return False


def graph_coloring(mat: List[List[int]], m: int) -> str:
    """
    Check if graph can be colored with m colors.
    
    Args:
        mat: Adjacency matrix
        m: Number of colors
        
    Returns:
        "YES" if possible, "NO" otherwise
    """
    n = len(mat)
    paint = [0] * n
    
    if recur(mat, paint, n, m, 0):
        return "YES"
    return "NO"

