#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """Print the usage message and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col].

    Args:
        board (list): The chessboard.
        row (int): The current row.
        col (int): The current column.

    Returns:
        bool: True if the queen can be placed, False otherwise.
    """
    # Check this column on upper side
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N):
    """Utilize backtracking to find all solutions for N queens.

    Args:
        board (list): The chessboard.
        row (int): The current row.
        N (int): The number of queens (and size of the board).
    """
    if row == N:
        # All queens are placed successfully, print the solution
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col  # Place the queen
            solve_nqueens(board, row + 1, N)  # Recur to place rest


def main():
    """Main function to handle the input and solve the N queens problem."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N  # Initialize the board
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
