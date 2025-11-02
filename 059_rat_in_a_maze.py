"""
Rat in a Maze - All Paths

Find all paths from (0,0) to (n-1, n-1) in a maze.

Time Complexity: O(4^(n^2))
Space Complexity: O(n^2)
"""

from typing import List


def is_safe(
    x: int,
    y: int,
    n: int,
    visited: List[List[int]],
    maze: List[List[int]]
) -> bool:
    """
    Check if cell (x, y) is valid and can be visited.
    
    Args:
        x: Row index
        y: Column index
        n: Size of maze
        visited: Visited cells matrix
        maze: Maze matrix (1 = path, 0 = wall)
        
    Returns:
        True if safe to visit, False otherwise
    """
    return (0 <= x < n and 0 <= y < n and
            visited[x][y] == 0 and maze[x][y] == 1)


def find_path(
    x: int,
    y: int,
    maze: List[List[int]],
    n: int,
    visited: List[List[int]],
    result: List[List[int]]
) -> None:
    """
    Find all paths using backtracking.
    
    Args:
        x: Current row
        y: Current column
        maze: Maze matrix
        n: Size of maze
        visited: Visited cells matrix
        result: List to store all path configurations
    """
    # Base case: reached destination
    if x == n - 1 and y == n - 1:
        visited[x][y] = 1
        
        # Store current path
        path = []
        for i in range(n):
            for j in range(n):
                path.append(visited[i][j])
        
        result.append(path)
        visited[x][y] = 0
        return
    
    visited[x][y] = 1
    
    # Try all 4 directions: Down, Up, Left, Right
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        if is_safe(new_x, new_y, n, visited, maze):
            find_path(new_x, new_y, maze, n, visited, result)
    
    # Backtrack
    visited[x][y] = 0


def rat_in_a_maze(maze: List[List[int]], n: int) -> List[List[int]]:
    """
    Find all paths for rat to reach destination.
    
    Args:
        maze: Maze matrix (1 = path, 0 = wall)
        n: Size of maze
        
    Returns:
        List of all path configurations
    """
    visited = [[0] * n for _ in range(n)]
    result = []
    
    if maze[0][0] == 0:
        return result
    
    find_path(0, 0, maze, n, visited, result)
    return result

