import pygame as py
from pygame import *
import random as ran

MOVE_SPEED = 7
PL_W = 20
PL_H = 30
JUMP = 10
GRAVITY = 0.5
PL_COLOUR = (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255))

class Player(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.onYoFeet = True
        self.vel_x = self.vel_y = 0
        self.X_start = x
        self.Y_start = y
        self.image = Surface((PL_W,PL_H))
        self.image.fill(PL_COLOUR)
        self.rect = Rect(x, y, PL_W, PL_H)
    def update(self, left, right, up, platforms):
        if left: self.vel_x = -MOVE_SPEED
        if right: self.vel_x = MOVE_SPEED
        if up and self.onYoFeet:
            self.vel_y = -JUMP
            self.onYoFeet = False
        if not self.onYoFeet:
            self.vel_y += GRAVITY
        if not(left or right or up): self.vel_x = 0
        self.rect.x += self.vel_x
        self.collision(self.vel_x, 0, platforms)
        self.rect.y += self.vel_y
        self.collision(0, self.vel_y, platforms)
    def collision(self, vel_x, vel_y, platforms):
        for platform in platforms:
            if sprite.collide_rect(self, platform):            # checking the collision between 2 objects
                if vel_x > 0: self.rect.right = platform.rect.left      # I really fkin' dont understand this
                if vel_x < 0: self.rect.left = platform.rect.right      # piece of damny code
                if vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.onYoFeet = True
                    self.vel_y = 0
                if vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
