import pygame
from pygame.locals import *
from PIL import Image

class SpriteSheetReader:
    def __init__(self, imageName, tileSize):
        self.spritesheet = Image.open(imageName)
        self.tileSize = tileSize
 
    def getTile(self, tileX, tileY):
        posX = (self.tileSize * tileX)
        posY = (self.tileSize * tileY)
        box = (posX, posY, posX + self.tileSize, posY + self.tileSize)
        return self.spritesheet.crop(box)
 
