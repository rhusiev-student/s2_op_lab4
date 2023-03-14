"""A simple text-based adventure game.

You try to win in a milk, cat and mosquitos fight.
A milk make a cat drown, a cat drinks milk and a mosquito bites a cat.

classes:
    Map
    Game
"""
from random import shuffle

from assets import EndRoom, Enemy, Friend, Item, Player, Room, Weapon

CHANGE = {"north": (0, -1), "south": (0, 1), "east": (-1, 0), "west": (1, 0)}


class Map:
    """A map of the game.

    Attributes:
        rooms (list[list[Room]]): A 2D list of rooms.
        player (Player): The player character.
    """

    def __init__(self, player: Player) -> None:
        """Initialize the map.

        Args:
            player (Player): The player character.
        """
        self.rooms: list[list[Room]] = [[] for _ in range(3)]
        self.player = player
        self.starting_room = Room(
            "Starting Room",
            "You are in the starting room. \
A mosquitto is saying that you should not have drunk the milk.",
        )
        self.starting_room.item = Weapon("mosquitto", "cat")
        self.starting_room.item.picked_up = True
        self.player.weapons.append(self.starting_room.item)
        self.rooms[0].append(self.starting_room)
        room = Room("Room.", "Just a room. Oh look! A cat! It says his name is Mykola")
        room.item = Weapon("cat", "milk")
        self.rooms[0].append(room)
        white_room = Room(
            "A white room",
            "There is a milk that you drank. You can offer it to a cat in the future.",
        )
        white_room.item = Weapon("milk", "mosquitto")
        self.rooms[1].append(white_room)
        other_rooms = [
            Room("A bloody red room", "A bloody room. Ouch, something bit me."),
            Room("A completely empty room", ""),
            Room(
                "A cave",
                "A dark cave. You can hear a HUUGE cat meowing. It wants to eat you.",
            ),
            Room(
                "A smelly room",
                "A smelly room. You can smell a mouse.",
            ),
            Room(
                "A white room",
                "A white room. There is a cat. Oh, no cat... \
This white substance drives you crazy.",
            ),
        ]
        end_room = EndRoom("The last room.", "Here is a cake", 8)
        other_rooms[0].set_character(Enemy("A blood master", Weapon("mosquitto")))
        other_rooms[2].set_character(Enemy("An old babusia with a cat", Weapon("cat")))
        other_rooms[3].set_character(
            Friend(
                "A friendly looking mouse. Not suspicious at all",
                "Hello, my fellow friend, how are you doing? It is a great pleasure to \
meet you. I'm totally not suspicious so go to the next room, quickly!",
            )
        )
        other_rooms[4].set_character(Enemy("Milk", Weapon("milk")))
        end_room.item = Item("cake")
        shuffle(other_rooms)
        self.rooms[0].append(other_rooms[0])
        self.rooms[1] += other_rooms[1:3]
        self.rooms[2] += other_rooms[3:]
        self.rooms[2].append(end_room)
        for i in range(3):
            for j in range(3):
                if j < 2:
                    self.rooms[i][j].add_neighbour("south", self.rooms[i][j + 1])
                if j > 0:
                    self.rooms[i][j].add_neighbour("north", self.rooms[i][j - 1])
                if i < 2:
                    self.rooms[i][j].add_neighbour("west", self.rooms[i + 1][j])
                if i > 0:
                    self.rooms[i][j].add_neighbour("east", self.rooms[i - 1][j])

    def enter_room(self, room_id: tuple[int, int]) -> bool:
        """Enter a room.

        Args:
            room_id (tuple[int, int]): The room's id.

        Returns:
            bool: True if the room was entered, False otherwise.
        """
        if room_id[0] > 2 or room_id[1] > 2 or room_id[0] < 0 or room_id[1] < 0:
            print("You can't go there.")
            print(room_id)
            return False
        room = self.rooms[room_id[1]][room_id[0]]
        print(f"You are entering {room.name}.")
        print(room.description)
        if isinstance(room, EndRoom):
            if room.can_enter(self.player):
                if room not in self.player.cleared_rooms:
                    self.player.clear_room(room)
            else:
                print("You can't go there. You need to clear all the rooms first.")
                return False
        character = room.character
        if character and isinstance(character, Enemy) and not character.defeated:
            print(f"There is a {character.name} in the room.")
            to_fight = input("Do you want to fight? (y/n) ")
            if to_fight == "n":
                return False
            print("You can use the following weapons:")
            for i, weapon in enumerate(self.player.weapons):
                print(f"{i}. {weapon.name}")
            weapon = input("What weapon do you want to use?\n")
            if not weapon.isdigit() or not 0 <= int(weapon) < len(self.player.weapons):
                print("Invalid weapon.")
                return False
            win = self.player.fight(character, int(weapon))
            if not win:
                exit()
            character.defeated = True
        elif room.character and isinstance(room.character, Friend):
            print(room.character.dialogue)
        if room not in self.player.cleared_rooms:
            self.player.clear_room(room)
        if room.item and not room.item.picked_up:
            won = self.player.pick_up_item(room)
            if won:
                exit()
            room.item.picked_up = True
            print(f"You picked up {room.item.name}.")
        return True

    def move(self, direction: str) -> None:
        """Move in a direction.

        Args:
            direction (str): The direction to move in.
        """
        room = self.rooms[self.player.current_room[0]][self.player.current_room[1]]
        if direction not in room.neighbours.keys():
            print("You can't go there.")
            return
        self.player.current_room = (
            self.player.current_room[0] + CHANGE[direction][0],
            self.player.current_room[1] + CHANGE[direction][1],
        )
        result = self.enter_room(self.player.current_room)
        if not result:
            self.player.current_room = (
                self.player.current_room[0] - CHANGE[direction][0],
                self.player.current_room[1] - CHANGE[direction][1],
            )
            return


class Game:
    """A game."""

    def __init__(self) -> None:
        """Initialize the game."""
        self.player = Player("Abdul Ali Al-Ahmed")
        self.map = Map(self.player)

    def start(self) -> None:
        """Start the game."""
        print("You are Abdul Ali Al-Ahmed.")
        print("You are in a dungeon.")
        print("You need to find a cake.")
        print("You have a friendly mosquitto to help in fight.")
        print("Good luck!")
        self.player.clear_room(self.map.rooms[0][0])
        print(self.map.starting_room.description)
        while True:
            print()
            for i, room_line in enumerate(self.map.rooms):
                for j, room in enumerate(room_line):
                    if (j, i) == self.player.current_room:
                        print("♙", end=" ")
                    elif room in self.player.cleared_rooms:
                        print("X", end=" ")
                    else:
                        print("O", end=" ")
                print()
            print()
            print("You can go to the following directions:")
            room = self.map.rooms[self.player.current_room[0]][
                self.player.current_room[1]
            ]
            for direction in room.neighbours:
                print(f"- {direction}")
            direction = input("Where do you want to go?\n")
            self.map.move(direction)


if __name__ == "__main__":
    game = Game()
    game.start()
