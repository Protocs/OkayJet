import random
import os

import pygame

from .x_slide_object import XSlideObject


def load_random_group():
    files = os.listdir("data/coin_groups")
    with open("data/coin_groups/group{}.txt".format(str(random.randint(1, len(files))))) as file:
        return file.readlines()


class Coin(XSlideObject):
    IMAGE = 'coin.png'
    SPRITE_GROUPS = ["coins"]
