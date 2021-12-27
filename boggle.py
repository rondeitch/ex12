import sys
from game import Game
from board import Board

if __name__ == "__main__":
    board = Board([])
    game = Game(board, {})
    game.play()
