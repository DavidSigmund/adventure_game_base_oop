import random
# Define a class for Rooms
# Ways to expand:
# - Add a method to add, remove and get enemies
# - Add room interactions, through items, added doors, traps, hidden passages
# - Add NPC (non-playable characters that give hints)
class Room:

    def __init__(self, name, description, x=0, y=0):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.x = x
        self.y = y

    def generate_room(x, y):
        room_type = {"Kitchen": "A dark and dirty room buzzing with flies.",
                     "Ballroom": "A large room with shiny wooden floors; it looks like a nice place to dance.",
                     "Dining Hall": "A vast room with a long table where a feast could be held.",
                     "Library": "A quiet place filled with books",
                     "Bedroom": "A chilly bedroom that looks like a crime scene.",
                     "Garden": "A lush garden full of flowers",
                     "Study": "You've entered a dimly lit Study Room, the scent of old books and parchment filling the air. Who knows what you could find in here?..."}

        name = random.choice(list(room_type.keys()))
        description = room_type[name]
        return [name, description, x, y]

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def __str__(self):
        return f"{self.name}\n\n{self.description}\n"
