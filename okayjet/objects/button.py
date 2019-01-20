import pygame
from .gameobject import GameObject


class Button(GameObject):
    def __init__(self, group, x, y, image):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
