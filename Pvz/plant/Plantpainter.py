import pygame
from ..util import bus


    # 繪製植物
    def paintPlants():
        for plant in bus.paintPlants:
            plant.blitme()
    # 繪製子彈
    def paintBullets():
        for bullet in bus.bullets:
            bullet.blitme()
