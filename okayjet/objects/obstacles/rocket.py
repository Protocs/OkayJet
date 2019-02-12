from .obstacle import Obstacle
from ...util import load_image
import pygame
import random
from ...settings import SCREEN_WIDTH, BOTTOM_BORDER


def get_random_pos(h):
    return SCREEN_WIDTH - 30, random.randint(0, BOTTOM_BORDER - h)


class Rocket(Obstacle):
    ROCKET_IMAGE = "obstacles/rocket.png"
    PREPARING_IMAGE = "obstacles/znak.png"
    PREPARING_TIME = 2000
    SPEED = 10
    SPRITE_GROUPS = ["rockets", "obstacles"]

    def __init__(self, game, pos=(0, 0), delay_before_spawn=0):
        super().__init__(game, pos, self.PREPARING_IMAGE)
        if pos == (0, 0):
            self.rect.topleft = get_random_pos(self.rect.h)
        self.start_y = self.rect.y
        self.moving = False
        self.delay_before_spawn = delay_before_spawn
        if random.randint(1, 2) == 1:
            if len(list(self.game.sprite_groups["rockets"].sprites())) < 3:
                x, y = get_random_pos(self.rect.h)
                while True:
                    if any(pygame.Rect(x, y, self.rect.w, self.rect.h).colliderect(o.rect)
                           for o in self.game.sprite_groups["rockets"]):
                        x, y = get_random_pos(self.rect.h)
                        continue
                    break
                Rocket(self.game, (x, y), random.randint(100, 1000))

        self.activate_sound = pygame.mixer.Sound("data/music/rocket.wav")

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
        else:
            self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
            if self.rect.x > SCREEN_WIDTH - 28:
                self.rect.x -= 1
            elif self.rect.x < 968:
                self.rect.x += 1
            if self.rect.y > self.start_y + 2:
                self.rect.y -= 1
            elif self.rect.y < self.start_y - 2:
                self.rect.y += 1

    def activate_rocket(self):
        self.moving = True
        y = self.rect.y
        self.image = load_image(self.ROCKET_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 10
        self.rect.y = y
        self.activate_sound.play()
