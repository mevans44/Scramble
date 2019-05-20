import pygame, sys, time
from pygame.locals import *

from ship import ship
from fire import fire
from fireball import fireball
ufo=ship()
fye=fire()
bal=fireball()
FPS = 1500000
WHITE=(250,250,250)
fpsClock = pygame.time.Clock()
def update_ship():
    DISPLAYSURF.blit(ufo.image,ufo.rect)
def update_fire():
    DISPLAYSURF.blit(fye.imgae,ufo.rect)
def update_fireball():
    DISPLAYSURF.blit(bal.imgae,bal.rect)

DISPLAYSURF = pygame.display.set_mode((1024,576), 0, 32)
pygame.display.set_caption("Scrambler Remake")

BACKGROUND = pygame.image.load('resources/spacex.png')
background_x = 0
background_y = BACKGROUND.get_width()
clock=pygame.time.Clock()
speed=60
def bg():
    DISPLAYSURF.blit (BACKGROUND, (background_x,0))
    DISPLAYSURF.blit(BACKGROUND,(background_y,0))

while True:
    bg()
    clock.tick(speed)
    background_x -= 5.0
    background_y -= 5.0
    if background_x < BACKGROUND.get_width() * -1:
        background_x= BACKGROUND.get_width()

    if background_y < BACKGROUND.get_width() * -1:
        background_y= BACKGROUND.get_width()

    DISPLAYSURF.blit(ufo.image,ufo.rect)
    DISPLAYSURF.blit(fye.image,fye.rect)
    DISPLAYSURF.blit(bal.image,bal.rect)
    fye.move()
    bal.move()
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
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
            update_ship()

    pygame.display.flip()
    fpsClock.tick(FPS)
