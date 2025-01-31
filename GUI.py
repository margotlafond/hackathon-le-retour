import flet as ft
TITLE = "Taquin"

class Board:
    def __init__(self, page):
        self.page = page
    
    def create_squares(self):
        pass

    def update(board):
        pass



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
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

ft.app(main)


