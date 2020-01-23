import configs
from board import Board, Player
from configs import *

class Game:

    def __init__(self, count_of_players):
        self.game_board = Board()
        self.count_of_players = count_of_players
        self.player_list = []
        self.player_color_list  = [RED, GREEN, BLUE]

        for i in range(self.count_of_players):
            name = input("Enter Name for Player 1 : ")
            self.player_list.append(Player(name,self.player_color_list[i]))
    
"""need to complete"""