#!/usr/bin/python3
"""Solves the N-queens puzzle.

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list representing the chessboard.
    soln (list): A list containing solutions.
"""

import sys


def init_chessboard(n):
    """Initializes a `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def chess_copy(board):
    """Returns a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(chess_copy, board))
    return (board)


def get_solutions(board):
    """Returns the list of lists representation of a solved chessboard."""
    soln = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                soln.append([r, c])
                break
    return (soln)


def xout(board, row, col):
    """X out spots on a chessboard.
    Spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        OA
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def rec_solve(board, row, Q, soln):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        Q (int): The current number of placed queens.
        soln (list): A list of solutions.

    Returns:
        soln
    """
    if Q == len(board):
        soln.append(get_solutions(board))
        return (soln)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = chess_copy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            soln = rec_solve(tmp_board, row + 1, Q + 1, soln)

    return (soln)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_chessboard(int(sys.argv[1]))
    soln = rec_solve(board, 0, 0, [])
    for sn in soln:
        print(sn)
