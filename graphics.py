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

def draw_board(board):

    DISPLAY.fill(BGCOLOR)

    pygame.draw.rect(DISPLAY, BLACK, (299, 99, 602, 602), 1)
    pygame.draw.rect(DISPLAY, WHITE, (300, 100, 600, 600), 0)
    
    # decrease y # increase x # increase y # decrease x
    increment = 120
    pos_x = 300
    pos_y = 580
    count=-1
    for square in board.square_list:
        square.draw_square(pos_x, pos_y)
        count += 1
        if count//4 == 0:
            pos_y -= increment
        elif count//4 == 1:
            pos_x += increment
        elif count//4 == 2:
            pos_y += increment
        else:
            pos_x -= increment

    pygame.draw.rect(DISPLAY, BLACK, (0, 0, 1200, 80))
    DISPLAY.blit(message_surface, (30, 30))


def clear_top_message(cls):
    configs.message_surface = myfont.render(configs.MESSAGE, False, BLACK)
    DISPLAY.blit(configs.message_surface, (30, 30))

def print_top_message(cls, message):
    configs.MESSAGE = message
    configs.message_surface = myfont.render(configs.MESSAGE, False, WHITE)
    DISPLAY.blit(configs.message_surface, (30, 30))
