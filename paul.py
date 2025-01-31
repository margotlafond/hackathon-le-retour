class Board:
    
    def __init__(self, grid):
        self.grid = grid

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.grid))

    def __eq__(self, other):
        if isinstance(other, Board):
            return self.grid == other.grid
        return False

    def __lt__(self, other):
        if isinstance(other, Board):
            return self.grid < other.grid
        return NotImplemented

    def __repr__(self):
        return f"TaquinState({self.grid})"

    def position_vide(self):
        for i, row in enumerate(self.grid):
            if 0 in row:
                return i, row.index(0)
        return None


