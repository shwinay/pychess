from typing import List
from side import Side
from abc import abstractmethod

class Piece:

    def __init__(self, side: Side):
        self.side = side

    @abstractmethod
    def _get_valid_moves(self, i: int, j: int, grid: List[List]) -> List[tuple]:
        pass

    @abstractmethod
    def get_piece_type(self):
        pass