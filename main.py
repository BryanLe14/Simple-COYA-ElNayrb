"""
This is a simple Choose Your Own Adventure Game

Things we need to program:
1. Player 
    - Health ✅
    - Movement ✅
    - Name ✅
    - Appearance/Traits (charisma, etc.) ✅
    - Attack power/weapon ✅
    - Money
2. NPCs ✅
3. Enemies ✅
4. ASCII map ✅
5. Quests (find key, fall in love)
6. Shop (items for sell)
7. Emoji map
8. Battle system
9. In-Game Display (Textualize and/or Rich)
10. Menus
11. Inn/sleep/heal
12. Use potions
13. Fog of War
14. Progression (open-world, linear like Zelda, branching paths like FTL sectors)
15. getkey for automatic key press recognition without the need to press ENTER
16. Save progress

"""

__author__ = "Mr McGarrah's 7th Period"
__version__ = "0.1"

from os import system
from functions import *
from classes import *
from getkey import getkey, keys
import time
from universal_globals import (width, height, width2, height2, floorwidth2, floorheight2, clear_screen, constrain, enter_to_continue)


# World map and player starting location
world = [
        "######################",
        "#    K           S   #",
        "#                    #",
        "# HP                 #",
        "#           L        #",
        "#                    #",
        "#                    #",
        "#        C           #",
        "# S                  #",
        "#               B    #",
        "#    C               #",
        "######################"
    ]
# Makes a fog world map
fog_world = ["/" * len(x) for x in world]

"""Add the ability to toggle map reveal"""
keep_fog_off = False
if not keep_fog_off:
    fog = fog_world

items = {}
for row in range(len(world)):
    for i, item in enumerate(world[row]):
        if item not in items:
            items[item] = [(row, world[row].index(item))]
        elif item in items:
            items[item].append((row, i))

location = list(items["P"][0])

def main(world, fog_world, items, location) -> None:    
    """ Main entry point for the game """
    while True:
        print("Love and Legends")
        print("""

        """)
        print("[S]tart New Game")
        print("[C]ontinue Old Game")
        start = input("> ")
        if start.upper() == "S":
            player = create_player()
            break
        elif start.upper() == "C":
            print("Load game code will go here")
            print("Press [C] to continue")
            input()
            break
        clear_screen()


        
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
    
    # Create characters, NPCs, and enemies
    name = "Trevor"
    gender = "male"
    attraction = "female"
    player = Player(name, gender, attraction)
    
    while True:
        system("clear")
        row, col = location

        """Switch between fog modes"""
        if keep_fog_off:
            fog_world = remove_fog(fog_world, items, location)
        else:
            fog_world = remove_fog(fog, items, location)
        
        fog_world = remove_fog(fog_world, items, location)
            
        print_map(emoji_map(fog_world))
        
        world_list = map2dlist(fog_world)
        
        direction = getkey()
        world_list, location, items = check_collision(direction, world_list, location, items)
        fog_world = list2ascii(world_list)

if __name__ == "__main__":
    """ This is executed when the file is run from the command line """
    main(world, fog_world, items, location)
    # import shop
    # store = shop.Shop([
    #     # [name, cost, supply]
    #     ['sword', 1000, 1],
    #     ['arrows', 10, 100000],
    # ])
    # store.buy()
