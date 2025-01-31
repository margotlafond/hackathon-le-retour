import flet as ft

TITLE = "Taquin"

class Tile(ft.TextField):
    def __init__(self, number: int, line: int, column: int) -> None:
        super().__init__(value=str(number), read_only=True, text_align=ft.TextAlign.CENTER, width=50)
        self._number = number
        self.line = line  # Ligne entre 0 et 2
        self.column = column  # Colonne entre 0 et 2

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
        self.squares = []  # Stocke les cases du taquin

    def create_tiles(self, position):
        self.squares = [
            Tile(number=position[i][j], line=i, column=j)
            for i in range(len(position))
            for j in range(len(position[i]))
        ]
        return self.squares

    def update(self, board):
        """Met à jour les valeurs des cases selon le nouvel état du plateau."""
        for square in self.squares:
            square.number = board[square.line][square.column]

def main(page: ft.Page):
    page.title = TITLE
    initial = [[1, 4, 6], [0, 5, 9], [8, 3, 2]]

    board = Board(page)
    grid = ft.GridView(expand=True, runs_count=3, spacing=5, run_spacing=5)
    grid.controls.extend(board.create_tiles(initial))  # Ajout des cases au GridView

    page.controls.append(grid)  # Ajout du GridView à la page
    page.update()

ft.app(target=main)