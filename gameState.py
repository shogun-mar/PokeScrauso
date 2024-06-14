from enum import Enum

# Define the possible game states using an Enum
class GameState(Enum):
    GAMEPLAY = 0
    PAUSE = 1
    INVENTORY = 2
    POKEDEX = 3
    MAP = 4
    START_MENU = 5
    