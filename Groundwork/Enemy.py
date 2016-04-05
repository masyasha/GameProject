from pygame import *
import pygame as py

ENEMY_W = 25
ENEMY_H = 35
ENEMY_COLOUR = (255,0,0)
ENEMY_SPEED = 0.1


class Enemy(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        x, y = 1504, 125
        self.image = Surface((ENEMY_W,ENEMY_H))
        self.image.fill(ENEMY_COLOUR)
        self.rect = Rect(x, y, ENEMY_W, ENEMY_H)
    def update(self, pl_x, pl_y, start, alive):
        if start and alive:
            self.rect.x -= ENEMY_SPEED
            self.collision(self.rect.x, self.rect.y, pl_x, pl_y)
    def collision(self, BLOCK_x, BLOCK_y, MARIO_x, MARIO_y):
        check = (((MARIO_x == BLOCK_x) and (MARIO_y == BLOCK_y + 5)) or
                 ((MARIO_x + 20 == BLOCK_x) and (MARIO_y == BLOCK_y + 5)))
        print BLOCK_x, BLOCK_y, MARIO_x, MARIO_y
        if check:
            print "WORKED!!!"
