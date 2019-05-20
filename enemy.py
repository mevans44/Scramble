import pygame, sys, time, random
from pygame.locals import *


BADGUY = pygame.image.load('resources/badguy.png')

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = BADGUY
        self.x = random.randrange(50,800)
        self.y = 500
        self.rect = pygame.Rect(self.x, self.y, 25, 25)

    def display(self):
        if self.x>-100:
            self.x=self.x-4
            self.rect.x=self.x
            self.rect.y=425
        elif self.x<= -100:
            self.x=1000
