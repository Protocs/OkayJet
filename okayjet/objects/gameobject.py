from pygame.sprite import Sprite

from ..util import load_image


class GameObject(Sprite):
    SPRITE_GROUPS = []

    def __init__(self, game, x, y):
        super().__init__(*(game.sprite_groups[g] for g in ('all', *self.SPRITE_GROUPS)))

        self.game = game

        # noinspection PyUnresolvedReferences
        self.image = load_image(self.IMAGE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        self.rect = self.rect.move(dx, dy)
