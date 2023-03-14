"""A module with classes for the explorer game."""
from __future__ import annotations


class Room:
    """A class for a room in the game.

    Attributes:
        name (str): The name of the room
        description (str): The description of the room
        character (Enemy): The enemy in the room
        linked_rooms (dict[str, Room]): The rooms linked to this room
        item (Item): The item in the room

    Methods:
        set_description: Set the description of the room
        link_room: Link a room to this room
        set_character: Set the character in the room
        set_item: Set the item in the room
        get_character: Get the character in the room
        get_details: Get the details in the room
        get_item: Get the item in the room
    """

    description: str = ""
    character: Enemy | None = None
    item: Item | None = None

    def __init__(self, name: str) -> None:
        self.name = name
        self.linked_rooms: dict[str, Room] = {}

    def set_description(self, description: str) -> None:
        """Set the description of the room.

        Args:
            description (str): The description of the room
        """
        self.description = description

    def link_room(self, room: Room, direction: str) -> None:
        """Link a room to this room.

        Args:
            room (Room): The room to link to
            direction (str): The direction of the room
        """
        self.linked_rooms[direction] = room

    def set_character(self, character: Enemy) -> None:
        """Set the character in the room.

        Args:
            character (Enemy): The character in the room
        """
        self.character = character

    def set_item(self, item: Item) -> None:
        """Set the item in the room.

        Args:
            item (Item): The item in the room
        """
        self.item = item

    def get_character(self) -> Enemy | None:
        """Get the character in the room.

        Returns:
            Enemy | None: The character in the room
        """
        if self.character is None:
            return None
        return self.character

    def get_details(self) -> None:
        """Get the details of the room.

        Prints the description of the room
        """
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"  The {room.name} is on the {direction}")

    def get_item(self) -> Item | None:
        """Get the item in the room.

        Returns:
            Item | None: The item in the room
        """
        if self.item is None:
            return None
        return self.item

    def move(self, direction: str) -> Room:
        """Move to a linked room.

        Args:
            direction (str): The direction to move

        Returns:
            Room: The room moved to
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        print("You can't go that way")
        return self


class Enemy:
    """A class for an enemy in the game.

    Attributes:
        name (str): The name of the enemy
        description (str): The description of the enemy
        conversation (str): The conversation of the enemy
        weakness (str): The weakness of the enemy
        defeated_times (int), a class variable: The number of times
                the enemy has been defeated

    Methods:
        set_conversation: Set the conversation of the enemy
        set_weakness: Set the weakness of the enemy
        fight: Fight the enemy
        describe: Describe the enemy
        talk: Talk to the enemy
        get_defeated: Get the number of times any enemy has been defeated
    """

    conversation: str
    weakness: str
    defeated_times: int = 0

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def set_conversation(self, conversation: str) -> None:
        """Set the conversation of the enemy.

        Args:
            conversation (str): The conversation of the enemy
        """
        self.conversation = conversation

    def set_weakness(self, weakness: str) -> None:
        """Set the weakness of the enemy.

        Args:
            weakness (str): The weakness of the enemy
        """
        self.weakness = weakness

    def fight(self, fight_with: str) -> bool:
        """Fight the enemy.

        Args:
            fight_with (str): The item to fight with

        Returns:
            bool: Whether the enemy was defeated
        """
        if fight_with == self.weakness:
            Enemy.defeated_times += 1
            return True
        return False

    def describe(self) -> None:
        """Describe the enemy.

        Prints the description of the enemy
        """
        print(f"There is an enemy: {self.description}")

    def talk(self) -> None:
        """Talk to the enemy.

        Prints the conversation of the enemy
        """
        print(f"Enemy says: {self.conversation}")

    def get_defeated(self) -> int:
        """Get the number of times any enemy has been defeated.

        Returns:
            int: The number of times any enemy has been defeated
        """
        return Enemy.defeated_times


class Item:
    """A class for an item in the game.

    Attributes:
        name (str): The name of the item
        description (str): The description of the item

    Methods:
        set_description: Set the description of the item
        describe: Describe the item
        get_name: Get the name of the item
    """

    description: str

    def __init__(self, name: str) -> None:
        self.name = name

    def set_description(self, description: str) -> None:
        """Set the description of the item.

        Args:
            description (str): The description of the item
        """
        self.description = description

    def describe(self) -> None:
        """Describe the item.

        Prints the description of the item
        """
        print(f"There is an item: {self.description}")

    def get_name(self) -> str:
        """Get the name of the item.

        Returns:
            str: The name of the item
        """
        return self.name
