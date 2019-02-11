import logging
import random

import pygame

from .util import load_image, terminate
from .pause_screen import Pause
from .objects.coin_structure import CoinStructure
from .objects.player import Player
from .objects.animated_sprite import AnimatedSprite
from .objects.coin_counter import CoinCounter
from .objects.obstacles import OBSTACLES
from .objects.obstacles.obstacle import Obstacle
from .settings import *
from .events import *

_logger = logging.getLogger('okayjet.game')


class Game:
    """Главный класс игры."""

    def __init__(self, surface):
        self.surface = surface

        # Идет ли игра?
        self.game = True
        # Поставлена ли игра на паузу?
        self.pause = False
        self.pause_start = 0

        self.background = load_image("background.jpg")
        self.background_width = self.background.get_rect().width
        self.background_x = 0

        self.sprite_groups = {
            "all": pygame.sprite.Group(),
            'coin_structure': pygame.sprite.Group(),
            "obstacles": pygame.sprite.Group()
        }

        self.start_time = pygame.time.get_ticks()
        self.clock = pygame.time.Clock()

        self.player = Player(self, (30, 0))
        # Собранные монеты
        self.coins = 0
        self.coin_counter = CoinCounter(self)
        self.coin_image = load_image("animated_coin.png").subsurface(pygame.Rect(0, 0, 20, 20))

        pygame.mixer.music.load("data/music/game.wav")
        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        pygame.mixer.music.play(-1)

    @property
    def slide_speed(self):
        """Скорость движения персонажа."""
        speed = min((pygame.time.get_ticks() - self.start_time) * SPEED_COEFFICIENT / 1000,
                    MAX_SPEED)
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
        self.key_hold_handler()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                self.keypress_handler(event.key)
            else:
                self.game_events(event)

    def game_events(self, event):
        if self.pause:
            return

        if event.type == COIN_SPAWN.id:
            CoinStructure.random(self).spawn()
        elif event.type == OBSTACLE_SPAWN.id:
            _logger.debug('OBSTACLE_SPAWN event')
            random.choice(OBSTACLES)(self)

    def update(self):
        if not self.pause:
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
        self.surface.blit(self.coin_image, (10, 10))

    def key_hold_handler(self):
        """Обработчик зажатых клавиш."""
        if self.pause:
            return

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and self.player.rect.y >= 0:
            self.player.rect.y = max(self.player.rect.y - 5.5, 0)

    def keypress_handler(self, key):
        if key == pygame.K_ESCAPE:
            if self.pause:
                self.unpause()
            else:
                self.set_pause()

    def unpause(self):
        self.pause = False
        pygame.mixer.music.unpause()
        pause_time = pygame.time.get_ticks() - self.pause_start
        self.start_time += pause_time
        for sprite in self.sprite_groups["all"]:
            if isinstance(sprite, AnimatedSprite):
                sprite.next_frame += pause_time
            if isinstance(sprite, Obstacle):
                sprite.start_time += pause_time

    def set_pause(self):
        self.pause = True
        pygame.mixer.music.pause()
        self.pause_start = pygame.time.get_ticks()
        Pause(self)
