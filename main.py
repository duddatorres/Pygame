import pygame as py
import sys
import settings
import sprites
from os import path

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((0,0), py.RESIZABLE)
        py.display.set_caption(settings.TITLE)
        self.clock = py.time.Clock()
        py.key.set_repeat(500, 100)
        self.load_data()
        
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        
    def new(self):
        self.all_sprites = py.sprite.Group()
        self.walls = py.sprite.Group()
        
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    sprites.Wall(self, col, row)
                    
                if tile == 'L':
                    sprites.Portal_L(self, col, row)
                if tile == 'l':
                    sprites.Portal_l(self, col, row)
                    
                if tile == 'R':
                    sprites.Portal_R(self, col, row)
                if tile == 'r':
                    sprites.Portal_r(self, col, row)
                    
                if tile == '!':
                    self.player_agua = sprites.Player(self, col, row)
                    self.players_agua = py.sprite.Group()
                    self.players_agua.add(self.player_agua)
                if tile == '@':
                    self.player_fogo = sprites.Player2(self, col, row)
                    self.players_fogo = py.sprite.Group()
                    self.players_fogo.add(self.player_fogo)
        
                if tile == 'i':
                    sprites.Indicador(self, col, row)
                
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.events()
            self.update()
            self.draw()
            
    def quit(self):
        py.quit()
        sys.exit()
        
    def update(self):
        self.all_sprites.update()        
            
    def draw(self):
        self.screen.fill(settings.BGCOLOR)
        self.all_sprites.draw(self.screen)
        py.display.flip()
        
    def events(self):
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



g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
