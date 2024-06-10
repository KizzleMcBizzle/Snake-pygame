from settings import *

class Snake:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.body = [pygame.Vector2(start_col - col,start_row) for col in range(start_length)]
        self.direction = pygame.Vector2(1,0) #initial direction is right
        
    def update(self):
        # 0. Copy the body list to avoid updating the original list while removing the last element
        bodyCopy = self.body[:-1]
        # 1. Moving the head and inserting the new head at index 0 (First element of the list)
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        # 3. update the original body list
        self.body = bodyCopy[:]
        
    
    def draw(self):
        for point in self.body:
            rect = pygame.Rect(point.x * cellSize, point.y * cellSize, cellSize, cellSize)
            pygame.draw.rect(self.display_surface,'red', rect)