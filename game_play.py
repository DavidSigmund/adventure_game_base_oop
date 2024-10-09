from game.room import Room
from game.item import Item
from game.player import Player
from enum import Enum


class Option(Enum):
    MOVE = 1
    PICK_UP = 2
    INVENTORY = 3
    PRINT_MAP = 4
    QUIT = 5

# Game Setup
def setup_game(player_name):
    # Create rooms
    startRoom = Room("elevator",
                   "The start of your journey in this dungeon of mistery.",
                   x=0, y=0)


    # Create a player and start the game in the elevator
    playerInstartRoom = Player(player_name, startRoom)

    return playerInstartRoom


# Main game loop
def play_game(user):
    while True:
        print(f"\n\n{user.name}, you are in the {user.current_room}")
        try:
            command = int(input("Choose an option:"
                            "\n1: move\n2: pick up"
                            "\n3: inventory\n4: display map of discovered rooms"
                            "\n5: quit\n\nOption: "))
        except ValueError:
            print("Invalid input.")
            continue

        if command == Option.MOVE.value:
            direction = input("Provide direction (left|right|up|down): ")
            user.move(direction)
        elif command == Option.PICK_UP.value:
            items = user.current_room.get_items()
            if len(items):
                print("The following items are available: ")
                print("0. I don't want to pick anything up")
                for item in items:
                    print(f"1. {item.name}")
                chosen_item = int(input("Which item would you like to pick up: "))
                if chosen_item != 0:
                    user.pick_up(items[chosen_item - 1].name)
                else:
                    continue
            else:
                print("There are no items available")
        elif command == Option.INVENTORY.value:
            user.show_inventory()
        elif command == Option.PRINT_MAP.value:
            user.display_map()
        elif command == Option.QUIT.value:
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    name = input("What is your name?: ")
    player = setup_game(name)
    play_game(player)
