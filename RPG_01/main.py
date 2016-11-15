
import pygame
from pygame.locals import *
from data import *
# from map import *
from read_tile_set import *
# import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()
main_screen = pygame.display.set_mode((screen_width, screen_height))
 
icon = pygame.image.load(icon_pic)
pygame.display.set_icon(icon)
pygame.display.set_caption("My first RPG")


 
# niveau = Niveau(map_file)
# niveau.generer()
# niveau.afficher(main_screen)


#show image from tmx file
tmxdata = load_pygame("map_02.tmx")
images0 = []
images1 = []

#height tiles number
for y in range(36):
    #width tiles number
    for x in range(64):
        #for the layer 0
        image = tmxdata.get_tile_image(x,y,0)
        images0.append(image)

#displays tiles in locations
i = 0
for y in range(36):
    for x in range(64):
        main_screen.blit(images0[i],(x*16,y*16))
        i += 1
        
        
        
for y in range(36):
    for x in range(64):
        image = tmxdata.get_tile_image(x,y,1)
        images1.append(image)

j = 0
for y in range(36):
    for x in range(64):
        main_screen.blit(images1[j],(x*16,y*16))
        j += 1
        
        


# reader = SpriteSheetReader("tiles.png", tile_size)
# tile1 = reader.getTile(0, 0)
# tile1.show()

pygame.display.flip()



while True:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
            
            
            
            