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

    def __init__(self, name, charisma=5, health=100):
        self.name = name
        self.charisma = charisma
        self.health = health


def main() -> None:
    """ Main entry point for the game """
    player = Character(name="Player", health=200)
    shopkeeper = Character(name="Keeper of Shops")
    print(shopkeeper.name)
    print(shopkeeper.health)


if __name__ == "__main__":
    """ This is excecuted when the file is run from the command line """
    main()
