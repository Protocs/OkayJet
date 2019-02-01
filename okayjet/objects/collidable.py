import pygame

from .x_slide_object import XSlideObject


class Collidable(XSlideObject):
    """
    Обьект с коллбэком для столкновения
    с другим обьектом.

    Наследующие классы должны определить метод collide(colliding_objects).
    """

    def collide(self, colliding_objects):
        pass

    def update(self):
        super().update()

        colliding_objects = pygame.sprite.spritecollide(self, self.game.sprite_groups["all"], False)
        if colliding_objects:
            self.collide(colliding_objects)
