import pygame, sys, time, random
from pygame.locals import *


FIRE = pygame.image.load('resources/fire.png')

class fire(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = FIRE



        self.x = 100
        self.y = 50
        self.rect = pygame.Rect(self.x, self.y, 25, 25)

    def move(self):
        if self.x>-100:
            self.x=self.x-3
            self.rect.x=self.x
            self.rect.y=50
        elif self.x<= -100:
            self.x=1000
