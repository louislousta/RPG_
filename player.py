import random, time
from items import *


class Player():
    def __init__(self):
        self.name = None
        self.pos_x = 0
        self.pos_y = 0
        self.level = None
        self.max_hp = None
        self.hp = self.max_hp
        self.str = None
        self.dex = None
        self.wis = None
        self.xp = 0
        self.gp = 0
        self.items = []
        self.weapons = [fist]
        self.armors = [cloth_shirt]
        self.dmg = self.weapons[0].dmg_value
        self.ar = self.armors[0].ar_value

    


    def status(self):
        print(self.name)
        print("X:",self.pos_x)
        print("Y:" , self.pos_y)
        print("Level:",self.level)
        print("Max HP:",self.max_hp)
        print("Current HP:",self.hp)
        print("Strength:",self.str)
        print("Dexterity", self.dex)
        print("Wisdom:",self.wis)
        print("XP:",self.xp)
        print("GP:",self.gp)
        print("Items in inventory:")
        for item in self.items:
            print(item.name)
        print("Weapons in inventory:")
        for weapon in self.weapons:
            print(weapon.name)        
        print("Armor in inventory:")
        for armor in self.armors:
            print(armor.name)

    def roll_die(self,die):
        roll = random.randint(1,die)
        print(self.name, " rolls ",roll)
        return roll
    def create(self):
        self.status()
        print("Create your character:")
        print("(N)ame")
        print("(R)oll stats")
        print("(P)lay the game")
        choice = self.user_input()
        if choice == "N":
            print("Enter your name:")
            self.name = self.user_input(char=False)
            self.create()
        elif choice == "R":
            print("Rolling {}'s stats".format(self.name))
            print("Rolling HP...")
            self.max_hp = self.roll_die(20)
            self.hp = self.max_hp
            print("Rolling Strength...")
            self.str = self.roll_die(100)
            print("Rolling Dexterity...")
            self.dex = self.roll_die(100)
            print("Rolling Wisdom...")
            self.wis = self.roll_die(100)
            self.create()
        elif choice == "P":
            print("Entering game")
            if (self.name == None) or (self.hp == 0):
                print("Please finish creating your character...") 
                self.create() 
            
        else: 
            print("Not a valid choice! Please enter N, R or P")
            self.create()
    

    def user_input(self, char=True, num=False):
        user_input = input(">>>:").upper()
        if num:
            try:
                user_input = int(user_input)
            except ValueError:
                print("Not a valid choice!")
            return user_input
        if char:
            return user_input[0]
        else:
            return user_input


