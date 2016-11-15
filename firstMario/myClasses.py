#@UndefinedVariable

import pygame, sys
from pygame.locals import *
from PIL import Image

class Character:
    def __init__(self, left, right):
        #Sprites du personnage
        self.left = pygame.image.load(left).convert_alpha()
        self.right = pygame.image.load(right).convert_alpha()
        #Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #Direction par dfaut
        self.direction = self.droite
        
    def loadSprites(self, charSprite):
        #parcourir l image pour localiser les differentes images
        #affecter une sequence d image a une direction
        pass
        
class Pictures:
    def __init__(self, myPicture):
        self.picture = myPicture
        
    def getTile(self, myPicture, xTile, yTile, tileSize):
        posX = (self.tileSize * xTile)
        posY = (self.tileSize * yTile)
        box = (posX, posY, posX + self.tileSize, posY + self.tileSize)
        return self.spritesheet.crop(box)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        