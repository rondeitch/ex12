import tkinter as tk
import boggle_board_randomizer as randomizer


class Gui:
    BUTTON_HOVER_COLOR = 'grey'
    REGULAR_BUTTON_COLOR = "#fffef8"

    def __init__(self, board, time):
        # root #
        self.__root = tk.Tk()
        self.__root.title('~BOGGLE~')
        # buttons #
        self.__buttons_frame = tk.Frame(self.__root)
        self.__dices = self.create_dices(board)
        # clock #
        self.__clock_frame = tk.Frame(self.__root)
        self.__time_minute = time // 60
        self.__time_second = time % 60
        self.__clock = self.creat_clock(self.__time_minute, self.__time_second)
        # pack all together #
        self.__clock_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.__buttons_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # TODO: makes the dices also expandable.

    def creat_clock(self, minute, second):
        """
        Creat a clock for the game.
        :param minute: int
        :param second: int
        :return: clock (Tk.Label)
        """
        if self.__time_second >= 10:
            if self.__time_minute >= 10:
                clock = tk.Label(self.__clock_frame, text=str(minute) + ':' + str(second), font=("Segue UI", 30),
                                 bg='green', fg='Black', border=10)
            else:
                clock = tk.Label(self.__clock_frame, text="0" + str(minute) + ':' + str(second), font=("Segue UI", 30),
                                 bg='green', fg='Black', border=10)
        else:
            if self.__time_minute >= 10:
                clock = tk.Label(self.__clock_frame, text=str(minute) + ':0' + str(second), font=("Segue UI", 30),
                                 bg='green', fg='Black', border=10)
            else:
                clock = tk.Label(self.__clock_frame, text="0" + str(minute) + ':0' + str(second), font=("Segue UI", 30),
                                 bg='green', fg='Black', border=10)
        time_left = tk.Label(self.__clock_frame, text='Time:', font=("Segue UI", 30), bg='grey', fg='black',
                             border=10)
        time_left.pack(side=tk.LEFT, fill=tk.BOTH)
        clock.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        return clock

    def clock_runner(self):
        """
        Run the time left for the game.
        :return: None
        """
        if self.__time_second >= 10:
            if self.__time_minute >= 10:
                self.__clock['text'] = str(self.__time_minute) + ':' + str(self.__time_second)
            else:
                self.__clock['text'] = "0" + str(self.__time_minute) + ':' + str(self.__time_second)
        else:
            if self.__time_minute >= 10:
                self.__clock['text'] = str(self.__time_minute) + ':0' + str(self.__time_second)
            else:
                self.__clock['text'] = "0" + str(self.__time_minute) + ':0' + str(self.__time_second)
        if self.__time_minute == 0 and self.__time_second == 30:
            self.__clock['fg'] = 'black'
            self.__clock['bg'] = 'red'
        if self.__time_second > 0:
            self.__time_second -= 1
            self.__clock.after(1000, self.clock_runner)
        elif self.__time_minute > 0 and self.__time_second == 0:
            self.__time_minute -= 1
            self.__time_second = 59
            self.__clock.after(1000, self.clock_runner)

    def create_dices(self, board):
        """
        Creat the dices of the board.
        :param board: List[List[str]]
        :return: List[Tk.Button]
        """
        board_buttons = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                board_buttons.append(self._make_button(str(board[r][c]), r, c))
        return board_buttons

    def _make_button(self, button_char: str, row: int, col: int):
        """
        Makes the buttons and their widgets.
        :param button_char: str
        :param row: int
        :param col: int
        :return: Tk.Button
        """
        cell_button = tk.Button(self.__buttons_frame, text=button_char, font=("Segue UI", 20),
                                width=5, height=2, bg="#fffef8", fg="#0583D2", border=5,
                                activebackground='#77c3ec', activeforeground="#ffffff")
        cell_button.grid(row=row, column=col)

        def _on_enter(event):
            if cell_button['bg'] != 'orange':
                cell_button['bg'] = self.BUTTON_HOVER_COLOR

        def _on_leave(event):
            if cell_button['bg'] != 'orange':
                cell_button['bg'] = self.REGULAR_BUTTON_COLOR

        def _if_press(event):
            if cell_button['bg'] != 'orange':
                cell_button['bg'] = 'orange'
                cell_button['fg'] = 'black'
            else:
                cell_button['bg'] = '#fffef8'
                cell_button['fg'] = '#0583D2'

        cell_button.bind('<Enter>', _on_enter)
        cell_button.bind('<Leave>', _on_leave)
        cell_button.bind('<Button-1>', _if_press)

        return cell_button

    @property
    def time_left(self):
        """
        Return how much seconds left for the game.
        :return: int
        """
        return self.__time_minute * 60 + self.__time_second

    def main_loop(self):
        """
        Doing the main loop , and start run the clock.
        :return: None
        """
        self.clock_runner()
        self.__root.mainloop()


