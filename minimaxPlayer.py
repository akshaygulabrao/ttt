import random
import numpy as np
import copy
from player import Player
from state import State

class minimaxPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self,board):
        a,b =  self.minimax(board,2,minimaxPlayer.evalID(board))
        if board[b] != 0:
            choices = np.nonzero(board == 0)
            numChoices = len(choices[0])
            randIndex = random.randint(0,numChoices - 1)
            return choices[0][randIndex], choices[1][randIndex]
        else: return b
    
    def minimax(self,board,depth,playerID):
        result = minimaxPlayer.winCheck(board)
        if result is not None:
            if result == -1:
                return -1000,None
            if result == 1:
                return 1000,None
            if result == 0:
                return 0,None
        elif depth == 0:
            return State(board).eval,None
        elif playerID == 1:
            value = -1000
            child_nodes = np.nonzero(board == 0)
            len_child_nodes = len(child_nodes[0])
            best_move = (0,0)
            for i in range(len_child_nodes):
                b2 = board.copy()
                b2[child_nodes[0][i], child_nodes[1][i]] = 1
                child_value = self.minimax(b2, depth-1, -1)[0]
                if child_value > value:
                    best_move = (child_nodes[0][i], child_nodes[1][i])
                    value = child_value
            return value,best_move
        elif playerID == -1:
            value = 1000
            child_nodes = np.nonzero(board == 0)
            len_child_nodes = len(child_nodes[0])
            best_move = (0,0)
            for i in range(len_child_nodes):
                b2 = board.copy()
                b2[child_nodes[0][i], child_nodes[1][i]] = -1
                child_value = self.minimax(b2, depth-1, 1)[0]
                if child_value < value:
                    best_move = (child_nodes[0][i], child_nodes[1][i])
                    value = child_value
            return value,best_move

    @staticmethod
    def evalID(board):
        if np.count_nonzero(board == 1) > np.count_nonzero(board == -1):
            return -1
        else:
            return 1
    
    @staticmethod
    def winCheck(b):
        cols = np.sum(b,axis=1)
        rows = np.sum(b,axis=0)
        diag1= int(sum(np.diag(b)))
        diag2 = int(sum(np.diag(np.fliplr(b))))
        if 3 in cols or 3 in rows or diag1 == 3 or diag2 == 3:
            return 1
        elif -3 in cols or -3 in rows or diag1 == -3 or diag2 == -3:
            return -1
        elif 0 not in b:
            return 0
        return None
    
    @staticmethod
    def evalBoard(self):
        board = self.board 
        playerID = self.playerID
        ans = -50 if playerID != self.evalID() else 0
        x2 = 0
        x1 = 0
        o2 = 0
        o1 = 0
        # rows
        for row in board:
            blanks = np.count_nonzero(row == 0)
            enemy = np.count_nonzero(row == -1 )
            ally = np.count_nonzero(row == 1)
            if blanks == 2 and enemy == 1:
                o1 +=1
            elif blanks == 2 and ally == 1:
                x1 +=1
            elif blanks == 1 and enemy == 2:
                o2 +=1
            elif blanks == 1 and ally == 2:
                x2 += 1
            elif enemy == 3:
                return -1000
            elif ally == 3:
                return 1000
        # columns
        for row in board.T:
            blanks = np.count_nonzero(row == 0)
            enemy = np.count_nonzero(row == -1 )
            ally = np.count_nonzero(row == 1)
            if blanks == 2 and enemy == 1:
                o1 +=1
            elif blanks == 2 and ally == 1:
                x1 +=1
            elif blanks == 1 and enemy == 2:
                o2 +=1
            elif blanks == 1 and ally == 2:
                x2 += 1
            elif enemy == 3:
                return -1000
            elif ally == 3:
                return 1000
        # northwest-diag
        diags = [np.diag(board),np.diag(np.fliplr(board))]
        for diag in diags:
            blanks = np.count_nonzero(diag == 0)
            enemy = np.count_nonzero(diag == -1)
            ally = np.count_nonzero(diag == 1)
            if blanks == 2 and enemy == 1:
                o1 +=1
            elif blanks == 2 and ally == 1:
                x1 +=1
            elif blanks == 1 and enemy == 2:
                o2 +=1
            elif blanks == 1 and ally == 2:
                x2 += 1
            elif enemy == 3:
                return -1000
            elif ally == 3:
                return 1000
        ans+= (3 * x2 + x1) - (3 * o2 + o1)
        return ans
    
    @staticmethod 
    def generateChildStates(board):
        root = State(board)
    
    def onWin(self):
        self.num_wins+=1

    def onLoss(self):
        self.num_losses+=1

    def onDraw(self):
        self.num_draws+=1
	


