from pygame import *
from Player import *
import pygame as pyg
import random as ran

WIN_W = 960
PLATFORM_W = 32
WIN_H = 640
PLATFORM_H = 32
BG_COLOUR = (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255))
PLATFORM_COLOUR = (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255))
DISPLAY = (WIN_W, WIN_H)


def main():
    play = True
    pyg.init()
    masya = Player()
    left = right = False
    up = False
    level = ["------------------------------",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "------------------------------"]
    screen = pyg.display.set_mode(DISPLAY)
    pyg.display.set_caption('BroFormer')
    clock = pyg.time.Clock()
    bg = Surface((WIN_W,WIN_H))
    while play:
        bg.fill(BG_COLOUR)
        bl_x = bl_y = 0
        for row in level:
            for symbol in row:
                if symbol == '-':
                    platform = Surface((PLATFORM_W,PLATFORM_H))
                    platform.fill(PLATFORM_COLOUR)
                    screen.blit(platform,(bl_x,bl_y))
                bl_x += PLATFORM_W
            bl_y += PLATFORM_H
            bl_x = 0
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                play = False
            if event.type == KEYDOWN:
                if event.key == K_LEFT: left = True
                if event.key == K_RIGHT: right = True
                if event.key == K_UP or event.key == 32: up = True
            if event.type == KEYUP:
                if event.key == K_RIGHT: right = False
                if event.key == K_LEFT: left = False
                if event.key == K_UP: up = False

        masya.update(left, right, up)
        masya.draw(screen)
        pyg.display.update()
        screen.blit(bg, (0,0))
        clock.tick(60)
    pyg.quit()


if __name__ == '__main__':
    main()
