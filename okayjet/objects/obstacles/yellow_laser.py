from .obstacle import Obstacle

import random

import pygame


class YellowLaser(Obstacle):
    IMAGE = "obstacles/yellow_laser.png"
    SPRITE_GROUPS = ["yellow_lasers"]
    FRAMES_CHANGING = 40

    def __init__(self, game, pos=(0, 0)):
        super().__init__(game, pos, self.IMAGE)
        self.rotation = random.randint(1, 4) == 1
        self.angle = 1
        self.image = pygame.transform.rotate(self.image, random.randint(0, 360))
        self.original_image = self.image
        self.next_frame = pygame.time.get_ticks()
        if pos == (0, 0):
            self.prepare_for_spawn()

    def update(self):
        if self.rotation and pygame.time.get_ticks() > self.next_frame:
            center = self.rect.center
            self.image = pygame.transform.rotate(self.original_image, self.angle % 360)
            self.angle += 1
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.next_frame += self.FRAMES_CHANGING
        super().update()
