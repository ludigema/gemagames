import tkinter as tk

class Morpion:
 def __init__(self, root):
        self.root = root
        self.root.title("Morpion")
        self.current_player = "X"
        self.board = [""] * 9

  self.buttons = [tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2, command=lambda i=i: self.on_click(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)
