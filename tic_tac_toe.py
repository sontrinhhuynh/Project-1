import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    n = len(board)
    win_condition = 5

    # Check rows
    for row in board:
        for i in range(n - win_condition + 1):
            if all(cell == player for cell in row[i:i + win_condition]):
                return True

    # Check columns
    for col in range(n):
        for i in range(n - win_condition + 1):
            if all(board[row][col] == player for row in range(i, i + win_condition)):
                return True

    # Check diagonals (top-left to bottom-right)
    for i in range(n - win_condition + 1):
        for j in range(n - win_condition + 1):
            if all(board[i + k][j + k] == player for k in range(win_condition)):
                return True

    # Check diagonals (top-right to bottom-left)
    for i in range(n - win_condition + 1):
        for j in range(win_condition - 1, n):
            if all(board[i + k][j - k] == player for k in range(win_condition)):
                return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

class TicTacToe:
    def __init__(self, root):
        self.size = 9  # Bảng 9x9
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.players = ["X", "O"]
        self.turn = 0

        self.root = root
        self.root.title("Tik Tac Toe")

        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.create_ui()

    def create_ui(self):
        for i in range(self.size):
            for j in range(self.size):
                button = tk.Button(self.root, text=" ", width=4, height=2, font=("Arial", 16),
                                   command=lambda x=i, y=j: self.handle_click(x, y))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def handle_click(self, row, col):
        if self.board[row][col] == " ":
            current_player = self.players[self.turn]
            self.board[row][col] = current_player
            self.buttons[row][col].config(text=current_player, state=tk.DISABLED)

            if check_win(self.board, current_player):
                messagebox.showinfo("Game Over", f"Player {current_player} won!")
                self.reset_board()
            elif is_full(self.board):
                messagebox.showinfo("Game Over", "Draw!")
                self.reset_board()
            else:
                self.turn = 1 - self.turn  # Chuyển lượt
        else:
            messagebox.showwarning("Choose another blank")

    def reset_board(self):
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.turn = 0
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j].config(text=" ", state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()