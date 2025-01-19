import tkinter as tk
from tkinter import messagebox
import tic_tac_toe_3x3
import minimax_3x3
import tic_tac_toe
import minimax

def start_game(mode, play_type):
    game_window = tk.Toplevel(root)

    if mode == "3x3":
        if play_type == "PvP":
            game_window.title("Tic Tac Toe 3x3 - Player vs Player")
            tic_tac_toe_3x3.TicTacToe(game_window)
        elif play_type == "PvC":
            game_window.title("Tic Tac Toe 3x3 - Player vs Computer")
            minimax_3x3.board = [[' ' for _ in range(3)] for _ in range(3)]
            minimax_3x3.running = True
            minimax_3x3.Xplayer_turn = True
            minimax_3x3.buttons = [[None for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    minimax_3x3.buttons[i][j] = tk.Button(
                        game_window, text=' ', font=('Arial', 20), width=5, height=2,
                        command=lambda row=i, col=j: minimax_3x3.handle_click(row, col)
                    )
                    minimax_3x3.buttons[i][j].grid(row=i, column=j)
    elif mode == "9x9":
        if play_type == "PvP":
            game_window.title("Tic Tac Toe 9x9 - Player vs Player")
            tic_tac_toe.TicTacToe(game_window)
        elif play_type == "PvC":
            game_window.title("Tic Tac Toe 9x9 - Player vs Computer")
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

def choose_play_type(mode):
    play_type_window = tk.Toplevel(root)
    tk.Button(
        play_type_window, text="PvP", font=("Arial", 14),
        command=lambda: [play_type_window.destroy(), start_game(mode, "PvP")]
    ).pack(pady=10)

    tk.Button(
        play_type_window, text="PvC", font=("Arial", 14),
        command=lambda: [play_type_window.destroy(), start_game(mode, "PvC")]
    ).pack(pady=10)

def choose_game_mode():
    mode_window = tk.Toplevel(root)

    tk.Button(
        mode_window, text="3x3", font=("Arial", 14),
        command=lambda: [mode_window.destroy(), choose_play_type("3x3")]
    ).pack(pady=10)

    tk.Button(
        mode_window, text="9x9", font=("Arial", 14),
        command=lambda: [mode_window.destroy(), choose_play_type("9x9")]
    ).pack(pady=10)

root = tk.Tk()
root.title("Tic Tac Toe")

tk.Label(root, text="Tic Tac Toe", font=("Arial", 20, "bold")).pack(pady=20)

tk.Button(
    root, text="Start Game", font=("Arial", 16),
    command=choose_game_mode
).pack(pady=10)

tk.Button(root, text="Exit", font=("Arial", 16), command=root.quit).pack(pady=20)

root.mainloop()

