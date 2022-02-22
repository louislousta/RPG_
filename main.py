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
        for room in rooms:
            if (player.pos_x == room.pos_x) and (player.pos_y == room.pos_y):
                room.status()
                return rooms.index(room)
        print("You can't go that direction!")                 
  
    def move(self,player):
        print("MOVE N, S, E, W. Press X to cancel")
        dir = player.user_input()
        if dir == "N":
            player.pos_y += 1
        elif dir == "S":
            player.pos_y -= 1
        elif dir == "W":
            player.pos_x -= 1
        elif dir == "E":
            player.pos_x += 1
        elif dir == "X":
            self.options(player)
        else:
            print("INVALID CHOICE")
            self.move(player)
        
    def look(self,player):
        pass
    def talk(self,player):
        print("Choose who to talk to:")
        count = 1
        dict = {}
        for npc in rooms[current_room].npcs:
            print(count,":",npc.name)
            dict[count] = npc
            count+=1
        choice = int(player.user_input())
        print(f"{dict[choice].name} says {dict[choice].dialog}")
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
       # player.create()
        while True:
            current_room = self.grid(player)            
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
current_room = 0 # index of rooms list where the player is standing
rooms = [start_room,courtyard]
game = Game()
player = Player()
print(intro_text)
game.main_loop(player)
