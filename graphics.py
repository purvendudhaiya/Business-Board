import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((1200, 800), 0, 32)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    DISPLAY.fill((255, 255, 102))

    pygame.draw.rect(DISPLAY, BLACK, (299, 99, 602, 602), 1)
    pygame.draw.rect(DISPLAY, WHITE, (300, 100, 600, 600), 0)


    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()