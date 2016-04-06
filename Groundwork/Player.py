import pygame as py
from pygame import *
from Enemy import *
import random as ran
import pyganim

MOVE_SPEED = 5
EXTRA_SPEED = 9
PL_W = 20
PL_H = 30
JUMP = 9.5
EXTRA_JUMP = 12.5
GRAVITY = 0.32
PL_COLOUR = (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255))
ANIM_DELAY = 0.1
ANIM_EXTRA_DELAY = 0.07
ANIM_R = ['mario/r1.png', 'mario/r2.png', 'mario/r3.png', 'mario/r4.png', 'mario/r5.png']
ANIM_L = ['mario/l1.png', 'mario/l2.png', 'mario/l3.png', 'mario/l4.png', 'mario/l5.png']
ANIM_JUMP_L = [('mario/jl.png', 0.1)]
ANIM_JUMP_R = [('mario/jr.png', 0.1)]
ANIM_JUMP = [('mario/j.png', 0.1)]
ANIM_STAY = [('mario/0.png', 0.1)]

class Player(sprite.Sprite):
    def __init__(self,x,y,):
        sprite.Sprite.__init__(self)
        self.onYoFeet = True
        self.vel_x = self.vel_y = 0
        self.X_start = x
        self.Y_start = y
        self.image = Surface((PL_W,PL_H))
        self.image.fill(PL_COLOUR)
        self.rect = Rect(x, y, PL_W, PL_H)
        self.image.set_colorkey(PL_COLOUR)
        self.enemy = Enemy()
        """ ANIMATION: RIGHT """
        boltAnim = []
        extra_boltAnim = []
        for picture in ANIM_R:
            boltAnim.append((picture, ANIM_DELAY))
            extra_boltAnim.append((picture, ANIM_EXTRA_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnim_EXTRA_Right = pyganim.PygAnimation(extra_boltAnim)
        self.boltAnimRight.play()
        self.boltAnim_EXTRA_Right.play()
        """ ANIMATION: LEFT """
        boltAnim = []
        extra_boltAnim = []
        for picture in ANIM_L:
            boltAnim.append((picture, ANIM_DELAY))
            extra_boltAnim.append((picture, ANIM_EXTRA_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnim_EXTRA_Left = pyganim.PygAnimation(extra_boltAnim)
        self.boltAnimLeft.play()
        self.boltAnim_EXTRA_Left.play()
        """ ANIMATION: STRAIGHT """
        self.boltAnimStay = pyganim.PygAnimation(ANIM_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))      # 'stay' as a default
        """ ANIMATION: JUMP - LEFT """
        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIM_JUMP_L)
        self.boltAnimJumpLeft.play()
        """ ANIMATION: JUMP - RIGHT """
        self.boltAnimJumpRight = pyganim.PygAnimation(ANIM_JUMP_R)
        self.boltAnimJumpRight.play()
        """ ANIMATION: JUMP """
        self.boltAnimJump = pyganim.PygAnimation(ANIM_JUMP)
        self.boltAnimJump.play()
        """ ANIMATION BLOCK ENDS HERE """
    def update(self, pl_alive, left, right, up, boost, platforms):
        if pl_alive:
            if left:
                self.vel_x = -MOVE_SPEED
                self.image.fill(PL_COLOUR)
                if up: self.boltAnimJumpLeft.blit(self.image, (0,0))
                else: self.boltAnimLeft.blit(self.image, (0,0))
                if boost:
                    self.boltAnim_EXTRA_Left.blit(self.image, (0,0))
                    self.vel_x = -EXTRA_SPEED
            if right:
                self.vel_x = MOVE_SPEED
                self.image.fill(PL_COLOUR)
                if up: self.boltAnimJumpRight.blit(self.image, (0,0))
                else: self.boltAnimRight.blit(self.image, (0,0))
                if boost:
                    self.boltAnim_EXTRA_Right.blit(self.image, (0,0))
                    self.vel_x = EXTRA_SPEED
            if up and self.onYoFeet:
                if boost and (left or right):
                    self.vel_y = -EXTRA_JUMP
                else:
                    self.vel_y = -JUMP
                self.onYoFeet = False
                self.image.fill(PL_COLOUR)
                self.boltAnimJump.blit(self.image, (0,0))
            if not self.onYoFeet:
                self.vel_y += GRAVITY
            if not(left or right or up):
                self.vel_x = 0
                if not up: self.image.fill(PL_COLOUR)
                self.boltAnimStay.blit(self.image, (0,0))
            self.onYoFeet = False
            self.rect.x += self.vel_x
            self.collision(self.vel_x, 0, platforms)
            self.rect.y += self.vel_y
            self.collision(0, self.vel_y, platforms)
        else:
            self.rect.x = self.X_start
            self.rect.y = self.Y_start
    def collision(self, vel_x, vel_y, platforms):
        for platform in platforms:
            if sprite.collide_rect(self, platform):                 # the moment of collision
                if vel_x > 0: self.rect.right = platform.rect.left
                if vel_x < 0: self.rect.left = platform.rect.right
                if vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.onYoFeet = True
                    self.vel_y = 0
                if vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
