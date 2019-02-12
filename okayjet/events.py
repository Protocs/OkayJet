from collections import namedtuple

_Event = namedtuple('Event', 'id delay')

COIN_SPAWN = _Event(29, 5000)
OBSTACLE_SPAWN = _Event(30, 2000)
EXTRA_LIFE_SPAWN = _Event(31, 60000)

ALL_EVENTS = {COIN_SPAWN, OBSTACLE_SPAWN, EXTRA_LIFE_SPAWN}
