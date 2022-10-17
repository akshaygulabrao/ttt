import random
import numpy as np

def winCheck(board):
    b = board.reshape((3,3))
    cols = np.sum(b,axis=1)
    rows = np.sum(b,axis=0)
    diag1= int(sum(np.diag(b)))
    diag2 = int(sum(np.diag(np.fliplr(b))))
    if 3 in cols or 3 in rows or diag1 == 3 or diag2 == 3:
        return 1
    elif -3 in cols or -3 in rows or diag1 == -3 or diag2 == -3:
        return -1
    elif 0 not in board:
        return 0
    return None 
board = np.zeros((9))
player = 1

while winCheck(board) == None:
    board[random.choice(np.nonzero(board==0)[0])] = player 
    player*=-1
    print(board.reshape((3,3)))
print(winCheck(board))
