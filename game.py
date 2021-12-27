# TODO: CHECK IN FORUM THE FOLLOWING TOPICS:
# 1. is board size is 4x4
# 2. if cell content is only string "A-Z" + "QU"
# 3. if game time is always 3 minutes
from mypy.typeshed.stdlib.enum import property
import time


class Game:
    BOARD_SIZE = 4
    GAME_MINS = 3
    POSSIBLE_MOVES = {"u": (0, -1), "r": (1, 0), "d": (0, 1), "l": (-1, 0), "ur": (1, -1), "dr": (1, 1), "dl": (-1, 1),
                      "ul": (-1, -1)}

    def __init__(self, board, word_dict):
        # TODO : Check if board is valid for game rules:
        self.__board = board  # Board object
        self.__score = 0
        # TODO: Check if word_dict is valid
        self.__word_dict = word_dict
        self.__time_left = Game.GAME_MINS * 60  # TODO: check how to set the time

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, points):
        self.__score += points

    # @time_left.setter
    # def time_left(self, num):
    #     self.__time_left += num

    def play(self):
        # TODO
        while self.__time_left > 0:
            pass
