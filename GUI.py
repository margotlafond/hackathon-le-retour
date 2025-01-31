import flet as ft
TITLE = "Taquin"

class Board:
    def __init__(self, page):
        self.page = page
    
    def create_tiles(self, position):
        self.squares = []
        for i in range(len(position)):
            for j in range(len(position[i])):
                self.squares.append(Tile(number = position[i][j], line = i, column = j))
        return self.squares

    def movable(self, tile):
        pass

    def update(self, board):
        for square in self.squares:
            square.number = board[square.line][square.column]



class Tile(ft.TextField):
    def __init__(self, number: int, line: int, column:int) -> None:
        self.number = number
        self.line = line #line number : between 0 and 2
        self.column = column #column number : between 0 and 2
"""
    @property
    def number(self) -> int:
        return self.number
    
    @Tile.setter
    def set_number(self, new_number: int) -> None:
        self.number = new_number
"""      

def main(page: ft.Page):
    page.title = TITLE
    initial = [[1, 4, 6], [0, 5, 9], [8, 3, 2]]
    board = Board(page)
    ft.Column[ft.GridView(board.create_tiles(initial))]
    page.update()

ft.app(main)


