import tkinter as tk
from gui_style import *


class GuessedWords:

    def __init__(self, parent, **kwargs):
        self.__frame = tk.Frame(parent)
        # the title of the frame- 'Guessed Words: '. #
        self.__frame_title = self._create_frame_title()
        # words list #
        self.__words = []
        # label list #
        self.__labels = []
        # packing the frame #
        self.__frame.pack(**kwargs)

    def _create_frame_title(self):
        """
        Create the title - 'Guessed Words: '.
        :return: Tk.Label (title)
        """
        title = tk.Label(self.__frame, text='Guessed Words: ', **STYLES['label']['h4'])
        title.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        return title

    def add(self, word):
        """
        Add label to labels, add word to words. Also create the label of the given word.
        :param word: str
        :return: bool TODO: if change change it too.
        """
        if not self.is_word_already_guessed(word):
            self._create_word_label(word)
            self.__words.append(word)
            return True  # TODO: check if need the boolean return, and delete if not.
        return False

    def is_word_already_guessed(self, word):
        """
        Check if the words is in words list.
        :param word: str
        :return: bool
        """
        if word in self.__words:
            return True
        return False

    def _create_word_label(self, word):
        """
        Create the word label, and append it into the label list.
        :param word: str
        :return: None
        """
        if len(self.__labels) == 0:
            word = tk.Label(self.__frame, text=str(word), **STYLES['label']['h4'])
        else:  # if it's not the first word added, put a comma before the word.
            word = tk.Label(self.__frame, text=", " + str(word), **STYLES['label']['h4'])
        # TODO: maybe add a term of decline line if the row length if too long.
        word.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.__labels.append(word)


# TODO: delete this at end (debug helper)
if __name__ == '__main__':
    root = tk.Tk()
    wor = GuessedWords(root, fill=tk.BOTH, expand=1)
    for i in range(10):
        wor.add('word' + str(i))
    root.mainloop()
