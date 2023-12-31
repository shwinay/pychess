from typing import List
from side import Side
from piece import Piece
from piecetype import PieceType

class King(Piece):

    def __init__(self, side: Side):
        super().__init__(side)
        self.has_moved = False
        self.direction = 1 if side == Side.BLACK else -1

    def __str__(self):
        return 'K' if self.side == Side.BLACK else 'k'
    
    # TODO akudva implement, add rules for reaching end of board, en passant
    def _get_valid_moves(self, i: int, j: int, grid: List[List]) -> List[tuple]:
        raise NotImplementedError()
    
    def get_piece_type(self):
        return PieceType.KING