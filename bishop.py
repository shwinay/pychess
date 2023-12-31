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

    def _get_valid_moves(self, i: int, j: int, grid: List[List]) -> List[tuple]:
        valid_moves = []
        directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        for i_dir, j_dir in directions:
            new_i, new_j = (i + i_dir, j + j_dir)
            while in_bounds(new_i, new_j):
                if grid[new_i][new_j] is not None:
                    break
                valid_moves.append((new_i, new_j))
    
    def get_piece_type(self):
        return PieceType.BISHOP