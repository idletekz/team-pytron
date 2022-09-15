import numpy
from prettytable import PrettyTable

class GameMap:
    def __init__(self, size=10):
        self.size = size
        self.positions = numpy.tile(" ", (size, size))

    def update(self, current_pos=(5,5), new_pos=(5,6)):
        self.positions[current_pos] = "-"
        self.positions[new_pos] = "O"

    def isValid(self, position):
        return ((position[0] < self.size) and (position[1] < self.size))