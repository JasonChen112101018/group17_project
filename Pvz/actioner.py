import pygame
import random
from sun import Sun

def sunAction(bus, screen, sets):
    for i in range(len(bus.sunFall)):
        bus.sunFall[i].step()
        #陽光隨機生成
        if bus.sunFall[i].index == bus.sunFall[i].goal:
            bus.sunStay.append(bus.sunFall[i])
            xx = random.randint(260, 880)
            yy = -random.randint(100, 300)
            goal = random.randint(300, 600)
            bus.sunFall[i] = Sun(screen, sets.sunImage, xx, yy, goal)

            break
    #陽光消失
    for i in range(len(bus.sunStay)):
        bus.sunStay[i].disappearTime += 1
        if bus.sunStay[i].disappearTime == 300:
            del bus.sunStay[i]
            break

def endAction(bus, screen, sets):
    if bus.endFlag == 1 and len(bus.zombies) == 0:
        bus.state = bus.END
        return

    for zombie in bus.zombies:
        if zombie.outOfBounds():
            bus.state = bus.DEAD
            break
