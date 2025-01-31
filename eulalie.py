class Board():

    def __init__(self, board):
        self.board = board

    def __eq__(self, other):
        return self.board == other.board 
    
    def __hash__(self):
        return hash(tuple(self.board))
    
    def __lt__(self, other):
        return self.board < other.board

    def __repr__(self):
        return f'{self.board}'
    
    



class Tuile():
    pass