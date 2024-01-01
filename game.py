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
        self.selected_valid_moves = []

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
            self.draw_selected_valid_moves()
            pygame.display.flip()
        
        pygame.quit()
    
    def handle_mouse_input(self, grid_pos: tuple):
        selected_i, selected_j = grid_pos
        selected_piece = self.board.grid[selected_i][selected_j]

        # unselect if already selected
        if self.selected_tile == grid_pos:
            self.selected_tile = None
            self.selected_valid_moves.clear()
        # set selected valid moves if mouse click is on a piece
        elif selected_piece is not None and selected_piece.side == self.board.current_turn:
            self.selected_tile = grid_pos
            self.selected_valid_moves = selected_piece.get_valid_moves(selected_i, selected_j, self.board.grid)
        # handle piece movement if piece already selected
        elif grid_pos in self.selected_valid_moves:
            self.board.handle_move(self.selected_tile, grid_pos)
            self.selected_tile = None
            self.selected_valid_moves.clear()

    def draw_board(self):
        for i in range(NUM_TILES):
            for j in range(NUM_TILES):
                # draw tile
                tile_color = WHITE if (i + j) % 2 == 0 else GREEN
                if (i, j) == self.selected_tile:
                    tile_color = YELLOW

                pygame.draw.rect(self.screen, tile_color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

                # draw piece if present
                piece = self.board.grid[i][j]
                if piece is not None:
                    draw_piece(piece.get_piece_type(), piece.side, j * TILE_SIZE + (TILE_SIZE // 2), i * TILE_SIZE + (TILE_SIZE // 2), self.screen)
    
    def draw_selected_valid_moves(self):
        for valid_i, valid_j in self.selected_valid_moves:
            selected_screen_coords = (valid_j * TILE_SIZE + (TILE_SIZE // 2), valid_i * TILE_SIZE + (TILE_SIZE // 2))
            pygame.draw.circle(self.screen, LIGHT_RED, selected_screen_coords, int(TILE_SIZE // 8))