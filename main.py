from player import *
from items import *
from character import *
from room import *

class Game():
    def __init__(self):
        self.name = "GAME "
    def status(self):
        print(self.name + "IS INSTANTIATED")
    
    def grid(self,player):
        print("INSTANTIATE GRID")
        rooms = [start_room,courtyard]
        for room in rooms:
            if (player.pos_x == room.pos_x) and (player.pos_y == room.pos_y):
                room.status()
  
    def move(self,player):
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
    def look(self,player):
        pass
    def talk(self,player):
        pass
    def options(self,player):
        opt = player.user_input()
        if opt == "M":
            self.move(player)
        elif opt == "H":
            print(help)
        elif opt == "L":
            self.look(player)
        elif opt == "T":
            self.talk(player)
        else: 
            print("Not a valid option, Enter 'H' for help")
            self.options(player)

    def main_loop(self,player):
        self.status()
        player.create()
        while True:
            self.grid(player)
            player.status()
            self.options(player)
help = {"Move":"M","Look":"L","Talk":"T","Help":"H"}
intro_text = ("""You wake, groaning with pain from your aching head. 
You smell the sweet, musty smell of manure and the metallic tang of dried blood in the air.
Where are you? What was your name? How did you end up here? 
You summon your strength and push yourself to your feet, swaying gently. 
Looking around as the fog clears from your eyes you see you are in a stable,
with thick wooden walls and straw underfoot. An old grey mule 
observes you briefly from a corner, then goes back to eating hay. """)


game = Game()
player = Player()
print(intro_text)
game.main_loop(player)
