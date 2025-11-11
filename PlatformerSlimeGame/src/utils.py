import pygame
import os

IMG_PATH = '../assets/'

def load_image(path: str, scale: int = 1) -> pygame.Surface:
    img = pygame.image.load(IMG_PATH + path).convert()
    img = pygame.transform.scale(img, (img.get_width()/scale, img.get_height()/scale))
    
    img.set_colorkey((0, 0, 0))
    return img


def load_images(path: str, scale: int = 1) -> list[pygame.Surface]:
    images_list = []
    
    listDirImage = sorted(os.listdir(IMG_PATH+path))
    for dirImg in listDirImage:
        images_list.append(load_image(path + "/" + dirImg))

    return images_list
    
    
    