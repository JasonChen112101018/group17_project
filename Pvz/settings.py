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
        # bucket zombie
        self.zombie_bucketImages = [
            "image/zombie_bucket/0.png",
            "image/zombie_bucket/1.png",
            "image/zombie_bucket/2.png",
            "image/zombie_bucket/3.png",
            "image/zombie_bucket/4.png",
            "image/zombie_bucket/5.png",
            "image/zombie_bucket/6.png",
            "image/zombie_bucket/7.png",
            "image/zombie_bucket/8.png",
            "image/zombie_bucket/9.png",
            "image/zombie_bucket/10.png",
            "image/zombie_bucket/11.png",
            "image/zombie_bucket/12.png",
            "image/zombie_bucket/13.png",
            "image/zombie_bucket/14.png"
        ]
	# lost head zombie
        self.zombieLostHeadImages = [
            "image/zombieLostHead/0.png",
            "image/zombieLostHead/1.png",
            "image/zombieLostHead/2.png",
            "image/zombieLostHead/3.png",
            "image/zombieLostHead/4.png",
            "image/zombieLostHead/5.png",
            "image/zombieLostHead/6.png",
            "image/zombieLostHead/7.png",
            "image/zombieLostHead/8.png",
            "image/zombieLostHead/9.png",
            "image/zombieLostHead/10.png",
            "image/zombieLostHead/11.png",
            "image/zombieLostHead/12.png",
            "image/zombieLostHead/13.png",
            "image/zombieLostHead/14.png",
            "image/zombieLostHead/15.png",
            "image/zombieLostHead/16.png",
            "image/zombieLostHead/17.png"
        ]
        # head
        self.zombieHeadImages = [
            "image/zombieHead/0.png",
            "image/zombieHead/1.png",
            "image/zombieHead/2.png",
            "image/zombieHead/3.png",
            "image/zombieHead/4.png",
            "image/zombieHead/5.png",
            "image/zombieHead/6.png",
            "image/zombieHead/7.png",
            "image/zombieHead/8.png",
            "image/zombieHead/9.png",
            "image/zombieHead/10.png",
            "image/zombieHead/11.png"
        ]
        # normal zombie attack
        self.normalAttackImages = [
            "image/zombie_normalAttack/0.png",
            "image/zombie_normalAttack/1.png",
            "image/zombie_normalAttack/2.png",
            "image/zombie_normalAttack/3.png",
            "image/zombie_normalAttack/4.png",
            "image/zombie_normalAttack/5.png",
            "image/zombie_normalAttack/6.png",
            "image/zombie_normalAttack/7.png",
            "image/zombie_normalAttack/8.png",
            "image/zombie_normalAttack/9.png",
            "image/zombie_normalAttack/10.png",
            "image/zombie_normalAttack/11.png",
            "image/zombie_normalAttack/12.png",
            "image/zombie_normalAttack/13.png",
            "image/zombie_normalAttack/14.png",
            "image/zombie_normalAttack/15.png",
            "image/zombie_normalAttack/16.png",
            "image/zombie_normalAttack/17.png",
            "image/zombie_normalAttack/18.png",
            "image/zombie_normalAttack/19.png",
            "image/zombie_normalAttack/20.png"

        ]
        # bucket zombie attack
        self.bucketAttackImages = [
            "image/zombie_bucketAttack/0.png",
            "image/zombie_bucketAttack/1.png",
            "image/zombie_bucketAttack/2.png",
            "image/zombie_bucketAttack/3.png",
            "image/zombie_bucketAttack/4.png",
            "image/zombie_bucketAttack/5.png",
            "image/zombie_bucketAttack/6.png",
            "image/zombie_bucketAttack/7.png",
            "image/zombie_bucketAttack/8.png",
            "image/zombie_bucketAttack/9.png",
            "image/zombie_bucketAttack/10.png"
        ]

        # zombie die
        self.zombieDieImages = [
            "image/zombieDie/0.png",
            "image/zombieDie/1.png",
            "image/zombieDie/2.png",
            "image/zombieDie/3.png",
            "image/zombieDie/4.png",
            "image/zombieDie/5.png",
            "image/zombieDie/6.png",
            "image/zombieDie/7.png",
            "image/zombieDie/8.png",
            "image/zombieDie/9.png"
        ]
        # lost head zombie attack
        self.zombieLostHeadAttackImages = [
            "image/zombieLostHeadAttack/0.png",
            "image/zombieLostHeadAttack/1.png",
            "image/zombieLostHeadAttack/2.png",
            "image/zombieLostHeadAttack/3.png",
            "image/zombieLostHeadAttack/4.png",
            "image/zombieLostHeadAttack/5.png",
            "image/zombieLostHeadAttack/6.png",
            "image/zombieLostHeadAttack/7.png",
            "image/zombieLostHeadAttack/8.png",
            "image/zombieLostHeadAttack/9.png",
            "image/zombieLostHeadAttack/10.png"
        ]
        # plant 
        self.plantsInitImages = [
            plantsImgDir + 'WallNut/',
            plantsImgDir + 'SunFlower/',
            plantsImgDir + 'Peashooter/',
            plantsImgDir + 'Spikeweed/',
            plantsImgDir + 'SnowPea/',
        ]
        self.peashooterImg = plantsImgDir + 'Peashooter/'
        self.sunFlowerImg = plantsImgDir + 'SunFlower/'
        self.wallNutImg = plantsImgDir + 'WallNut/'
        self.wallNutCrackedImg = plantsImgDir + 'WallNutCracked/'
        self.wallNutBadlyCrackedImg = plantsImgDir + 'WallNutBadlyCracked/'
        self.snowPeaImg = plantsImgDir + 'SnowPea/'
        self.spikeWeedImg = plantsImgDir + 'Spikeweed/'
