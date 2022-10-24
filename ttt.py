from board import Board
from randomPlayer import RandomPlayer
from alphaBetaPlayer import alphaBetaPlayer

p2 = alphaBetaPlayer()
p1 = RandomPlayer()

b = Board(num_games = 100_000,player1 = p1,player2=p2)
b.playGames()
print(p1.num_wins,p2.num_wins,p1.num_draws)
