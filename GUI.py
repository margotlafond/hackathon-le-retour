import flet as ft
TITLE = "Taquin"

class Board:
    def __init__(self, page):
        self.page = page
    
    def create_tiles(self):
        self.squares = [Tile for i in range(9)]
        return self.squares

    def movable(self, tile):
        pass

    def update(self, board):
        for square in self.squares:
            square.number = board[square.line][square.column]



class Tile(ft.ElevatedButton):
    def __init__(self, number: int, line: int, column:int) -> None:
        super().__init__()
        self.number = number
        self.line = line #line number : between 0 and 2
        self.column = column #column number : between 0 and 2

    @property
    def number(self) -> int:
        return self.number
    
    def set_number(self, new_number: int) -> None:
        self.number = new_number
        

def main(page: ft.Page):
    page.title = TITLE

    board = Board(page)
    ft.Column[ft.GridView(board.squares)]
    page.update()

ft.app(main)


