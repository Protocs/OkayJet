import pygame

from .gameobject import GameObject
from ..settings import SCREEN_WIDTH


class Player(GameObject):
    IMAGE = "player.png"

    def __init__(self, game, pos):
        super().__init__(game, pos)
        self.speedup = 0.1
        self.game = game

    def update(self):
        if self.game.intro:
            self.rect = self.rect.move(3, 0)

        space_bar_pressed = pygame.key.get_pressed()[pygame.K_SPACE]
        if self.rect.y < 355 and not space_bar_pressed:
            self.rect.y += (3 * self.speedup)
            self.speedup += 0.05
        elif space_bar_pressed:
            self.speedup = 0.1

        pygame.sprite.spritecollide(self, self.game.sprite_groups["coins"], True)
