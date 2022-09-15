from enum import Enum
from dataclasses import dataclass
from levelup.character import Character

DEFAULT_CHARACTER_NAME = "Character"


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


@dataclass
class GameStatus:
    running: bool = False
    character: Character = Character(DEFAULT_CHARACTER_NAME)
    current_position: tuple = (-1,-1)

class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def create_character(self, character_name: str) -> None:
        if not character_name:
            character_name = DEFAULT_CHARACTER_NAME
        self.status.character = Character(character_name)

    def move(self, direction: Direction) -> None:
        print(f"Moved {direction.name}")

    def set_character_position(self, xycoordinates: tuple) -> None:
        print(f"Set character position state for testing")
        self.status.current_position = xycoordinates

    def start_game() -> None:
        return null

    def get_status() -> GameStatus:
        return GameStatus

    def set_character_positionY() -> int:
        return y

    def set_character_positionX() -> int:
        return x

    def get_total_positions() -> int:
        return int
