import pygame
from .gameobject import GameObject


class Player(GameObject):
    def __init__(self, group, x, y):
        super().__init__(group)
        # self.image = Player.image
        # self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y
