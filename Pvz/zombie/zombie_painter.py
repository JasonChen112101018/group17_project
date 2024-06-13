import pygame
import ..painter
import ..util.bus
import .zombie



# 繪製僵屍
def paintZombies():
    for zombie in bus.zombies:
        zombie.blitme()
        if isinstance(zombie, Zombie_head) or isinstance(zombie, Zombie_dead):
            if zombie.reloadFlag == 1:
                bus.zombies.remove(zombie)

