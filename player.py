import random, time


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
        self.dmg = None
        self.items = []
        self.weapons = []
        self.armors = []
            
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
        print("Damage:",self.dmg)
        print("Items in inventory:")
        print(*self.items, sep="\n")
        print("Weapons in inventory:")
        print(*self.weapons, sep="\n")
        print("Armor in inventory:")
        print(*self.armors, sep="\n")

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
            self.name = self.user_input()
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

    
    def user_input(self):
        user_input = input(">>>:").upper()
        return user_input

player = Player()
player.create()