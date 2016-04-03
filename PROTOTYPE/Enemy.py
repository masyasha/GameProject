from pygame import *
import pygame as py

ENEMY_W = 25
ENEMY_H = 35
ENEMY_COLOUR = (255,0,0)
ENEMY_SPEED = 1


class Enemy(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        x, y = 1504, 125
        self.image = Surface((ENEMY_W,ENEMY_H))
        self.image.fill(ENEMY_COLOUR)
        self.rect = Rect(x, y, ENEMY_W, ENEMY_H)
    def update(self, start, screen, alive):
        if start and alive:
            self.image.fill(ENEMY_COLOUR)
            print self.rect.x
            while self.rect.x != 950:
                self.rect.x -= ENEMY_SPEED
            screen.blit(self.image, (self.rect.x, self.rect.y))
