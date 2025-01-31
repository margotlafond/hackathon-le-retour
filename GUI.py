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



class Tile():
    def __init__(self):
        pass

        

def main(page: ft.Page):
    page.title = TITLE

    board = Board(page)
    ft.Column[]
    page.update()

ft.app(main)


