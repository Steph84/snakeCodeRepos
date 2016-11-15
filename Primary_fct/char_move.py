import pygame
from pygame.locals import * 
from constantes import *

#define movement of the character in 2D, keyboard and gamepad
class Movement:
    
    def __init__(self, left_pic, right_pic, up_pic, down_pic, map, type_key):
        #character sprites loaded
        self.left_pic = pygame.image.load(left_pic).convert_alpha()
        self.right_pic = pygame.image.load(right_pic).convert_alpha()
        self.up_pic = pygame.image.load(up_pic).convert_alpha()
        self.down_pic = pygame.image.load(down_pic).convert_alpha()
        
        #character position initialization in square and pixel
        #square mapping is defined in *** file
        self.square_x = 0
        self.square_y = 0
        self.x = 0
        self.y = 0
        
        #default direction
        self.direction = self.left_pic
        
        #map where is the character 
        self.map = map
        
        #keyboard or gamepad
        self.type_key = type_key
    
    
    def keyboard_move(self, direction):
        
        #movement to the left
         if direction == 'left':
            if self.square_x > 0:
                if self.map.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.gauche
        
        if direction == 'droite':
            #Pour ne pas dépasser l'écran
            if self.case_x < (nombre_sprite_cote - 1):
                #On vérifie que la case de destination n'est pas un mur
                if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                    #Déplacement d'une case
                    self.case_x += 1
                    #Calcul de la position "réelle" en pixel
                    self.x = self.case_x * taille_sprite
            #Image dans la bonne direction
            self.direction = self.droite
        
        #Déplacement vers la gauche
       
        
        #Déplacement vers le haut
        if direction == 'haut':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.haut
        
        #Déplacement vers le bas
        if direction == 'bas':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.bas