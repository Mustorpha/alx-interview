import sys

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row=0, board=[]):
    if row == n:
        print([[i, col] for i, col in enumerate(board)])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board.append(col)
            solve_nqueens(n, row + 1, board)
            board.pop()

def main():
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