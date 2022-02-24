from multiprocessing.dummy import current_process
from player import *
from items import *
from character import *
from room import *

class Game():
    def __init__(self):
        self.name = "GAME "
        self.current_room = 0
        self.move_history = []
    def status(self):
        print(self.name + "IS INSTANTIATED")
    
    def grid(self,player):
        print("INSTANTIATE GRID")
        for room in rooms:
            if (player.pos_x == room.pos_x) and (player.pos_y == room.pos_y):
                print(room.name)
                self.current_room = rooms.index(room)             
         

    def battle(self,player):
        def initiative(attacker,defender):
            atk_roll = (attacker.roll_die(100)*attacker.dex)/100
            def_roll = (defender.roll_die(100)*defender.dex)/100
            initiative = max(atk_roll,def_roll)
            if initiative == atk_roll:
                time.sleep(1)
                print(attacker.name," has initiative")
                return attacker
            else:
                time.sleep(1)
                print(defender.name," has initiative")
                return defender

        def attack(attacker,defender):
            print(attacker.name,"is attacking")
            hit = (attacker.roll_die(20)*attacker.dex)/100 > defender.ar
            if hit:
                time.sleep(1)
                print("A good hit!")
                defender.hp -= attacker.dmg
            else:
                time.sleep(1)
                print("Swish... missed!")

        for enemy in rooms[self.current_room].enemies:
            print("You attack ",enemy.name)
            init = initiative(player,enemy)
            while enemy.hp > 0:
                if init == player:
                    attack(player,enemy)
                    init = enemy
                else:
                    attack(enemy,player)
                    init = player
            print("You defeated ",enemy.name)
            self.kill(player,enemy)
            
    def kill(self,player,enemy):
        print(enemy.name," has died")
        xp = enemy.xp
        print(f"You gained {xp} XP")
        player.xp += xp
        gp = enemy.gp
        print(f"You gained {gp} GP")
        player.gp += gp
        for item in enemy.items:
            print(f"{enemy.name} dropped {item.name}")
            rooms[self.current_room].items.append(item)
        for weapon in enemy.weapons:
            print(f"{enemy.name} dropped {weapon.name}")
            rooms[self.current_room].weapons.append(weapon) 
        for armor in enemy.armors:
            print(f"{enemy.name} dropped {armor.name}")
            rooms[self.current_room].armors.append(armor) 
        rooms[self.current_room].enemies.remove(enemy)


            
            





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
    def pickup(self,player):
        print("Choose an item to pick up:")
        count = 1
        dict = {}
        for item in rooms[self.current_room].items:
            print(count,":",item.name)
            dict[count] = item
            count += 1
        for weapon in rooms[self.current_room].weapons:
            print(count,":",weapon.name)
            dict[count] = weapon
            count += 1
        for armor in rooms[self.current_room].armors:
            print(count,":",armor.name)
            dict[count] = armor
            count += 1
        choice = player.user_input(num=True)
        if choice in dict:
            chosen = dict[choice]
            if chosen in rooms[self.current_room].items:
                player.items.append(chosen)
                rooms[self.current_room].items.remove(chosen)
            elif chosen in rooms[self.current_room].weapons:
                player.weapons.append(chosen)
                rooms[self.current_room].weapons.remove(chosen)
            elif chosen in rooms[self.current_room].armors:
                player.armors.append(chosen)
                rooms[self.current_room].armors.remove(chosen)
    def look(self,player):
        pass
    def talk(self,player):
        print("Choose who to talk to:")
        count = 1
        dict = {}
        for npc in rooms[self.current_room].npcs:
            print(count,":",npc.name)
            dict[count] = npc
            count+=1
        choice = player.user_input(num=True)
        if choice in dict:
            print(f"{dict[choice].name} says {dict[choice].dialog}")
        else: 
            print("Not a valid choice!")
            self.talk(player)
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
        elif opt == "P":
            self.pickup(player)
        elif opt == "B":
            self.battle(player)
        else: 
            print("Not a valid option, Enter 'H' for help")
            self.options(player)

    def main_loop(self,player):
        self.status()
        player.create()
        while True:
            self.grid(player)            
            
            self.options(player)
help = {"Move":"M","Look":"L","Talk":"T","P": "Pick up","Help":"H"}
intro_text = ("""You wake, groaning with pain from your aching head. 
You smell the sweet, musty smell of manure and the metallic tang of dried blood in the air.
Where are you? What was your name? How did you end up here? 
You summon your strength and push yourself to your feet, swaying gently. 
Looking around as the fog clears from your eyes you see you are in a stable,
with thick wooden walls and straw underfoot. An old grey mule 
observes you briefly from a corner, then goes back to eating hay. """)

rooms = [start_room,courtyard,tavern,tavern_cellar]
game = Game()
player = Player()
print(intro_text)
game.main_loop(player)
