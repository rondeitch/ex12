import tkinter as tk
import boggle_board_randomizer as randomizer


class Gui:
    def __init__(self, board):
        self.__root = tk.Tk()
        self.__dices = self.create_dices()

    def create_dices(self):
        board_buttons = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                cell_button = tk.Button(self.__root, text=str(board[r][c]), font=("Segue UI", 20),
                                        width=5, height=2, bg="#fffef8", fg="#0583D2", border=0.5,
                                        activebackground='#77c3ec', activeforeground="#ffffff")
                # cell_button.bind("<Button-1>", lambda event: self.change_btn(cell_button))
                cell_button.grid(row=r, column=c)
                board_buttons.append(cell_button)
        for btn in board_buttons:
            btn.bind("<Button-1>", lambda event: self.change_btn(btn))

        return board_buttons

    def change_btn(self, btn):
        btn['bg'] = "red"

    def main_loop(self):
        self.__root.mainloop()


board = randomizer.randomize_board()
gui = Gui(board)
gui.main_loop()
