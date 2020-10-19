board = [' ' for _ in range(9)]

def insertAtPosition(letter, pos):
    board[pos] = letter

def printBoard():
    print("     |     |     ")
    print("  "+board[0]+"  |  "+board[1]+"  |  "+board[2]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[3]+"  |  "+board[4]+"  |  "+board[5]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[6]+"  |  "+board[7]+"  |  "+board[8]+"  ")
    print("     |     |     ")
    print("\n")

def safeIsFree(pos):
    return board[pos]==' '

def isBoardFull():
    return board.count(' ')==0

