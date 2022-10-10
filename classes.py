class Player:
    # def __init__(self, name, attack = {"fist":10}, love = 5, health = 100):
    def __init__(self, name, gender, attr, gold=15, fame=5, love = 5, weapon = None, health = 100, inventory=[], gen=1):
        self.name = name
        self.gender = gender
        self.attr = attr
        self.gold = gold
        self.fame = fame
        self.love = love
        self.weapon = weapon
        self.health = health
        self.gen = gen
        self.inventory = inventory

    def change_weapon(self, weapon):
        self.weapon = weapon
        
    def update_inventory_item(self, name, amount):
        if name in self.inventory:
            self.inventory[name] += amount
        else:
            self.inventory.update({name: amount})
    
    
    def set_inventory_item(self, name, amount):
        if name in self.inventory:
            self.inventory[name] = amount
        else:
            self.inventory.update({name: amount})

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0

    # method to add/subtract quantity of item
    def change(self, quantity):
        self.quantity = self.quantity + quantity

        

class Weapon(Item):
    def __init__(self, name, price, attack, range=False):
        # inherit name and price for the Item superclass 
        super().__init__(name, price)
        self.attack = attack
        self.range = range


class Potion(Item):
    def __init__(self, name: str, price: int, effect: str, amount = 0):
        super().__init__(name, price)
        self.effect = effect
        self.amount = amount
