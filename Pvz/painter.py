from util.constant import Constant
import pygame
from  pygame.locals import *


# 開始遊戲界面
def initStartSurface(bus, screen, sets):
    screen.blit(sets.surface, (0,0))
    screen.blit(sets.beginBtn, (740,100))

# 滑鼠拖曳植物
def cardMovePaint(bus, screen, sets):
    if bus.cardState == Constant.CARD_CLICKED:
        dict = {
            Constant.NUT_SELECTED: 0,
            Constant.SUNFLOWER_SELECTED: 1,
            Constant.PEASHOOTER_SELECTED: 2,
            Constant.SPIKEWEED_SELECTED: 3,
            Constant.SNOWPEA_SELECTED: 4,
            Constant.SHOVEL_SELECTED: 5
        }
        drawImgIdx = dict[bus.cardSelection]
        mousex, mousey = pygame.mouse.get_pos()
        screen.blit(sets.cardImgs[drawImgIdx], (mousex - 27, mousey - 34))

#初始場景繪製
def initScenario(bus, screen, sets):
    screen.blit(sets.background, (0, 0))
    screen.blit(sets.seedBank, (0, 0))
    # 顯示卡片
    CARD_OFFSET = 60
    dict = {
        0: sets.cardNutWall,
        1: sets.sunflower,
        2: sets.cardPeashooter,
        3: sets.cardspikeWeed,
        4: sets.cardsnowPea,
        5: sets.cardShovel
    }
    dictDark = {
        0: sets.cardNutWallDark,
        1: sets.sunflowerDark,
        2: sets.cardPeashooterDark,
        3: sets.cardspikeWeedDark,
        4: sets.cardsnowPeaDark,
    }
    
    sun_requirements = [50, 50, 100, 100, 175]
    
    for i in range(len(sun_requirements)):
        if bus.sunScore >= sun_requirements[i]:
            screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
        else:
            screen.blit(dictDark[i], (80 + CARD_OFFSET * i, 10))
    
    screen.blit(sets.cardShovelBack, (448, 0))
    screen.blit(sets.cardShovel, (444, 10))

    # 暫停按鈕
    screen.blit(sets.Button, (1265, 10))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 28)
    Str = ft.render("Pause", True, (0, 0, 0))
    screen.blit(Str, (1290, 14))

# 陽光圖形
def paintSun(bus, screen, sets):
    for i in range(len(bus.sunFall)):
        bus.sunFall[i].blitme()

    for i in range(len(bus.sunStay)):
        bus.sunStay[i].blitme()

# 陽光數量
def paintSunScore(bus, screen, sets):
    pygame.font.init()
    ft = pygame.font.Font('msyh.ttf', 20)
    scoreStr = ft.render("%d"%bus.sunScore, True, (0, 0, 0))
    if bus.sunScore <= 1000:
        screen.blit(scoreStr, (19, 59))
    else:
        screen.blit(scoreStr, (17, 59))


#進度條
def painProgressBar(bus, screen, sets):
    # 進度條
    percentage = bus.globalTime / 100

    # 開始標語
    if percentage <= 2 and percentage >= 1:
        screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 0), (255, 112))), (550, 240))

    if percentage >= 2 and percentage <= 3:
        screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 112), (255, 100))), (550, 240))

    if percentage >= 3 and percentage <= 4:
        screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 212), (255, 112))), (550, 240))
    if not bus.midPercentage and 40 < percentage < 99 :
        bus.midPercentage = True

    # 一大波殭屍提示語
    if percentage >= 70 and percentage <= 80:
        screen.blit(sets.largeWave, (525, 240))


    # 最后一波提示語
    if percentage >= 143 and percentage <= 144:
        screen.blit(sets.finalWave, (525, 240))
        if not bus.finalPercentage:
            bus.finalPercentage = True


    screen.blit(sets.flagMeterFull, (1200, 560))

    if percentage <= 145:
        screen.blit(sets.flagMeterEmpty.subsurface(Rect((0, 0), (157 - percentage, 21))), (1200, 560))
        screen.blit(sets.flagMeterParts1, (1340 - percentage, 560))
    else:
        screen.blit(sets.flagMeterParts1, (1340 - 145, 560))

    screen.blit(sets.flagMeterParts2, (1205, 557))

# 暫停標誌
def paintPause(bus, screen, sets):
    screen.blit(sets.Pause, (500, 0))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 20)
    Str = ft.render("Press to continue", True, (255, 0, 0))
    screen.blit(Str, (562, 92))

# 失敗畫面
def deadPaint(bus, screen, sets):
    screen.blit(sets.menuBar, (466, 100))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 45)
    Str = ft.render("Game Defeat", True, (255, 255, 255))
    screen.blit(Str, (550, 255))
    # 結束
    screen.blit(sets.selectionBar, (555, 410))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 32)
    Str = ft.render("exit", True, (60, 60, 60))
    screen.blit(Str, (628, 417))

def restartPaint(bus, screen, sets):
    screen.blit(sets.selectionBar, (555, 340))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 32)
    Str = ft.render("重新開始", True, (60, 60, 60))
    screen.blit(Str, (605, 346))

def wonPaint(bus, screen, sets):
    screen.blit(sets.menuBar, (466, 100))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 45)
    Str = ft.render("闖 關 成 功", True, (255, 255, 255))
    screen.blit(Str, (560, 255))
    # 結束
    screen.blit(sets.selectionBar, (555, 410))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 32)
    Str = ft.render("結  束", True, (60, 60, 60))
    screen.blit(Str, (628, 417))
