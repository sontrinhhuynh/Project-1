import tkinter as tk
from tkinter import messagebox

board = [[' ' for _ in range(3)] for _ in range(3)]
Xplayer_turn = True
running = True

def putX(a, b):
    board[a][b] = 'X'

def putO(a, b):
    board[a][b] = 'O'

def checkWinner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2 - i] == player for i in range(3)):
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

    if running and all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        messagebox.showinfo("Game Over", "It's a draw!")
        running = False

root = tk.Tk()
root.title("Tic Tac Toe 3x3")

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', font=('Arial', 20), width=5, height=2,
                                  command=lambda row=i, col=j: handle_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
