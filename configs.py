import pygame
from pygame.locals import *

pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('dejavusans', 20)
DISPLAY=pygame.display.set_mode((1200, 800), 0, 32)
MESSAGE = 'WELCOME TO BUSINESS BOARD '
message_surface = myfont.render(MESSAGE, False, (0, 0, 0))
top_message_patch = pygame.Surface((1200, 80))

BGCOLOR = (255, 255, 102)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def clear_top_message():
    print("Inside Clear top")
    DISPLAY.blit(top_message_patch, (0,0))
    pygame.display.update()

def write_top_message(message):
    print("inside write top")
    DISPLAY.blit(myfont.render(message, True, WHITE), (30, 30))
    print("wrote - inside one")
    pygame.display.update()