board = randomizer.randomize_board()
gui = Gui(board, 35)
gui.main_loop()

# class GuiClock:
#     def __init__(self, time):
#         self.__root = tk.Tk()
#         self.__time_left = time
#         self.__clock = self.creat_clock(time)
#         self.clock_runner()
#
#     def creat_clock(self, time):
#         clock = tk.Label(self.__root, text=str(time), font=("Segue UI", 30), bg='white', fg='blue', border=10)
#         clock.pack()
#         return clock
#
#     def clock_runner(self):
#         self.__clock['text'] = str(self.__time_left)
#         if self.__time_left > 0:
#             self.__time_left -= 1
#             self.__root.after(1000, self.clock_runner)
#
#     @property
#     def time_left(self):
#         return self.__time_left
#
#     def main_loop(self):
#         self.__root.mainloop()


# clock = GuiClock(10)
# clock.main_loop()


# TODO: delete this (Alon try for clock)
# self.__time_left = time
# self.__clock = self.creat_clock(time)
# self.__clock_frame.pack(side=tk.TOP)
# self.__buttons_frame.pack(side=tk.BOTTOM)
# self.clock_runner()


# def creat_clock(self, time):
#     clock = tk.Label(self.__clock_frame, text=str(time), font=("Segue UI", 30), bg='white', fg='blue', border=10)
#     # clock.grid(row=0, column=0, columnspan=4)
#     clock.pack(side=tk.TOP)
#     return clock
#
# def clock_runner(self):
#     self.__clock['text'] = str(self.__time_left)
#     if self.__time_left == 10:
#         self.__clock['fg'] = 'black'
#         self.__clock['bg'] = 'red'
#     if self.__time_left > 0:
#         self.__time_left -= 1
#         self.__clock.after(1000, self.clock_runner)

# TODO: another try

#     self.__time = time
#     self.__clock = self.creat_clock(time)
#     # self.__clock.after(1000, self.clock_runner(self.__time))
#     self.clock_runner(self.__time)
#
# def creat_clock(self, time):
#     clock = tk.Label(self.__root, text=str(time), font=("Segue UI", 30), bg='white', fg='blue', border=10)
#     # clock.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#     clock.grid(row=4, column=0)
#     return clock
#
# def clock_runner(self, time):
#     self.__time = time - 1
#     self.__clock['text'] = str(time - 1)
#     self.__clock.after(1000, self.clock_runner(self.__time))

# TODO: delete this (Ron try for buttons)

#         cell_button = tk.Button(self.__root, text=str(board[r][c]), font=("Segue UI", 20),
#                                 width=5, height=2, bg="#fffef8", fg="#0583D2", border=5,
#                                 activebackground='#77c3ec', activeforeground="#ffffff")
#         # cell_button.bind("<Button-1>", lambda event: self.change_btn(cell_button))
#         cell_button.grid(row=r, column=c)
#         board_buttons.append(cell_button)
# for btn in board_buttons:
#     btn.bind("<Button-1>", lambda event: self.change_btn(btn))

# def change_btn(self, btn):
#     btn['bg'] = "red"
