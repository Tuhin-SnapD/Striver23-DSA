"""
Flood Fill Algorithm

Fill connected region starting from given position with new color.

Time Complexity: O(n * m)
Space Complexity: O(n * m) for recursion stack
"""

from typing import List


def dfs(
    image: List[List[int]],
    row: int,
    col: int,
    new_color: int,
    initial_color: int,
    result: List[List[int]],
    del_row: List[int],
    del_col: List[int]
) -> None:
    """
    DFS to fill connected region.
    
    Args:
        image: Original image
        row: Current row
        col: Current column
        new_color: New color to fill
        initial_color: Original color to replace
        result: Result image
        del_row: Row direction deltas
        del_col: Column direction deltas
    """
    result[row][col] = new_color
    n = len(image)
    m = len(image[0])
    
    # Check 4 directions
    for i in range(4):
        new_row = row + del_row[i]
        new_col = col + del_col[i]
        
        if (0 <= new_row < n and 0 <= new_col < m and
            image[new_row][new_col] == initial_color and
            result[new_row][new_col] != new_color):
            dfs(image, new_row, new_col, new_color, initial_color,
                result, del_row, del_col)


def flood_fill(
    image: List[List[int]],
    sr: int,
    sc: int,
    new_color: int
) -> List[List[int]]:
    """
    Fill connected region with new color.
    
    Args:
        image: 2D image matrix
        sr: Starting row
        sc: Starting column
        new_color: New color to fill
        
    Returns:
        Modified image
    """
    initial_color = image[sr][sc]
    result = [row[:] for row in image]
    del_row = [-1, 0, 1, 0]
    del_col = [0, 1, 0, -1]
    
    dfs(image, sr, sc, new_color, initial_color, result, del_row, del_col)
    return result

