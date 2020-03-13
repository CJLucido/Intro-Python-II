# Write a class to hold player information, e.g. what room they are in
# currently.

# NAME
# CURRENT_ROOM - change ROOM STATE based on what it is passed from adv.py 
#     initialize with default value of outside room - will have to be done when initializing object
#   

# add inventory list of items

class Player:
    def __init__(self, name, their_current_room, their_worth):
        self.name = name
        #READABILITY CHANGE from current_room
        self.their_current_room = their_current_room
        self.inventory = {}
        self.their_worth = their_worth
    def addToInventory(self, key, value):
        if key not in self.inventory.keys():
            self.inventory[key] = value
            print(f"{key} added to {self.name}'s' inventory")
        else:
            print("You already have one of those!")
    # READABILITY CHANGE and OOP BEST PRACTICE (player does the thing, not the game loop)
    def movePlayer(self, their_current_room, direction_to):
        self.their_current_room = getattr(their_current_room, direction_to)
    # could put describe location in movePlayer but not as readable
    def describesLocation(self):
        print(f"\r\nCurrent Location: \r\n\n{self.their_current_room.name} \r\n\n{self.their_current_room.descr} \r\n\nItems:{self.their_current_room.items}\r\n\n ---------------------------------------------- \r\n\n")
    def removeFromInventory(self, key):
        return self.inventory.pop(key)
    #OOP BEST PRACTICE player lists the inventory, not the game loop
    def listInventory(self):
        print(f"\r\nInventory: {self.inventory}")