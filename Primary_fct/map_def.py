import pygame
from pygame.locals import * 
from constantes import *

class Mapping:
    
    def __init__(self, file):
        self.file = file
        self.structure = 0
        
    def generate(self):
        #create a list to generate a map from a file 
        with open(self.file, "r") as file:
            map_structure = []
            for line in file:
                map_line = []
                for sprite in line:
                    if sprite != '\n':
                        map_line.append(sprite)
                map_structure.append(map_line)
            self.structure = map_structure
            
    def afficher(self, screen_game):
#         motif_01 = pygame.image.load(motif_01_pic).convert()
#         motif_02 = pygame.image.load(motif_02_pic).convert_alpha()
        
        line_num = 0
        for line in self.structure:
            square_num = 0
            for sprite in line:
                #On calcule la position réelle en pixels
                x = square_num * sprite_size
                y = line_num * sprite_size
#                 if sprite == 'm01':  
#                     screen_game.blit(motif_01, (x,y))
#                 elif sprite == 'm02':       
#                     screen_game.blit(motif_02, (x,y))
                square_num += 1
            line_num += 1