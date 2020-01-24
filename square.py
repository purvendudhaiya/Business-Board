import pygame
from pygame.locals import *
import configs
from configs import *

class Square:
    """classes for squares on the board"""

    def __init__(self, name):
        self.name = name

class City(Square):

    def __init__(self, name, price):
        super().__init__(name)
        self.price = price
        self.tax = price//10
        self.color = WHITE 
    
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
        namesurface = myfont.render(self.name, True, (0, 0, 0))
        DISPLAY.blit(namesurface, (pos_x + 10, pos_y + 40))
        pricesurface = myfont.render(str(self.price)+" ₹", True, (0, 0, 0))
        DISPLAY.blit(pricesurface, (pos_x + 10, pos_y + 70))
    
    def action(self, player):
        """Takes all the appropriate actions on reaching a City"""
        if self.color == WHITE and player.balance >= self.price:
            clear_top_message()
            write_top_message("Do you want to buy {} ? (Y / N) - Enter in terminal".format(self.name))
            pygame.display.update()
            
            # for taking apt user input
            while True:
                flag = 0
                pygame.display.update()
                pygame.time.Clock().tick(1)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_y:
                            flag = 1
                            self.buy(player)
                            break
                        if event.key == K_n:
                            flag =1
                            break
                        if event.key == K_ESCAPE:
                            exit(1)
                if flag == 1:
                    break

            # pygame.display.update()
            # pygame.time.Clock().tick(1)

    def fill_bar(self, color):
        pygame.draw.rect(DISPLAY, color, (self.pos_x, self.pos_y + 100, 120, 20), 0)
    
    def buy(self, player):

        self.color = player.player_color
        player.balance -= self.price
        player.update_balance()
        self.fill_bar(player.player_color)
    


class StartSquare(Square):

    def __init__(self, increment):
        super().__init__('start')
        self.increment = increment

    def draw_square(self, pos_x, pos_y):
        pygame.draw.rect(DISPLAY, BLACK, (pos_x, pos_y, 120, 120), 1)
        namesurface = myfont.render(self.name, False, (0, 0, 0))
        DISPLAY.blit(namesurface, (pos_x + 10, pos_y + 40))
    
    def action(self, player):
        player.balance+=100
    
class Jail(Square):

    def __init__(self, penalty):
        super().__init__('Jail')
        self.penalty = penalty

    def draw_square(self, pos_x, pos_y):
        pygame.draw.rect(DISPLAY, BLACK, (pos_x, pos_y, 120, 120), 1)
        namesurface = myfont.render(self.name, False, (0, 0, 0))
        DISPLAY.blit(namesurface, (pos_x + 10, pos_y + 40))

    def action(self, player):
        
        clear_top_message()
        
        if player.balance < 100:
            write_top_message("Skipping 2 Turns........")
            pygame.time.Clock().tick(0.5)
            player.turn_flag = -2
        else:
            write_top_message("Pay penalty of 100 rs. (Y / N) ; otherwise skip 2 turns")

            while True:
                    flag = 0
                    pygame.display.update()
                    pygame.time.Clock().tick(1)

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_y:
                                flag = 1
                                player.balance -= 100
                                player.update_balance()
                                break
                            if event.key == K_n:
                                flag =1
                                clear_top_message()
                                write_top_message("Skipping 2 Turns........")
                                pygame.time.Clock().tick(0.5)
                                player.turn_flag = -2
                                break
                            if event.key == K_ESCAPE:
                                exit(1)
                    if flag == 1:
                        break

