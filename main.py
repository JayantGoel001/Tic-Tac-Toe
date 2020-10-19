import random

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
    print("")


def posIsFree(pos):
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


print("Tic Tac Toe\n")
printBoard()


def AIMove():
    possibleMoves = [x for x in range(0, 9) if board[x] == ' ']
    pos = 0
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardTemp = board
            boardTemp[i] = let
            if isWinner(pos, let):
                pos = i
                return pos

    corner = [x for x in possibleMoves if x in [0, 2, 6, 8]]
    if len(corner) > 0:
        pos = random.choice(corner)
        return pos

    if 4 in possibleMoves:
        pos = 4
        return pos

    edges = [x for x in possibleMoves if x in [1, 3, 5, 7]]
    if len(edges) > 0:
        pos = random.choice(edges)
        return pos


while not isBoardFull():
    print("Please Select a position to place\033[1m X \033[0m (0-8):")
    x = int(input())
    if 0 <= x <= 8 and posIsFree(x):
        insertAtPosition("X", x)
        printBoard()
        if isWinner(x, "X"):
            break

        position = AIMove()
        insertAtPosition("O", position)
        printBoard()
        if isWinner(position, "O"):
            break
    elif not (0 <= x <= 8):
        printBoard()
        print("Oops \033[1mPosition " + str(x) + "\033[0m does not exists.\nTry Again\n")
    else:
        printBoard()
        print("\033[1mPosition " + str(x) + "\033[0m Already Occupied By \033[1m" + str(board[x]) + "\033[0m\n")
