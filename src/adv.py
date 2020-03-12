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
    'sword_of_unyielding_effort' : Item("sword_of_unyielding_effort", """Permanently destroy what it cuts into, effects may be delayed"""),
    'wandering_wand' : Item("wandering_wand", """sheds new information on situations with relavent examples from far off places"""),
    'deadman\'s_shield' : Item("deadman\'s_shield", """Doesn\'t work too well"""),
    'rusty_key' : Item("rusty_key", """Probably useless, maybe rub the rust on your clothes to slow mold grow for when you die here."""),
    'busted_chandelier' : Item("busted_chandelier", """sharp glass, too sharp to touch"""),
    'theives_decoder_ring' : Item("theives_decoder_ring", """The theif on the team that pillaged this place must have dropped it. It's gold but probably worth more than that."""),
    'herbal_medicine_root' : Item("herbal_medicine_root", """Found on high cliffs and other dangerous spots for the irony"""),
    'Immigrating_coin' : Item("Immigrating_coin","""This type of coin was made from strange and famous meteor! And it is element more rare and valuable than gold! you can hear a vibration if you put it near your ear.""")
}


# Add items to rooms

    # outside
room['outside'].storeInThatRoom(items['sword_of_unyielding_effort'].name, items['sword_of_unyielding_effort'].descr)
room['outside'].storeInThatRoom(items['deadman\'s_shield'].name, items['deadman\'s_shield'].descr)
    # foyer
room['foyer'].storeInThatRoom(items['rusty_key'].name, items['rusty_key'].descr)
room['foyer'].storeInThatRoom(items['busted_chandelier'].name, items['busted_chandelier'].descr)
    #treasure room
room['treasure'].storeInThatRoom(items['theives_decoder_ring'].name, items['theives_decoder_ring'].descr)
    #overlook
room['overlook'].storeInThatRoom(items['herbal_medicine_root'].name, items['herbal_medicine_root'].descr)
    #narrow
room['narrow'].storeInThatRoom(items['Immigrating_coin'].name, items['Immigrating_coin'].descr)

# Main
#
# DESCRIPTIVE CHANGE from CJ to player_one
player_one = Player("Carlo", room['outside'])

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

#DESCRIPTIVE CHANGE from going_toward (started with directionality)
player_action = input("\r\nWhat do you want to do? \r\n\nGo [n] [s] [e] or [w] \r\nCheck Inventory [i] or [inventory] \r\n[take] or [get] \"item\" \r\n[drop] \"item\" \r\n[q]uit the game :") #split on this was delaying my ability to go north from instatiation room..was changing the value of single value commands

while not player_action == "q": 
    #DRY CHANGE changed from the following with lines 3 and 4 repeated for every direction
    # if player_action not in ["n", "s", "e", "w"]:
    #     print("there's nutin o'er yonder!!")
        # elif player_action == "s" and player_one.current_room.s_to != "default":
    #     player_one.current_room = player_one.current_room.s_to
    isItemAction = player_action.split(" ")
    #READABILITY CHANGE from just using isItemAction[1] in code
    if len(isItemAction) > 1:
        item_key = isItemAction[1]
    
    if len(isItemAction) > 1 and isItemAction[0] in ["get", "take"] and item_key in player_one.their_current_room.items.keys():
        try:
            #READABILITY CHANGE keyValue = player_one.their_current_room.items.pop(item_key)
            keyValue = player_one.their_current_room.removeFromThatRoom(item_key)

            player_one.addToInventory(item_key, keyValue)

            items[item_key].on_take(item_key)

            # OPP BP CHANGE print(f"{item_key} added to {player_one.name}'s' inventory")
        except KeyError:
            print("This room doesn't contain that item.")
    elif len(isItemAction) > 1 and isItemAction[0] == "drop":
        try:
            #READABILITY CHANGE from keyValue = player_one.inventory.pop(item_key)
            keyValue = player_one.removeFromInventory(item_key)

            player_one.their_current_room.storeInThatRoom(item_key, keyValue)

            items[item_key].on_drop(item_key)

            print(f"{item_key} dropped in {player_one.their_current_room.name}")
        except KeyError:
            print("No such item in inventory.")
    #ISSUE direction list below not very maintainable, if I want to change the controls I have to change it in both player and room classes as well as here
    elif player_action in ["n", "s", "e", "w"] and getattr(player_one.their_current_room, f"{player_action}_to") != "default":
        #READABILITY CHANGE player_one.their_current_room = getattr(player_one.their_current_room, f"{player_action}_to")
        player_one.movePlayer(player_one.their_current_room, f"{player_action}_to")

        player_one.describesLocation()
    elif player_action == "i" or player_action == "inventory":
        #OOP BEST PRACTICE CHANGE from print(f"\r\nInventory: {player_one.inventory}")
        player_one.listInventory()
    else:  
        #This OK, I want the world to enforce some rules
        print("\r\nThere's nutin o'er yonder!! \r\nWhat exactly are you trying to do!??!")

    #OPP and READABILITY following moved to nsew elif print(f"\r\nCurrent Location: \r\n\n{player_one.their_current_room.name} \r\n\n{player_one.current_room.descr} \r\n\nItems:{player_one.current_room.items}\r\n\n")
    # ^^^ also solves the display issue of showing current location for every action
    player_action = input("\r\nWhat do you want to do? \r\n\nGo [n] [s] [e] or [w] \r\nCheck Inventory [i] or [inventory] \r\n[take] or [get] \"item\" \r\n[drop] \"item\" \r\n[q]uit the game :")
   
print(f"{player_one.name} quit the game")


