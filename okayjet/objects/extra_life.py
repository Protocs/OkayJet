from .gameobject import GameObject

from math import sin, radians
from ..settings import BOTTOM_BORDER, SCREEN_WIDTH

import pygame


class ExtraLivesCounter(GameObject):
    def __init__(self, game):
        super().__init__(game, (SCREEN_WIDTH - 65, 18))
        self.font = pygame.font.Font("data/fonts/PressStart2P.ttf", 18)

    def update(self):
        self.image = self.font.render(str(self.game.player.extra_lives), True, (207, 0, 0))


class ExtraLife(GameObject):
    IMAGE = "extra_life.png"
    SPRITE_GROUPS = ["extra_lives"]

    def __init__(self, game):
        super().__init__(game, (-100, 0))

    def update(self):
        self.rect.x += 1
        self.rect.y = abs(int(sin(radians(self.rect.x)) * (BOTTOM_BORDER - self.rect.h - 100)))
        if self.rect.x > SCREEN_WIDTH:
            self.kill()
