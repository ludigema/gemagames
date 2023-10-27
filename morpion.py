import tkinter as tk
from tkinter import messagebox
class Morpion:
 def __init__(self, root):
        self.root = root
        self.root.title("Morpion")
        self.current_player = "X"
        self.board = [""] * 9

# Création des boutons pour le morpion
        self.buttons = [tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2, command=lambda i=i: self.on_click(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

    def on_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Victoire", f"Le joueur {self.current_player} a gagné !")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Match nul", "Match nul !")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
