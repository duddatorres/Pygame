import pygame as py
import sys
from os import path

import settings
import sprites

#-----------------------------------------------------------------------------#

class Game:#JOGO
    def __init__(self):                           #DEFINIÇÕES INICIAIS
        py.init()
        self.screen = py.display.set_mode((0,0), py.RESIZABLE)
        py.display.set_caption(settings.TITLE)
        self.clock = py.time.Clock()
        py.key.set_repeat(500, 100)
        self.load_data()
        
    def load_data(self):                          #CARREGAMENTO DO MAPA
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        
    def new(self):                                #SPAWN DAS SPRITES
        self.all_sprites = py.sprite.Group()
        self.walls = py.sprite.Group()
        
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':                   #SPAWN DO MURO
                    sprites.Wall(self, col, row)
                    
                if tile == 'L':                   #SPAWN DO PORTAL LARANJA DE CIMA
                    sprites.Portal_L(self, col, row)
                if tile == 'l':                   #SPAWN DO PORTAL LARANJA DE BAIXO
                    sprites.Portal_l(self, col, row)
                    
                if tile == 'R':                   #SPAWN DO PORTAL ROXO DE CIMA
                    sprites.Portal_R(self, col, row)
                if tile == 'r':                   #SPAWN DO PORTAL ROXO DE BAIXO
                    sprites.Portal_r(self, col, row)
                    
                if tile == '!':                   #SPAWN DO PLAYER 1 / AZUL / ÁGUA
                    self.player_agua = sprites.Player(self, col, row)
                    self.players_agua = py.sprite.Group()
                    self.players_agua.add(self.player_agua)
                if tile == '@':                   #SPAWN DO PLAYER 2 / AMARELO / FOGO
                    self.player_fogo = sprites.Player2(self, col, row)
                    self.players_fogo = py.sprite.Group()
                    self.players_fogo.add(self.player_fogo)
        
                if tile == 'i':                   #SPAWN DO INDICADOR DE COM QUEM ESTÁ
                    sprites.Indicador(self, col, row)
                
    def run(self):                                #LOOP PARA RODAR O JOGO
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.events()
            self.update()
            self.draw()
            
    def quit(self):                               #DEFINIÇÃO PAR SAIR DO JOGO
        py.quit()
        sys.exit()
        
    def update(self):                             #ATUALIZAÇÃO DO JOGO CONSTANTEMENTE
        self.all_sprites.update()        
            
    def draw(self):                               #DESENHA O MAPA
        self.screen.fill(settings.BGCOLOR)
        self.all_sprites.draw(self.screen)
        py.display.flip()
        
    def events(self):                             #DEFINIÇÃO DE EVENTOS PARA O JOGO
        for event in py.event.get():
            if event.type == py.QUIT:
                self.quit()

            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

#-----------------------------------------------------------------------------#

g = Game()
g.show_start_screen()
while True:                                       #LOOP PRINCIPAL DO JOGO
    g.new()
    g.run()
    g.show_go_screen()