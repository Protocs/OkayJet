import time
import logging

import pygame

from okayjet.objects.obstacle import Obstacle
from .util import load_image, terminate
from .objects.coin_structure import CoinStructure
from .objects.player import Player
from .settings import *
from .events import *

_logger = logging.getLogger('okayjet.game')


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
            'coin_structure': pygame.sprite.Group(),
        }

        self.start_time = time.time()
        self.clock = pygame.time.Clock()

        self.player = Player(self, (30, 0))
        # Собранные монеты
        self.coins = 0

        pygame.mixer.music.load("data/music/game.wav")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)

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

    def run(self):
        for event in ALL_EVENTS:
            pygame.time.set_timer(*event)
        while self.game:
            self.events()
            self.update()
            self.clock.tick(FPS)

    def events(self):
        self.keypress_handler()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == COIN_SPAWN.id:
                CoinStructure.random(self).spawn()
            elif event.type == OBSTACLE_SPAWN.id:
                _logger.debug('OBSTACLE_SPAWN event')
                Obstacle(self)

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
