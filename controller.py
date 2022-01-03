from boggle_gui import BoggleGui
from game import BoggleGame


class BoggleController:
    def __init__(self):
        self.__model = BoggleGame()
        self.__view = BoggleGui()

    def update_game(self):
        game_state = self.__model.game_state
        score = self.__model.score
        guessed_words = self.__model.guessed_words
        self.__view.update_gui(game_state, score, guessed_words)

    def start_game(self, event):    # self.__model.GAME_MINS * 60
        self.__model.start_game()
        self.__view.create_play_screen(self.guess, self.__model.board, self.__model.score, 45,
                                       self.start_new_game)

    def guess(self, event):
        msg, word = self.__model.run_single_turn(self.__view.get_marked_dices())
        self.__view.clear_dices()
        if word is not None:
            self.__view.guessedwords_add_word(word)

    def run(self):
        msg = "Score: " + str(self.__model.score)
        print(msg)
        self.__view.create_start_screen(msg, self.start_game)
        self.__view.run()

    def start_new_game(self):
        self.__model.end_game()
        self.run()

    def end(self):
        pass


if __name__ == "__main__":
    controller = BoggleController()
    controller.run()


