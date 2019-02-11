from collections import namedtuple

_Event = namedtuple('Event', 'id delay')

COIN_SPAWN = _Event(30, 5000)
OBSTACLE_SPAWN = _Event(31, 3000)

ALL_EVENTS = {COIN_SPAWN, OBSTACLE_SPAWN}
