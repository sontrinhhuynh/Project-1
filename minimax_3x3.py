import tkinter as tk
from tkinter import messagebox
import math

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

def getValidMoves():
    valid_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                valid_moves.append((i, j))
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

def isDraw():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def reset_game():
    global board, Xplayer_turn, running
    board = [[' ' for _ in range(3)] for _ in range(3)]
    Xplayer_turn = True
    running = True

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ', state='normal')

def handle_click(row, col):
    global Xplayer_turn, running

    if not running or board[row][col] != ' ':
        return
    if Xplayer_turn:
        putX(row, col)
        buttons[row][col].config(text='X', state='disabled')
        if checkWinner('X'):
            messagebox.showinfo("Game Over", "You won!")
            reset_game()
            return
        elif isDraw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
            return
        else:
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
            reset_game()
            return
        elif isDraw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
            return

    Xplayer_turn = True

root = tk.Tk()
root.title("Tic Tac Toe 3x3")

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', font=('Arial', 20), width=5, height=2,
                                  command=lambda row=i, col=j: handle_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
