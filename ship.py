import pygame, sys, time, random
from pygame.locals import *

FROG = pygame.image.load('resources/frog.png')
class ship(pygame.sprite.Sprite):
    def __init__(self):
        #When frog calss is ran
        super().__init__()
        self.image = FROG
        #Image name
        self.imgage = pygame.transform.scale(FROG, (25,25))
        #Size of image
        self.points = 0
        self.x = 200
        self.y = 280
        #Spawn
        self.rect = pygame.Rect(self.x, self.y, 25, 25)
