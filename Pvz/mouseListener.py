from util.constant import Constant
from settings import Setting
import pygame
from util.loadimages import getImages
from sun import Sun
from plant.wallnut import Wallnut
from plant.sunflower import Sunflower
from plant.peashooter import Peashooter
from plant.snowshooter import Snowshooter
from plant.spikeweed import Spikeweed
import sys
from util.bus import Bus
import random

sets = Setting()

# 當滑鼠被點即時啟用函數
# 判斷滑鼠點擊卡片
def cardMouseClickListener(bus):
    leftButtonDown = pygame.mouse.get_pressed()[0]
    rightButtonDown = pygame.mouse.get_pressed()[2]
    if leftButtonDown:
        mousex, mousey = pygame.mouse.get_pos()
        CARD_BASIC_X = 80
        CARD_BASIC_Y = 10
        CARD_HEIGHT = 68
        CARD_WIDTH = 55
        CARD_OFFSET = 60
        # i --> 0-堅果 1-向日葵 2-豌豆射手 4-寒冰射手 3-地刺
        # 設置count循環次數 控制反白植物不能點擊
        rangeCount = 0
        if bus.sunScore < 50:
            rangeCount = 0
        elif 50 <= bus.sunScore < 100:
            rangeCount = 2
        elif 100 <= bus.sunScore < 175:
            rangeCount = 4
        else:
            rangeCount = 5

        # 選卡片
        for i in range(rangeCount):
            if CARD_BASIC_X + CARD_OFFSET * i < mousex < CARD_BASIC_X + CARD_WIDTH + CARD_OFFSET * i and \
                    CARD_BASIC_Y < mousey < CARD_BASIC_Y + CARD_HEIGHT:
                dict = {
                    0: Constant.NUT_SELECTED,
                    1: Constant.SUNFLOWER_SELECTED,
                    2: Constant.PEASHOOTER_SELECTED,
                    3: Constant.SPIKEWEED_SELECTED,
                    4: Constant.SNOWPEA_SELECTED,
                }
                bus.cardState = Constant.CARD_CLICKED
                bus.cardSelection = dict[i]
        ## 選鏟子
        if CARD_BASIC_X + CARD_OFFSET * 6 < mousex < CARD_BASIC_X + CARD_WIDTH + CARD_OFFSET * 6 and \
                    CARD_BASIC_Y < mousey < CARD_BASIC_Y + CARD_HEIGHT:
            bus.cardState = Constant.CARD_CLICKED
            bus.cardSelection = Constant.SHOVEL_SELECTED
    if rightButtonDown:
        bus.cardState = Constant.CARD_NOT_CLICKED

# 用來判斷格子的x座標（滑鼠點擊在第幾格）
def getGridX(mouseX):
    if mouseX < sets.gridXIndexes[0]:
        return -1
    for i in range(len(sets.gridXIndexes)):
        if mouseX <= sets.gridXIndexes[i]:
            return i - 1
    return -1

# 用來綁定滑鼠點擊事件
def initPlantsMouseClickListener(bus, screen):
    leftButtonDown = pygame.mouse.get_pressed()[0]
    if leftButtonDown:
        mouseX, mouseY = pygame.mouse.get_pos()
        gridX = getGridX(mouseX)
        gridY = int((mouseY - sets.topY) / sets.gridHeight)
        plantX = sets.gridXIndexes[gridX]
        plantY = sets.topY + sets.gridHeight * gridY
        if mouseX >= sets.leftX and mouseX <= sets.rightX \
            and mouseY <= sets.bottomY and mouseY >= sets.topY \
                    and bus.gridList[gridX][gridY] == -1:
            imagedict = {
                Constant.NUT_SELECTED: 0,
                Constant.SUNFLOWER_SELECTED: 1,
                Constant.PEASHOOTER_SELECTED: 2,
                Constant.SPIKEWEED_SELECTED: 3,
                Constant.SNOWPEA_SELECTED: 4,
            }
            plantdict = [
                Wallnut(screen, plantX, plantY, getImages(sets.plantsInitImages[0])),
                Sunflower(screen, plantX, plantY, getImages(sets.plantsInitImages[1])),
                Peashooter(screen, plantX, plantY, getImages(sets.plantsInitImages[2])),
                Spikeweed(screen, plantX, plantY+40, getImages(sets.plantsInitImages[3])),
                Snowshooter(screen, plantX, plantY, getImages(sets.plantsInitImages[4])),
            ]
            if bus.cardState == Constant.CARD_CLICKED and bus.cardSelection in imagedict:
                index = imagedict[bus.cardSelection]
                plantdict[index].gridX = gridX
                plantdict[index].gridY = gridY
                bus.paintPlants.append(plantdict[index])
                bus.cardState = Constant.CARD_NOT_CLICKED
                bus.sunScore -= plantdict[index].sunshine
                bus.gridList[gridX][gridY] = index
        # 如果點擊的是鏟子
        elif bus.cardState == Constant.CARD_CLICKED and bus.cardSelection == Constant.SHOVEL_SELECTED \
                and bus.gridList[gridX][gridY] != -1:
            for i in range(len(bus.paintPlants)):
                if bus.paintPlants[i].gridX == gridX \
                        and bus.paintPlants[i].gridY == gridY:
                    del bus.paintPlants[i]
                    break
            bus.gridList[gridX][gridY] = -1
            bus.cardState = Constant.CARD_NOT_CLICKED

