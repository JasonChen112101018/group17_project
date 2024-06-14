import pygame
from zombie.Parentzombie import ParentZombie
import random


class Zombie_normal(ParentZombie):
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image = pygame.image.load(images[0])
        self.x = 1000
        self.y = 15 + random.randint(0, 4) * 100
        self.life = 5
        self.damage = 1
        super(Zombie_normal, self).__init__(screen, self.x, self.y, self.image, self.life, self.damage)

        self.index = 0
        self.headFlag = True

    def step(self, sets):
        if self.images == sets.zombie_normalImages or self.images == sets.zombieLostHeadImages:
            self.x -= 0.1
        self.index += 1
        ix = self.index / (len(self.images)/2) % len(self.images)
        self.image = pygame.image.load(self.images[int(ix)])
