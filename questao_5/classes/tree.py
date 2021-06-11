class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(f"Source => {self.cargo} Left Node => {self.left} Right Node =>{self.right} ")
