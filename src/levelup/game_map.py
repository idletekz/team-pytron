import numpy
from levelup.direction import Direction

class GameMap:
    def __init__(self, size=10):
        self.size = size
        self.positions = numpy.tile(" ", (size, size))

    def update(self, current_pos, new_pos):
        self.positions[current_pos] = "-"
        self.positions[new_pos] = "O"

    def calculate_position(self, current_pos, direction):
        x = current_pos[0]
        y = current_pos[1]
        match direction:
            #Don't forget, X is each row, Y is each item in each row.
            case Direction.NORTH:
                tmp_position = (x - 1, y)
            case Direction.SOUTH:
                tmp_position = (x + 1, y)
            case Direction.EAST:
                tmp_position = (x, y + 1)
            case Direction.WEST:
                tmp_position = (x, y - 1)

        if self.isValid(tmp_position):
            return tmp_position
        return current_pos

    def isValid(self, position):
        return ((position[0] < self.size) and (position[0] > -1) and (position[1] < self.size) and (position[1] > -1))