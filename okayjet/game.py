import time

import pygame

from .util import load_image, terminate
from .objects.coin import spawn_coin_group, load_random_group
from .objects.player import Player
from .settings import *


class Game:
    """Главный класс игры."""
    
    def __init__(self, surface):
        self.surface = surface

        # Идет ли игра?
        self.game = True

        self.background = load_image("background.jpg")
        self.background_width = self.background.get_rect().width
        self.background_x = 0

        self.sprite_groups = {
            "all": pygame.sprite.Group(),
            "coins": pygame.sprite.Group()
        }

        self.start_time = time.time()
        self.clock = pygame.time.Clock()

        self.player = Player(self, (30, 355))
        self.coins = 0

    @property
    def slide_speed(self):
        """Скорость движения персонажа."""
        speed = min((time.time() - self.start_time) * SPEED_COEFFICIENT, MAX_SPEED)
        return START_SPEED + speed

    @property
    def intro(self):
        """
        Идёт ли сейчас анимация начала игры
        (персонаж выбегает из левой части экрана 
        без прокрутки фона)?
        """
        return self.player.rect.x < SCREEN_WIDTH // 4

    @property
    def _background_x(self):
        return abs(self.background_x)

    def run(self):
        pygame.time.set_timer(*COIN_SPAWN_EVENT)
        while self.game:
            self.events()
            self.update()
            self.clock.tick(FPS)

    def events(self):
        self.keypress_handler()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == COIN_SPAWN_EVENT[0]:
                spawn_coin_group(self, load_random_group())

    def update(self):
        self.update_background()
        self.sprite_groups['all'].update()
        self.sprite_groups['all'].draw(self.surface)
        pygame.display.flip()

    def update_background(self):
        """Осуществляет прокрутку фона.""" 
        x = self.background_x % self.background_width
        self.surface.blit(self.background, (x - self.background_width, 0))
        if x < SCREEN_WIDTH:
            self.surface.blit(self.background, (x, 0))
        if not self.intro:
            self.background_x -= self.slide_speed

    def keypress_handler(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_SPACE] and self.player.rect.y >= 0:
            self.player.move(0, -5.5)

