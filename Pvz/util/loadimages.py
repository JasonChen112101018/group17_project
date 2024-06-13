
import os, pygame
def getImages(dir):
    # calculate the number of pic
    imageCounts = 0
    for i in os.listdir(dir):
        imageCounts += 1
    images = []
    imageStr = ""
    for j in range(imageCounts):
        imageStr = dir + str(j) + '.png'
        img = pygame.image.load(imageStr)
        images.append(img)
    return images

