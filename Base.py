from pygame import *
import pygame as pyg
import random as ran

WIN_W = 1388
PLATFORM_W = 32
WIN_H = 1266
PLATFORM_H = 32
BG_COLOUR = (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255))
PLATFORM_COLOUR = (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255))
DISPLAY = (WIN_W, WIN_H)
level = ["---------------------------------------------------------------------------------------------------",
         "",
         "",
         "",
         "",
         "",
         "",
         "--------------------------------------------------------------------------------------------------",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "---------------------------------------------------------------------------------------------------"]

def main():
    play = True
    pyg.init()
    screen = pyg.display.set_mode(DISPLAY)
    pyg.display.set_caption('BroFormer')
    clock = pyg.time.Clock()
    while play:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                play = False
        bg = Surface((WIN_W,WIN_H))
        bg.fill(BG_COLOUR)
        pl_x = pl_y = 0
        for row in level:
            for symbol in row:
                if symbol == '-':
                    print 'yeap'
                    platform = Surface((PLATFORM_W,PLATFORM_H))
                    platform.fill(PLATFORM_COLOUR)
                    screen.blit(platform,(pl_x,pl_y))
                    pl_x += PLATFORM_W
                pl_y += PLATFORM_H
                pl_x = 0

        screen.blit(bg, (0,0))
        pyg.display.update()
        clock.tick(60)
    pyg.quit()


if __name__ == '__main__':
    main()
