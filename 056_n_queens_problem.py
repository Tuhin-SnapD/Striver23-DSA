"""
N Queens Problem

Place N queens on N×N chessboard such that no two queens attack each other.

Time Complexity: O(N!)
Space Complexity: O(N^2)
"""

from typing import List


def add_board(board: List[List[int]], result: List[List[int]]) -> None:
    """
    Add current board configuration to result.
    
    Args:
        board: Current board configuration
        result: List to store all valid configurations
    """
    temp = []
    n = len(board)
    
    for i in range(n):
        for j in range(n):
            temp.append(board[i][j])
    
    result.append(temp)


def helper(
    col: int,
    board: List[List[int]],
    n: int,
    left_row: List[bool],
    left_upper_diagonal: List[bool],
    left_lower_diagonal: List[bool],
    result: List[List[int]]
) -> None:
    """
    Recursive helper to place queens using backtracking.
    
    Args:
        col: Current column
        board: Chessboard
        n: Size of board
        left_row: Track queens in rows
        left_upper_diagonal: Track queens in upper diagonals
        left_lower_diagonal: Track queens in lower diagonals
        result: List to store valid configurations
    """
    if col == n:
        add_board(board, result)
        return
    
    for row in range(n):
        # Check if queen can be placed
        if (not left_row[row] and
            not left_lower_diagonal[row + col] and
            not left_upper_diagonal[n - 1 + col - row]):
            
            # Place queen
            board[row][col] = 1
            left_row[row] = True
            left_lower_diagonal[row + col] = True
            left_upper_diagonal[n - 1 + col - row] = True
            
            # Recurse for next column
            helper(
                col + 1, board, n, left_row,
                left_upper_diagonal, left_lower_diagonal, result
            )
            
            # Backtrack
            board[row][col] = 0
            left_row[row] = False
            left_lower_diagonal[row + col] = False
            left_upper_diagonal[n - 1 + col - row] = False


def solve_n_queens(n: int) -> List[List[int]]:
    """
    Solve N-Queens problem.
    
    Args:
        n: Size of board (n×n) and number of queens
        
    Returns:
        List of all valid board configurations
    """
    left_row = [False] * n
    left_upper_diagonal = [False] * (2 * n - 1)
    left_lower_diagonal = [False] * (2 * n - 1)
    
    board = [[0] * n for _ in range(n)]
    result = []
    
    helper(0, board, n, left_row, left_upper_diagonal, left_lower_diagonal, result)
    
    return result

