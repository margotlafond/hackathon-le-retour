class Board():

    def __init__(self, board):
        self.board = board

    def __eq__(self, other):
        if isinstance(other, Board):
            return self.board == other.board 
        return False
    
    def __hash__(self):
        return hash(tuple(tuple(ligne) for ligne in self.board))
    
    def __lt__(self, other):
        if isinstance(other, Board):
            return self.board < other.board
        return False

    def __repr__(self):
        return f'{self.board}'
    
    def vide(self):
        for ligne in range(3):
            for colonne in range(3):
                if self.board[ligne][colonne] == 0:
                    return ligne, colonne

    def moves(self):
        moves = []
        ligne_vide = self.vide()[0]
        colonne_vide = self.vide()[1]
        if ligne_vide != 0:
            new_board = [l[:] for l in self.board]
            new_board[ligne_vide][colonne_vide] = new_board[ligne_vide - 1][colonne_vide]
            new_board[ligne_vide - 1][colonne_vide] = 0
            moves.append(Board(new_board))
        if ligne_vide != 2:
            new_board = [l[:] for l in self.board]
            new_board[ligne_vide][colonne_vide] = new_board[ligne_vide + 1][colonne_vide]
            new_board[ligne_vide + 1][colonne_vide] = 0
            moves.append(Board(new_board))
        if colonne_vide != 0:
            new_board = [l[:] for l in self.board]
            new_board[ligne_vide][colonne_vide] = new_board[ligne_vide][colonne_vide - 1]
            new_board[ligne_vide][colonne_vide - 1] = 0
            moves.append(Board(new_board))
        if colonne_vide != 2:
            new_board = [l[:] for l in self.board]
            new_board[ligne_vide][colonne_vide] = new_board[ligne_vide][colonne_vide + 1]
            new_board[ligne_vide][colonne_vide + 1] = 0
            moves.append(Board(new_board))
        return moves

dico = {}
matrice = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
board = Board(matrice)
dico[board] = board.moves()
#print(board)
#print(dico)

def DFS(matrice):
    fin = Board([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    board = Board(matrice)
    dico = {}
    longueur = 0
    dico[board] = [board.moves(), longueur, []]

    algorithme(board, dico, longueur)

    solution = [fin]
    etape = dico[fin][2]
    while etape != board:
        solution.append(etape)
        etape = dico[etape][2]
    
    return len(solution), solution[::-1]

def algorithme(board, dico, longueur):
    fin = Board([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    pere = board 
    if board != fin :
        longueur += 1
        #dico[board][0] = dico[board][0].sort()
        for new_board in dico[board][0]:
            dico[new_board] = [new_board.moves(), longueur, pere]
            algorithme(new_board, dico, longueur)
    else :
        dico[fin] = [[], longueur, pere]

DFS(matrice)