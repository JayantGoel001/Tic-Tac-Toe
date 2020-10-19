board = [' ' for _ in range(9)]


def insertAtPosition(letter, pos):
    board[pos] = letter


def printBoard():
    print("     |     |     ")
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  ")
    print("     |     |     ")
    print("\n")


def safeIsFree(pos):
    return board[pos] == ' '


def isBoardFull():
    return board.count(' ') == 0


def isWinner(pos, move):
    for i in range(3):
        if board[(i + pos) % 3] != move:
            return False

    for i in range(3):
        if board[(i + 3 * pos) % 3] != move:
            return False

    if pos in [0, 4, 8]:
        for i in range(3):
            if board[4 * i] != move:
                return False

    if pos in [2, 4, 6]:
        for i in range(3):
            if board[2 * i + 2] != move:
                return False

    return True
