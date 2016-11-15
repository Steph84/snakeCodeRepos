import pygame
from pygame.locals import *

class Niveau:
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
    
    
    def generer(self): 
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau
    
    
    def afficher(self, fenetre):
#         mur = pygame.image.load(image_mur).convert()
#         depart = pygame.image.load(image_depart).convert()
#         arrivee = pygame.image.load(image_arrivee).convert_alpha()
        
        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #On calcule la position réelle en pixels
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':           #m = Mur
                    fenetre.blit(mur, (x,y))
                elif sprite == 'd':           #d = Départ
                    fenetre.blit(depart, (x,y))
                elif sprite == 'a':           #a = Arrivée
                    fenetre.blit(arrivee, (x,y))
                num_case += 1
            num_ligne += 1
            