import os
import random

import pygame

from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT, COIN_DISTANCE
from .x_slide_object import XSlideObject
from .coin import Coin


def _get_coin_structure_template(filename):
    full_filename = os.path.join('data', 'coin_structure_templates', filename)
    with open(full_filename) as f:
        return f.readlines()


class CoinStructure(XSlideObject):
    def __init__(self, game, filename, pos=None):
        # Если pos - None, выбирается случайная позиция

        # Временно устанавливаем хоть куда-нибудь, лишь бы поскорей вызвать super().__init__()
        if pos is None:
            pos = 0, 0

        super().__init__(game, pos)

        # Содержимое файла шаблона
        self._template = _get_coin_structure_template(filename)

        # Количество монет в самом длинном ряду
        max_coins_along_x = max(len(row.rstrip()) for row in self._template)
        max_coins_along_y = len(self._template)

        # Установка границ структуры дял предотвращения их пересечения
        self.rect.w, self.rect.h = max_coins_along_x * COIN_DISTANCE, max_coins_along_y * COIN_DISTANCE
        # Наконец, ставим структуру в случайное место, раз на то пошло
        if pos == (0, 0):
            self._set_random_pos()

    def _set_random_pos(self):
        self.rect.x = random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH - 100)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 250)
        # Генерируем новые позиции до тех пор, пока мы налезаем на уже существующую структуру
        while pygame.sprite.spritecollideany(self, self.game.sprite_groups['coin_structure']):
            self.rect.x = random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH - 100)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - 250)

        self.game.sprite_groups['coin_structure'].add(self)

    @staticmethod
    def random(game, pos=None):
        templates_dir = os.path.join('data', 'coin_structure_templates')
        random_template_filename = random.choice(os.listdir(templates_dir))
        return CoinStructure(game, random_template_filename, pos)

    def spawn(self):
        for i in range(len(self._template)):
            for j in range(len(self._template[i].rstrip())):
                if self._template[i].rstrip()[j] == "*":
                    Coin(self.game, (self.rect.x + COIN_DISTANCE * j,
                                     self.rect.y + COIN_DISTANCE * i))
