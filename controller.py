from boggle_gui import BoggleGui
from game import BoggleGame


class BoggleController:
    def __init__(self):
        self.__model = BoggleGame()
        self.__view = BoggleGui()

    def display_game(self):
        game_state = self.__model.game_state
        score = self.__model.score
        board = self.__model.board
        guessed_words = self.__model.guessed_words
        self.__view.update_gui(game_state, score, board, guessed_words)

    def start_game(self, event):
        self.__model.start_game()
        self.__view.create_play_screen(self.guess, self.__model.board, self.__model.score)

    def guess(self, event):
        self.__model.run_single_turn(self.__view.get_marked_dices())
        self.__view.clear_dices()

    def run(self):
        msg = "Score: " + str(self.__model.score)
        print(msg)
        self.__view.create_start_screen(msg, self.start_game)
        self.__view.run()

    def end(self):
        pass


if __name__ == "__main__":
    controller = BoggleController()
    controller.run()
