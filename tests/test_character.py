from levelup.character import Character
from levelup.game_map import GameMap
from mock_game_map import MockGameMap
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

def test_move_count_middle(character):
    direction = Direction.NORTH
    current_pos = (5,5)
    map = GameMap()
    character.set_position(current_pos)
    character.set_map(map)
    character.move(direction)
    want = 2
    got = character.move_count
    assert got == want

def test_move_count_boundary(character):
    direction = Direction.NORTH
    current_pos = (0,0)
    map = GameMap()
    character.set_position(current_pos)
    character.set_map(map)
    character.move(direction)
    want = 2
    got = character.move_count
    assert got == want

def test_move(character):
    direction = Direction.NORTH
    current_pos = (5,5)
    #ERINs note: This now tests in isolatin. It just tests that move called the right method. Let the map decide how that works.
    map = MockGameMap()
    character.set_position(current_pos)
    character.set_map(map)
    character.move(direction)
    want = map.RETURN_THIS_POSITION_WHEN_CALLED
    assert character.position == want