import pygame, sys, time, random
from pygame.locals import *

SHIP = pygame.image.load('resources/UFO.png')
class ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = SHIP
        #Image name
        self.imgage = pygame.transform.scale(SHIP, (25,25))
        self.ground=ground
        self.x = 200
        self.y = 280
        self.rect = pygame.Rect(self.x, self.y, 25, 25)

    def up(self):
        self.rect.y = self.rect.y - 25

    def down(self):
        self.rect.y = self.rect.y + 25

    def left(self):
        self.rect.x = self.rect.x - 25

    def right(self):
        self.rect.x = self.rect.x + 25
