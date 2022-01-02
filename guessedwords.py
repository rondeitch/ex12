import tkinter as tk


class GuessedWords:
    def _init_(self, parent, **kwargs):
        self.__frame = tk.Frame(parent, **kwargs)
        self.__words = []
        self.__labels = []

    def add(self, word):
        # add label to labels, add word to words
        pass