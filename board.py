from square import Square, StartSquare, City, Jail
import pygame
import random
from pygame.locals import *
import configs
from configs import *
import sys
import time

class Board:

    def __init__(self):
        self.square_list= [
            StartSquare(100),
            City('Baroda', 200),
            City('Surat', 200),
            City('Valsad', 200),
            City('Rest Here', 0),
            City('Mumbai', 200),
            City('Pune', 200),
            City('Goa', 200),
            Jail(100),
            City('Chennai', 200),
            City('Agra', 200),
            City('Kochi', 200),
            City('Surprise',0),
            City('Jammu', 200),
            City('Delhi', 200),
            City('Kolkata', 200)
            ]


    def draw_board(self):

        DISPLAY.fill(BGCOLOR)

        pygame.draw.rect(DISPLAY, BLACK, (299, 99, 602, 602), 1)
        pygame.draw.rect(DISPLAY, WHITE, (300, 100, 600, 600), 0)
        
        # decrease y
        # increase x
        # increase y
        # decrease x
        increment = 120
        pos_x = 300
        pos_y = 580
        count=-1
        for square in self.square_list:
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

        # moved the class methods to configs.py.  Works GREAAAAAT ! can use those in other modules also now.
            



class Player:
    count = 0
    player_patch = pygame.Surface((20, 20))  # white patch for the player
    player_patch.fill(WHITE)
    player_details_patch = pygame.Surface((100, 30))  # background patch for player's balance
    player_details_patch.fill(BGCOLOR)

    def __init__(self, name, player_color):
        self.name = name
        self.balance = 1000
        self.player_color = player_color
        self.player_pos = 0
        self.player_surface = pygame.Surface((20, 20))
        self.player_surface.fill(player_color)
        Player.count += 1
        self.pos_x = 290 + (2 * Player.count - 1)* 20 
        self.pos_y = 590
        self.name_pos_x = 10                                                        # x coordinate for player's name surface
        self.name_pos_y = 350 + (2 * Player.count - 1)* 20
        self.balance_pos_x = 100                                                    # x coordinate for player's balance surface 
        self.balance_pos_y = self.name_pos_y
        DISPLAY.blit(self.player_surface, (self.pos_x, self.pos_y))
        self.player_name_surface = myfont.render(self.name, False, self.player_color)
        DISPLAY.blit(self.player_name_surface, (self.name_pos_x, self.name_pos_y))
        self.player_balance_surface = myfont.render(str(self.balance)+" ₹", False, self.player_color)
        DISPLAY.blit(self.player_balance_surface, (self.balance_pos_x, self.balance_pos_y))
    
    def update_balance(self):
        """updates the particular player's balance in GUI"""
        DISPLAY.blit(Player.player_details_patch, (self.balance_pos_x, self.balance_pos_y))
        self.player_balance_surface = myfont.render(str(self.balance)+" ₹", False, self.player_color)
        DISPLAY.blit(self.player_balance_surface, (self.balance_pos_x, self.balance_pos_y))

    def roll_dice(self):
        dice_value = random.randint(1,6)
        clear_top_message()
        write_top_message(str(dice_value))
        return dice_value

    def move(self, steps, b):
        
        for i in range(1, steps+1):
            DISPLAY.blit(Player.player_patch, (self.pos_x, self.pos_y))
            self.player_pos = (self.player_pos + 1) % 16
            if (self.player_pos - 1)//4 == 0:
                self.pos_y -= 120
            if (self.player_pos - 1)//4 == 1:
                self.pos_x += 120
            if (self.player_pos - 1)//4 == 2:
                self.pos_y += 120
            if (self.player_pos -1)//4 == 3:
                self.pos_x -= 120
            
            pygame.display.update()
            pygame.time.Clock().tick(5)
            
            DISPLAY.blit(self.player_surface, (self.pos_x, self.pos_y))

            pygame.display.update()
            pygame.time.Clock().tick(5)
        
        print(self.player_pos)
        (b.square_list[self.player_pos]).action(self)


b = Board()
b.draw_board()
p1 = Player('Vatsal', RED)
p2 = Player('Dhruv', BLUE)
p3 = Player('Purven', GREEN)
val = p1.roll_dice()
p1.move(val, b)
# p2.move(16)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        pygame.display.update()