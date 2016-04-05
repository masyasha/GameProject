from pygame import *
import pygame as py
import random as ran

PLATFORM_W = 32
PLATFORM_H = 32
PLATFORM_COLOUR = (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255))

class Blocks(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_W, PLATFORM_H))
        self.image = image.load("bl.gif")
        #self.image.fill(PLATFORM_COLOUR)
        self.rect = Rect(x, y, PLATFORM_W, PLATFORM_H)

