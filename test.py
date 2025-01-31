import flet as ft
import paul as algo
import random

TITLE = "Taquin"
HEIGHT = 350
WIDTH = 250

sequence = [
    [1, 4, 6, 0, 5, 9, 8, 3, 2], 
    [0, 4, 6, 1, 5, 9, 8, 3, 2], 
    [4, 0, 6, 1, 5, 9, 8, 3, 2], 
    [4, 5, 6, 1, 0, 9, 8, 3, 2]
]

class Tile(ft.TextField):
    def __init__(self, number: int, line: int, column: int) -> None:
        super().__init__(
            value=str(number),
            read_only=True,
            text_align=ft.TextAlign.CENTER,
            width=60, height=60
        )
        self.number = number
        self.line = line  
        self.column = column  


class Board:
    def __init__(self, page):
        self.page = page
        self.squares = []
        self.current_step = 0  

    def create_tiles(self, position):
        self.squares = [
            Tile(number=position[i], line=i//3, column=i%3)
            for i in range(len(position))
        ]
        return self.squares

    def update(self, e):
        if self.current_step < len(sequence) - 1:
            self.current_step += 1  
            new_state = sequence[self.current_step]

            for i, tile in enumerate(self.squares):
                tile.value = str(new_state[i])  

            self.page.update()

    
    def shuffle(self, e):
        shuffled = sequence[self.current_step]
        random.shuffle(shuffled)
        for i, tile in enumerate(self.squares):
            tile.number = shuffled[i]
            tile.value = str(shuffled[i])
        self.page.update()
    

def main(page: ft.Page):
    page.title = TITLE
    page.window_height = HEIGHT
    page.window_width = WIDTH



    board = Board(page)
    grid = ft.GridView(expand=True, runs_count=3, spacing=5, run_spacing=5)
    grid.controls.extend(board.create_tiles(sequence[0]))  

    buttons = ft.Row([
        ft.IconButton(icon=ft.icons.FIRE_TRUCK, on_click = board.update), 
        ft.IconButton(icon=ft.icons.LOCK, on_click = board.shuffle),
        ft.IconButton(icon=ft.icons.FIRE_EXTINGUISHER), 
        ft.IconButton(icon=ft.icons.BIKE_SCOOTER)],
        alignment=ft.MainAxisAlignment.CENTER)

    page.controls.append(grid)
    page.controls.append(buttons)
    page.update()

ft.app(target=main)