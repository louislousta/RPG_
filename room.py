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
start_room = Room("Old Stable","""
A wooden stable. You woke up here. There is a mule in the corner eating hay, 
and a bloodstain on the floor where you were lying. The door is to the north.  
""",0,0,[],[],[],[mule],[])
courtyard = Room("Tavern Courtyard","""
The courtyard of a tavern. The yard is paved with cobbles and filthy with mud. To the east
lies the tavern itself, where you can here the sounds of drinking and merriment. 
To the north is a high stone wall, green with moss and ivy. 
To the west lies the open road. 
To the south is the stable where you woke up. A short sword is propped up against the wall, 
probably left there by one of the patrons of the tavern""",0,1,[],[short_sword],[],[],[])



