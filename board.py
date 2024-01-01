from typing import List
from side import Side
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from util import *

class Board:
    
    def __init__(self):
        self.current_turn = Side.WHITE
        self.grid = self.init_grid() # each square is either Piece, or None
    
    def init_grid(self) -> List[List]:
        initial_board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

        grid = []
        for i in range(NUM_TILES):
            side = Side.BLACK if i < NUM_TILES // 2 else Side.WHITE
            row = []
            for j in range(NUM_TILES):
                char = initial_board[i][j]                
                match char.lower():
                    case ' ':
                        row.append(None)
                    case 'p':
                        row.append(Pawn(side))
                    case 'r':
                        row.append(Rook(side))
                    case 'n':
                        row.append(Knight(side))
                    case 'b':
                        row.append(Bishop(side))
                    case 'q':
                        row.append(Queen(side))
                    case 'k':
                        row.append(King(side))
            grid.append(row)

        return grid

    # TODO akudva error checking
    def handle_move(self, old_pos: tuple, new_pos: tuple):
        old_i, old_j = old_pos
        new_i, new_j = new_pos
        piece_to_move = self.grid[old_i][old_j]
        self.grid[old_i][old_j] = None
        self.grid[new_i][new_j] = piece_to_move
        self.current_turn = Side.WHITE if self.current_turn == Side.BLACK else Side.BLACK

'''
TODO notes to implement:

King cannot move if move results in check
Piece cannot move if it puts king in check

'''