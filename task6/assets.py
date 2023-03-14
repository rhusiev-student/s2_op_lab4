"""This module contains all the assets for the game.

classes:
    Room
    Character
    Player(Character)
    Enemy(Character)
    Friend(Character)
    Weapon
"""
from __future__ import annotations

KILL_MESSAGES = {
    "cat": "Your mosquitto has annoyed the cat. It does not want to fight any more",
    "mosquitto": "The mosquittos drown in the milk. They can no longer fly",
    "milk": "Your cat has drunk all the milk. Mykola seemed to like it",
}

DEATH_MESSAGES = {
    "cat-cat": "Mykola became best friends with the HUUGE cat. He betrayed you.",
    "cat-mosquitto": "Mykola was bitten by the mosquitto. He died. You are next",
    "mosquitto-milk": "The mosquitto drowned in the milk. You will get drunk by it now",
    "mosquitto-mosquitto": "There were more master's mosquittos. Yours had no chance.",
    "milk-cat": "The cat drank all the milk. You do not have any more milk to drink",
    "milk-milk": "The milk stacked with the milk. Too much milk. You drowned in it",
}


class Room:
    """A room in the game.

    Attributes:
        name (str): The name of the room.
        description (str): A description of the room.
        neighbours (dict): A dictionary of neighbouring rooms.
        item (Item): An item in the room.
        character (Character): A character in the room.

    Methods:
        add_neighbour: Add a neighbouring room on the west, east, north or south.
        set_character: Set the character(enemy or friend) in the room.
    """

    character: Character | None = None
    item: Item | None = None

    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description
        self.neighbours: dict[str, Room] = {}

    def add_neighbour(self, direction: str, room: Room) -> None:
        """Add a neighbouring room.

        Args:
            direction (str): The direction of the neighbouring room.
            room (Room): The neighbouring room.
        """
        self.neighbours[direction] = room

    def set_character(self, character: Character) -> None:
        """Set the character(enemy or friend) in the room.

        Args:
            character (Character): The character in the room.
        """
        self.character = character


class EndRoom(Room):
    """The end room of the game.

    Attributes:
        name (str): The name of the room.
        description (str): A description of the room.
        item (Item): An item in the room.
        cleared_rooms_needed (int): The number of rooms that need to be cleared to enter.
    """

    def __init__(self, name: str, description: str, cleared_rooms_needed: int) -> None:
        super().__init__(name, description)
        self.cleared_rooms_needed: int = cleared_rooms_needed

    def can_enter(self, player: Player) -> bool:
        """Check if the player can enter the room.

        Args:
            player (Player): The player character.

        Returns:
            bool: True if the player can enter the room, False otherwise.
        """
        return len(player.cleared_rooms) >= self.cleared_rooms_needed


class Character:
    """A character in the game.

    Attributes:
        name (str): The name of the character.
    """

    def __init__(self, name: str) -> None:
        self.name: str = name


class Player(Character):
    """The player character.

    Attributes:
        name (str): The name of the character.
        weapons (list[Weapon]): The player's weapons.
        cleared_rooms (list[Room]): The rooms that have been cleared.
        current_room (tuple[int, int]): The player's current room.

    Methods:
        clear_room: Clear a room.
        fight: Fight against an enemy.
        pick_up_item: Pick up an item.
    """

    def __init__(self, name: str, current_room: tuple[int, int] = (0, 0)) -> None:
        super().__init__(name)
        self.weapons: list[Weapon] = []
        self.cleared_rooms: list[Room] = []
        self.current_room: tuple[int, int] = current_room

    def clear_room(self, room: Room) -> None:
        """Clear a room.

        Args:
            room (Room): The room to clear.
        """
        self.cleared_rooms.append(room)

    def fight(self, enemy: Enemy, weapon_id: int = 0) -> bool:
        """Fight against an enemy.

        Args:
            enemy (Enemy): The enemy to fight.

        Returns:
            bool: True if the player wins, False otherwise.
        """
        print("You are fighting against the " + enemy.name)
        print("You are using the " + self.weapons[weapon_id].name)
        if self.weapons[weapon_id].can_kill == enemy.weapon.name:
            print(KILL_MESSAGES[enemy.weapon.name])
            return True
        print(DEATH_MESSAGES[f"{self.weapons[weapon_id].name}-{enemy.weapon.name}"])
        print("You lose!")
        return False

    def pick_up_item(self, room: Room) -> bool:
        """Pick up an item.

        Args:
            room (Room): The room to pick up the item from.

        Returns:
            bool: True if the player wins, False otherwise.
        """
        if room.item is not None:
            if room.item.name == "cake":
                print("==================")
                print("The cake is a lie.")
                print("==================")
                return True
            if isinstance(room.item, Weapon) and not room.item.picked_up:
                self.weapons.append(room.item)
                room.item.picked_up = True
        else:
            print("There is no item in this room.")
        return False


class Enemy(Character):
    """An enemy character.

    Attributes:
        name (str): The name of the character.
        weapon (Weapon): The enemy's weapon.
        defeated (bool): Whether the enemy has been defeated.
    """

    def __init__(self, name: str, weapon: Weapon) -> None:
        super().__init__(name)
        self.weapon: Weapon = weapon
        self.defeated: bool = False


class Friend(Character):
    """A friendly character.

    Attributes:
        name (str): The name of the character.
        dialogue (str): The friendly character's dialogue.

    Methods:
        talk: Talk to the friendly character.
    """

    def __init__(self, name: str, dialogue: str) -> None:
        super().__init__(name)
        self.dialogue: str = dialogue

    def talk(self) -> str:
        """Talk to the friendly character.

        Returns:
            str: The friendly character's dialogue.
        """
        return self.dialogue


class Item:
    """An item in the game.

    Attributes:
        name (str): The name of the item.
        picked_up (bool): Whether the item has been picked up.
    """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.picked_up: bool = False


class Weapon(Item):
    """A weapon.

    Attributes:
        name (str): The name of the weapon.
        can_kill (str): The name of weapon that this weapon can kill.
    """

    def __init__(self, name: str, can_kill: str = "") -> None:
        super().__init__(name)
        self.can_kill: str = can_kill
