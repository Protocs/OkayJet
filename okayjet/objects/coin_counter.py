import pygame

from .gameobject import GameObject


class CoinCounter(GameObject):
    """Счетчик собранных монет."""

    def __init__(self, game):
        super().__init__(game, (10, 10))
        self.image = pygame.Surface((100, 100))

    def update(self):
        font = pygame.font.Font("data/fonts/freesansbold.ttf", 16)
        self.image = font.render(f'Монеты: {self.game.coins}', True, (0, 0, 0))
