import flet as ft
TITLE = "Taquin"

class Board:
    def __init__(self, page):
        self.page = page
    
    def create_squares(self):
        pass

    def update(board):
        pass



class Tile():
    def __init__(self):
        pass

        

def main(page: ft.Page):
    page.title = TITLE

    board = Board(page)
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

ft.app(main)


