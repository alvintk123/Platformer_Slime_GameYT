import pygame
import sys

from animation import Animation
from utils import load_image, load_images

FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Slime Game")
        
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))
        self.clock  = pygame.time.Clock()
        
        # --------------------- load image ----------------
        self.assets = {
            'background': load_image('ui/backgrounds/background.png'),
            'player/idle': load_images('sprites/player/idle', 1),
            'player/run': Animation(load_images('sprites/player/run', 1), imgDuration=3),
            'player/roll': Animation(load_images('sprites/player/roll', 1), imgDuration=15),
        }
        
        self.animation = self.assets['player/run'].copy()
        self.animation1 = self.assets['player/roll'].copy()
        
        self.count = 0
    
    def run(self):
        while True:
            self.screen.fill((0, 0 , 0))
            self.display.blit(self.assets['background'], (0, 0))
            # blit character for testing
            imgChar = self.assets['player/idle'][self.count]
            self.count += 1
            
            self.animation.update()
            self.animation1.update()
            print("done: ", self.animation1.done)
            if self.count >= len(self.assets['player/idle']):
                self.count = 0
                
            self.display.blit(self.animation.getImg(), (80, 80))
            self.display.blit(self.animation1.getImg(), (240, 240))
            self.display.blit(imgChar, (50, 50))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.blit(pygame.transform.scale(self.display, (self.screen.get_width(), self.screen.get_height())), (0, 0))
            
            pygame.display.update()
            self.clock.tick(FPS)

Game().run()