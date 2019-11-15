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
        self.vx, self.vy = 0, 0
        self.x = x * settings.TILESIZE
        self.y = y * settings.TILESIZE
        
    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = py.key.get_pressed()
        if keys[py.K_RIGHT]:
            self.vx = settings.PLAYER_SPEED
        if keys[py.K_UP]:
            self.vy = -settings.PLAYER_SPEED
        if keys[py.K_LEFT]:
            self.vx = -settings.PLAYER_SPEED
        if keys[py.K_DOWN]:
            self.vy = settings.PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
            
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = py.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x= hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x= hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
                
        if dir == 'y':
            hits = py.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y= hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y= hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
        
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

class Player2(py.sprite.Sprite):
    #PLAYER FOGO
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.RED)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * settings.TILESIZE
        self.y = y * settings.TILESIZE
        
    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = py.key.get_pressed()
        if keys[py.K_d]:
            self.vx = settings.PLAYER_SPEED
        if keys[py.K_w]:
            self.vy = -settings.PLAYER_SPEED
        if keys[py.K_a]:
            self.vx = -settings.PLAYER_SPEED
        if keys[py.K_s]:
            self.vy = settings.PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
            
    def collide_with_player(self):
        g = py.sprite.Group()
        g.add(self.game.player_agua)
        hits = py.sprite.spritecollide(self, g, False)
        if hits:
            print("colidiu")

            
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = py.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x= hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x= hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
                
        if dir == 'y':
            hits = py.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y= hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y= hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
                        
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')  
        self.collide_with_player()
        
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
