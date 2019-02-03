import pygame

from ..util import load_image


class GameObject(pygame.sprite.Sprite):
    """Базовый класс всех игровых обьектов.

    Наследующие классы должны определять атрибут класса
    IMAGE, содержащий путь к изображению обьекта.

    Все обьекты наследующих классов автоматически
    добавляются в группу спрайтов
    Game.sprite_groups['all'].
    Необязательный атрибут класса SPRITE_GROUPS - список
    с названиями дополнительных групп спрайтов.
    """

    SPRITE_GROUPS = []

    def __init__(self, game, pos):
        super().__init__(*(game.sprite_groups[g] for g in ('all', *self.SPRITE_GROUPS)))

        self.game = game

        # noinspection PyUnresolvedReferences
        self.image = load_image(self.IMAGE)
        if self.SOUND is not None:
            self.sound = pygame.mixer.Sound(self.SOUND)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def move(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

