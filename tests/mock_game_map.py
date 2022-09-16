import numpy
from levelup.direction import Direction
class MockGameMap:
    def __init__(self, size=10):
        self.RETURN_THIS_POSITION_WHEN_CALLED = (99, 99)

    def calculate_position(self, current_pos, direction):
        return self.RETURN_THIS_POSITION_WHEN_CALLED

    def isValid(self, position):
        return True

    def update(self, current_pos, new_pos):
        pass
