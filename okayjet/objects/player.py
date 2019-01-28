import pygame

from .gameobject import GameObject
from ..settings import SCREEN_WIDTH


class Player(GameObject):
    IMAGE = "player.png"

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.speedup = 0.1

    def update(self):
        if self.rect.x < SCREEN_WIDTH // 4:
            self.rect = self.rect.move(3, 0)

        space = pygame.key.get_pressed()[pygame.K_SPACE]

        if self.rect.y < 355 and not space:
            self.rect.y += (3 * self.speedup)
            self.speedup += 0.05
        elif space:
            self.speedup = 0.1
