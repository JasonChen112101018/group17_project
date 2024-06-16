import pygame
import random
from zombie.Parentzombie import ParentZombie
from util.bus import Bus
bus = Bus()


class Zombie_bucket(ParentZombie):
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image = pygame.image.load(self.images[0])
        self.x = 1150
        self.y = 30 + random.randint(0, 4)*95
        self.life = 500
        self.damage = 1
        super(Zombie_bucket, self).__init__(screen, self.x, self.y, self.image, self.life, self.damage)
        self.index = 0

    def step(self, sets):
        # 1.移動
        if self.images == sets.zombie_bucketImages or self.images == sets.zombieLostHeadImages or self.images == sets.zombie_normalImages:
            self.x -= bus.speed
        # 2.走路動畫
        self.index += 1
        ix = self.index / (len(self.images)/2) % len(self.images)
        self.image = pygame.image.load(self.images[int(ix)])