def sunMouseClickListener(bus, screen, sets):
        # 用中左鍵撿太陽並返回TrueorFalse
        leftFlag = pygame.mouse.get_pressed()[0]

        mouseX, mouseY = pygame.mouse.get_pos()

        # 判斷滑鼠點擊到了太陽
        for i in range(len(bus.sunFall)):
            if leftFlag and mouseX > bus.sunFall[i].x and mouseX < bus.sunFall[i].x + bus.sunFall[i].width and \
                    mouseY > bus.sunFall[i].y and mouseY < bus.sunFall[i].y + bus.sunFall[i].height:
                bus.sunScore += bus.sunFall[i].score
                xx = random.randint(260, 880)
                yy = -random.randint(100, 300)
                goal = random.randint(300, 600)
                bus.sunFall[i] = Sun(screen, sets.sunImage, xx, yy, goal)
                break

        for i in range(len(bus.sunStay)):
            if leftFlag and mouseX > bus.sunStay[i].x and mouseX < bus.sunStay[i].x + bus.sunStay[i].width and \
                    mouseY > bus.sunStay[i].y and mouseY < bus.sunStay[i].y + bus.sunStay[i].height:
                bus.sunScore += bus.sunStay[i].score
                xx = random.randint(260, 880)
                yy = -random.randint(100, 300)
                goal = random.randint(300, 600)
                bus.sunStay[i] = Sun(screen, sets.sunImage, xx, yy, goal)
                break

def runOrPause(bus, screen, sets):
    leftFlag = pygame.mouse.get_pressed()[0]

    mouseX, mouseY = pygame.mouse.get_pos()
    
    width, height = screen.get_size()
    half_x = width / 2
    half_y = height / 2

    if mouseX >= width - 200 and mouseX <= width - 20 and mouseY >= 10 and mouseY <= 10 + 41 and bus.state == bus.RUNNING:
        bus.state = bus.PAUSE
    elif 750 < mouseX  < 900 and 100 < mouseY < 200 + 100 and bus.state == bus.START:
        bus.state = bus.RUNNING
    elif 1257 < mouseX < 1350 and 495 < mouseY < 539:
        sys.exit(0)
    elif leftFlag and bus.state == bus.PAUSE:
        bus.state = bus.RUNNING
    elif bus.state == bus.DEAD or bus.state == bus.END:
        if 555 < mouseX < 780 and  340 < mouseY < 390 :
            restart(bus, screen)
            bus.state = bus.START
        elif 555 < mouseX < 780 and  410 < mouseY < 460 :
            sys.exit(0)

# 初始化bus中的各個值
def restart(bus, screen):
    # 是否選擇了卡片
    bus.cardState = Constant.CARD_NOT_CLICKED

    #  選擇卡片的類型
    bus.cardSelection = Constant.NUT_SELECTED

    # 表示當前需要繪製的圖片
    bus.paintPlants = []

    # 殭屍列表
    bus.zombies = []
    # 殭屍生成頻率
    bus.zombieIndex = 0
    # 殭屍掉頭信號
    bus.headFlag = True
    bus.zombieRate = 0

    # 存放正在下落太陽的列表
    bus.sunFall = []
    # 存放已經停止的太陽的列表
    bus.sunStay = []

    for i in range(1):
        xx = random.randint(260, 880)
        yy = -random.randint(100, 300)
        goal = random.randint(300, 600)
        sun = Sun(screen, sets.sunImage, xx, yy,goal)
        bus.sunFall.append(sun)
    # 初始太陽量
    bus.sunScore = 100
    # 初始化4個太陽  xx  yy 分别紀錄的x坐標和y坐标
    # xx = []
    # yy = []

    # 時間軸
    bus.globalTime = 0

    # 格子的二維數組
    bus.gridList = [([-1] * 5) for i in range(9)]

    # 遊戲狀態
    bus.state = bus.START

    # 子彈儲存列表
    bus.bullets = []

    #是否進入中段和末段
    bus.midPercentage = False
    bus.finalPercentage = False

    # 植物頻率
    bus.plantIndex = 0
    # 子彈生成頻率值
    bus.shootIndex = 0

    # 遊戲結束
    bus.endFlag = 0
