import pygame, sys, random
from settings import Setting
from zombie.buckzombie import Zombie_bucket
from zombie.normzombie import Zombie_normal
from util.constant import Constant
from sun import Sun
from util.bus import Bus
import mouseListener
import painter
import actioner
from zombie.head import Zombie_head
from zombie.dead import Zombie_dead
from plant.spikeweed import Spikeweed
import threading
import time

bus = Bus()
sets = Setting()

screen = pygame.display.set_mode((1050, 600), 0, 0)

def initSun():
    for i in range(1):
        xx = random.randint(260, 880)
        yy = -random.randint(100, 300)
        goal = random.randint(300, 600)
        sun = Sun(screen, sets.sunImage, xx, yy,goal)
        bus.sunFall.append(sun)

'''
paint part
'''

# 場景繪製
def paint():
    if bus.state == bus.START:
        painter.initStartSurface(bus, screen, sets)
        return

    # 繪製背景
    painter.initScenario(bus, screen, sets)
    #paintZombies()
    painter.cardMovePaint(bus, screen, sets)
    paintPlants()
    paintBullets()
    paintZombies()
    painter.cardMovePaint(bus, screen, sets)
    # 繪製太陽
    painter.paintSun(bus, screen, sets)
    # 繪製太陽數量
    painter.paintSunScore(bus, screen, sets)
    # 繪製進度條
    painter.painProgressBar(bus, screen, sets)
    if bus.state == bus.PAUSE:
        painter.paintPause(bus, screen, sets)
    elif bus.state == bus.DEAD:
        painter.deadPaint(bus, screen, sets)
    elif bus.state == bus.END:
        painter.wonPaint(bus, screen, sets)
        

# 繪製殭屍
def paintZombies():
    for zombie in bus.zombies:
        zombie.blitme()
        if isinstance(zombie, Zombie_head) or isinstance(zombie, Zombie_dead):
            if zombie.reloadFlag == 1:
                bus.zombies.remove(zombie)
# 繪製植物
def paintPlants():
    for plant in bus.paintPlants:
        plant.blitme()
# 繪製子彈
def paintBullets():
    for bullet in bus.bullets:
        bullet.blitme()

'''
action部分
'''


# 事件函數
def action():

    # 滑鼠事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseListener.initPlantsMouseClickListener(bus, screen)
            mouseListener.cardMouseClickListener(bus)
            mouseListener.sunMouseClickListener(bus, screen, sets)
            mouseListener.runOrPause(bus, screen, sets)
    if bus.state == bus.RUNNING:
        stepAction()
        zombiesAction()
        #  陽光動作
        actioner.sunAction(bus, screen, sets)
        # 全局時間增加
        bus.globalTime += 1
        for plant in bus.paintPlants:
            plant.step(bus, screen, sets)
        hitAction()
        actioner.endAction(bus, screen, sets)

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
    if 7000 <= bus.globalTime <= 8000:
        bus.zombieRate = 100
    elif 13500 <= bus.globalTime <= 14400:
        bus.zombieRate = 50
    else:
        bus.zombieRate = 1000

    if bus.globalTime == 14300:
        bus.endFlag = 1

    if bus.globalTime < 14400:
        if bus.zombieIndex % bus.zombieRate == 0:
            type = random.randint(0, 20)
            if type < 8:
                bus.zombies.append(Zombie_bucket(screen, sets.zombie_bucketImages))
            else:
                # 儲存殭屍到列表中
                bus.zombies.append(Zombie_normal(screen, sets.zombie_normalImages))


# 殭屍行動函數
def hitAction():
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

# 殭屍吃植物
def eat(zb):
    for plant in bus.paintPlants:
        if not isinstance(plant, Spikeweed) and not isinstance(zb, Zombie_head) and not isinstance(zb, Zombie_dead):
           if abs((plant.x + plant.width / 2) - (zb.x + 20)) < 10 and zb.y < plant.y - 40 and zb.y + 140 > plant.y:
                if zb.life <= 3:
                    zb.images = sets.zombieLostHeadAttackImages
                elif zb.life <= 5:
                    zb.images = sets.normalAttackImages
                else:
                    zb.images = sets.bucketAttackImages
                plant.life -= 1
                if plant.life == 0:
                    bus.gridList[plant.gridX][plant.gridY] = -1
                    bus.paintPlants.remove(plant)
                    if zb.images == sets.zombieLostHeadAttackImages:
                        zb.images = sets.zombieLostHeadImages
                    else:
                        if zb.images == sets.normalAttackImages:
                            zb.images = sets.zombie_normalImages
                        else:
                            zb.images = sets.zombie_bucketImages

        if isinstance(plant, Spikeweed):
            if abs((plant.x + plant.width / 2) - (zb.x + 20)) < 10 and zb.y < plant.y - 40 and zb.y + 140 > plant.y:
                zb.life -= 1
                zb.x += 0.01
                if zb.life == 5:
                    zb.images = sets.zombie_normalImages
                elif zb.life == 3:
                    zb.images = sets.zombieLostHeadImages
                    bus.zombies.append(Zombie_head(screen, sets.zombieHeadImages, zb.x, zb.y))
                elif zb.life == 0:
                    bus.zombies.append(Zombie_dead(screen, sets.zombieDieImages, zb.x, zb.y))


# 殭屍被攻擊
def hit(zombie):
    global zombie_killed
    zombie_killed = 0
    for bullet in bus.bullets:
        if zombie.hitBy(bullet) and not isinstance(zombie, Zombie_head) and not isinstance(zombie, Zombie_dead):
            zombie.life -= 1
            if bullet.type == 0:
                # for i in range(100):
                #     screen.blit(sets.bulletHitImg, (zombie.x-100, zombie.y))
                bus.bullets.remove(bullet)

            if zombie.life == 5:
                if not isinstance(zombie, Zombie_normal):
                    zombie.images = sets.zombie_normalImages
            elif zombie.life == 3:
                if zombie.headFlag is True:
                    zombie.images = sets.zombieLostHeadImages
                    bus.zombies.append(Zombie_head(screen, sets.zombieHeadImages, zombie.x, zombie.y))
            elif zombie.life == 0:
                zombie_killed += 1
                bus.zombies.append(Zombie_dead(screen, sets.zombieDieImages, zombie.x, zombie.y))

        # 子彈超出邊界移除
        if bullet.outOfBounds():
            bus.bullets.remove(bullet)


'''
 main function 
'''


def main():
    pygame.display.set_caption("Plants vs Zombies")
    initSun()
    while True:
        action()
        paint()
        pygame.display.update()


if __name__ == '__main__':
    main()
