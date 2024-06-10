import pygame
from sys import exit
from os.path import join

cellSize = 80
rows = 10
cols = 16
window_width = cellSize * cols
window_height = cellSize * rows

# Colors
lightGreen = '#aad751'
darkGreen = '#a2d149'

# Start position
start_length = 3
start_row = rows // 2
start_col = start_length + 2

# Shadow
shadow_size = pygame.Vector2(4, 4)
shadow_opacity = 50
