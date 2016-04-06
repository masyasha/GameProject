from pygame import *
import pygame as py

ENEMY_W = 25
ENEMY_H = 35
ENEMY_COLOUR = (255,0,0)
ENEMY_SPEED = 0.01


class Enemy(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        x, y = 1504, 125
        self.pl_alive = True
        self.image = Surface((ENEMY_W,ENEMY_H))
        self.image.fill(ENEMY_COLOUR)
        self.rect = Rect(x, y, ENEMY_W, ENEMY_H)
    def update(self, pl_x, pl_y, start, alive):
        if start and alive:
            self.rect.x -= ENEMY_SPEED
            self.collision(self.rect.x, self.rect.y, pl_x, pl_y)
    def collision(self, BLOCK_x, BLOCK_y, MARIO_x, MARIO_y):
        check = (((BLOCK_x <= MARIO_x <= BLOCK_x + 25)
                and (BLOCK_x <= MARIO_x + 20 <= BLOCK_x + 25))
                and ((BLOCK_y <= MARIO_y <= BLOCK_y + 35)
                and (BLOCK_y <= MARIO_y + 30 <= BLOCK_y + 35)))

        if check:
            self.pl_alive = False
