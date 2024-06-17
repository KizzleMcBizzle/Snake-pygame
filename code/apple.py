import os
from settings import *
from random import choice

class Apple:
    def __init__(self, snake):
        self.display_surface = pygame.display.get_surface()
        self.snake = snake
        self.set_pos()
        
        #Apple image
        script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        rel_path = "../graphics/apple.png"  # The path to the image file relative to the script directory
        abs_file_path = os.path.join(script_dir, rel_path)  # Join the two paths
        self.surf = pygame.image.load(abs_file_path).convert_alpha()  # Load the image
        
    def set_pos(self):
        availablePos = [pygame.Vector2(x,y) 
                        for x in range(cols) 
                        for y in range(rows)
                        if pygame.Vector2(x,y) not in self.snake.body]
        self.pos = choice(availablePos)
        
        
        
    def draw(self):
        rect = pygame.Rect(self.pos.x * cellSize, self.pos.y * cellSize, cellSize, cellSize)
        pygame.draw.rect(self.display_surface,'blue', rect)
        # self.display_surface.blit(self.surf, rect)