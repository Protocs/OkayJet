import pygame

from .gameobject import GameObject


class BestMetres(GameObject):
    """Лучший прогресс игрока."""

    def __init__(self, game):
        super().__init__(game, (10, 64))
        self.font = pygame.font.Font("data/fonts/PressStart2P.ttf", 12)
        self.image = pygame.Surface((100, 100))

    def update(self):
        self.image = self.font.render("BEST: " + str(self.game.best_progress) + "m",
                                      True, (130, 130, 130))


class MetresCounter(GameObject):
    """Счетчик пройденного расстояния."""

    def __init__(self, game):
        super().__init__(game, (10, 44))
        self.font = pygame.font.Font("data/fonts/PressStart2P.ttf", 16)
        self.image = pygame.Surface((100, 100))
        self.color = (155, 154, 151)
        BestMetres(self.game)

    def update(self):
        self.image = self.font.render(str(self.game.metres) + "m", True, self.color)
