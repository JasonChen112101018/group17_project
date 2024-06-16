import pygame
from zombie.Parentzombie import ParentZombie
import random
from util.bus import Bus 

bus = Bus() 


class Zombie_normal(ParentZombie):
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image = pygame.image.load(images[0])
        self.x = 1150
        self.y = 30 + random.randint(0, 4) * 95
        self.life = 100
        self.damage = 1
        super(Zombie_normal, self).__init__(screen, self.x, self.y, self.image, self.life, self.damage)

        self.index = 0
        self.headFlag = True

    def step(self, sets):
        if self.images == sets.zombie_normalImages or self.images == sets.zombieLostHeadImages:
            self.x -= bus.speed
        self.index += 1
        ix = self.index / (len(self.images)/2) % len(self.images)
        self.image = pygame.image.load(self.images[int(ix)])
