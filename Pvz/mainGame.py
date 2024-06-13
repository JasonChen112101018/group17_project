'''import pygame, sys, random
from conf.settings import Setting
from entity.zombie.zombie_bucket import Zombie_bucket
from entity.zombie.zombie_conehead import Zombie_conehead
from entity.zombie.zombie_normal import Zombie_normal
from util.constant import Constant
from musicplayer import MusicPlayer
from entity.sun import Sun
from util.bus import Bus
import mouseListener
import painter
import actioner
from entity.zombie.zombie_head import Zombie_head
from entity.zombie.zombie_dead import Zombie_dead
from entity.plant.cherryBomb import CherryBomb
import threading
import time
'''
import pygame, sys, random
import painter , actioner , mouseListener , threading , time
import .back, .plant, .zombie, .util, .images


'''#生成太陽
bus = Bus()
sets = Setting()

screen = pygame.display.set_mode((1400, 600), 0, 0)
bus.music = MusicPlayer()

bus.music.play()

def initSun():
    for i in range(1):
        xx = random.randint(260, 880)
        yy = -random.randint(100, 300)
        goal = random.randint(300, 600)
        sun = Sun(screen, sets.sunImage, xx, yy,goal)
        bus.sunFall.append(sun)'''

'''
paint部分
'''

'''# 繪製場景
def paint():
    if bus.state == bus.START:
        painter.initStartSurface(bus, screen, sets)
        return

    # 判斷是否需要繪製背景
    painter.initScenario(bus, screen, sets)
    paintZombies()
    painter.cardMovePaint(bus, screen, sets)
    paintPlants()
    paintBullets()

    # 繪製下落及在地上的太陽
    painter.paintSun(bus, screen, sets)
    # 繪製太陽總數
    painter.paintSunScore(bus, screen, sets)
    # 繪製時間條
    painter.painProgressBar(bus, screen, sets)
    if bus.state == bus.PAUSE:
        painter.paintPause(bus, screen, sets)
    elif bus.state == bus.DEAD:
        painter.deadPaint(bus, screen, sets)
    elif bus.state == bus.END:
        painter.wonPaint(bus, screen, sets)'''
        

'''# 繪製僵屍
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
        bullet.blitme()'''

'''
action部分
'''


'''# 事件處理函數
def action():

   # 事件觸發
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
        # 陽光的行動
        actioner.sunAction(bus, screen, sets)
        # 全局時間軸增加
        bus.globalTime += 1
        for plant in bus.paintPlants:
            plant.step(bus, screen, sets)
        hitAction()
        actioner.endAction(bus, screen, sets)
        '''

'''# 走一步
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
        bus.zombieRate = 50
    else:
        bus.zombieRate = 500

    if bus.globalTime == 14300:
        bus.zombies.append(Zombie_bucket(screen, sets.zombie_bucketImages))
        bus.endFlag = 1
    if bus.globalTime < 14400:
        if bus.zombieIndex % bus.zombieRate == 0:
            type = random.randint(0, 20)
            if type < 8:
                bus.zombies.append(Zombie_conehead(screen, sets.zombie_coneheadImages))
            else:
                bus.zombies.append(Zombie_normal(screen, sets.zombie_normalImages))


# 殭屍被攻擊
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
        if not isinstance(plant, CherryBomb) and not isinstance(zb, Zombie_head) and not isinstance(zb, Zombie_dead):
            if plant.x + plant.width/2 == zb.x + 20 and zb.y + 100 < plant.y + 100 and zb.y + 100 > plant.y:
                if zb.life <= 3:
                    zb.images = sets.zombieLostHeadAttackImages
                elif zb.life <= 5:
                    zb.images = sets.normalAttackImages
                elif zb.life <= 8:
                    if not isinstance(zb, Zombie_bucket):
                        zb.images = sets.coneheadAttackImages
                    else:
                        zb.images = sets.bucketAttackImages
                else:
                    zb.images = sets.bucketAttackImages
                plant.life -= 0.5
                if plant.life == 0:
                    bus.gridList[plant.gridX][plant.gridY] = -1
                    bus.paintPlants.remove(plant)
                    if zb.images == sets.zombieLostHeadAttackImages:
                        zb.images = sets.zombieLostHeadImages
                    else:
                        if zb.images == sets.normalAttackImages:
                            zb.images = sets.zombie_normalImages
                        elif zb.images == sets.coneheadAttackImages:
                            zb.images = sets.zombie_coneheadImages
                        else:
                            zb.images = sets.zombie_bucketImages



# 殭屍被攻擊
def hit(zombie):
    for bullet in bus.bullets:
        if zombie.hitBy(bullet) and not isinstance(zombie, Zombie_head) and not isinstance(zombie, Zombie_dead):
            zombie.life -= 1
            # 豌豆不穿透，仙人掌刺穿透
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
                bus.zombies.append(Zombie_dead(screen, sets.zombieDieImages, zombie.x, zombie.y))'''

   '''# 子彈超出邊界
        if bullet.outOfBounds():
            bus.bullets.remove(bullet)'''


'''
程序入口
'''


def main():
    pygame.display.set_caption("plants vs zombies")
    initSun()
    while True:
        action()
        paint()
        pygame.display.update()


if __name__ == '__main__':
    main()
