from board import Board
from randomPlayer import RandomPlayer
from alphaBetaPlayer import alphaBetaPlayer
import random

p2 = alphaBetaPlayer()
p1 = alphaBetaPlayer()
b = Board(num_games = int(1e3),player1 = p1,player2=p2)
b.playGames()
print('p1 wins:', p1.num_wins)
print('p2 wins:', p2.num_wins)
print('draws:', p1.num_draws)
