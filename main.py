board = [' ' for _ in range(10)]

def insertAtPosition(letter, pos):
    board[pos] = letter

def printBoard(board):
    print("\n")
    print("     |     |     ")
    print("  "+board[0]+"  |  "+board[1]+"  |  "+board[2]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[4]+"  |  "+board[5]+"  |  "+board[6]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[7]+"  |  "+board[8]+"  |  "+board[9]+"  ")
    print("     |     |     ")


printBoard(board)