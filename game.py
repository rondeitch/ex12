# TODO: CHECK IN FORUM THE FOLLOWING TOPICS:
# 1. is board size is 4x4
# 2. if cell content is only string "A-Z" + "QU"
# 3. if game time is always 3 minutes


import boggle_board_randomizer as randomizer
import ex12_utils as utils


class BoggleGame:
    # Constants:
    WORD_DICT_PATH = "boggle_dict.txt"
    GAME_MINS = 3
    POSSIBLE_MOVES = {"u": (0, -1), "r": (1, 0), "d": (0, 1), "l": (-1, 0), "ur": (1, -1), "dr": (1, 1), "dl": (-1, 1),
                      "ul": (-1, -1)}

    def __init__(self):
        # TODO : Check if board is valid for game rules:
        # Single game attributes:
        self.__board = []
        # self.__marked_board = []
        self.__score = 0
        self.__guessed_words = []

        # Cross-game attributes:
        self.__game_state = False  # True if in middle of a game, False otherwise
        self.__games_played = 0
        self.__word_dict = self.create_words_dict()  # TODO : SWITCH TO THIS
        # self.__word_dict = ["queen", "hello", "note", "let", "hen", "eel", "tell"]

    @property
    def score(self):
        return self.__score

    def reward_score(self, path):
        self.__score += len(path) ** 2

    @property
    def board(self):
        return self.__board

    # @property
    # def marked_board(self):
    #     return self.__marked_board

    @property
    def guessed_words(self):
        return self.__guessed_words

    @property
    def game_state(self):
        return self.__game_state

    def add_guess(self, guess):
        self.guessed_words.append(guess)

    # def create_marked_board(self):
    #     for r, row in enumerate(self.__board):
    #         self.__marked_board.append([])
    #         for _ in row:
    #             self.__marked_board.append(False)

    def is_word_guessed(self, word):
        if word in self.__guessed_words:
            return True
        return False

    @staticmethod
    def create_words_dict():
        word_dict = []
        with open(BoggleGame.WORD_DICT_PATH, "r") as file:
            for _ in file:
                word_dict.append(file.readline().strip())
        return word_dict

    def run_single_turn(self, path):
        print("You guessed:", utils.path_to_str(self.board, path))
        print(path, utils.is_valid_path(self.board, path, self.__word_dict))
        if utils.is_valid_path(self.board, path, self.__word_dict):
            if not self.is_word_guessed(utils.path_to_str(self.board, path)):  # Check if word not already guessed
                self.add_guess(utils.path_to_str(self.board, path))  # Add guess to score
                self.reward_score(path)
            else:
                print("Word already guessed")
        else:
            print("Path not valid", )
        print(self.print_state())

    def start_game(self):
        # TODO: replace to randomize board
        # self.__board = randomizer.randomize_board()
        brd = [
            ["H", "E", "QU", "E"],
            ["E", "E", "T", "A"],
            ["L", "L", "N", "O"],
            ["O", "T", "X", "L"]
        ]
        self.__board = brd
        # self.create_marked_board()
        self.__games_played += 1
        self.__game_state = True
        print("Game started")
        self.print_state()
        # return self.game_state()

    # TODO: These are debugging functions DELETE THEM:
    def print_state(self):
        for line in self.board:
            print(line)
        print("Score:", self.score)
        print("Words guessed:", self.guessed_words)


game = BoggleGame()
# game.start_game()
#
# guess = [(0, 2), (0, 1), (1, 1), (2, 2)]
# print(utils.path_to_str(game.board, guess))
# fixed_guess = [(y, x) for x, y in guess]
# game.run_single_turn(fixed_guess)
