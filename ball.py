import pygame, sys, time, random
from pygame.locals import *


BALL = pygame.image.load('resources/fire.png')

class ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = BALL



        self.x = 100
        self.y = 50
        self.rect = pygame.Rect(self.x, self.y, 25, 25)

    def move(self):
        if self.x>-100:
            self.x=self.x-4
            self.rect.x=self.x
            self.rect.y=200
        elif self.x<= -100:
            self.x=1000
