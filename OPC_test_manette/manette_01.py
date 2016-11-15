import pygame
from pygame.locals import *

pygame.init()

nb_joysticks = pygame.joystick.get_count()
print("Il y a", nb_joysticks, "joystick(s) branche(s)")

#Et on en cree un s'il y a en au moins un
if nb_joysticks > 0:
    mon_joystick = pygame.joystick.Joystick(0)

mon_joystick.init() #Initialisation

print("Axes :", mon_joystick.get_numaxes())
print("Boutons :", mon_joystick.get_numbuttons())
print("Trackballs :", mon_joystick.get_numballs())
print("Hats :", mon_joystick.get_numhats())

nb_boutons = mon_joystick.get_numbuttons()

if nb_boutons >= 4:
    continuer = 1
    while continuer:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                    
            if event.type == JOYAXISMOTION:
                if event.axis == 0 and event.value > 0:
                    print("mouvement_droite")
                if event.axis == 0 and event.value < 0:
                    print("mouvement_gauche")
                if event.axis == 1 and event.value > 0:
                    print("mouvement_bas")
                if event.axis == 1 and event.value < 0:
                    print("mouvement_haut")
                    
            if event.type == JOYBUTTONDOWN:
                if event.button == 0:
                    print("1st button")
                elif event.button == 1:
                    print("2nd button")
                elif event.button == 2:
                    print("3rd button")
                elif event.button == 3:
                    print("4th button")
                elif event.button == 4:
                    print("5th button")
                elif event.button == 5:
                    print("6th button")
                elif event.button == 6:
                    print("7th button")
                elif event.button == 7:
                    print("8th button")
                elif event.button == 8:
                    print("9th button")
                elif event.button == 9:
                    print("10th button")
                    
    else:
        print("Votre Joystick ne possede pas au moins 4 boutons")
else:
    print("Vous n'avez pas branche de Joystick...")