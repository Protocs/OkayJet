import random
import os

import pygame

from .player import Player
from ..settings import SCREEN_WIDTH, COIN_DISTANCE, COIN_HEIGHT, BOTTOM_BORDER
from .animated_sprite import AnimatedSprite


def get_random_coin_structure():
    coin_groups_dir_path = os.path.join('data', 'coin_groups')
    random_group_file_path = os.path.join(coin_groups_dir_path, random.choice(os.listdir(coin_groups_dir_path)))
    with open(random_group_file_path) as f:
        return f.readlines()


# TODO: Предотвращать наложение структур
def spawn_coin_structure(game, group):
    x = random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH - 100)
    y = random.randint(0, BOTTOM_BORDER - ((len(group) - 1) * (COIN_DISTANCE - COIN_HEIGHT) +
                                           len(group) * COIN_HEIGHT))
    for i in range(len(group)):
        for j in range(len(group[i].rstrip())):
            if group[i].rstrip()[j] == "*":
                Coin(game, (x + COIN_DISTANCE * j, y + COIN_DISTANCE * i), 7, 1)


class Coin(AnimatedSprite):
    IMAGE = 'animated_coin.png'
    SPRITE_GROUPS = ["coins"]
    SOUND = "data/music/coin.wav"

    def collide(self, colliding_objects):
        if any(isinstance(o, Player) for o in colliding_objects):
            self.game.coins += 1
            self.sound.play()
            self.kill()
