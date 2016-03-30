import pygame as py
import random


class Block:
    def __init__(self, w=15, h=15):
        self.w = w
        self.h = h
        self.x = self.y = 0
        self.block_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.level = ["------------------------------------------------------",
                      "---                            -           -          ",
                      "            -----              -           -          ",
                      "-   --             -                                  ",
                      "      --       ---                                    ",
                      "           ----                                       ",
                      "    --            -                                   ",
                      " --      -    -                                       ",
                      " --      -    -                                       ",
                      " --      -    -                                       ",
                      " --      -    -                                       ",
                      "           --                                         ",
                      " ---             -                                    ",
                      "                                                      ",
                      "    -----           --                                ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "------------------------------------------------------"]


class Base:
    def __init__(self):
        self.main()
    def main(self, Play=True):
        py.init()
        self.window = py.display.set_mode((800, 630))
        py.display.set_caption('Psyho Masya')
        bgColour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.window.fill(bgColour)
        self.draw()
        while Play:
            for event in py.event.get():
                if event.type == py.QUIT:
                    Play = False
            py.display.update()
    """ FUNCTIONS """
    def draw(self):
        for row in b.level:
            for symbol in row:
                if symbol == '-':
                    self.block = py.Surface((b.w, b.h))
                    self.block.fill(b.block_colour)
                    self.window.blit(self.block, (b.x,b.y))
                b.x += b.w
            b.y += b.h
            b.x = 0


b = Block()
base = Base()
py.quit()
