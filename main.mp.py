# Pygameimport pygame as py
import sys
import settings
import sprites
import os
from os import path

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((settings.WIDTH, settings.HEIGHT)) #escolhendo largura e altura da malha quadriculada
#        os.environ['SDL_VIDEO_CENTERED'] = '1'
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
                if tile == 'S':
                    self.player_agua = sprites.Player(self, col, row)
                if tile == 'L':
                    self.player_fogo = sprites.Player2(self, col, row)
                    
        
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
        
    def draw_grid(self):
        for x in range(0, settings.WIDTH, settings.TILESIZE):
            py.draw.line(self.screen, settings.LIGHTGREY, (x,0), (x,settings.HEIGHT))
            
        for y in range(0, settings.HEIGHT, settings.TILESIZE):
            py.draw.line(self.screen, settings.LIGHTGREY, (0,y), (settings.WIDTH,y))
            
    def draw(self):
        self.screen.fill(settings.BGCOLOR)
        self.draw_grid()
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
