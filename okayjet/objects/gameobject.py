import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
