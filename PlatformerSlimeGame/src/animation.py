import pygame
from utils import load_images

class Animation:
    def __init__(self, imageList: list[pygame.Surface], imgDuration: int = 6, isAlive: bool = False):
        self.imageList = imageList
        self.lenImageList = len(imageList)
        self.isAlive = isAlive
        self.imgDuration = imgDuration
        self.frame = 0
        self.done  = False

    def copy(self):
        return Animation(self.imageList, self.imgDuration)
    
    def update(self):
        if self.isAlive:
            self.frame = (self.frame + 1) % (self.lenImageList * self.imgDuration)
            print(self.frame)
        else:
            self.frame = min(self.frame+1, self.lenImageList*self.imgDuration - 1)
            if (self.frame >= self.lenImageList*self.imgDuration - 1):
                self.done = True
                
    def getImg(self):
        return self.imageList[int(self.frame/self.imgDuration)]
        