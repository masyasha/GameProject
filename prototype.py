import pygame as py
import random


class Block:
    def __init__(self, w=100, h=100):
        self.w = w
        self.h = h
        self.x = self.y = 0
    def draw(self):
        self.block_colour = (139,56,20)
        level = ["------  ------------   ------------- -"
                 "---  -------------   -----------------"
                 "--------- ----------------      ------"
                 "--------------   -------------  ------"
                 "------       -------------------  ----"
                 "---  ------   -----------   ----------"]
        for row in level:
            for symbol in row:
                if symbol == '-':
                    self.block = py.Surface((self.w, self.h))
                    self.block.fill(self.block_colour)
                    base.window.blit(self.block, [self.x,self.y])


class Base:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.main()
    def main(self, Play=True):
        py.init()
        self.window = py.display.set_mode((1260, 750))
        py.display.set_caption('Psyho Masya')
        while Play:
            bgColour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            self.window.fill(bgColour)
            b.draw()
            py.display.update()
            for event in py.event.get():
                if event.type == py.QUIT:
                    Play = False


base = Base()
b = Block()
py.quit()