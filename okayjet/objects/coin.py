import pygame
from .gameobject import GameObject
from okayjet import util

class Coin(GameObject):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = util.load_image("coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_taken = False

    def update(self):
        self.rect.x -= 3