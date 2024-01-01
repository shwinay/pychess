from typing import List
from side import Side
from piece import Piece
from piecetype import PieceType
from util import *

class Knight(Piece):

    def __init__(self, side: Side):
        super().__init__(side)

    def __str__(self):
        return 'N' if self.side == Side.BLACK else 'n'
    
    # TODO akudva implement, add rules for reaching end of board, en passant
    def get_valid_moves(self, i: int, j: int, grid: List[List]) -> List[tuple]:
        valid_moves = []
        directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, -2), (-1, 2)]

        for i_dir, j_dir in directions:
            new_i, new_j = (i + i_dir, j + j_dir)
            if in_bounds(new_i, new_j) and grid[new_i][new_j] is None:
                valid_moves.append((new_i, new_j))

        return valid_moves

    def get_piece_type(self):
        return PieceType.KNIGHT