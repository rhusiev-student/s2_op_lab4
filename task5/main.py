"""A simple text-based adventure game.

classes:
    Room
    Character
    Player(Character)
    Enemy(Character)
    Friend(Character)
    Item
    Weapon(Item)
    Game
"""
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Room:
    pass


class Character:
    pass


class Player(Character):
    pass


class Enemy(Character):
    pass


class Friend(Character):
    pass


class Item:
    pass


class Weapon(Item):
    pass


class Game:
    pass
