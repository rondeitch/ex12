import tkinter as tk
from gui_style import *
# from boggle_screen import BoggleScreen


class BoggleGui:

    def __init__(self):
        # root #
        self.__root = tk.Tk()
        self.__root.configure(**STYLES["root"])
        self.__root.title('PLAY BOGGLE!')
        self.__root.minsize(MIN_WIDTH, MIN_HEIGHT)
        # frames
        self.__start_frame = tk.Frame(self.__root, **STYLES["frame"]["start"])
        self.__start_frame.pack(expand=1)
        self.__play_frame = tk.Frame(self.__root, **STYLES["frame"]["play"])
        self.__game_info_frame = tk.Frame(self.__play_frame)

        self.__dices_frame = tk.Frame(self.__play_frame, **STYLES["frame"]["play"])

        self.__dices_list = []
        self.__play_frame.pack(expand=1)

        # variables
        self.__current_path = []


    @staticmethod
    def _pack_elements(elements):
        for element in elements:
            element.pack()

    @staticmethod
    def clear_frame(frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def set_button_command(self, button, cmd):
        button.configure(command=cmd)

    def get_marked_dices(self):
        # TODO : fix this to work in order of selection ?
        path = []
        for dice in self.__dices_list:
            if dice[0]["bg"] == STYLES["dice"]["on_click"]["bg"]:
                path.append(dice[1])
        return path

    def update_gui(self, game_state, score, board, guessed_words):
        if game_state is True:
            pass

    def create_dices(self, board):
        """
        Creat the dices of the board.
        :param board: List[List[str]]
        :return: List[Tk.Button]
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.__dices_list.append(self._make_button(self.__dices_frame, str(board[r][c]), r, c))

    def clear_dices(self):
        for dice in self.__dices_list:
            if dice[0]["bg"] == STYLES["dice"]["on_click"]["bg"]:
                dice[0].configure(**STYLES["dice"]["default"])

    def _make_button(self, frame, char, row, col):
        """
        Makes the buttons and their widgets.
        :param button_char: str
        :param row: int
        :param col: int
        :return: Tk.Button
        """
        cell_button = tk.Button(frame, text=char, **STYLES["dice"]["default"])
        cell_button.grid(row=row, column=col)

        def _on_enter(event):
            if cell_button["bg"] != STYLES["dice"]["on_click"]["bg"]:
                cell_button.configure(**STYLES["dice"]["on_enter"])

        def _on_leave(event):
            if cell_button["bg"] != STYLES["dice"]["on_click"]["bg"]:
                cell_button.configure(**STYLES["dice"]["default"])

        def _on_click(event):
            if cell_button["bg"] != STYLES["dice"]["on_click"]["bg"]:
                cell_button.configure(**STYLES["dice"]["on_click"])
            else:
                cell_button.configure(**STYLES["dice"]["default"])

        cell_button.bind('<Enter>', _on_enter)
        cell_button.bind('<Leave>', _on_leave)
        cell_button.bind('<Button-1>', _on_click)

        return cell_button, (row, col)

    def create_game_info_frame(self):
        info_label = tk.Label(self.__game_info_frame, text="Words:", **STYLES["label"]["h2"])
        words_labels = tk.Label(self.__game_info_frame, text="Hello", **STYLES["label"]["h2"])
        info_label.pack()
        words_labels.pack()
        self.__game_info_frame.pack(side=tk.RIGHT)

    def create_start_screen(self, msg, callback):
        self.__root.after(300)  # delay by 300ms
        self.__play_frame.pack_forget()  # hide play_frame
        start_frame_elements = list()  # create frame element list
        start_frame_elements.append(tk.Label(self.__start_frame, name="main_header", text="Let's Play Boggle!",
                                             **STYLES["label"]["h2"]))  # Primary label
        start_frame_elements.append(tk.Label(self.__start_frame, name="game_info",
                                             text=msg, **STYLES["label"]["h3"]))  # Game details
        start_button = tk.Button(self.__start_frame, text="START", name="start_btn",
                                 **STYLES["button"]["default"])  # Start button
        start_frame_elements.append(start_button)
        self._pack_elements(start_frame_elements)  # pack elements to frame

        start_button.bind("<Button-1>", callback)  # bind callback to start button
        # self.__play_frame.pack()  # pack frame

    def create_play_screen(self, callback, board, score):
        self.__root.after(300)
        self.__start_frame.pack_forget()
        play_frame_elements = list()
        score_str = "SCORE: " + str(score)
        play_frame_elements.append(tk.Label(self.__play_frame, text="BOGGLE", **STYLES["label"]["h1"]))
        play_frame_elements.append(tk.Label(self.__play_frame, text=score_str, name="score", **STYLES["label"]["h2"]))
        guess_button = tk.Button(self.__play_frame, text="Guess", **STYLES["button"]["default"])
        self.create_dices(board)
        play_frame_elements.append(self.__dices_frame)
        play_frame_elements.append(guess_button)
        self.__game_info_frame.pack()
        play_frame_elements.append(self.__game_info_frame)
        self._pack_elements(play_frame_elements)

        guess_button.bind("<Button-1>", callback)
        self.__play_frame.pack()

    def set_display(self):
        pass

    def run(self):
        self.__root.mainloop()


if __name__ == "__main__":
    gui = BoggleGui()
    gui.run()
