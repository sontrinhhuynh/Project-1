import tkinter as tk
from tkinter import messagebox
import math

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

def getValidMoves():
    valid_moves = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == ' ':
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < 9 and 0 <= nj < 9 and board[ni][nj] != ' ':
                            valid_moves.append((i, j))
                            break
    return valid_moves

def minimax(depth, isMax, alpha, beta):
    score = evaluate()
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not getValidMoves() or depth == 3:
        return 0

    if isMax:
        best = -math.inf
        for i, j in getValidMoves():
            board[i][j] = 'O'
            best = max(best, minimax(depth + 1, not isMax, alpha, beta))
            board[i][j] = ' '
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i, j in getValidMoves():
            board[i][j] = 'X'
            best = min(best, minimax(depth + 1, not isMax, alpha, beta))
            board[i][j] = ' '
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def findBestMove():
    bestVal = -math.inf
    bestMove = (-1, -1)
    for i, j in getValidMoves():
        board[i][j] = 'O'
        moveVal = minimax(0, False, -math.inf, math.inf)
        board[i][j] = ' '
        if moveVal > bestVal:
            bestVal = moveVal
            bestMove = (i, j)
    return bestMove

def evaluate():
    if checkWinner('X'):
        return -10
    elif checkWinner('O'):
        return 10
    else:
        return 0

def handle_click(row, col):
    global Xplayer_turn, running

    if not running or board[row][col] != ' ':
        return

    if Xplayer_turn:
        putX(row, col)
        buttons[row][col].config(text='X', state='disabled')
        if checkWinner('X'):
            messagebox.showinfo("Game Over", "You won!")
            running = False
        Xplayer_turn = False
    
    if running and not Xplayer_turn:
        computer_move()

def computer_move():
    global Xplayer_turn, running

    if running:
        bestMove = findBestMove()
        putO(bestMove[0], bestMove[1])
        buttons[bestMove[0]][bestMove[1]].config(text='O', state='disabled')

        if checkWinner('O'):
            messagebox.showinfo("Game Over", "Computer wins!")
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