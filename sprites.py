import pygame as py
import settings
vec = py.math.Vector2

#-----------------------------------------------------------------------------#

class Player(py.sprite.Sprite):                   #PLAYER AZUL 
    def __init__(self, game, x, y):               #DEFINIÇÕES INICIAIS
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.BLUE)
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * settings.TILESIZE
        
    def get_keys(self):                           #DEFINIÇÃO DO MOVIMENTO PELAS TECLAS
        self.vel = vec(0,0)
        keys = py.key.get_pressed()
        if keys[py.K_d]:
            self.vel.x = settings.PLAYER_SPEED
        if keys[py.K_w]:
            self.vel.y = -settings.PLAYER_SPEED
        if keys[py.K_a]:
            self.vel.x = -settings.PLAYER_SPEED
        if keys[py.K_s]:
            self.vel.y = settings.PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
            
    def collide_with_walls(self, dir):            #DEFINIÇÃO DA COLISÃO DE PAREDE
        if dir == 'x':                            #SENTIDO X
            hits = py.sprite.spritecollide(self, self.game.walls, False)
            if hits:                
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
                
        if dir == 'y':                            #SENTIDO Y
            hits = py.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y
                
    def collide_with_player(self):               #DEFINIÇÃO DA COLISÃO ENTRE PLAYERS
        hits = py.sprite.spritecollide(self, self.game.players_fogo, False)
        agua = 0
        if hits:
            agua+=1
            print(agua)
        
    def update(self):                             #ATUALIZAÇÃO DO JOGO CONSTANTEMENTE
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')

#-----------------------------------------------------------------------------#
        
class Player2(py.sprite.Sprite):                  #PLAYER AMARELO
    def __init__(self, game, x, y):               #DEFINIÇÕES INICIAIS
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.YELLOW)
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * settings.TILESIZE
        
    def get_keys(self):                           #DEFINIÇÃO DO MOVIMENTO PELAS TECLAS
        self.vel = vec(0,0)
        keys = py.key.get_pressed()
        if keys[py.K_RIGHT]:
            self.vel.x = settings.PLAYER_SPEED
        if keys[py.K_UP]:
            self.vel.y = -settings.PLAYER_SPEED
        if keys[py.K_LEFT]:
            self.vel.x = -settings.PLAYER_SPEED
        if keys[py.K_DOWN]:
            self.vel.y = settings.PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
            
    def collide_with_walls(self, dir):            #DEFINIÇÃO DA COLISÃO DE PAREDE
        if dir == 'x':                            #SENTIDO X
            hits = py.sprite.spritecollide(self, self.game.walls, False)
            if hits:                
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
                
        if dir == 'y':                            #SENTIDO Y
            hits = py.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y
                
    def collide_with_player(self):                #DEFINIÇÃO DA COLISÃO ENTRE PLAYERS
        hits = py.sprite.spritecollide(self, self.game.players_agua, False)
        fogo = 0
        if hits:
            fogo+=1
            print(fogo)
                        
    def update(self):                             #ATUALIZAÇÃO DO JOGO CONSTANTEMENTE
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
        self.collide_with_player()
   
#-----------------------------------------------------------------------------#
     
class Wall(py.sprite.Sprite):                     #SPRITE DE PAREDE
    def __init__(self, game, x ,y):               #DEFINIÇÕES INICIAIS
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
        
#-----------------------------------------------------------------------------#

class Indicador(py.sprite.Sprite):                #SPRITE DO 'PLACAR'
    def __init__(self, game, x ,y):               #DEFINIÇÕES INICIAIS
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        
        self.image.fill(settings.WHITE)
#        if :
#            self.image.fill(settings.BLUE)
#        if :
#            self.image.fill(settings.YELLOW)
            
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.TILESIZE
        self.rect.y = y * settings.TILESIZE
        
#    def update(self, colisao):
#        if colisao != 0:
#            self.image.fill(settings.BLUE)

#-----------------------------------------------------------------------------#

class Portal_L(py.sprite.Sprite):                 #PORTAL LARANJA DE CIMA
    def __init__(self, game, x ,y):               #DEFINIÇÕES INICIAIS
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.ORANGE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.TILESIZE
        self.rect.y = y * settings.TILESIZE
        
#-----------------------------------------------------------------------------#        
        
class Portal_l(py.sprite.Sprite):                 #PORTAL LARANJA DE BAIXO
    def __init__(self, game, x ,y):               #DEFINIÇÕES INICIAIS
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.ORANGE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.TILESIZE
        self.rect.y = y * settings.TILESIZE
        
#-----------------------------------------------------------------------------# 
        
class Portal_R(py.sprite.Sprite):                 #PORTAL ROXO DE CIMA
    def __init__(self, game, x ,y):               #DEFINIÇÕES INICIAIS
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.PURPLE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.TILESIZE
        self.rect.y = y * settings.TILESIZE
        
#-----------------------------------------------------------------------------#
        
class Portal_r(py.sprite.Sprite):                 #PORTAL ROXO DE BAIXO
    def __init__(self, game, x ,y):               #DEFINIÇÕES INICIAIS
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = py.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.PURPLE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.TILESIZE
        self.rect.y = y * settings.TILESIZE