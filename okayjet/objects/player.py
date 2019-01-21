import pygame
from .gameobject import GameObject
from okayjet import util
from ..settings import SCREEN_WIDTH

class Player(GameObject):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = util.load_image("player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedup = 0.1

    def move(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def update(self):
        if self.rect.x < SCREEN_WIDTH // 4:
            self.rect = self.rect.move(3, 0)
        space = pygame.key.get_pressed()[pygame.K_SPACE]
        if self.rect.y < 355 and not space:
            self.rect.y += (3 * self.speedup)
            self.speedup += 0.05
        elif space:
            self.speedup = 0.1
