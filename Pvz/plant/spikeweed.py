from plant.Parentplant import Plant
from settings import Setting
from util.loadimages import getImages

class Spikeweed(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]
        self.width = 0
        self.height = 0
        super(Spikeweed, self).__init__(screen, self.x, self.y, self.image)

        self.index = 0
        self.life = 100
        self.sunshine = 100
        self.attack = 20
        self.interval = 50
        self.cd = 10

    def function(self):
        pass

    def step(self, bus, screen, sets):
        self.index += 1

        if self.index % 600 == 0:
            self.function()

        ix = self.index / 10 % len(self.images)
        self.image = self.images[int(ix)]
        
