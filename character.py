import random
from items import *

class Character():
    def __init__(self,name,pos_x,pos_y,level,max_hp,str,dex,wis,gp,xp,items,weapons,armors,dialog):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.level = level
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.str = str
        self.dex = dex
        self.wis = wis
        self.gp = gp
        self.xp = xp
        self.items = items
        self.weapons = weapons
        self.armors = armors
        self.dialog = dialog
        self.dmg = self.weapons[0].dmg_value
        self.ar = self.armors[0].ar_value

    def status(self):
        print(self.name)
        print("X:{}".format(self.pos_x))
        print("Y:{}".format(self.pos_y))
        print("Level: {}".format(self.level))
        print("HP: {}".format(self.hp))
        print("STR: {}".format(self.str))
        print("DEX: {}".format(self.dex))
        print("WIS: {}".format(self.wis))
        print("DMG: {}".format(self.dmg))
        print("ARMOUR:{}".format(self.ar))
        print("GP:{}".format(self.gp))
        print("XP:{}".format(self.xp))
        print("Items in inventory:",*self.items, sep="\n")
        print("Weapons in inventory:",*self.weapons, sep="\n")
        print("Armor in inventory:",*self.armors, sep="\n")
    
    def roll_die(self,die):
        roll = random.randint(0,die)
        print("{} rolls: {}".format(self.name,roll))
    # Character - name,x,y,level,hp,str,dex,wis,gp,xp,items,weapons,armors,dialog
mule = Character("Old Mule",0,0,1,2,4,1,0,0,2,[],[teeth],[boots],"Hee-Haw")
baby_goblin = Character("Baby Goblin",0,0,1,4,2,1,0,5,3,[ruby],[short_sword],[leather_breastplate],"Eeek! Don't hurt me!")   
friendly_wizard = Character("Friendly Wizard",0,0,10,200,15,15,200,100,150,[],[wizards_staff],[cloth_robes],"Hello, I'm a friendly wizard")