import pygame
from pygame.locals import *
import configs
from configs import *
import random

class Square:
    """classes for squares on the board"""

    def __init__(self, name):
        self.name = name

class City(Square):

    def __init__(self, name, price):
        super().__init__(name)
        self.price = price
        self.tax = price//5
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


    
    def action(self, player, player_list):
        """Takes all the appropriate actions on reaching a City"""
        if self.color == WHITE and player.balance >= self.price:
            clear_top_message()
            write_top_message("{}, do you want to buy {} ? (Y / N)".format(player.name, self.name))
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
        elif player.player_color != self.color and self.color != WHITE:
            if player.balance >= self.tax:

                player.balance -= self.tax
                
                for i in player_list:
                    if i.player_color == self.color:
                        i.balance += self.tax
                        break
                
                pygame.time.Clock().tick(1)
                player.update_balance()
                i.update_balance()
                clear_top_message()
                write_top_message("{} paid rs. {} to {} in city {}".format(player.name, self.tax, i.name, self.name))
                pygame.time.Clock().tick(0.33)
                # receiving_player = find_player_by_color(self.color)

                # player.balance -= tax
                
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
        super().__init__('START')
        self.increment = increment

    def draw_square(self, pos_x, pos_y):
        pygame.draw.rect(DISPLAY, BLACK, (pos_x, pos_y, 120, 120), 1)
        namesurface = myfont.render(self.name, True, (0, 0, 0))
        DISPLAY.blit(namesurface, (pos_x + 10, pos_y + 40))
    
    def action(self, player, player_list):
        player.balance+=100

class RestHere(Square):

    def __init__(self):
        super().__init__('Rest Here')

    def draw_square(self, pos_x, pos_y):
        pygame.draw.rect(DISPLAY, BLACK, (pos_x, pos_y, 120, 120), 1)
        namesurface = myfont.render(self.name, True, (0, 0, 0))
        DISPLAY.blit(namesurface, (pos_x + 10, pos_y + 40))

        REST_IMAGE = pygame.image.load(r'./assets/rest_image.png', )
        REST_IMAGE_SMALL = pygame.transform.smoothscale(REST_IMAGE, (100, 70))
        DISPLAY.blit(REST_IMAGE_SMALL, (pos_x + 10, pos_y + 60))
    
    def action(self, player, player_list):
        pass

class Surprise(Square):

    def __init__(self):
        super().__init__('Surprise')

    def draw_square(self, pos_x, pos_y):
        pygame.draw.rect(DISPLAY, BLACK, (pos_x, pos_y, 120, 120), 1)
        namesurface = myfont.render(self.name, True, (0, 0, 0))
        DISPLAY.blit(namesurface, (pos_x + 10, pos_y + 40))

        SURPRISE_IMAGE = pygame.image.load(r'./assets/surprise_image.png', )
        SURPRISE_IMAGE_SMALL = pygame.transform.smoothscale(SURPRISE_IMAGE, (80, 50))
        DISPLAY.blit(SURPRISE_IMAGE_SMALL, (pos_x + 10, pos_y + 70))
    
    def action(self, player, player_list):
        
        surprise_number = random.randint(1,2)

        if surprise_number == 1:
            clear_top_message()
            write_top_message("SURPRISE ! Give 100 rs. to Bank")
            pygame.time.Clock().tick(0.5)
            player.balance -= 100
            player.update_balance()
        elif surprise_number == 2:
            clear_top_message()
            write_top_message("SURPRISE ! You received 200 rs. from Bank")
            pygame.time.Clock().tick(0.5)
            player.balance += 200
            player.update_balance()
    
class Jail(Square):

    def __init__(self, penalty):
        super().__init__('Jail')
        self.penalty = penalty

    def draw_square(self, pos_x, pos_y):
        pygame.draw.rect(DISPLAY, BLACK, (pos_x, pos_y, 120, 120), 1)
        namesurface = myfont.render(self.name, False, (0, 0, 0))
        DISPLAY.blit(namesurface, (pos_x + 10, pos_y + 40))

        SURPRISE_IMAGE = pygame.image.load(r'./assets/jail_image.png', )
        SURPRISE_IMAGE_SMALL = pygame.transform.smoothscale(SURPRISE_IMAGE, (80, 40))
        DISPLAY.blit(SURPRISE_IMAGE_SMALL, (pos_x + 10, pos_y + 70))


    def action(self, player, player_list):
        
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

