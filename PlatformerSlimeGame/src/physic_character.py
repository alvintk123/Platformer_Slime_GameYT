from __future__ import annotations
from typing import TYPE_CHECKING

import pygame
from levelmap import LevelMap
if TYPE_CHECKING:
    from main import Game

class PhysicCharacter:
    def __init__(self, game: Game, e_type: str, pos: tuple[int, int], size: tuple[int, int]) -> None:
        self.game = game
        self.type = e_type
        self.pos  = list(pos)
        self.size = size
        
        # velocity 
        self.velocity = [0, 0]
        self.action = 'idle'
        self.animation = self.game.assets[self.type + '/' + self.action]

    
    def update(self, levelMap: LevelMap, movement: tuple[int, int] ) -> None:
        
        Movement =  (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        self.pos[0] += Movement[0]
        
        self.pos[1] += Movement[1]
        
        # Add gravity force 
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
        # update animation
        self.animation.update()
    
    
    def render(self, displaySurf: pygame.Surface, offset: tuple[int, int] = (0, 0)) -> None:
        displaySurf.blit(self.animation.getImg(), (self.pos[0]-offset[0], self.pos[1]-offset[1]))
        