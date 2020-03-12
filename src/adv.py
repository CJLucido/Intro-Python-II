from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
#           |ovlk|trsr|
#           | foy|nrrw|
#           | out|

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Create Items

items ={
    'sword' : Item("sword_of_unyielding_effort", """Permanently destroy what it cuts into, effects may be delayed"""),
    'wand' : Item("wandering_wand", """sheds new information on situations with relavent examples from far off places"""),
    'shield' : Item("deadman\'s_shield", """Doesn\'t work too well"""),
    'key_rust' : Item("rusty_key", """Probably useless, maybe rub the rust on your clothes to slow mold grow for when you die here."""),
    'chandelier' : Item("busted_chandelier", """sharp glass, too sharp to touch"""),
    'decoder_ring' : Item("theives_ring", """The theif on the team that pillaged this place must have dropped it. It's gold but probably worth more than that."""),
    'med_root' : Item("herbal_root", """Found on high cliffs and other dangerous spots for the irony"""),
    'rarest_coins' : Item("Immigrating_coin","""This type of coin was made from strange and famous meteor! And it is element more rare and valuable than gold! you can hear a vibration if you put it near your ear.""")
}


# Add items to rooms

    # outside
room['outside'].storeInRoom(items['sword'].name, items['sword'].descr)
room['outside'].storeInRoom(items['shield'].name, items['shield'].descr)
    # foyer
room['foyer'].storeInRoom(items['key_rust'].name, items['key_rust'].descr)
room['foyer'].storeInRoom(items['chandelier'].name, items['chandelier'].descr)
    #treasure room
room['treasure'].storeInRoom(items['decoder_ring'].name, items['decoder_ring'].descr)
    #overlook
room['overlook'].storeInRoom(items['med_root'].name, items['med_root'].descr)
    #narrow
room['narrow'].storeInRoom(items['rarest_coins'].name, items['rarest_coins'].descr)

# Main
#
CJ = Player("Carlo", room['outside'])

# 4 cardinal direction INPUT pass to room instance
# if the room > 0 then pass the room to the player elif n_to == 0 then return "there's nothing over there try again" and input
#     n_to
#     e_to
#     s_to
#     w_to
#     they PRINT the player's NAME and current ROOM
#     they PRINT error IF string does not equal n, s, e, or w 
#     they PRINT error IF room does not exist

# user inputs n 
#     north exists so room.n_to returns viable room to adv condition
#         the loop updates the player's current_room with that variable
#             the adv.py REPL prints the player's name and current_room

going_toward = input("\r\nWhat do you want to do? \r\n\nGo [n] [s] [e] or [w] \r\nCheck Inventory [i] or [inventory] \r\n[take] or [get] \"item\" \r\n[drop] \"item\" \r\n[q]uit the game :") #split on this was delaying my ability to go north from instatiation room..was changing the value of single value commands

while not going_toward == "q": 
    # changed from the following with lines 3 and 4 repeated for every direction
    # if going_toward not in ["n", "s", "e", "w"]:
    #     print("there's nutin o'er yonder!!")
        # elif going_toward == "s" and CJ.current_room.s_to != "default":
    #     CJ.current_room = CJ.current_room.s_to
    isItemAction = going_toward.split(" ")
    
    if len(isItemAction) > 1 and isItemAction[0] in ["get", "take"]:
        pass
    elif len(isItemAction) > 1 and isItemAction[0] == "drop":
        pass   
    elif going_toward in ["n", "s", "e", "w"] and getattr(CJ.current_room, f"{going_toward}_to") != "default":
        CJ.current_room = getattr(CJ.current_room, f"{going_toward}_to")
    elif going_toward == "i" or going_toward == "inventory":
        print(f"\r\nInventory: {CJ.inventory}")
    else:  
        print("\r\nThere's nutin o'er yonder!! \r\nWhat exactly are you trying to do!??!")

    print(f"\r\nCurrent Location: \r\n\n{CJ.current_room.name} \r\n\n{CJ.current_room.descr} \r\n\nItems:{CJ.current_room.items}\r\n\n")
    going_toward = input("which direction are you headed? ")

# Make a new player object that is currently in the 'outside' room.

print(f"{CJ.name} quit the game")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
