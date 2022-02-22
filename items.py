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
    
short_sword = Item("Short Sword",random.randint(3,6),0,50,6)
leather_whip = Item("Leather Whip",random.randint(2,4),0,25,1)
leather_breastplate = Item("Leather Breastplate",0,random.randint(4,8),35,6)
wizards_staff = Item("Wizards Staff",random.randint(12,20),0,300,4)
cloth_robes = Item("Cloth Robes",0,random.randint(1,3),15,1)
