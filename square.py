import pygame
from pygame.locals import *
from configs import DISPLAY, BLACK, WHITE, RED, GREEN, BLUE, myfont

class Square:
    """classes for squares on the board"""

    def __init__(self, name):
        self.name = name

class City(Square):

    def __init__(self, name, price):
        super().__init__(name)
        self.price = price
        self.tax = price//10
        self.owner = WHITE 
    
    def change_color(self, color):
        self.color = color
    
    def compare_player_color(self, player_color):
        if self.color == 'white' or self.color == player_color:
            return True
        return False
    
    def draw_square(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        pygame.draw.rect(DISPLAY, BLACK, (pos_x, pos_y, 120, 120), 1)
        namesurface = myfont.render(self.name, False, (0, 0, 0))
        DISPLAY.blit(namesurface, (pos_x + 10, pos_y + 40))
        pricesurface = myfont.render(str(self.price)+" ₹", False, (0, 0, 0))
        DISPLAY.blit(pricesurface, (pos_x + 10, pos_y + 70))
    
    def fill_bar(self, color):
        pygame.draw.rect(DISPLAY, color, (self.pos_x, self.pos_y + 100, 120, 20), 0)
    
    def buy(self, player):

        self.owner = player.player_color
        self.fill_bar(player.player_color)
    
    





class StartSquare(Square):

    def __init__(self, increment):
        super().__init__('start')
        self.increment = increment

    def draw_square(self, pos_x, pos_y):
        pygame.draw.rect(DISPLAY, BLACK, (pos_x, pos_y, 120, 120), 1)
        namesurface = myfont.render(self.name, False, (0, 0, 0))
        DISPLAY.blit(namesurface, (pos_x + 10, pos_y + 40))
    
class Jail(Square):

    def __init__(self, penalty):
        super().__init__('jail')
        self.penalty = penalty

    def draw_square(self, pos_x, pos_y):
        pygame.draw.rect(DISPLAY, BLACK, (pos_x, pos_y, 120, 120), 1)
        namesurface = myfont.render(self.name, False, (0, 0, 0))
        DISPLAY.blit(namesurface, (pos_x + 10, pos_y + 40))

    