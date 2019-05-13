import pygame, sys, time, random
from pygame.locals import *

SHIP = pygame.image.load('resources/UFO.png')
class ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = SHIP
        #Image name

        self.x = 100
        self.y = 100
        self.rect = pygame.Rect(self.x, self.y, 25, 25)

    def up(self):
        self.rect.y = self.rect.y - 25
        if self.rect.y < 0:
            self.kill()

    def down(self):
        self.rect.y = self.rect.y + 25
        if self.rect.x < 0:
            self.kill()

    def left(self):
        self.rect.x = self.rect.x - 25

    def right(self):
        self.rect.x = self.rect.x + 25
