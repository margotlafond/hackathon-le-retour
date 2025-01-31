import flet as ft

TITLE = "Taquin"
HEIGHT = 350
WIDTH = 250

sequence = [[1, 4, 6, 0, 5, 9, 8, 3, 2], 
            [0, 4, 6, 1, 5, 9, 8, 3, 2], 
            [4, 0, 6, 1, 5, 9, 8, 3, 2], 
            [4, 5, 6, 1, 0, 9, 8, 3, 2]]

class Tile(ft.TextField):
    def __init__(self, number: int, line: int, column: int) -> None:
        super().__init__(value=str(number), read_only=True, text_align=ft.TextAlign.CENTER, width=100, height=100)
        self._number = number
        self.line = line  
        self.column = column  
       
        

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, new_number: int) -> None:
        self._number = new_number
        self.value = str(new_number)  # Mise à jour de l'affichage


class Board:
    def __init__(self, page):
        self.page = page
        self.squares = []  

    def create_tiles(self, position):
        self.squares = [
            Tile(number=position[i], line=i//3, column=i%3)
            for i in range(len(position))]
        return self.squares

    def update(self, sequence, i):
        #for square in self.squares:
        #    square.number = position[square.line][square.column]
        #self.create_tiles(sequence[i+1])
        self.squares = self.create_tiles(sequence[i + 1])



def main(page: ft.Page):
    page.title = TITLE
    page.window_height = HEIGHT
    page.window_width = WIDTH

    board = Board(page)
    grid = ft.GridView(expand=True, runs_count=3, spacing=5, run_spacing=5)
    grid.controls.extend(board.create_tiles(sequence[0]))  

    for i in range(len(sequence)):
        buttons = ft.Row([
            ft.IconButton(icon=ft.Icons.FIRE_TRUCK, on_click=lambda e: board.update(sequence, i)), 
            ft.IconButton(icon = ft.Icons.LOCK),
            ft.IconButton(icon = ft.Icons.FIRE_EXTINGUISHER), 
            ft.IconButton(icon = ft.Icons.BIKE_SCOOTER)],
            alignment=ft.MainAxisAlignment.CENTER)
    
        page.controls.append(grid)
        page.controls.append(buttons)
        page.update()
        

ft.app(target=main)