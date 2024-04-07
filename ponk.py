from pygame import *
from random import randint 

back = (100, 255, 255)
win_width = 600
win_height = 500
win = display.set_mode((win_width, win_height))
win.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

while True:
    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(FPS)