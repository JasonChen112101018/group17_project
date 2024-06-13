import pygame
import abc

class Plant(object):
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.width = 0
        self.height = 0
        # 植物選中判定
        self.gridX = -1
        self.gridY = -1

        # 生命植，消耗陽光, 攻擊力，攻擊間隔，冷卻時間
        self.life = 0
        self.sunshine = 0
        self.attack = 0
        self.interval = 0
        self.cd = 0

    # 植物功能
    @abc.abstractmethod
    def function(self):
        pass

    # 植物圖案
    def blitme(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 植物晃動
    @abc.abstractmethod
    def step(self, bus, screen, sets):
        pass
