import pygame
from  pygame.locals import *


plantsImgDir = 'image/plants/'

class Setting(object):
    def __init__(self):
        pygame.display.init()
        self.background = pygame.image.load('image/background1.jpg')
        self.seedBank = pygame.image.load('image/SeedBank.png')
        self.sunImage = 'image/sun.png'
        
        self.flagMeterEmpty = pygame.image.load('image/progress_bar/FlagMeterEmpty.png')
        self.flagMeterFull = pygame.image.load('image/progress_bar/FlagMeterFull.png')
        self.flagMeterParts1 = pygame.image.load('image/progress_bar/FlagMeterParts1.png')
        self.flagMeterParts2 = pygame.image.load('image/progress_bar/FlagMeterParts2.png')
        
        self.prepareGrowPlants = pygame.image.load('image/prompt_words/PrepareGrowPlants.png')
        self.largeWave = pygame.image.load('image/prompt_words/LargeWave.png')
        self.finalWave = pygame.image.load('image/prompt_words/FinalWave.png')
        
        self.Button = pygame.image.load('image/game_state/Button.png')
        self.Pause = pygame.image.load('image/game_state/Pause.png')

        # normal zombie
        self.zombie_normalImages = [
            "image/zombie_normal/0.png",
            "image/zombie_normal/1.png",
            "image/zombie_normal/2.png",
            "image/zombie_normal/3.png",
            "image/zombie_normal/4.png",
            "image/zombie_normal/5.png",
            "image/zombie_normal/6.png",
            "image/zombie_normal/7.png",
            "image/zombie_normal/8.png",
            "image/zombie_normal/9.png",
            "image/zombie_normal/10.png",
            "image/zombie_normal/11.png",
            "image/zombie_normal/12.png",
            "image/zombie_normal/13.png",
            "image/zombie_normal/14.png",
            "image/zombie_normal/15.png",
            "image/zombie_normal/16.png",
            "image/zombie_normal/17.png",
            "image/zombie_normal/18.png",
            "image/zombie_normal/19.png",
            "image/zombie_normal/20.png",
            "image/zombie_normal/21.png"
        ]
        
