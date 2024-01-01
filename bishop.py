from typing import List
from side import Side
from piece import Piece
from util import *
from piecetype import PieceType

class Bishop(Piece):

    def __init__(self, side: Side):
        super().__init__(side)

    def __str__(self):
        return 'B' if self.side == Side.BLACK else 'b'

    def get_valid_moves(self, i: int, j: int, grid: List[List]) -> List[tuple]:
        return self.get_directional_valid_moves(i, j, grid, [(-1, 1), (1, 1), (1, -1), (-1, -1)])
    
    def get_piece_type(self):
        return PieceType.BISHOP