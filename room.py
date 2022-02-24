from items import *
from character import *

class Room():
    def __init__(self,name,desc,pos_x,pos_y,items,weapons,armors,lootboxes,npcs,enemies):
        self.name = name
        self.desc = desc
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.items = items
        self.weapons = weapons
        self.armors = armors
        self.lootboxes = lootboxes
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
        for lootbox in self.lootboxes:
            print(lootbox.name)
        for npc in self.npcs:
            print(npc.name)
        for enemy in self.enemies:
            print(enemy.name)


###    name , desc , x, y, items, weapons, armor, npcs, enemies
start_room = Room("Old Stable","""
A wooden stable. You woke up here. There is a mule in the corner eating hay, 
a large pile of manure and a bloodstain on the floor where you were lying. The door is to the north.  
""",0,0,[],[],[],[manure_pile],[mule],[])

courtyard = Room("Tavern Courtyard","""
The courtyard of a tavern. The yard is paved with cobbles and filthy with mud. 
Looking up you see a clear night sky dotted with stars. To the east
lies the tavern itself, where you can hear the sounds of drinking and merriment. 
To the north is a high stone wall, green with moss and ivy. 
To the west lies the open road. 
To the south is the stable where you woke up.""",0,1,[],[short_sword],[],[],[])

tavern = Room("Tavern","""A warm, inviting tavern. The landlord stands behind the bar,
laughing with his patrons. A roaring log fire is blazing and you instantly 
begin to feel more at ease. You should speak to people and try to work out
what happened to you""",1,1,[],[],[],[],[landlord,old_drunk_1,old_drunk_2],[])

tavern_cellar = Room("Tavern Cellar","""Cool and dark, you can see looming hulks 
of ale barrels and various junk the landlord must have been acccumulating 
since he started the place.""",2,1,[],[],[],[wood_chest],[],[rat,rat,rat])

