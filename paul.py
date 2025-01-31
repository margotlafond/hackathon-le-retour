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
        return f"Board({self.grid})"

    def position_vide(self):
        for i, row in enumerate(self.grid):
            if 0 in row:
                return i, row.index(0)
        return None

    def moves(self):
        i, j = self.position_vide()
        mouvements = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_grid = [row[:] for row in self.grid]
                new_grid[i][j], new_grid[ni][nj] = new_grid[ni][nj], new_grid[i][j]
                mouvements.append(Board(new_grid))
        return mouvements





