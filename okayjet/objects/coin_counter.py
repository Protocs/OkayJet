import pygame

from .gameobject import GameObject


class CoinCounter(GameObject):
    """Счетчик собранных монет."""

    def __init__(self, game):
        super().__init__(game, (40, 13))
        self.font = pygame.font.Font("data/fonts/PressStart2P.ttf", 16)
        self.image = pygame.Surface((100, 100))

    def update(self):
        self.image = self.font.render(str(self.game.coins), True, (255, 188, 0))
