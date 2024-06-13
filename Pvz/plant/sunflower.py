import pygame
from conf.settings import Setting #圖片路徑
from plant.Parentplant import Plant #植物父類
from entity.sun import Sun #太陽
from util.bus import Bus #全局狀態

sets = Setting()

class Sunflower(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]

        super(Sunflower, self).__init__(screen, self.x, self.y, self.image)

        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
        self.index = 0
        self.life = 50
        self.sunshine = 50
        self.attack = 0
        # 產生陽光的間隔
        self.interval = 50
        # 種植間隔
        self.cd = 5

    # 在右下生成太陽
    def function(self):
        sun = Sun(self.screen, sets.sunImage, self.x + self.width/2, self.y - self.height/2, 0)

        Bus.sunStay.append(sun)

    #實現植物搖晃
    def step(self, bus, screen, sets):
        self.index += 1

        if self.index % 600 == 0:
            self.function()

        ix = self.index / 10 % len(self.images)
        self.image = self.images[int(ix)]

