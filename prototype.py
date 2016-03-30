import pygame as py
import random


class Block:
    def __init__(self, w=15, h=15):
        self.w = w
        self.h = h
        self.x = self.y = 0
        self.block_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.level = ["--------------------------            ----------------",
                      "                                                      ",
                      "                                                      ",
                      "                             ---                      ",
                      "                                                      ",
                      "                                                      ",
                      "             --                                       ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                 ------------         ",
                      "                                                      ",
                      "    -----                                             ",
                      "                                                      ",
                      "                                                      ",
                      "              ------                                  ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                     ------           ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                         ------                       ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "    -------                                           ",
                      "                                                   -- ",
                      "                                                      ",
                      "                                                      ",
                      "                     -----                            ",
                      "                                                      ",
                      "                                         -----        ",
                      "                                                      ",
                      "                                                      ",
                      "                                                      ",
                      "------------------------------------------------------"]


class Base:
    def __init__(self):
        self.moveX = {97 and 276: -p.move_speed, 100 and 275: p.move_speed}
        self.moveY = {32: p.move_speed}
        self.main()
    def main(self, Play=True):
        py.init()
        self.window = py.display.set_mode((800, 630))
        py.display.set_caption('Psyho Masya')
        while Play:
            bgColour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            self.window.fill(bgColour)
            self.draw()
            self.window.blit(p.player, (p.pl_x,p.pl_y))
            for event in py.event.get():
                if event.type == py.QUIT:
                    Play = False
                if event.type == py.KEYDOWN:
                    p.vel = self.moveX[event.key]
                    p.pl_x += p.vel
                    self.window.fill(bgColour)
                    self.window.blit(p.player, (p.pl_x,p.pl_y))
                    self.draw()

            py.display.update()

    """ FUNCTIONS """
    def draw(self):
        b.x = b.y = 0
        for row in b.level:
            for symbol in row:
                if symbol == '-':
                    self.block = py.Surface((b.w, b.h))
                    self.block.fill(b.block_colour)
                    self.window.blit(self.block, (b.x,b.y))
                b.x += b.w
            b.y += b.h
            b.x = 0


class Player:
    def __init__(self,pl_w=20,pl_h=22):
        self.pl_w = pl_w
        self.pl_h = pl_h
        self.pl_x = 535
        self.pl_y = 593
        self.st_X = self.pl_x
        self.st_Y = self.pl_y
        self.player_view()
        self.move_speed = 7
        self.vel = 0
    def player_view(self):
        self.player = py.Surface((self.pl_w, self.pl_h))
        self.player.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))


b = Block()
p = Player()
base = Base()
py.quit()
