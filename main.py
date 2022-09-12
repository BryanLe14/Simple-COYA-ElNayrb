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

    # def __init__(self, name, attack={"fist": 10}, charisma=5, health=100):
    def __init__(self, name, weapon=None, charisma=5, health=100):
        self.name = name
        self.weapon = weapon
        self.charisma = charisma
        self.health = health

    def change_weapon(self, weapon):
        self.weapon = weapon

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.type = type

class Weapon(Item):
    def __init__(self, name, price, attack, range=False):
        super().__init__(name, price)
        self.attack = attack
        self.range = range

class Potion(Item):
    def __init__(self, name: str, price: int, effect: str, amount=0):
        super().__init__(name, price)
        self.effect = effect
        self.amount = amount

def main() -> None:
    """ Main entry point for the game """
    # Create weapons
    sword = Weapon("Toby", 25, 50)
    fist = Weapon("fist", 0, 10)
    dagger = Weapon("Dolly Dagger", 15, 20)
    weapon_list = [sword, fist, dagger]
    
    # Create potions
    health_potion = Potion("Health Potion", 25, "heal", 50)
    poison_potion = Potion("Poison Potion", 35, "poison", 10)
    love_potion = Potion("Love Potion", 50, "love", 25)
    potion_list = [health_potion, poison_potion, love_potion]
    
    #  Create characters, NPCs, and enemies
    player = Character(name="Player", weapon=fist, health=200)
    shopkeeper = Character(name="Keeper of Shops", weapon=sword)
    thief = Character(name="Zaam", weapon=dagger, health=100)

    # Testing functionality
    print(shopkeeper.name)
    print(shopkeeper.weapon.name)
    print(shopkeeper.health)
    print(thief.weapon.name)

    


if __name__ == "__main__":
    """ This is excecuted when the file is run from the command line """
    main()
