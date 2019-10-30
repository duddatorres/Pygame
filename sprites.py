import pygame as py
import settings

class Player(py.sprite.Sprite):
    #PLAYER ÁGUA
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        
    def move(self,dx=0, dy=0):
        if not self.collide_with_walls(dx,dy):
            self.x += dx
            self.y += dy
            
    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
        
    def update(self):
        self.rect.x = self.x * settings.TILESIZE
        self.rect.y = self.y * settings.TILESIZE
        

class Player2(py.sprite.Sprite):
    #PLAYER FOGO
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        
    def move(self,dx=0, dy=0):
        if not self.collide_with_walls(dx,dy):
            self.x += dx
            self.y += dy
        
    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
        
    def update(self):
        self.rect.x = self.x * settings.TILESIZE
        self.rect.y = self.y * settings.TILESIZE
        
        
class Wall(py.sprite.Sprite):
    def __init__(self, game, x ,y):
        self.groups = game.all_sprites, game.walls
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.TILESIZE
        self.rect.y = y * settings.TILESIZE
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
