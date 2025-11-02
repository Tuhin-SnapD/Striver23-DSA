"""
Rotting Oranges

Find minimum time to rot all oranges using BFS.

Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""

from typing import List
from collections import deque


def min_time_to_rot(grid: List[List[int]], n: int, m: int) -> int:
    """
    Find minimum time to rot all oranges.
    
    Grid: 0 = empty, 1 = fresh, 2 = rotten
    
    Args:
        grid: Grid of oranges
        n: Number of rows
        m: Number of columns
        
    Returns:
        Minimum time, or -1 if impossible
    """
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    
    # Initialize: add all rotten oranges
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append(((i, j), 0))
                visited[i][j] = 2
    
    # Directions: up, left, down, right
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    max_time = 0
    
    while queue:
        (r, c), time = queue.popleft()
        max_time = max(max_time, time)
        
        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc
            
            if (0 <= new_r < n and 0 <= new_c < m and
                visited[new_r][new_c] != 2 and grid[new_r][new_c] == 1):
                queue.append(((new_r, new_c), time + 1))
                visited[new_r][new_c] = 2
    
    # Check if all fresh oranges are rotten
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 2 and grid[i][j] == 1:
                return -1
    
    return max_time

