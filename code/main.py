from settings import *
from snake import Snake
class Main:
    def __init__(self):
        
        #general 
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('Snake')
        
        #game objects
        
        #checkerboard background
        self.bg_rects = [ pygame.Rect((col + row%2) * cellSize, row * cellSize, cellSize, cellSize) 
                         for row in range(rows) 
                         for col in range(0,cols,2)]
        
        #Snake
        self.snake = Snake()
        
    def draw_bg(self):
        for bg_rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, darkGreen, bg_rect)
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.display_surface.fill(lightGreen)
            self.draw_bg()
            self.snake.draw()        
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()