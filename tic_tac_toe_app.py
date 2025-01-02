import tkinter as tk
from tkinter import messagebox
import tic_tac_toe 
import minimax 

def pvp():
    game_window = tk.Toplevel(root)
    tic_tac_toe.TicTacToe(game_window)

def pvc():
    game_window = tk.Toplevel(root)
    minimax.board = [[' ' for _ in range(9)] for _ in range(9)]
    minimax.running = True
    minimax.Xplayer_turn = True

    minimax.buttons = [[None for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            minimax.buttons[i][j] = tk.Button(
                game_window, text=' ', font=('Arial', 20), width=3, height=1,
                command=lambda row=i, col=j: minimax.handle_click(row, col)
            )
            minimax.buttons[i][j].grid(row=i, column=j)

    game_window.title("Play with Computer")

root = tk.Tk()
root.title("Tic Tac Toe")

title_label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

btn_2_players = tk.Button(root, text="PvP", font=("Arial", 16), command=pvp)
btn_2_players.pack(pady=10)

btn_vs_computer = tk.Button(root, text="PvC", font=("Arial", 16), command=pvc)
btn_vs_computer.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", font=("Arial", 16), command=root.quit)
btn_exit.pack(pady=10)

root.mainloop()
