"""
This is a simple Choose Your Own Adventure Game

Things we need to program:
1. Player
  - Health
  - Movement
  - Name
  - Appearance/traits (charisma, etc.)
  - Attack power/weapon
2. NPCs
3. Enemies/boss
4. ASCII map
5. Quests
"""

__author__ = "Mr. McGarrah's 7th Period"
__version__ = "0.1"


class Character:

    def __init__(self, name, attack={"fist": 10}, charisma=5, health=100):
        self.name = name
        self.charisma = charisma
        self.health = health
        self.attack = attack

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.type = type

class Weapon(Item):
    def __init__(self, name, price, attack, range=False):
        Item.__init__(self, name, price)
        self.attack = attack
        self.range = range

def main() -> None:
    """ Main entry point for the game """
    #  Create characters, NPCs, and enemies
    player = Character(name="Player", health=200)
    shopkeeper = Character(name="Keeper of Shops")
    thief = Character(name="Zaam", attack={"dagger": 20})
    print(shopkeeper.name)
    print(shopkeeper.health)


if __name__ == "__main__":
    """ This is excecuted when the file is run from the command line """
    main()
