#!/usr/bin/python3
"""0-nqueens"""

import sys

def is_safe(board, row, col, n):
    """Checks if a queen can be placed at a given position on the board without being attacked by any other queen.

    Args:
        board (list): A list of column indices where queens have been placed so far.
        row (int): The current row being processed.
        col (int): The current column being considered.
        n (int): The size of the board.

    Returns:
        bool: True if the queen can be placed at the given position, else False.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row=0, board=[]):
    """Solves the N queens problem using a recursive backtracking approach.

    Args:
        n (int): The size of the board.
        row (int, optional): The current row being processed. Defaults to 0.
        board (list, optional): A list of column indices where queens have been placed so far. Defaults to an empty list.

    Returns:
        None
    """
    if row == n:
        print([[i, col] for i, col in enumerate(board)])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board.append(col)
            solve_nqueens(n, row + 1, board)
            board.pop()

def main():
    """The main function that checks the command-line arguments and calls the solve_nqueens function.

    Returns:
        None
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(n)

if __name__ == "__main__":
    main()