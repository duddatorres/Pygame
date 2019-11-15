# Pygameimport pygame as py
import settings

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)
        
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data[0])
        self.width = self.tilewidth * settings.TILESIZE
        self.height = self.tileheight * settings.TILESIZE
                
class Camera:
    def __init__(self, width, height):
        self.camera = py.Rect(0,0,width,height)
        self.width = width
        self.height = height
        
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self, target):
        x = -target.rect.x + int(settings.WIDTH / 2)
        y = -target.rect.y + int(settings.HEIGHT / 2)
        self.camera = py.Rect(x,y,self.width,self.height)
