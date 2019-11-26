import pygame as py

#-----------------------------------------------------------------------------#

# - CORES:
RED = (255,0,0)            #player 1 / amarelo / fogo
BLUE = (0,255,255)              #player 2 / azul / água

GREEN = (0,255,0)               #parede
ORANGE = (255,102,0)            #portal 1 / laranja
PURPLE = (126,58,153)           #portal 2 / roxo

BLACK = (0,0,0)
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
PLAYER_SPEED = 1200             #velocidade do player
PLAYER_ROT_SPEED = 250

PLAYER_HIT_RECT = py.Rect(0, 0, 35, 35)

PLAYER_IMG = 'PLAYER1.png'
PLAYER2_IMG = 'PLAYER2.png'
MURO_IMG = 'MURO.png'