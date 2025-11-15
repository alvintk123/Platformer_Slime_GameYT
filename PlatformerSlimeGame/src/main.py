import pygame
import sys

from animation import Animation
from levelmap import LevelMap
from utils import load_image, load_images
from physic_character import PhysicCharacter


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
            'player/idle': Animation(load_images('sprites/player/idle', 1), imgDuration=10 , isAlive=True),
            'player/run': Animation(load_images('sprites/player/run', 1), imgDuration=5, isAlive=True),
            'player/roll': Animation(load_images('sprites/player/roll', 1), imgDuration=5, isAlive=True),
            'player/hit': Animation(load_images('sprites/player/hit', 1), imgDuration=5, isAlive=True),
            'player/death': Animation(load_images('sprites/player/death', 1), imgDuration=5, isAlive=True),

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
        
        # movement (left, right)
        self.keyMovement = [False, False]
        self.offsetScroll = [0, 0]
        
        # -------------- Tile Map ---------------
        self.levelMap = LevelMap(self, 16)
        
        # --------------- Player  ----------------
        self.player = PhysicCharacter(self, 'player', (70, 70), (13, 19))
        
        # Load Map
        self.level = 1
        self.levelMap.loadTileMap("level" + str(self.level) + ".json")

    def run(self):
        while True:
            self.screen.fill((0, 0 , 0))
            self.display.blit(self.assets['background'], (0, 0))

            
            # Update character
            self.player.update(self.levelMap, (self.keyMovement[1] - self.keyMovement[0], 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pass
                    if event.key == pygame.K_LEFT:
                        self.keyMovement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.keyMovement[1] = True
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        pass
                    if event.key == pygame.K_LEFT:
                        self.keyMovement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.keyMovement[1] = False
            
            # render Level map
            self.levelMap.render(self.display, offset=(0, 0))
            
            # render player
            self.player.render(self.display, offset=(0, 0))
            
            self.screen.blit(pygame.transform.scale(self.display, (self.screen.get_width(), self.screen.get_height())), (0, 0))
            
            pygame.display.update()
            self.clock.tick(FPS)

Game().run()