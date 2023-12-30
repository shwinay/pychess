from side import Side

class Board:
    
    BOARD_SIZE = 8

    def __init__(self):
        self.grid = [[None for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.current_move = Side.WHITE
    
    def print_board():
        for i in range()