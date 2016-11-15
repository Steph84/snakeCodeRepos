import pygame
from pygame.locals import * 
from constantes import *
from msilib.schema import ControlEvent


detecter si manette
si oui, mettre type_key = gp
else type_key = kb

Control
if type_key == gp
gamepad()
else
keyboard