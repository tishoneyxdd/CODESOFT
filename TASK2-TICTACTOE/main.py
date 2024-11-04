import tkinter as tk
from tkinter import messagebox
from board import check_winner, is_board_full, reset_board
from ai import ai_move

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="#f7f7f7")
        self.board = reset_board()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board_ui()
        self.player_turn = 'O'

    def create_board_ui(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 24),
                                   width=5, height=2,
                                   bg="#ffffff", fg="#333333",
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

    def on_click(self, row, col):
        if self.board[row][col] == '' and self.player_turn == 'O':
            self.make_move(row, col, 'O')
            if not self.check_game_over():
                self.root.after(500, self.ai_turn)

    def make_move(self, row, col, player):      #updating
        self.board[row][col] = player
        self.buttons[row][col].config(text=player, state="disabled")
        self.player_turn = 'X' if player == 'O' else 'O'

    def ai_turn(self):
        move = ai_move(self.board)
        if move:
            row, col = move
            self.make_move(row, col, 'X')
            self.check_game_over()

    def check_game_over(self):
        winner = check_winner(self.board)       #ENDGAME
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.reset_game()
            return True
        elif is_board_full(self.board):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return True
        return False

    def reset_game(self):
        self.board = reset_board()
        self.player_turn = 'O'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
