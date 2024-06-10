from settings import *

class Snake:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.body = [pygame.Vector2(start_col - col,start_row) for col in range(start_length)]
    
    def draw(self):
        for point in self.body:
            rect = pygame.Rect(point.x * cellSize, point.y * cellSize, cellSize, cellSize)
            pygame.draw.rect(self.display_surface,'red', rect)