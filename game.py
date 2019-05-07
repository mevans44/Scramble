import pygame, sys, time
from pygame.locals import *

from ship import ship




DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("Scrambler Remake")

while True:
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
