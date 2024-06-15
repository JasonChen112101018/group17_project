import pygame, sys, random
import painter as painter
import actioner as actioner
import mouseListener as mouseListener
from settings import Setting
from util.bus import Bus
from sun import Sun
import zombie 
import zombie_actioner as z_actioner
import zombie.zombie_painter as z_painter
import plant.Plantpainter as plantpainter
import plant

screen = pygame.display.set_mode((1100, 600), 0, 0)

sets = Setting()
bus = Bus()

def initSun():
    for i in range(1):
        xx = random.randint(260, 880)
        yy = -random.randint(100, 300)
        goal = random.randint(300, 600)
        sun = Sun(screen, sets.sunImage, xx, yy,goal)
        bus.sunFall.append(sun)

# 繪製場景
def paint():
    if bus.state == bus.START:
        painter.initStartSurface(bus, screen, sets)
        return

    # 判斷是否需要繪製背景
    painter.initScenario(bus, screen, sets)
    z_painter.paintZombies()
    painter.cardMovePaint(bus, screen, sets)
    plantpainter.paintPlants()
    plantpainter.paintBullets()

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
        painter.wonPaint(bus, screen, sets)


# 事件處理函數
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
        bus.globalTime += 1
        time = bus.globalTime
        z_actioner.stepAction()
        z_actioner.zombiesAction()
        # 陽光的行動
        actioner.sunAction(bus, screen, sets)
        # 全局時間軸增加
        #bus.globalTime += 1
        #print("time = %d"%bus.globalTime)
        for plant in bus.paintPlants:
            plant.step(bus, screen, sets)
        z_actioner.hitAction()
        actioner.endAction(bus, screen, sets)



