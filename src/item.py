# NAME - limit of 1 word
# DESCR


class Item:
    def __init__(self, name, descr):
        self.name = name
        self.descr = descr
    def on_take(self, name):
        print(f"You have picked up {name}")
    def on_drop(self, name):
        print(f"You have dropped {name}")


class Treasure(Item):
    def __init__(self, name, descr, worth):
        self.worth = worth
        super().__init__(name, descr)
    def changePlayerWorth(self, key, player, player_inventory):
        if key not in player_inventory.keys():
            player.their_worth += self.worth
        else:
            print("There aren\'t two of these!!!! FORGER!!")