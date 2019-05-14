import pygame, sys, time
from pygame.locals import *

from ship import ship
from fire import fire
from fireball import fireball
ufo=ship()
fye=fire()
bal=fireball()
FPS = 90
WHITE=(250,250,250)
fpsClock = pygame.time.Clock()
def update_ship():
    DISPLAYSURF.blit(ufo.image,ufo.rect)
def update_fire():
    DISPLAYSURF.blit(fye.imgae,ufo.rect)
def update_fireball():
    DISPLAYSURF.blit(bal.imgae,bal.rect)

DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("Scrambler Remake")

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(ufo.image,ufo.rect)
    DISPLAYSURF.blit(fye.image,fye.rect)
    DISPLAYSURF.blit(bal.image,bal.rect)
    fye.move()
    bal.move()
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
                update_ship()
                update_fire()
                update_fireball()
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
