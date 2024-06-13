
from util.constant import Constant


class Bus:
    # Indicates whether a card has been selected
    cardState = Constant.CARD_NOT_CLICKED

    # Indicates the type of card selected
    cardSelection = Constant.NUT_SELECTED

    # Represents the images that need to be drawn currently
    paintPlants = []

    # List to store zombies
    zombies = []
    # Zombie frequency value
    zombieIndex = 0
    # Head signal flag
    headFlag = True
    zombieRate = 0

    # List to store falling suns
    sunFall = []
    # List to store stationary suns
    sunStay = []
    # Records the initial amount of sunshine
    sunScore = 100
    # Initializes 4 suns; xx and yy record the x and y coordinates of the suns, respectively
    # xx = []
    # yy = []

    # Global unified timeline
    globalTime = 0

    # Two-dimensional array for grid cells
    gridList = [([-1] * 5) for i in range(9)]

    # Game state
    START = 0
    RUNNING = 1
    PAUSE = 2
    END = 3
    DEAD = 4
    state = START


    # List to store bullets
    bullets = []

    # Indicates if the game has entered the mid and final stages
    midPercentage = False
    finalPercentage = False

    # Plant frequency value
    plantIndex = 0
    # Bullet generation frequency value
    shootIndex = 0

    # Game end signal
    endFlag = 0

