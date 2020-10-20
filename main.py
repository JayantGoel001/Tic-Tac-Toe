import random
from time import sleep

TTTBoard = [' ' for _ in range(9)]


def insertAtPosition(letter, pos):
    TTTBoard[pos] = letter


def printBoard():
    print("     |     |     ")
    print("  " + TTTBoard[0] + "  |  " + TTTBoard[1] + "  |  " + TTTBoard[2] + "  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + TTTBoard[3] + "  |  " + TTTBoard[4] + "  |  " + TTTBoard[5] + "  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + TTTBoard[6] + "  |  " + TTTBoard[7] + "  |  " + TTTBoard[8] + "  ")
    print("     |     |     ")
    print("")


def posIsFree(pos):
    return TTTBoard[pos] == ' '


def isBoardFull():
    return TTTBoard.count(' ') == 0


def isWinner(move, board=TTTBoard):
    return (board[0] == move and board[1] == move and board[2] == move) or (
            board[3] == move and board[4] == move and board[5] == move) or (
            board[6] == move and board[7] == move and board[8] == move) or (
            board[0] == move and board[3] == move and board[6] == move) or (
            board[1] == move and board[4] == move and board[7] == move) or (
            board[2] == move and board[5] == move and board[8] == move) or (
            board[0] == move and board[4] == move and board[8] == move) or (
            board[2] == move and board[4] == move and board[6] == move)


print("Tic Tac Toe\n")
printBoard()

def AIMove():
    possibleMoves = [x for x in range(0, 9) if TTTBoard[x] == ' ']
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardTemp = TTTBoard[:]
            boardTemp[i] = let
            if isWinner(let, boardTemp):
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
        if isWinner("X"):
            print("\033[1mCongratulations \nYou Won The Game.\033[0m")
            break

        print("AI is Thinking....")
        sleep(2)

        position = AIMove()
        insertAtPosition("O", position)
        printBoard()
        if isWinner("O"):
            print("\033[1mAI Won The Game.\033[0m")
            break

        if isBoardFull():
            print("\033[1mGame Resulted in Tie\033[0m")
            break
    elif not (0 <= x <= 8):
        printBoard()
        print("Oops \033[1mPosition " + str(x) + "\033[0m does not exists.\nTry Again\n")
    else:
        printBoard()
        print("\033[1mPosition " + str(x) + "\033[0m Already Occupied By \033[1m" + str(TTTBoard[x]) + "\033[0m\n")
