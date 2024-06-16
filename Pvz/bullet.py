import pygame
import zombie as zombie

class Bullet(object):
    def __init__(self, screen, image, peaX, peaY, type):
        self.screen = screen
        self.image = pygame.image.load(image)
        # x,y
        self.x = peaX
        self.y = peaY
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
        # 子彈種類， 0代表豌豆  1代表冰豌豆（減速）
        self.type = type

    def outOfBounds(self):
        return self.x > 1600

    def step(self):
        self.x += 3

    def blitme(self):
        self.screen.blit(self.image, (self.x, self.y))
