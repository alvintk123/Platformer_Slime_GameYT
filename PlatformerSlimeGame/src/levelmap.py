
import pygame
import os
from typing import TYPE_CHECKING
import json

# Get dir path to current file
BASE_DIR_TILEMAP = os.path.dirname(os.path.abspath(__file__))

# Get dir path to the level file
BASE_DIR_LEVEL = os.path.join(BASE_DIR_TILEMAP, "../levels/")

class LevelMap:
    def __init__(self, game, tileSize: int = 16):
        self.game = game
        self.tileSize = tileSize
        
        self.offTileMap = []
        self.tileMap = {}
        for i in range(5):
            self.tileMap[str(i) + ';10'] = {'type': 'ground', 'count': 1, 'pos': (i, 10)}
            self.tileMap['10;' + str(i)] = {'type': 'ground', 'count': 1, 'pos': (10, i)}
            
        # self.tileMap['5;10'] = {'type': 'ground', 'count': 1, 'pos': (5, 10)}
    
    def saveTileMap(self, pathName: str) -> None:
        with open(BASE_DIR_LEVEL + pathName, "w") as file:
            json.dump({'tileMap': self.tileMap, 'offTileMap': self.offTileMap, 'tileSize': self.tileSize}, file)
    
    def loadTileMap(self, pathName: str) -> None:
        fullPath = BASE_DIR_LEVEL + pathName
        
        if not os.path.exists(fullPath):
            raise FileNotFoundError(f"Can't find : {fullPath}")
        
        with open(fullPath, 'r') as file:
            mapData = json.load(file)
        
        self.tileMap = mapData['tileMap']
        self.offTileMap = mapData['offTileMap']
        self.tileSize = mapData['tileSize']
        
    
    def render(self, displaySurf: pygame.Surface, offset: tuple[int, int] = (0, 0)) -> None:
        
        for x in range(offset[0]//self.tileSize, (displaySurf.get_width()+offset[0])//self.tileSize+1):
            for y in range(offset[1]//self.tileSize,( displaySurf.get_height()+offset[1])//self.tileSize+1):
                pos = str(x) + ';' + str(y)
                if pos in self.tileMap:
                    tile = self.tileMap[pos]
                    displaySurf.blit(self.game.assets[tile['type']][tile['count']], (tile['pos'][0]*self.tileSize-offset[0],tile['pos'][1]*self.tileSize -offset[1]))
        
        for offTile in self.offTileMap:
            displaySurf.blit(self.game.assets[offTile['type']][offTile['count']], (offTile['pos'][0]-offset[0],offTile['pos'][1] -offset[1]))          
        
        