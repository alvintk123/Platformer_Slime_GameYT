import pygame
import sys

from utils import load_image, load_images

FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Slime Game")
        
        self.screen = pygame.display.set_mode((640, 480))
        
        self.clock  = pygame.time.Clock()
        
        # --------------------- load image ----------------
        self.assets = {
            'background': load_image('ui/backgrounds/background.png'),
            'player/idle': load_images('sprites/player/idle', 1),
        }
        
        self.count = 0
    
    def run(self):
        while True:
            self.screen.fill((0, 0 , 0))
            # blit character for testing
            imgChar = self.assets['player/idle'][self.count]
            self.count += 1
            if self.count >= len(self.assets['player/idle']):
                self.count = 0
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.blit(self.assets['background'], (0, 0))
            self.screen.blit(imgChar, (50, 50))
            pygame.display.update()
            self.clock.tick(FPS)

Game().run()