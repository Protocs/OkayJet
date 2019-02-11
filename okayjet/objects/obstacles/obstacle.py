import os
import random
import logging

import pygame

from ..player import Player
# from ..collidable import Collidable
from ..x_slide_object import XSlideObject

_logger = logging.getLogger('okayjet.objects.obstacle')


def _get_random_obstacle_image_path():
    obstacles_dir = os.path.join('data', 'images', 'obstacles')
    # Имена относительно data/images/obstacles/
    obstacles_images_filenames = os.listdir(obstacles_dir)
    # Имена относительно data/images/
    obstacles_images_paths = [os.path.join('obstacles', filename) for filename in
                              obstacles_images_filenames]
    return random.choice(obstacles_images_paths)


class Obstacle(XSlideObject):
    SPRITE_GROUPS = ["obstacles"]

    def __init__(self, game, pos=(0, 0), image=None):
        if image is None:
            image = _get_random_obstacle_image_path()

        self.IMAGE = image
        self.start_time = pygame.time.get_ticks()

        super().__init__(game, pos)

        if pos == (0, 0):
            self.prepare_for_spawn()

        _logger.debug('Spawned at %i, %i, model: %s', self.rect.x, self.rect.y, self.IMAGE)
        _logger.debug('Surface: %s', self.image)
        _logger.debug('Groups: %s', self.groups())

    def collide(self, colliding_objects):
        if any(isinstance(o, Player) for o in colliding_objects):
            self.game.player.kill()
