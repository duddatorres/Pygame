import pygame as py

#CORES:
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,255)
GREEN = (0,255,0)
DARKGREY = (40,40,40)
LIGHTGREY = (100,100,100)



#DEFINIÇÕES:

TITLE = "SharkBoy & LavaGirl"

py.init()
screenInfo = py.display.Info()

WIDTH = screenInfo.current_w
HEIGHT = screenInfo.current_h

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

FPS = 60

BGCOLOR = DARKGREY



#DEFINIÇÕES DO PLAYER:
PLAYER_SPEED= 300





























