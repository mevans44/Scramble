import pygame, sys, time
from pygame.locals import *

from ship import ship
ufo=ship()
FPS = 90

fpsClock = pygame.time.Clock()


DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("Scrambler Remake")
x=0
while True:
    if x==0:
        DISPLAYSURF.blit(ufo.image,ufo.rect)
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    ship.up()
                    DISPLAYSURF.blit(ufo.image,ufo.rect)
                if event.key==K_DOWN:
                    ship.down()
                    DISPLAYSURF.blit(ufo.image,ufo.rect)
                if event.key==K_RIGHT:
                    ship.right()
                    DISPLAYSURF.blit(ufo.image,ufo.rect)
                if event.key==K_LEFT:
                    ship.left()
                    DISPLAYSURF.blit(ufo.image,ufo.rect)
    pygame.display.update()
    fpsClock.tick(FPS)
