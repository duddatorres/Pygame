import pygame as py

#-----------------------------------------------------------------------------#

# - CORES:
YELLOW = (255,204,0)            #player 1
BLUE = (0,255,255)              #player 2

GREEN = (0,255,0)               #parede
ORANGE = (255,102,0)            #portal 1
PURPLE = (126,58,153)           #portal 2

WHITE = (255,255,255)           #indicador

DARKGREY = (40,40,40)           #cor do fundo

#-----------------------------------------------------------------------------#

# - DEFINIÇÕES:
TITLE = "TAG"                   #título do jogo

py.init()
screenInfo = py.display.Info()  #pega as infos da tela do pc
WIDTH = screenInfo.current_w    #tamanho do comprimento da tela
HEIGHT = screenInfo.current_h   #tamanho da altura da tela

TILESIZE = 32

BGCOLOR = DARKGREY              #cor do fundo

FPS = 1000                      #quantidade de frames per second

#-----------------------------------------------------------------------------#

# - DEFINIÇÕES DO PLAYER:
PLAYER_SPEED = 1000             #velocidade do player