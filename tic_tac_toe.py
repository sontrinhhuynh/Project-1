import tkinter as tk
from tkinter import messagebox

board = [[' ' for _ in range(9)] for _ in range(9)]
Xplayer_turn = True
running = True

def putX(a, b):
    board[a][b] = 'X'

def putO(a, b):
    board[a][b] = 'O'

def checkWinner(player):
    for i in range(9):
        for j in range(5):
            if all(board[i][j + k] == player for k in range(5)):
                return True

    for i in range(5):
        for j in range(9):
            if all(board[i + k][j] == player for k in range(5)):
                return True

    for i in range(5):
        for j in range(5):
            if all(board[i + k][j + k] == player for k in range(5)):
                return True

    for i in range(5):
        for j in range(4, 9):
            if all(board[i + k][j - k] == player for k in range(5)):
                return True

    return False

def handle_click(row, col):
    global Xplayer_turn, running

    if not running or board[row][col] != ' ':
        return

    if Xplayer_turn:
        putX(row, col)
        buttons[row][col].config(text='X', state='disabled')
        if checkWinner('X'):
            messagebox.showinfo("Game Over", "Player X wins!")
            running = False
        Xplayer_turn = False
    else:
        putO(row, col)
        buttons[row][col].config(text='O', state='disabled')
        if checkWinner('O'):
            messagebox.showinfo("Game Over", "Player O wins!")
            running = False
        Xplayer_turn = True

root = tk.Tk()
root.title("Tic Tac Toe 9x9")

buttons = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        buttons[i][j] = tk.Button(root, text=' ', font=('Arial', 20), width=3, height=1,
                                  command=lambda row=i, col=j: handle_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
