import pygame
from piecetype import PieceType
from side import Side

WINDOW_SIZE = 800
NUM_TILES = 8
TILE_SIZE = WINDOW_SIZE / NUM_TILES
IMG_SIZE = int(0.90 * TILE_SIZE)
WHITE = (255, 255, 255)
GREEN = (118,150,86)
YELLOW = (204, 237, 0)
LIGHT_RED = (255, 150, 125)
        
def in_bounds(i, j) -> bool:
    return i >= 0 and i < NUM_TILES and j >= 0 and j < NUM_TILES

base_path = './piece-images/'

def draw_piece(piece_type: PieceType, side: Side, center_i: int, center_j: int, screen):
    piece_type_str = piece_type.name.lower()
    side_str = 'black-' if side == Side.BLACK else 'white-'
    img_path = base_path + side_str + piece_type_str + '.png'

    piece_img = pygame.transform.smoothscale(pygame.image.load(img_path), (IMG_SIZE, IMG_SIZE))
    piece_rect = piece_img.get_rect()
    piece_rect.center = (center_i, center_j)
    screen.blit(piece_img, piece_rect)

def mouse_to_grid_coords(mouse_i: int, mouse_j: int) -> tuple:
    return (int(mouse_j // TILE_SIZE), int(mouse_i // TILE_SIZE))