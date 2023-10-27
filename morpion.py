class Morpion:
 def __init__(self, root):
        self.root = root
        self.root.title("Morpion")
        self.current_player = "X"
        self.board = [""] * 9
