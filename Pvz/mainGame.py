import pygame
import sys
import random
import threading
import time

import painter
import actioner
import mouseListener

from background import initSun
from background import paint
from background import action
import plant
import zombie
import util
import image

def main():
    pygame.display.set_caption("plants vs zombies")
    initSun()
    while True:
        action()
        paint()
        pygame.display.update()


if __name__ == '__main__':
    main()
