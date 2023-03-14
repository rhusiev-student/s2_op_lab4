# Tasks 6 and 5 of lab4

# Task 6

## Usage

To run the game, run the file `main.py`

Or import and invoke:
```python
game = Game()
game.start()
```

## The file `main.py` contains the following:
### Map class

The class `Map` is used to represent the map of the game. It has the following attributes:

- `rooms`: a 2D list of the rooms in the game
- `player`: the player in the game
- `starting_room`: the starting room of the game

It initialises the 3x3 map. The top left room is the start room, the bottom right room is the end room.

The weapons are:
- A cat - can drink the milk
- Milk - can drown the mosquito
- Mosquito - can annoy the cat

If the same weapons are clashed, the player loses.

From the begginning the player has a mosquito. The room on the bottom of start is always with a weapon, so that it is possible to pass

Methods:

- `enter_room`: enters the room, if possible. Fights and takes an item if there is one. If the room is the end room and all conditions are met, the game ends.
- `move`: translates the direction into a room to enter. Moves the player's position

### Game class

The class `Game` is used to represent the game. It has the following attributes:

- `map`: the map of the game
- `player`: the player in the game

Methods:

- `start`: starts the game

## The file `assets.py` contains the following classes:

### Room

The class `Room` is used to represent a room in the game. It has the following attributes:

- `name`: the name of the room
- `description`: the description of the room
- `neighbours`: a dictionary of the rooms linked to the current room
- `item`: the item in the room
- `character`: the character in the room(an Enemy or a Friend)

Methods:

- `add_neighbour`: links a room to the current room
- `set_character`: sets the character in the room

### EndRoom

The class `EndRoom` is used to represent the end room in the game. It extends the class `Room` and has the following attributes:

- `name`: the name of the room
- `description`: the description of the room
- `item`: the item in the room
- `cleared_rooms_needed`: the number of rooms that need to be cleared before the player can enter the end room

Methods:

- `add_neighbour`: links a room to the current room
- `set_character`: sets the character in the room
- `can_enter`: returns True if the player can enter the end room, False otherwise

### Character

The class `Character` is used to represent a character in the game. It has the following attributes:

- `name`: the name of the character

### Player

The class `Player` is used to represent the player in the game. It extends the class `Character` and has the following attributes:

- `name`: the name of the player
- `current_room`: the room the player is currently in
- `weapons`: a list of the weapons the player has
- `cleared_rooms`: a list of the rooms the player has cleared

Methods:

- `clear_room`: clears the room the player is currently in
- `fight`: fights the enemy
- `pick_up_item`: picks up the item in the room

### Enemy

The class `Enemy` is used to represent an enemy in the game. It extends the class `Character` and has the following attributes:

- `name`: the name of the enemy
- `weapon`: the weapon the enemy has
- `defeated`: True if the enemy has been defeated, False otherwise

### Friend

The class `Friend` is used to represent a friend in the game. It extends the class `Character` and has the following attributes:

- `name`: the name of the friend
- `dialogue`: the dialogue the friend has

Methods:

- `talk`: returns the dialogue the friend has

### Item

A generic class to represent an item in the game. It has the following attributes:

- `name`: the name of the item
- `picked_up`: True if the item has been picked up, False otherwise

### Weapon

The class `Weapon` is used to represent a weapon in the game. It extends the class `Item` and has the following attributes:

- `name`: the name of the weapon
- `picked_up`: True if the weapon has been picked up, False otherwise
- `can_kill`: What other weapon user the weapon can kill


# Task 5

## The file `game.py` classes:

### Room

The class `Room` is used to represent a room in the game. It has the following attributes:

- `name`: the name of the room
- `description`: the description of the room
- `character`: the character in the room(an Enemy)
- `item`: the item in the room
- `linked_rooms`: a dictionary of the rooms linked to the current room

Methods:

- `set_description`: sets the description of the room
- `link_room`: links a room to the current room
- `set_character`: sets the character in the room
- `set_item`: sets the item in the room
- `get_character`: returns the character in the room
- `get_item`: returns the item in the room
- `get_details`: returns the name and description of the room
- `move`: moves the player to the room linked to the current room(returns that room)

### Enemy

The class `Enemy` is used to represent an enemy in the game. It has the following attributes:

- `name`: the name of the enemy
- `description`: the description of the enemy
- `conversation`: the conversation you can have with the enemy
- `weakness`: the weakness of the enemy
- `defeated_times`: the number of times any enemy has been defeated

Methods:

- `set_conversation`: sets the conversation you can have with the enemy
- `set_weakness`: sets the weakness of the enemy
- `fight`: fights the enemy
- `describe`: prints the description of the enemy
- `talk`: prints the conversation you can have with the enemy
- `get_defeated`: returns the number of times any enemy has been defeated

### Item

The class `Item` is used to represent an item in the game. It has the following attributes:

- `name`: the name of the item
- `description`: the description of the item

Methods:

- `set_description`: sets the description of the item
- `describe`: prints the description of the item
- `get_name`: returns the name of the item

