import random

class Item(): # name, damage, armor, price, weight
    def __init__(self,name,dmg_value,ar_value,gp_value,weight):
        self.name = name
        self.dmg_value = dmg_value
        self.ar_value = ar_value
        self.gp_value = gp_value
        self.weight = weight
    
    def status(self):
        print(self.name)
        print("Damage: {}".format(self.dmg_value))
        print("Armour rating: {}".format(self.ar_value))
        print("Value: {} GP".format(self.gp_value))
        print("Weight: {}".format(self.weight))

class Lootbox():
    def __init__(self,name,items,weapons,armors,flavor_text):
        self.name = name
        self.items = []
        self.weapons = []
        self.armors = []
        self.flavor_text = flavor_text



#######--------------Items----------------
fist = Item("Fists",1,0,0,0)
cloth_shirt = Item("Cloth Shirt",0,2,3,0.2)
teeth = Item("Sharp Teeth",1,0,0,0)
rat_tail = Item("Rat Tail",0,0,6,0.1)
boots = Item("Leather Boots",0,2,15,1)
wooden_club = Item("Wooden Club",4,0,25,4)
short_sword = Item("Short Sword",random.randint(3,6),0,50,6)
leather_whip = Item("Leather Whip",random.randint(2,4),0,25,1)
leather_breastplate = Item("Leather Breastplate",0,random.randint(4,8),35,6)
leather_pants = Item("Leather Britches",0,3,20,4)
wizards_staff = Item("Wizards Staff",random.randint(12,20),0,300,4)
cloth_robes = Item("Cloth Robes",0,random.randint(1,3),15,1)
ruby = Item("Ruby",0,0,75,0.1)
weapon_list = [short_sword,leather_whip]
armor_list = [cloth_robes,leather_breastplate,boots,leather_pants]

#######-------------Lootboxes (searchable)------------------------
manure_pile = Lootbox("Pile of Manure",[],[],[boots],"Grimacing, you reach in and check if anything is inside")
wood_chest = Lootbox("Wooden Chest",[],[weapon_list[random.randint(0,1)]],[armor_list[random.randint(0,3)]],"""
The hinges creak as you lift open the lid""")