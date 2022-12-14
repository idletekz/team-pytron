from levelup.controller import GameController
from levelup.controller import Direction

start_x: int
start_y: int

class MoveLibrary:
    def initialize_character_xposition_with(self, x_position):
        self.start_x = x_position
    
    def initialize_character_yposition_with(self, y_position):
        self.start_y = y_position

    def initialize_character_move_count_with(self, move_count):
        self.controller = GameController()
        self.controller.status.character.move_count = int(move_count)

    def move_in_direction(self, direction):
        self.controller.set_character_position(self.start_x, self.start_y)
        self.controller.move(Direction[direction])

    def character_xposition_should_be(self, expected):
        end_x = self.controller.status.character.position[0]
        if int(end_x) != int(expected):
            raise AssertionError(
                "%s != %s" % (end_x, expected)
            )

    def character_yposition_should_be(self, expected):
        end_y = self.controller.status.character.position[1]
        if int(end_y) != int(expected):
            raise AssertionError(
                "%s != %s" % (end_y, expected)
            )

    def character_move_count_should_be(self, expected):
        end_move_count = self.controller.status.character.move_count
        if int(end_move_count) != int(expected):
            raise AssertionError(
                "%s != %s" % (end_move_count, expected)
            )
