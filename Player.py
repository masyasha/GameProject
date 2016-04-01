import pygame as py
from pygame import *
import random as ran

MOVE_SPEED = 5
PL_W = 20
PL_H = 30
PL_COLOUR = (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255))

class Player(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        x, y = 540, 578
        self.vel_x = self.vel_y = 0
        self.X_start = x
        self.Y_start = y
        self.image = Surface((PL_W,PL_H))
        self.image.fill(PL_COLOUR)
        self.rect = Rect(x, y, PL_W, PL_H)
    def update(self, left, right):
        if left: self.vel_x = -MOVE_SPEED
        if right: self.vel_x = MOVE_SPEED
        if not(left or right): self.vel_x = 0
        self.rect.x += self.vel_x
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
