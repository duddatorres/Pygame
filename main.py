import pygame as py
import sys
import settings
import sprites

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((settings.WIDTH, settings.HEIGHT))
        py.display.set_caption(settings.TITLE)
        self.clock = py.time.Clock()
        py.key.set_repeat(500, 100)
        self.load_data()
        
    def load_data(self):
        pass
    
    def new(self):
        self.all_sprites = py.sprite.Group()
        self.walls = py.sprite.Group()
        self.player_agua = sprites.Player(self, 10, 10)
        self.player_fogo = sprites.Player2(self, 5, 10)
        
        for x in range(10, 20):
            sprites.Wall(self, x, 5)
        
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
                    
                #ÁGUA:
                if event.key == py.K_LEFT:
                    self.player_agua.move(dx = -1)
                if event.key == py.K_RIGHT:
                    self.player_agua.move(dx = 1)
                if event.key == py.K_UP:
                    self.player_agua.move(dy = -1)
                if event.key == py.K_DOWN:
                    self.player_agua.move(dy = 1)
                    
                #FOGO:
                if event.key == py.K_a:
                    self.player_fogo.move(dx = -1)
                if event.key == py.K_d:
                    self.player_fogo.move(dx = 1)
                if event.key == py.K_w:
                    self.player_fogo.move(dy = -1)
                if event.key == py.K_s:
                    self.player_fogo.move(dy = 1)
                    
    def show_start_screen(self):
        pass
    
    def show_go_screen(self):
        pass
    
g=Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
