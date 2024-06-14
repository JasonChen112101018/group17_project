import random, sys, abc, pygame
from zombie.normzombie import Zombie_normal
from zombie.buckzombie import Zombie_bucket
from zombie.head import Zombie_head
from zombie.dead import Zombie_dead
from plant.spikeweed import Spikeweed
from util.bus import Bus
from settings import Setting

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
    if 7000 <= bus.globalTime <= 8000 or 14200 <= bus.globalTime <= 14400:
        bus.zombieRate = 10
    else:
        bus.zombieRate = 1000

    if bus.globalTime == 14300:
        bus.zombies.append(Zombie_bucket(screen, sets.zombie_bucketImages))
        bus.endFlag = 1
    if bus.globalTime < 14400:
        if bus.zombieIndex % bus.zombieRate == 0:
            type = random.randint(0, 20)
            if type < 8:
                bus.zombies.append(Zombie_bucket(screen, sets.zombie_bucketImages))
            else:
                bus.zombies.append(Zombie_normal(screen, sets.zombie_normalImages))

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
            bus.zombies.remove(zombie)
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
                elif zombie.life <= 8:
                    zombie.images = sets.bucketAttackImages
                else:
                    zombie.images = sets.bucketAttackImages
                plant.life -= 0.5
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
        elif isinstance(plant, Spikeweed):
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
                elif zombie.life <= 0:
                    bus.zombies.append(Zombie_dead(screen, sets.zombieDieImages, zombie.x, zombie.y))
                    zombies_killed += 1  # Increment counter when zombie dies

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
                


