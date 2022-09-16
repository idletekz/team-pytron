from dataclasses import dataclass
from levelup.game_map import GameMap
@dataclass
class Character:
    name: str

    def __init__(self, name, size=10, map=GameMap()):
        self.name = name
        self.position = (0,0)
        self.map = map
        self.move_count = 1

    def set_position(self, position):
        self.position = position

    def set_map(self, map):
        self.map = map

    def move(self, direction):
        new_position = self.map.calculate_position(self.position, direction)
        if self.map.isValid(new_position):
            self.map.update(self.position, new_position)
            self.set_position(new_position)
            self.move_count += self.move_count


        