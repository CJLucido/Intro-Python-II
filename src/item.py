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