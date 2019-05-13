import pygame, sys, time
from pygame.locals import *

from ship import ship
ufo=ship()
FPS = 90
WHITE=(250,250,250)
fpsClock = pygame.time.Clock()
def update_ship():
    DISPLAYSURF.blit(ufo.image,ufo.rect)

DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("Scrambler Remake")

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(ufo.image,ufo.rect)
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
                update_ship()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    ufo.up()
                    DISPLAYSURF.blit(ufo.image,ufo.rect)

                if event.key==K_DOWN:
                    ufo.down()
                    DISPLAYSURF.blit(ufo.image,ufo.rect)

                if event.key==K_RIGHT:
                    ufo.right()
                    DISPLAYSURF.blit(ufo.image,ufo.rect)

                if event.key==K_LEFT:
                    ufo.left()
                    DISPLAYSURF.blit(ufo.image,ufo.rect)

    pygame.display.flip()
    fpsClock.tick(FPS)
