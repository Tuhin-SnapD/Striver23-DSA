"""
Valid Sudoku

Check if given Sudoku board is valid (can be solved).

Time Complexity: O(9^(empty_cells))
Space Complexity: O(1)
"""

from typing import List


def is_valid(board: List[List[int]], row: int, col: int, c: int) -> bool:
    """
    Check if placing character c at (row, col) is valid.
    
    Args:
        board: 9x9 Sudoku board
        row: Row index
        col: Column index
        c: Character to place (1-9)
        
    Returns:
        True if valid placement, False otherwise
    """
    for i in range(9):
        # Check row
        if board[i][col] == c:
            return False
        
        # Check column
        if board[row][i] == c:
            return False
        
        # Check 3x3 box
        box_row = 3 * (row // 3) + i // 3
        box_col = 3 * (col // 3) + i % 3
        if board[box_row][box_col] == c:
            return False
    
    return True


def is_it_sudoku(board: List[List[int]]) -> bool:
    """
    Check if Sudoku board can be solved (is valid).
    
    Args:
        board: 9x9 Sudoku board (0 represents empty cell)
        
    Returns:
        True if board is valid, False otherwise
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Try each possible value
                for c in range(1, 10):
                    if is_valid(board, i, j, c):
                        board[i][j] = c
                        if is_it_sudoku(board):
                            return True
                        else:
                            board[i][j] = 0
                return False
    
    return True

