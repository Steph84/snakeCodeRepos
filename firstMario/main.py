#@UndefinedVariable

import pygame, sys
from pygame.locals import *
from myClasses import Pictures

#background picture 1280x800 ratio 1,6
windowWidth = 960
windowHeight = 600

#initialize pygame
pygame.init()

#create a window with size setting
myWindow = pygame.display.set_mode((windowWidth, windowHeight))

#add the background from a picture and convert to the right format
myBackground = pygame.image.load("background.png").convert()
#change the opacity alpha
gumba = pygame.image.load("perso.png").convert_alpha()
gumba_size = gumba.get_rect().size


#paste the background on the window
myWindow.blit(pygame.transform.scale(myBackground, (windowWidth, windowHeight)), (0, 0))
#manage of the picture position by the rect coordonate origin by default
myWindow.blit(gumba, (0, windowHeight-gumba_size[1]-52))

myTest = pygame.image.load("SpriteSheet.png").convert_alpha()
myWindow.blit(pygame.transform.scale(myTest, (20, 30)), (5, 5))
truc = myTest.getTile(myTest, 1, 2, 5)
myWindow.blit(pygame.transform.scale(truc, (20, 30)), (200, 200))


#refresh
pygame.display.flip()

# infinite loop
while True:
    #Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
            
        elif event.type == KEYDOWN:
            
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                    
#             #movement
#             elif event.key == K_RIGHT:
#                 dk.deplacer('droite')
#             elif event.key == K_LEFT:
#                 dk.deplacer('gauche')
#             elif event.key == K_UP:
#                 dk.deplacer('haut')
#             elif event.key == K_DOWN:
#                 dk.deplacer('bas')    
#             
#             
            
            
            
            
            
            
            
            
            
            
            
            