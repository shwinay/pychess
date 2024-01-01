from typing import List
from side import Side
from abc import abstractmethod
from util import *

class Piece:

    def __init__(self, side: Side):
        self.side = side

    @abstractmethod
    def get_valid_moves(self, i: int, j: int, grid: List[List]) -> List[tuple]:
        pass

    @abstractmethod
    def get_piece_type(self):
        pass

    def get_directional_valid_moves(self, i: int, j: int, grid: List[List], directions: List[tuple]):
        valid_moves = []

        for i_dir, j_dir in directions:
            new_i, new_j = (i + i_dir, j + j_dir)
            while in_bounds(new_i, new_j):
                tile_piece = grid[new_i][new_j]
                if tile_piece is None:
                    valid_moves.append((new_i, new_j))
                    new_i += i_dir
                    new_j += j_dir
                else:
                    if tile_piece.side != self.side:
                        valid_moves.append((new_i, new_j))
                    break

        return valid_moves