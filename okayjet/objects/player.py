import pygame

from .gameobject import GameObject
from ..settings import BOTTOM_BORDER


class Player(GameObject):
    IMAGE = "player.png"
    SOUND = None

    def __init__(self, game, pos):
        super().__init__(game, pos)

        self.rect.y = BOTTOM_BORDER - self.rect.height

        # Ускорение свободного падения
        self.speedup = 0.1

    def update(self):
        if self.game.intro:
            self.rect = self.rect.move(3, 0)

        space_bar_pressed = pygame.key.get_pressed()[pygame.K_SPACE]
        if self.rect.y < (BOTTOM_BORDER - self.rect.height) and not space_bar_pressed:
            self.rect.y = min((self.rect.y + (3 * self.speedup)), BOTTOM_BORDER - self.rect.height)
            self.speedup += 0.05
        elif space_bar_pressed:
            self.speedup = 0.1
