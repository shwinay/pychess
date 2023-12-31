from board import Board
from side import Side
import pygame
from util import *

class Game:

    def __init__(self):
        self.board = Board()
        pygame.init()
        pygame.display.set_caption("Chess")
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        self.selected_tile = None

    def play_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.handle_mouse_input(mouse_to_grid_coords(*mouse_pos))
       
            self.draw_board()
            pygame.display.flip()
        
        pygame.quit()
    
    def handle_mouse_input(self, grid_pos: tuple):
        if self.selected_tile == grid_pos:
            self.selected_tile = None
        else:
            self.selected_tile = grid_pos

    def draw_selected_valid_moves(self):
        if self.selected_tile is None:
            return
        # TODO akudva

    def draw_board(self):
        # draw chessboard
        for i in range(NUM_TILES):
            for j in range(NUM_TILES):
                tile_color = WHITE if (i + j) % 2 == 0 else GREEN
                if (i, j) == self.selected_tile:
                    tile_color = YELLOW

                pygame.draw.rect(self.screen, tile_color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

                piece = self.board.grid[i][j]
                if piece is not None:
                    draw_piece(piece.get_piece_type(), piece.side, j * TILE_SIZE + (TILE_SIZE // 2), i * TILE_SIZE + (TILE_SIZE // 2), self.screen)