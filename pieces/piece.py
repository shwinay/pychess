from typing import List
from abc import abstractmethod

class Piece:

    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
        pass

    @abstractmethod
    def _get_valid_moves(self) -> List[tuple]:
        pass 