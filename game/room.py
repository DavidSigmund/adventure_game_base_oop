import json
import random
from .item import Item

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
        # get rooms and items from json file
        roomsFilePath = 'libraries/rooms.json'
        with open(roomsFilePath, 'r') as file:
            rooms = json.load(file)

        itemsFilePath = 'libraries/items.json'
        with open(itemsFilePath, 'r') as file:
            items = json.load(file)


        # get random rooms out json file
        name = random.choice(list(rooms['rooms']))
        description = rooms['rooms'][name]['description']

        # make the room
        newRoom = Room(name, description, x=x, y=y)

        # choose if room has item
        if random.random() < rooms['rooms'][name]['hasItemProbability']:
            # create item
            itemName = random.choice(list(items['weapons']))
            itemDetails = items['weapons'][itemName]
            item = Item(itemName, itemDetails['description'])

            #add item
            newRoom.add_item(item)


        return newRoom
        #noitem


    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def __str__(self):
        return f"{self.name}\n\n{self.description}\n"
