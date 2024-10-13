import json
import random
from .item import Item
from .enemy import Enemy

class Room:
    def __init__(self, name, description, x=0, y=0):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.enemies = []
        self.x = x
        self.y = y

    def generate_room(x, y):
        # get rooms, items and enemies from json file
        roomsFilePath = 'libraries/rooms.json'
        with open(roomsFilePath, 'r') as file:
            rooms = json.load(file)

        itemsFilePath = 'libraries/items.json'
        with open(itemsFilePath, 'r') as file:
            items = json.load(file)

        enemiesFilePath = 'libraries/enemies.json'
        with open(enemiesFilePath, 'r') as file:
            enemies = json.load(file)


        # get random rooms out json file
        name = random.choice(list(rooms['rooms']))
        description = rooms['rooms'][name]['description']

        # make the room
        newRoom = Room(name, description, x=x, y=y)

        # choose if room has weapon
        if random.random() < rooms['rooms'][name]['hasItemProbability']:

            # randomly choose what kind of item to add
            item_type = random.choice(['weapon', 'healing', 'armor'])

            # create item
            itemName = random.choice(list(items[item_type]))
            itemDetails = items['weapons'][itemName]
            if item_type == 'weapong':
                item = Item(itemName, itemDetails['description'], itemDetails['damage'])
            elif item_type == 'healing':
                item = Item(itemName, itemDetails['description'], itemDetails['healing'])
            elif item_type == 'armor':
                item = Item(itemName, itemDetails['description'], itemDetails['armor'])

            #add item
            newRoom.add_item(item)

        # choose if to add enemy
        if random.random() < rooms['rooms'][name]['spawnsEnemyProbability']:
            #create enemy
            enemyName = random.choice(list(enemies['enemies']))
            enemyDetails = enemies['enemies'][enemyName]
            enemy = Enemy(enemyName, enemyDetails['description'], enemyDetails['weapon'], enemyDetails['health'])

            # add enemy
            newRoom.add_enemy(enemy)

        return newRoom

    # enemies
    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    # items
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def __str__(self):
        return f"{self.name}\n\n{self.description}\n"
