import pygame
from pygame.locals import *

pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 20)
DISPLAY=pygame.display.set_mode((1200, 800), 0, 32)
MESSAGE = 'WELCOME TO BUSINESS BOARD '
message_surface = myfont.render(MESSAGE, False, (0, 0, 0))

BGCOLOR = (255, 255, 102)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def print_mess():
    print(MESSAGE)

    
