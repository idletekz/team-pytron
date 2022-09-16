from prettytable import PrettyTable
from levelup.direction import Direction
from dataclasses import dataclass
from levelup.character import Character
from levelup.direction import Direction
DEFAULT_CHARACTER_NAME = "Character"


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
        self.status.character.move(direction)
        pretty_map = PrettyTable(header=False, vrules=2, hrules=0)
        for row in self.status.character.map.positions:
            pretty_map.add_row(row)
        print(pretty_map)
        print(f"Moved {direction.name}")

    def set_character_position(self, x, y) -> None:
        print(f"Set character position state for testing")
        self.status.character.set_position((int(x),int(y)))

    def start_game() -> None:
        return null

    def get_status() -> GameStatus:
        return GameStatus

    def get_total_positions() -> int:
        return int
