from levelup.game_map import GameMap
import pytest
from levelup.controller import Direction
map_size = 10

@pytest.fixture
def map():
    return GameMap()

def test_size(map):
    want = map_size
    assert len(map.positions) == want

def test_update(map):
    current = (5,5)
    new = (5,6)
    want = {
        'current': '-',
        'new': 'O'
    }
    map.update(current, new)
    assert map.positions[current] == want['current']
    assert map.positions[new] == want['new']

@pytest.mark.parametrize("input,want", 
[((5,5), True), 
  ((5,10), False),
  ((11,11), False),
  ((-1,9), False),
])
def test_is_valid_position(input, want, map):
    got = map.isValid(input)
    assert got == want
    
def test_calculate_position(map):
    want = (0,9)
    got = map.calculate_position((0,9), Direction.NORTH)
    assert got == want