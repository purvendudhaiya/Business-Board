import pygame
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()
pygame.font.init()
move_sound = pygame.mixer.Sound("./assets/mario_jump.wav")
pygame.mixer.music.load("./assets/Greenback_Boogie.mp3")
pygame.mixer.music.play(-1)
myfont = pygame.font.SysFont('Comic Sans MS', 20)
DISPLAY=pygame.display.set_mode((1200, 800), 0, 32)
MESSAGE = 'WELCOME TO BUSINESS BOARD '
message_surface = myfont.render(MESSAGE, False, (0, 0, 0))
top_message_patch = pygame.Surface((1200, 80))

BGCOLOR = (255, 194, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 51)

def clear_top_message():
    DISPLAY.blit(top_message_patch, (0,0))
    pygame.display.update()

def write_top_message(message):
    DISPLAY.blit(myfont.render(message, True, WHITE), (300, 30))
    pygame.display.update()