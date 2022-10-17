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

class Player:
    def __init__(self):
        self.num_wins = 0
        self.num_losses = 0
        self.num_draws = 0
        self.total = 0

    def move(self,board):
        pass

    def onWin(self):
        pass

    def onLoss(self):
        pass

    def onDraw(self):
        pass


class RandomPlayer(Player):
    def move(self,board):
        return random.choice(np.nonzero(board == 0)[0])
    
    def onWin(self):
        self.num_wins+=1

    def onLoss(self):
        self.num_losses+=1

    def onDraw(self):
        self.num_draws+=1

class Board:
    def __init__(self,num_games = 10_000,player1 = RandomPlayer(),
            player2 = RandomPlayer()):
        self.num_games = num_games
        self.player1 = player1
        self.player2 = player2

    #1 for player1, -1 for player2
    def playGame(self,first_move = 1):
        move_fn = [None,self.player1.move,self.player2.move]
        playerID = first_move
        board = np.zeros((9))
        gameState = winCheck(board)
        while gameState == None:
            board[move_fn[playerID](board)] = playerID 
            playerID*=-1
            gameState = winCheck(board)
        return gameState

    def playGames(self):
        first_move = 1
        for i in range(self.num_games):
            result = self.playGame(first_move)
            if result == 0:
                self.player1.onDraw()
                self.player2.onDraw()
            elif result == 1:
                self.player1.onWin()
                self.player2.onLoss()
            else:
                self.player1.onLoss()
                self.player2.onWin()
            first_move *=-1            


board = np.zeros((9))
player = 1
p1 = RandomPlayer()
p2 = RandomPlayer()
b = Board(10_000,p1,p2)
b.playGames()
print(p1.num_wins,p2.num_wins)
