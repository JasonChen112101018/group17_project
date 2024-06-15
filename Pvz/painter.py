from util.constant import Constant
import pygame
from  pygame.locals import *



# 開始遊戲界面
def initStartSurface(bus, screen, sets):
    window_size = screen.get_size()
    scaled_surface = pygame.transform.scale(sets.surface, window_size)
    scaled_wood = pygame.transform.scale(sets.wood, (400, 300))
    scaled_beginBtn = pygame.transform.scale(sets.beginBtn, (300, 200))
    screen.blit(scaled_surface, (0,0))
    screen.blit(scaled_wood, (180,110))
    screen.blit(scaled_beginBtn, (600,100))

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
    width, height = screen.get_size()
    half_x = width / 2
    half_y = height / 2

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
    screen.blit(sets.Button, (width - 150, 10))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 28)
    Str = ft.render("Pause", True, (0, 0, 0))
    screen.blit(Str, (width - 130, 14))

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

    width, height = screen.get_size()
    half_x = width / 2
    half_y = height / 2
    # 進度條
    percentage = bus.globalTime / 100

    # 開始標語
    if percentage <= 3 and percentage >= 1:
        screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 0), (290, 120))), (440, 240))

    if percentage >= 3 and percentage <= 5:
        screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 120), (290, 100))), (440, 260))

    if percentage >= 5 and percentage <= 7:
        screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 212), (290, 120))), (440, 240))
    if not bus.midPercentage and 40 < percentage < 99 :
        bus.midPercentage = True

    # 一大波殭屍提示語
    if percentage >= 70 and percentage <= 80:
        screen.blit(sets.largeWave, (half_x - 250, half_y - 50))


    # 最后一波提示語
    if percentage >= 134 and percentage <= 144:
        screen.blit(sets.finalWave, (half_x -100, half_y - 50))
        if not bus.finalPercentage:
            bus.finalPercentage = True


    screen.blit(sets.flagMeterFull, (width-160, height-25))

    if percentage <= 145:
        screen.blit(sets.flagMeterEmpty.subsurface(Rect((0, 0), (157 - percentage, 21))), (width-160, height-25))
        screen.blit(sets.flagMeterParts2, (width - 5 - percentage, height - 35))
        screen.blit(sets.flagMeterParts1, (width - 20 - percentage, height - 25))


    else:
        screen.blit(sets.flagMeterParts2, (width - 150, height - 35))
        screen.blit(sets.flagMeterParts1, (width - 165, height - 25))


# 暫停標誌
def paintPause(bus, screen, sets):
    width, height = screen.get_size()
    half_x = width / 2
    half_y = height / 2
    x_image , y_image = sets.Pause.get_size()
    screen.blit(sets.Pause, (half_x - x_image/2, 0))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 20)
    Str = ft.render("Press to continue", True, (255, 0, 0))
    screen.blit(Str, (half_x - x_image/2 +50  , 90))

# 失敗畫面
def deadPaint(bus, screen, sets):
    width, height = screen.get_size()
    half_x = width / 2
    half_y = height / 2
    x_image , y_image = sets.menuBar.get_size()
    scaled_menuBar = pygame.transform.scale(sets.menuBar, (x_image*0.8, y_image*0.8))
    scaled_x_image, scaled_y_image = scaled_menuBar.get_size()
    screen.blit(scaled_menuBar, (half_x - (scaled_x_image/2), height - (scaled_y_image)))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 45)
    Str = ft.render("Game Defeat", True, (0, 195, 0))
    screen.blit(Str, (half_x - (scaled_x_image/3), height - (scaled_y_image)+150) )

    # 結束
    #screen.blit(sets.selectionBar, (555, 410))
    #pygame.font.init()
    #ft = pygame.font.Font('hiw.ttf', 32)
    #Str = ft.render("exit", True, (60, 60, 60))
    #screen.blit(Str, (628, 417))

def restartPaint(bus, screen, sets):
    screen.blit(sets.selectionBar, (555, 340))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 32)
    Str = ft.render("重新開始", True, (60, 60, 60))
    screen.blit(Str, (605, 346))

def wonPaint(bus, screen, sets):
    width, height = screen.get_size()
    half_x = width / 2
    half_y = height / 2
    x_image , y_image = sets.menuBar.get_size()
    scaled_menuBar = pygame.transform.scale(sets.menuBar, (x_image*0.8, y_image*0.8))
    scaled_x_image, scaled_y_image = scaled_menuBar.get_size()
    screen.blit(scaled_menuBar, (half_x - (scaled_x_image/3), height - (scaled_y_image)))
    pygame.font.init()
    ft = pygame.font.Font('hiw.ttf', 45)
    Str = ft.render("You Win", True, (0, 195, 0))
    screen.blit(Str, (half_x - (scaled_x_image/3)+125, height - (scaled_y_image)+150))
    # 結束
    #screen.blit(sets.selectionBar, (555, 410))
    #pygame.font.init()
    #ft = pygame.font.Font('hiw.ttf', 32)
    #Str = ft.render("", True, (60, 60, 60))
    #screen.blit(Str, (628, 417))
