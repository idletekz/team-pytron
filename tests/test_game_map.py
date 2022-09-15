from levelup.game_map import GameMap
import pytest
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
])
def test_is_valid_position(input, want, map):
    got = map.isValid(input)
    assert got == want