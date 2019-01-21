import pygame
from .gameobject import GameObject
from okayjet import util


class Player(GameObject):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = util.load_image("player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def update(self):
        self.rect = self.rect.move(3, 0)
        if self.rect.y < 355 and not pygame.key.get_pressed()[pygame.K_SPACE]:
            self.rect.y += 3
