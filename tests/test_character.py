from levelup.character import Character
from levelup.game_map import GameMap
from levelup.controller import Direction
import pytest

@pytest.fixture
def character():
    return Character('pytron')

def test_set_character_position(character):
    input = (1,1)
    want = (1,1)
    character.set_position(input)
    assert character.position == want

def test_has_a_map(character):
    map = GameMap()
    want = map
    character.set_map(map)
    assert character.map == want

def test_move(character):
    direction = Direction.NORTH
    current_pos = (5,5)
    map = GameMap()
    character.set_position(current_pos)
    character.set_map(map)
    character.move(direction)
    want = (5,4)
    assert character.position == want