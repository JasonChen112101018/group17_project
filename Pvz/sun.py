import pygame

class Sun(object):
    def __init__(self, screen, image, x, y, goal):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.goal = goal
        self.x = x
        self.y = y
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]

        self.index = 0 #太陽位置
        self.score = 25 #分數
        self.disappearTime = 0 #消失時間



    def blitme(self):
        self.screen.blit(self.image, (self.x, self.y))


    def step(self):
        self.y += 0.5
        self.index += 0.5
