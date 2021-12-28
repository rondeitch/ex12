import sys
import tkinter as tk
import boggle_board_randomizer as randomizer


# from game import Game
# from board import Board

def cell_click(*args):
    print("You clicked", *args)


if __name__ == "__main__":
    # board = Board([])
    board = randomizer.randomize_board()
    # game = Game(board, {})
    root = tk.Tk()
    # Display board
    board_buttons = []
    state = "a"
    for r in range(len(board)):
        for c in range(len(board[0])):
            cell_button = tk.Button(root, text=str(board[r][c]), font=("Segue UI", 20),
                                    width=5, height=2, bg="#fffef8", fg="#0583D2", border=0.5,
                                    activebackground='#77c3ec', activeforeground="#ffffff")

            cell_button.grid(row=r, column=c)
            cell_button.bind("<Button-1>", cell_click)
            board_buttons.append(cell_button)
    root.mainloop()
