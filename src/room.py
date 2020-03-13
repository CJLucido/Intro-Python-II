# Implement a class to hold room information. This should have name and
# description attributes.

# NAME 
# DESCRIPTION 
# 4 cardinal direction attrs
#     n_to - holds the room set on adv.py or a default which will return an error on adv.py
#     e_to - if default return 0 trigger adv error
#     s_to
#     w_to

# add list of items to room

class Room:
    def __init__(self, name, descr):
        self.name = name
        self.descr = descr
        self.n_to = "default"
        self.s_to = "default"
        self.e_to = "default"
        self.w_to = "default"
        self.items = {}
    #READABILITY CHANGE added That to storeInRoom and removeFromRoom
    def storeInThatRoom(self, key, value):
        if key not in self.items.keys():
            self.items[key] = value
    def removeFromThatRoom(self, key):
        if key in self.items.keys():
            return self.items.pop(key)