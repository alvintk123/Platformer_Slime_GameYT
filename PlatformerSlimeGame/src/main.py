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
            # Background
            'background': load_image('ui/backgrounds/background.png'),
            'player/idle': Animation(load_images('sprites/player/idle', 1), imgDuration=10 , loopImg=True),
            'player/run': Animation(load_images('sprites/player/run', 1), imgDuration=5, loopImg=True),
            'player/roll': Animation(load_images('sprites/player/roll', 1), imgDuration=5, loopImg=True),
            'player/hit': Animation(load_images('sprites/player/hit', 1), imgDuration=5, loopImg=True),
            'player/death': Animation(load_images('sprites/player/death', 1), imgDuration=5, loopImg=True),

            # Tile Map
            'ground': load_images('sprites/environment/tiles/ground'),
            
            # items
            'fruits': load_images('sprites/environment/items/fruits'),
            'coins': load_images('sprites/environment/items/coins'),
            'potions': load_images('sprites/environment/items/potions'),
            
            # Decorations
            'grass': load_images('sprites/environment/decorations/grass'),
            'large_decor': load_images('sprites/environment/decorations/large_decor'),
            'mushrooms': load_images('sprites/environment/decorations/mushrooms'),
            'sign': load_images('sprites/environment/decorations/sign'),
            'trees': load_images('sprites/environment/decorations/trees'),

            # interactives
            'boxes': load_images('sprites/environment/interactives/boxes'),
            'crates': load_images('sprites/environment/interactives/crates'),
            'ladders': load_images('sprites/environment/interactives/ladders'),
            'platforms': load_images('sprites/environment/interactives/platforms'),
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