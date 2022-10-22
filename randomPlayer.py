import random
import numpy as np
from player import Player

class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
    def move(self,board):
        choices = np.nonzero(board == 0)
        numChoices = len(choices[0])
        randIndex = random.randint(0,numChoices - 1)
        return choices[0][randIndex], choices[1][randIndex]

    def onWin(self):
        self.num_wins+=1

    def onLoss(self):
        self.num_losses+=1

    def onDraw(self):
        self.num_draws+=1


