import pygame
import sys

from utils import load_images
from levelmap import LevelMap

FPS = 60
RENDER_SCALE = 2
NAME_LEVEL   = 'level1.json'
NAME_LOAD_LEVEL = 'Level1.json'
class MapEditor:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Slime Game")
        
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))
        self.clock  = pygame.time.Clock()
        
        # --------------------- load image ----------------
        self.assets = {
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
        
        self.tileAssetsList = list(self.assets)
        self.tileTypeIndex  = 0
        self.tileCount      = 0
        
        # ---- Key Handler ----
        self.leftShift   = False
        self.leftClick   = False
        self.rightClick  = False
        self.onGrid      = True
        self.leftCtrl    = False
        
        self.keyMovement = [False, False, False, False]
        self.offsetScroll = [0, 0]
        
        self.levelMap = LevelMap(self, tileSize=16)
        
    def run(self):
        while True:
            self.display.fill((0, 0 , 0))
            
            self.offsetScroll[0] += int((self.keyMovement[1] - self.keyMovement[0])*2)
            self.offsetScroll[1] += int((self.keyMovement[3] - self.keyMovement[2])*2)
            renderOffsetScroll = (self.offsetScroll[0], self.offsetScroll[1])
            # Get current Image
            curTileImg = self.assets[self.tileAssetsList[self.tileTypeIndex ]][self.tileCount]
            # print(self.offsetScroll)
            
            mousePos = pygame.mouse.get_pos()
            mousePos = (mousePos[0]//RENDER_SCALE, mousePos[1]//RENDER_SCALE)

            imgMousePos = (int(mousePos[0]+self.offsetScroll[0])//self.levelMap.tileSize, int(mousePos[1]+self.offsetScroll[1])//self.levelMap.tileSize)
            
            # Create tile 
            if self.leftClick:
                if self.onGrid:
                    self.levelMap.tileMap[str(imgMousePos[0])+';'+str(imgMousePos[1])] = {'type': self.tileAssetsList[self.tileTypeIndex], 'count': self.tileCount, 'pos': imgMousePos}
                else:
                    self.levelMap.offTileMap.append({'type': self.tileAssetsList[self.tileTypeIndex], 'count': self.tileCount, 'pos': (mousePos[0] +renderOffsetScroll[0],mousePos[1] +renderOffsetScroll[1] )})
            
            # Delete tile 
            if self.rightClick:
                if self.onGrid:
                    curTilePos = str(imgMousePos[0])+';'+str(imgMousePos[1])
                    if curTilePos in self.levelMap.tileMap:
                        del self.levelMap.tileMap[curTilePos]
                else:
                    for offTile in self.levelMap.offTileMap:
                        tileImg = self.assets[offTile['type']][offTile['count']]
                        tileRect = pygame.Rect((offTile['pos'][0] - renderOffsetScroll[0], offTile['pos'][1] - renderOffsetScroll[1], tileImg.get_width(), tileImg.get_height()))
                        if tileRect.collidepoint(mousePos):
                            self.levelMap.offTileMap.remove(offTile)
                            
            # Show tile image at cursor
            if self.onGrid:
                self.display.blit(curTileImg, (int(imgMousePos[0]*self.levelMap.tileSize-self.offsetScroll[0]),int(imgMousePos[1]*self.levelMap.tileSize-self.offsetScroll[1])))
            else:
                self.display.blit(curTileImg, mousePos)
            self.levelMap.render(self.display, offset=renderOffsetScroll)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.leftClick = True
                    if event.button == 3:
                        self.rightClick = True
                    if self.leftShift:
                        if event.button == 4:
                            self.tileTypeIndex = (self.tileTypeIndex - 1) % len(self.tileAssetsList)
                            self.tileCount = 0
                        if event.button == 5:
                            self.tileTypeIndex = (self.tileTypeIndex + 1) % len(self.tileAssetsList)
                            self.tileCount = 0
                    else:
                        if event.button == 4:
                            self.tileCount = (self.tileCount - 1) % len(self.assets[self.tileAssetsList[self.tileTypeIndex]])
                        if event.button == 5:
                            self.tileCount = (self.tileCount + 1) % len(self.assets[self.tileAssetsList[self.tileTypeIndex]])
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.leftClick = False
                    if event.button == 3:
                        self.rightClick = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.keyMovement[0] = True
                    if event.key == pygame.K_d:
                        self.keyMovement[1] = True
                    if event.key == pygame.K_w:
                        self.keyMovement[2] = True
                    if event.key == pygame.K_s:
                        self.keyMovement[3] = True
                    if event.key == pygame.K_LSHIFT:
                        self.leftShift = True
                    if event.key == pygame.K_g:
                        self.onGrid = not self.onGrid
                    if event.key == pygame.K_LCTRL:
                        self.leftCtrl = True
                    if event.key == pygame.K_s:
                        if self.leftCtrl:
                            print("in")
                            self.levelMap.saveTileMap(NAME_LEVEL)
                    if event.key == pygame.K_l:
                        if self.leftCtrl:
                            print("in_2")
                            self.levelMap.loadTileMap(NAME_LOAD_LEVEL)       
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.keyMovement[0] = False
                    if event.key == pygame.K_d:
                        self.keyMovement[1] = False
                    if event.key == pygame.K_w:
                        self.keyMovement[2] = False
                    if event.key == pygame.K_s:
                        self.keyMovement[3] = False
                    if event.key == pygame.K_LSHIFT:
                        self.leftShift = False
                    if event.key == pygame.K_LCTRL:
                        self.leftCtrl = False
                        
            self.screen.blit(pygame.transform.scale(self.display, (self.screen.get_width(), self.screen.get_height())), (0, 0))
            
            pygame.display.update()
            self.clock.tick(FPS)

MapEditor().run()