from pygame import *
from Blocks import *
from Player import *
from Enemy import *
import pygame as pyg
import random as ran

WIN_W = 960
WIN_H = 640
BG_COLOUR = (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255))
DISPLAY = (WIN_W, WIN_H)
ENEMY_START_BOX_X = [x for x in range(912, 948)]
ENEMY_START_BOX_Y = [y for y in range(0, 1000)]


class Camera(object):
    def __init__(self, cam_func, w, h):
        self.camera_func = cam_func
        self.state = Rect(0, 0, w, h)
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def cam_cfg(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_W / 2, -t + WIN_H / 2

    l = min(0, l)                           # no far LEFT border
    l = max(-(camera.width - WIN_W), l)     # no far RIGHT border
    t = max(-(camera.height - WIN_H), t)    # no far BOTTOM border
    t = min(0, t)                           # no far TOP border

    return Rect(l, t, w, h)


def main():
    play = True
    pyg.init()
    clock = pyg.time.Clock()
    masya = Player(540, 578)
    meandr = Enemy()
    left = right = up = boost = start = False
    alive = True
    everything = pyg.sprite.Group()
    everything.add(masya, meandr)
    platforms = []
    level = ["------------------------------------------------------------------------------------",
             "-                             ",
             "-                             ",
             "-                             ",
             "-                             ",
             "-                        -----------------------------------------------------------",
             "-      ---                   -",
             "-               -----        -",
             "-                            -",
             "--                           -",
             "-                            -",
             "-                            -",
             "-                            -",
             "-   ----                     -",
             "-                            -",
             "-                            -",
             "-              ---           -",
             "-                            -",
             "-                            -",
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
    total_lvl_w = len(level[0]) * PLATFORM_W    # stage's width
    total_lvl_h = len(level) * PLATFORM_H       # stage's height
    camera = Camera(cam_cfg, total_lvl_w, total_lvl_h)
    while play:
        pyg.display.set_caption('BroFormer: FPS = ' + str(int(clock.get_fps())))
        if masya.rect.x in ENEMY_START_BOX_X:
            if masya.rect.y in ENEMY_START_BOX_Y:
                start = True
        meandr.update(start, screen, alive)
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                play = False
            if event.type == KEYDOWN:
                if event.key == K_LEFT: left = True
                if event.key == K_RIGHT: right = True
                if event.key == K_UP: up = True
                if event.key == 304: boost = True
            if event.type == KEYUP:
                if event.key == K_LEFT: left = False
                if event.key == K_RIGHT: right = False
                if event.key == K_UP: up = False
                if event.key == 304: boost = False
        masya.update(left, right, up, boost, platforms)
        camera.update(masya)
        for something in everything:
            screen.blit(something.image, camera.apply(something))
        pyg.display.update()
        screen.blit(bg, (0,0))
        clock.tick(60)
    pyg.quit()


if __name__ == '__main__':
    main()
