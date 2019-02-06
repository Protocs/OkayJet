import random

import pygame

from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .gameobject import GameObject


class XSlideObject(GameObject):
    """Обьект, скользящий вместе с фоном."""

    def update(self):
        if not self.game.intro:
            self.rect.x -= self.game.slide_speed
            if self.rect.x < -SCREEN_WIDTH:
                self.kill()

    def prepare_for_spawn(self):
        """Перемещает обьект за правую часть экрана в случайное место, подготавливая его для появления."""
        # Временно убираем себя из всех групп, иначе pygame.sprite.spritecollideany() будет выдавать True всегда
        self.kill()

        self.rect.x = random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH - 100)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 250)
        # Генерируем новые позиции до тех пор, пока мы налезаем на уже существующий обьект
        while pygame.sprite.spritecollideany(self, self.game.sprite_groups['all']):
            self.rect.x = random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH - 100)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - 250)

        # Возвращаем себя обратно в группы
        self.add(*(group for name, group in self.game.sprite_groups.items() if name in self.SPRITE_GROUPS),
                 self.game.sprite_groups['all'])

