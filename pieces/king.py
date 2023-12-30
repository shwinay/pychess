from typing import List
from piece import Piece
from abc import override

class King(Piece):

    def __init__(self, i: int, j: int):
        super().__init__(i, j)
    
    @override
    def _get_valid_moves(self) -> List[tuple]:
        return super()._get_valid_moves()