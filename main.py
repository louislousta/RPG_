from player import *
from items import *
from character import *
from room import *

class Game():
    def __init__(self):
        self.name = "GAME"
    def status(self):
        print(self.name + "IS INSTANTIATED")
    
    def grid(self,player):
        print("INSTANTIATE GRID")
        rooms = [start_room,goblin_room,treasure_room]
        for room in rooms:
            if (player.pos_x == room.pos_x) and (player.pos_y == room.pos_y):
                room.status()
    
    def options(self,player):
        print("MOVE N, S, E, W")
        dir = player.user_input()
        if dir == "N":
            player.pos_y += 1
        elif dir == "S":
            player.pos_y -= 1
        elif dir == "W":
            player.pos_x -= 1
        elif dir == "E":
            player.pos_x += 1
        else:
            print("INVALID CHOICE")
        return
    
    def main_loop(self,player):
        self.status()
        player.create()
        while True:
            self.grid(player)
            player.status()
            self.options(player)



game = Game()
player = Player()

game.main_loop(player)
