import tkinter as tk
from tkinter import messagebox
import importlib

def start_9x9_with_computer():
    minimax = importlib.import_module('minimax')
    minimax.root.mainloop()

def start_9x9_2players():
    tic_tac_toe = importlib.import_module('tic_tac_toe')
    tic_tac_toe.root.mainloop()


def start_3x3_with_computer():
    minimax_3x3 = importlib.import_module('minimax_3x3')
    minimax_3x3.root.mainloop()

def start_3x3_2players():
    tic_tac_toe_3x3 = importlib.import_module('tic_tac_toe_3x3')
    tic_tac_toe_3x3.root.mainloop()

def main_menu():
    root = tk.Tk()
    root.title("Tic Tac Toe - Main Menu")

    label = tk.Label(root, text="Choose Game Mode", font=('Arial', 20))
    label.pack(pady=20)

    btn_9x9_ai = tk.Button(root, text="9x9 PvC", font=('Arial', 14), width=20, command=start_9x9_with_computer)
    btn_9x9_ai.pack(pady=5)

    btn_9x9_2players = tk.Button(root, text="9x9 PvP", font=('Arial', 14), width=20, command=start_9x9_2players)
    btn_9x9_2players.pack(pady=5)

    btn_3x3_ai = tk.Button(root, text="3x3 PvC", font=('Arial', 14), width=20, command=start_3x3_with_computer)
    btn_3x3_ai.pack(pady=5)

    btn_3x3_2players = tk.Button(root, text="3x3 PvP", font=('Arial', 14), width=20, command=start_3x3_2players)
    btn_3x3_2players.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
