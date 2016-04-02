from pygame import *
from Blocks import *
from Player import *
import pygame as pyg
import random as ran

WIN_W = 960
WIN_H = 640
BG_COLOUR = (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255))
DISPLAY = (WIN_W, WIN_H)


def main():
    play = True
    pyg.init()
    clock = pyg.time.Clock()
    masya = Player(540, 578)
    left = right = False
    up = False
    everything = pyg.sprite.Group()
    everything.add(masya)
    platforms = []
    level = ["------------------------------",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "                              ",
             "-                             ",
             "                              ",
             "                              ",
             "                              ",
             "    ----                      ",
             "                              ",
             "                              ",
             "               ---            ",
             "                              ",
             "                              ",
             "------------------------------"]
    screen = pyg.display.set_mode(DISPLAY)
    bg = Surface((WIN_W,WIN_H))
    bg.fill(BG_COLOUR)
    bl_x = bl_y = 0
    for row in level:
        for symbol in row:
            if symbol == '-':
                block = Blocks(bl_x,bl_y)
                everything.add(block)
                platforms.append(block)
            bl_x += PLATFORM_W
        bl_y += PLATFORM_H
        bl_x = 0
    while play:
        pyg.display.set_caption('BroFormer: FPS = ' + str(int(clock.get_fps())))
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

        masya.update(left, right, up, platforms)
        everything.draw(screen)
        pyg.display.update()
        screen.blit(bg, (0,0))
        clock.tick(60)
    pyg.quit()


if __name__ == '__main__':
    main()
