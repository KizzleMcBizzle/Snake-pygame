from settings import *
from random import choice

class Apple:
    def __init__(self, snake):
        self.display_surface = pygame.display.get_surface()
        self.snake = snake
        self.set_pos()
        
    def set_pos(self):
        availablePos = [pygame.Vector2(x,y) 
                        for x in range(cols) 
                        for y in range(rows)
                        if pygame.Vector2(x,y) not in self.snake.body]
        self.pos = choice(availablePos)
        
        
        
    def draw(self):
        rect = pygame.Rect(self.pos.x * cellSize, self.pos.y * cellSize, cellSize, cellSize)
        pygame.draw.rect(self.display_surface,'blue', rect)