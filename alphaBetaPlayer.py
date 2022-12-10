import random
import numpy as np
import copy
from player import Player
from state import State

class alphaBetaPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self,board):
        playerID = alphaBetaPlayer.evalID(board)
        choices = np.nonzero(board == 0)
        numChoices = len(choices[0])
        evals = np.zeros((numChoices)) 
        for i in range(numChoices):
            b2 = board.copy()
            square = choices[0][i], choices[1][i]
            b2[square] = playerID
            s = State(b2)
            evals[i] = self.minimax(s,2,playerID)
        if playerID == 1:
            choice = np.argmax(evals)
        else:
            choice = np.argmin(evals)
        square = choices[0][choice], choices[1][choice]
        tmp = board.copy()
        tmp[square] = playerID
        #print(tmp,evals[choice]) 
        return choices[0][choice], choices[1][choice]

    def minimax(self,state,depth,playerID):
        state.generateChildren()
        #print(depth, playerID)
        if depth == 0 or len(state.children) == 0:
            return state.eval     
        if playerID == 1:
            value = -1000
            for i in state.children:
                value = max(value,self.minimax(copy.deepcopy(i),depth-1,-1))
            return value
        else:
            value = 1000
            for i in state.children:
                value = min(value,self.minimax(copy.deepcopy(i),depth-1,1))
            return value
                
    @staticmethod
    def evalID(board):
        if np.count_nonzero(board == 1) > np.count_nonzero(board == -1):
            return -1
        else:
            return 1
    
    @staticmethod 
    def generateChildStates(board):
        root = State(board)
    
    def onWin(self):
        self.num_wins+=1

    def onLoss(self):
        #print("LOSS")
        self.num_losses+=1

    def onDraw(self):
        self.num_draws+=1
	


