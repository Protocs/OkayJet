import random
import os

import pygame

from .collidable import Collidable
from .player import Player


def load_random_group():
    files = os.listdir("data/coin_groups")
    with open("data/coin_groups/group{}.txt".format(str(random.randint(1, len(files))))) as file:
        return file.readlines()


class Coin(Collidable):
    IMAGE = 'coin.png'
    SPRITE_GROUPS = ["coins"]

    def collide(self, colliding_objects):
        if any(isinstance(o, Player) for o in colliding_objects):
            self.game.coins += 1
            self.kill()
