from items import *
from character import *

class Room():
    def __init__(self,name,desc,pos_x,pos_y,items,weapons,armors,npcs,enemies):
        self.name = name
        self.desc = desc
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.items = items
        self.weapons = weapons
        self.armors = armors
        self.npcs = npcs
        self.enemies = enemies

    def status(self):
        print(self.name)
        print(self.desc)
        print("X: ",self.pos_x)
        print("Y: ", self.pos_y)
        print("Looking around this room, you see:")
        for item in self.items:
            print(item.name)
        for weapon in self.weapons:
            print(weapon.name)
        for armor in self.armors:
            print(armor.name)
        for npc in self.npcs:
            print(npc.name)
        for enemy in self.enemies:
            print(enemy.name)

###    name , desc , x, y, items, weapons, armor, npcs, enemies
start_room = Room("Starting Room","""
This is the room you started in, i will fill this with stuff later
""",0,0,[ruby],[leather_whip,short_sword],[leather_breastplate],[friendly_wizard],[])
goblin_room = Room("Goblin room","""
A room full of goblins""",1,0,[],[],[],[],[baby_goblin,baby_goblin,baby_goblin])
treasure_room = Room("Treasure Room","""
A room full of rubies""",0,1,[ruby,ruby,ruby],[],[],[],[])

