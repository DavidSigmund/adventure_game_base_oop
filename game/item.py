# Defined a class for Items
# Expand items with superpower actions
class Item:
    def __init__(self, name, description, damage=0, armor=0, healing=0):
        self.name = name
        self.description = description
        self.damage = damage
        self.armor = armor
        self.healing = healing

    def __str__(self):
        return f"{self.name} - {self.description}"
