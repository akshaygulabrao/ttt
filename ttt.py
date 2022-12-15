from board import Board
from randomPlayer import RandomPlayer
from minimaxPlayer import minimaxPlayer
import random

p1 = minimaxPlayer()
p2 = RandomPlayer()
b = Board(num_games = int(1e3),player1 = p1,player2=p2)
b.playGames()
print('p1 wins:', p1.num_wins)
print('p2 wins:', p2.num_wins)
print('draws:', p1.num_draws)
