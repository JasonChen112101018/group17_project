import pygame, sys, random
import ..painter, ..actioner, ..mouseListener , ..settings
import ..util
import ..zombie
import ..plant


#生成太陽
bus = Bus()
sets = Setting()

screen = pygame.display.set_mode((1400, 600), 0, 0)

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

# 子彈超出邊界
        if bullet.outOfBounds():
            bus.bullets.remove(bullet)

