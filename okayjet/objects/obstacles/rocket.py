from .obstacle import Obstacle
from ...util import load_image
import pygame


class Rocket(Obstacle):
    ROCKET_IMAGE = "obstacles/rocket.png"
    PREPARING_IMAGE = "obstacles/znak.png"
    PREPARING_TIME = 2000

    def __init__(self, game, pos=(0, 0)):
        super().__init__(game, pos, self.PREPARING_IMAGE)

        self.start_time = pygame.time.get_ticks()
        self.moving = False

    def update(self):
        if pygame.time.get_ticks() - self.start_time >= self.PREPARING_TIME and not self.moving:
            self.moving = True
            x, y = self.rect.x, self.rect.y
            self.image = load_image(self.ROCKET_IMAGE)
            self.rect = self.image.get_rect()
            self.rect.x = x + 100
            self.rect.y = y
        if self.moving:
            self.rect.x -= (self.game.slide_speed + 3)
            super().update()
