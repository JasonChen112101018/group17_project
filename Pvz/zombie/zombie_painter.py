import pygame
import painter as painter
from util.bus import Bus
from zombie.head import Zombie_head
from zombie.dead import Zombie_dead


bus = Bus()
# 繪製僵屍
def paintZombies():
    for zombie in bus.zombies:
        zombie.blitme()
        if isinstance(zombie, Zombie_head) or isinstance(zombie, Zombie_dead):
            if zombie.reloadFlag == 1:
                bus.zombies.remove(zombie)

