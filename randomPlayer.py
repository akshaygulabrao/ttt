from player import Player
import numpy as np

class RandomPlayer(Player):
    def move(self,board):
        return random.choice(np.nonzero(board == 0)[0])

    def onWin(self):
        self.num_wins+=1

    def onLoss(self):
        self.num_losses+=1

    def onDraw(self):
        self.num_draws+=1


