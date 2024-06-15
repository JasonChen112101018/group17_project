import random, sys, abc, pygame
from zombie.normzombie import Zombie_normal
from zombie.buckzombie import Zombie_bucket
from zombie.head import Zombie_head
from zombie.dead import Zombie_dead
import pygame, sys, random
import painter as painter
import actioner as actioner
import mouseListener as mouseListener
from settings import Setting
from util.bus import Bus
from sun import Sun
import zombie 
#import zombie_actioner as z_actioner
import zombie.zombie_painter as z_painter
import plant.Plantpainter as plantpainter
from plant.spikeweed import Spikeweed
#import background 

bus = Bus()
sets = Setting()
screen = pygame.display.set_mode((1600, 900), 0, 0)
zombies_killed = 0  # Counter for killed zombies

# 走一步
def stepAction():
    # 殭屍走一步
    for zombie in bus.zombies:
        zombie.step(sets)
    for bullet in bus.bullets:
        bullet.step()

# 生成殭屍
def zombiesAction():
    bus.zombieIndex += 1
    bus.globalTime += 1
    #print("time : %d"%bus.globalTime)
    if 7000 <= bus.globalTime <= 8000 or 14200 <= bus.globalTime <= 14400:
        bus.zombieRate = 100
    else:
        bus.zombieRate = 1000

    if bus.globalTime >= 14300:
        bus.endFlag = 1
        print("endFlag : %d"%bus.endFlag)
        
    if bus.globalTime < 14400:
        if bus.zombieIndex % bus.zombieRate == 0:
            type = random.randint(0, 20)
            if type < 8:
                bus.zombies.append(Zombie_bucket(screen, sets.zombie_bucketImages))
            else:
                bus.zombies.append(Zombie_normal(screen, sets.zombie_normalImages))
    #else:
     #   if len(bus.zombies) == 0:
      #      bus.endFlag = 1

# 殭屍被攻擊
def hitAction():
    global zombies_killed
    for zombie in bus.zombies:
        eat(zombie)
        hit(zombie)
        if zombie.life == 5:
            if not isinstance(zombie, Zombie_normal):
                zombie.images = sets.zombie_normalImages
        elif zombie.life == 3:
            if zombie.headFlag is True:
                zombie.images = sets.zombieLostHeadImages
                zombie.headFlag = False
        elif zombie.life == 0:
            print("before remove : %d"%len(bus.zombies))
            bus.zombies.remove(zombie)
            print("after remove : %d"%len(bus.zombies))
            zombies_killed += 1  # Increment counter when zombie dies

# 殭屍吃植物
def eat(zombie):
    global zombies_killed
    for plant in bus.paintPlants:
        if not isinstance(plant, Spikeweed) and not isinstance(zombie, Zombie_head) and not isinstance(zombie, Zombie_dead):
            if abs((plant.x + plant.width / 2) - (zombie.x + 20)) < 10 and zombie.y < plant.y and zombie.y + 100 > plant.y:
                if zombie.life <= 3:
                    zombie.images = sets.zombieLostHeadAttackImages
                elif zombie.life <= 5:
                    zombie.images = sets.normalAttackImages
                else:
                    zombie.images = sets.bucketAttackImages
                plant.life -= 1
                if plant.life <= 0:
                    bus.gridList[plant.gridX][plant.gridY] = -1
                    bus.paintPlants.remove(plant)
                    if zombie.images == sets.zombieLostHeadAttackImages:
                        zombie.images = sets.zombieLostHeadImages
                    else:
                        if zombie.images == sets.normalAttackImages:
                            zombie.images = sets.zombie_normalImages
                        else:
                            zombie.images = sets.zombie_bucketImages
        if isinstance(plant, Spikeweed):
            if abs((plant.x + plant.width / 2) - (zombie.x + 20)) < 10 and zombie.y < plant.y - 40 and zombie.y + 140 > plant.y:
                zombie.life -= 1
                zombie.x += 0.05
                if zombie.life > 3:
                    if not isinstance(zombie, Zombie_normal):
                        zombie.images = sets.zombie_normalImages
                elif zombie.life <= 3 and zombie.life > 0:
                    if zombie.headFlag is True:
                        zombie.images = sets.zombieLostHeadImages
                        bus.zombies.append(Zombie_head(screen, sets.zombieHeadImages, zombie.x, zombie.y))
                elif zombie.life == 0:
                    bus.zombies.append(Zombie_dead(screen, sets.zombieDieImages, zombie.x, zombie.y))
                    #zombies_killed += 1  # Increment counter when zombie dies

# 殭屍被攻擊
def hit(zombie):
    global zombies_killed
    for bullet in bus.bullets:
        if zombie.hitBy(bullet) and not isinstance(zombie, Zombie_head) and not isinstance(zombie, Zombie_dead):
            zombie.life -= 1
            if bullet.type == 0:
                bus.bullets.remove(bullet)
            elif bullet.type == 1:
                zombie.life -= 1
                zombie.x += 0.2
                bus.bullets.remove(bullet)
            if zombie.life <= 5 and zombie.life > 3:
                if not isinstance(zombie, Zombie_normal):
                    zombie.images = sets.zombie_normalImages
            elif zombie.life <= 3 and zombie.life > 0:
                if zombie.headFlag is True:
                    zombie.images = sets.zombieLostHeadImages
                    bus.zombies.append(Zombie_head(screen, sets.zombieHeadImages, zombie.x, zombie.y))
            elif zombie.life <= 0:
                bus.zombies.append(Zombie_dead(screen, sets.zombieDieImages, zombie.x, zombie.y))
        
                


