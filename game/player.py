import json
from .room import Room
# Ideas to extend functionality:
# Add health & resource management:
# - add health attribute
# - health decreases when you pass through the fire room
# - health increases when you find a health item
# - use your creativity

# Define a class for the Player
class Player:
    def __init__(self, name, current_room, health=100):
        self.name = name
        self.current_room = current_room
        self.health = health
        self.inventory = []
        self.visited_rooms = {current_room}

    def fightEnemy(self, enemy):
        # Load items from JSON file
        itemsFilePath = 'libraries/items.json'
        with open(itemsFilePath, 'r') as file:
            items = json.load(file)

        # Assuming enemy.weapon is the name of the weapon
        enemy.weaponName = enemy.weapon
        enemy.weapon = items["weapons"].get(enemy.weapon, {"damage": 0})

        print(f"You encountered an {enemy.name}!")

        while enemy.health > 0 and self.health > 0:
            print("\n--- Enemy Stats ---")
            print(f"Name: {enemy.name}")
            print(f"Description: {enemy.description}")
            print(f"Health: {enemy.health}")
            print(f"Enemy has item: {enemy.weaponName} with damage {enemy.weapon['damage']}")

            print("\n--- Player Stats ---")
            print(f"Name: {self.name}")
            print(f"Health: {self.health}")
            self.show_inventory()


            selected_item = None

            # Prompt for item selection
            while not selected_item:
                option = input("Choose your item to use: ").lower()
                for item in self.inventory:
                    if item.name.lower() == option:
                        selected_item = item
                        break

                if selected_item:
                    # Player attacks
                    print(f"You used {selected_item.name} to attack the enemy!")
                    enemy.health -= selected_item.damage
                    print(f"You did {selected_item.damage} damage!")
                    print(f"The {enemy.name} has {enemy.health} health left!")

                    # end the fight if enemy is defeated
                    if enemy.health <= 0:
                        print(f"You defeated the {enemy.name}!")
                        break

                    # Enemy attacks
                    print(f"{enemy.name} used {enemy.weaponName} to attack you!")
                    self.health -= enemy.weapon['damage']
                    print(f"{enemy.name} did {enemy.weapon['damage']} damage!")
                    print(f"You have {self.health} health left!")

                    # End the game if player is defeated
                    if self.health <= 0:
                        print("\033[91mYou have been defeated!\033[0m")
                        exit()
                else:
                    print("You don't have that item in your inventory! Try again.")

        print("Fight ended.")

    def move(self, direction):
        new_x, new_y = self.current_room.x, self.current_room.y
        if direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1
        elif direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        else:
            print("Invalid direction.")
            return

        #if you have been in the room use the existing room
        for room in self.visited_rooms:
            if new_x == room.x and new_y == room.y:
                self.current_room = room
                return

        # otherwise create new room
        self.current_room = Room.generate_room(new_x, new_y)
        self.visited_rooms.add(self.current_room)

        # check for enemy and start fight
        if self.current_room.enemies:
            enemy = self.current_room.enemies[0]
            self.fightEnemy(enemy)

        return



    def pick_up(self, chosen_item_name):
        for item in self.current_room.items:
            if item.name == chosen_item_name:
                self.inventory.append(item)
                self.current_room.remove_item(item)
                print(f"You picked up the {chosen_item_name}.")
                return
        print(f"There is no {chosen_item_name} here.")

    def show_inventory(self):
        if self.inventory:
            print("You are carrying:")
            for item in self.inventory:
                print(f"- {item.name}")
        else:
            print("Your inventory is empty.")

    def show_map(self):
        self.display_map()

    def display_map(self):
        # Determine the bounds of the map
        # Only the discovered rooms will be shown
        min_x = min(room.x for room in self.visited_rooms)
        max_x = max(room.x for room in self.visited_rooms)
        min_y = min(room.y for room in self.visited_rooms)
        max_y = max(room.y for room in self.visited_rooms)

        # Create the map grid
        # Added spaces to determinate the length of the cell
        map_grid = [["      " for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

        # Place rooms in the grid
        for room in self.visited_rooms:
            if room.items:
                map_grid[room.y - min_y][room.x - min_x] = f"[{room.name[:3].upper()}.]"
            else:
                map_grid[room.y - min_y][room.x - min_x] = f"[{room.name[:3].upper()} ]"

        # Display the map
        print("\nMap:")
        for row in map_grid:
            print("".join(row))
        print(f"\nYou are currently in the {self.current_room.name}")
