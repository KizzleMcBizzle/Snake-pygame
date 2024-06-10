from settings import *

class Main:
    def __init__(self):
        
        #general 
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()


main = Main()
main.run()