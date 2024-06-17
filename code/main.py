from settings import *
from snake import Snake
from apple import Apple
class Main:
    def __init__(self):
        
        #general 
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('Snake')
        self.game_paused = False
        
        #game objects
        
        #checkerboard background
        self.bg_rects = [ pygame.Rect((col + row%2) * cellSize, row * cellSize, cellSize, cellSize) 
                         for row in range(rows) 
                         for col in range(0,cols,2)]
        
        #instances
        self.snake = Snake()
        self.apple = Apple(self.snake)
        
        #timer
        self.update_timer = pygame.event.custom_type()
        pygame.time.set_timer(self.update_timer, 100)
        self.game_active = False
        
    def draw_bg(self):
        self.display_surface.fill(lightGreen)
        for bg_rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, darkGreen, bg_rect)
        

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.snake.direction.y != 1:
            self.snake.direction = pygame.Vector2(0,-1)
        if keys[pygame.K_DOWN] and self.snake.direction.y != -1:
            self.snake.direction = pygame.Vector2(0,1)
        if keys[pygame.K_LEFT] and self.snake.direction.x != 1:
            self.snake.direction = pygame.Vector2(-1,0)
        if keys[pygame.K_RIGHT] and self.snake.direction.x != -1:
            self.snake.direction = pygame.Vector2(1,0)
            
    def collision(self):
        # 1. Apple collision
        if self.snake.body[0] == self.apple.pos:
            self.snake.body.append(self.snake.body[-1])
            self.apple.set_pos()
    
        #2. Wall or Snake collision (Game Over) 
        if self.snake.body[0] in self.snake.body[1:] or \
            not 0 <= self.snake.body[0].x < cols or \
            not 0 <= self.snake.body[0].y < rows:
            self.snake.reset()
            self.game_active = False
            
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == self.update_timer and self.game_active and not self.game_paused:
                    self.snake.update()
                if event.type == pygame.KEYDOWN:
                    self.game_active = True
                    if event.key == pygame.K_ESCAPE:
                        self.game_paused = not self.game_paused

            #updates
            if self.game_active:
                self.input()
                self.collision()
                
            #drawing
            self.draw_bg()
            self.snake.draw()
            self.apple.draw()        
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()