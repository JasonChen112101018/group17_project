import pygame
from plant.Parentplant import Plant # 植物父類
from settings import Setting #圖片路徑
from bullet import Bullet #子彈定義
from util.bus import Bus

bus = Bus()

class Peashooter(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]

        super(Peashooter, self).__init__(screen, self.x, self.y, self.image)
        self.width = 0
        self.height = 0
        self.index = 0
        self.life = 100
        self.sunshine = 100
        self.attack = 50
        self.interval = 150
        self.cd = 10

    # 植物晃動
    def step(self, bus, screen, sets):
        self.index += 1
        if self.index == self.interval:
            self.index = 0
            if self.zombieflag():
                bus.bullets.append(self.shootBy(screen, sets.peaBulletImg))
        ix = self.index / 7 % len(self.images)
        self.image = self.images[int(ix)]

    # 子彈生成
    def shootBy(self, screen, image):
        bs = Bullet(screen, image, self.x + 55, self.y, 0)
        return bs
