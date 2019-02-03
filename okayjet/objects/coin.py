import random
import os

from .collidable import Collidable
from .player import Player
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT, COIN_DISTANCE, COIN_HEIGHT, BOTTOM_BORDER


def load_random_group():
    files = list(filter(lambda f: f.endswith(".txt") and f.startswith("group"),
                        os.listdir("data/coin_groups")))
    with open("data/coin_groups/group{}.txt".format(str(random.randint(1, len(files))))) as file:
        return file.readlines()


def spawn_coin_group(game, group):
    left = random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH - 100)
    top = random.randint(0, BOTTOM_BORDER - ((len(group) - 1) * (COIN_DISTANCE - COIN_HEIGHT) +
                                             len(group) * COIN_HEIGHT))
    for i in range(len(group)):
        for j in range(len(group[i].rstrip())):
            if group[i].rstrip()[j] == "*":
                Coin(game, (left + COIN_DISTANCE * j,
                            top + COIN_DISTANCE * i))


class Coin(Collidable):
    IMAGE = 'coin.png'
    SPRITE_GROUPS = ["coins"]

    def collide(self, colliding_objects):
        if any(isinstance(o, Player) for o in colliding_objects):
            self.game.coins += 1
            self.kill()
