class Game():
    def __init__(self):
        self.name = "GAME"
    def status(self):
        print(self.name + "IS INSTANTIATED")
    
    def grid(self,player):
        print("INSTANTIATE GRID")
        rooms = [start_room,empty_room]
        for room in rooms:
            if (player.pos_x == room.pos_x) and (player.pos_y == room.pos_y):
                room.status()
    
    def options(self,player):
        print("MOVE N, S, E, W")
        dir = player.user_input()
        if dir == "N":
            player.pos_y += 1
        elif dir == "S":
            player.pos_y -= 1
        elif dir == "W":
            player.pos_x -= 1
        elif dir == "E":
            player.pos_x += 1
        else:
            print("INVALID CHOICE")
        return
    
    def main_loop(self,player):
        self.status()
        while True:
            self.grid(player)
            player.status()
            self.options(player)

class Player():
    def __init__(self):
        self.name = "PLAYER"
        self.pos_x = 0
        self.pos_y = 0
    
    def status(self):
        print(self.name)
        print("X:",self.pos_x)
        print("Y:" , self.pos_y)
    
    def user_input(self):
        user_input = input(">>>:").upper()
        return user_input

class Room():
    def __init__(self,name,desc,pos_x,pos_y):
        self.name = name
        self.desc = desc
        self.pos_x = pos_x
        self.pos_y = pos_y
    def status(self):
        print(self.name)
        print(self.desc)
        print("X: ",self.pos_x)
        print("Y: ", self.pos_y)

game = Game()
player = Player()
start_room = Room("start room","This is the starting room",0,0)
empty_room = Room("empty room","This is an empty room",0,1)

game.main_loop(player)
