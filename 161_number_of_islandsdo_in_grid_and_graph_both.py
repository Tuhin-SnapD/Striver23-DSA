"""
Find Number Of Islands

Count number of islands (connected 1s) in 2D grid (8-directional).

Time Complexity: O(n * m)
Space Complexity: O(n * m) for recursion stack
"""

from typing import List


def dfs(grid: List[List[int]], i: int, j: int, n: int, m: int) -> None:
    """
    DFS to mark all connected 1s as visited (change to 0).
    
    Args:
        grid: 2D grid (modified in-place)
        i: Current row
        j: Current column
        n: Number of rows
        m: Number of columns
    """
    if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != 1:
        return
    
    grid[i][j] = 0
    
    # 8 directions: up, right, down, left, and 4 diagonals
    directions = [
        (-1, 0), (0, 1), (1, 0), (0, -1),
        (-1, 1), (1, -1), (-1, -1), (1, 1)
    ]
    
    for dx, dy in directions:
        dfs(grid, i + dx, j + dy, n, m)


def get_total_islands(grid: List[List[int]], n: int, m: int) -> int:
    """
    Count number of islands in grid.
    
    Args:
        grid: 2D grid (0 = water, 1 = land)
        n: Number of rows
        m: Number of columns
        
    Returns:
        Number of islands
    """
    count = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dfs(grid, i, j, n, m)
                count += 1
    
    return count

