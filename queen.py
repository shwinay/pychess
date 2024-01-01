from typing import List
from side import Side
from piece import Piece
from piecetype import PieceType
from util import *

class Queen(Piece):

    def __init__(self, side: Side):
        super().__init__(side)

    def __str__(self):
        return 'Q' if self.side == Side.BLACK else 'q'
    
    # TODO akudva implement, add rules for reaching end of board, en passant
    def get_valid_moves(self, i: int, j: int, grid: List[List]) -> List[tuple]:
        return self.get_directional_valid_moves(i, j, grid, [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (1, -1), (-1, -1)])
  
    def get_piece_type(self):
        return PieceType.QUEEN