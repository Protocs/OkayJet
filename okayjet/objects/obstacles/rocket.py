from .obstacle import Obstacle
from ...util import load_image
import pygame
import random
from ...settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Rocket(Obstacle):
    ROCKET_IMAGE = "obstacles/rocket.png"
    PREPARING_IMAGE = "obstacles/znak.png"
    PREPARING_TIME = 2000
    SPEED = 10

    def __init__(self, game, pos=(0, 0), delay_before_spawn=0):
        super().__init__(game, pos, self.PREPARING_IMAGE)
        self.moving = False
        self.delay_before_spawn = delay_before_spawn
        if random.randint(1, 2) == 1:
            if len(list(filter(lambda o: isinstance(o, Rocket),
                               self.game.sprite_groups["obstacles"].sprites()))) < 3:
                Rocket(self.game, (SCREEN_WIDTH - 30, random.randint(0, SCREEN_HEIGHT)),
                       random.randint(100, 1000))

    def update(self):
        if self.delay_before_spawn:
            if pygame.time.get_ticks() - self.start_time >= self.delay_before_spawn:
                self.start_time += self.delay_before_spawn
                self.delay_before_spawn = 0
            return
        if pygame.time.get_ticks() - self.start_time >= self.PREPARING_TIME and not self.moving:
            self.activate_rocket()
        if self.moving:
            self.rect = self.rect.move(random.randrange(3) - 1 - self.SPEED, random.randrange(3) - 1)
            super().update()

    def activate_rocket(self):
        self.moving = True
        x, y = self.rect.x, self.rect.y
        self.image = load_image(self.ROCKET_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 10
        self.rect.y = y
