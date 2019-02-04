from collections import namedtuple

_Event = namedtuple('Event', 'id delay')

COIN_SPAWN = _Event(30, 5000)
