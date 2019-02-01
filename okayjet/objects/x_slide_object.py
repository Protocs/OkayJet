from .gameobject import GameObject


class XSlideObject(GameObject):
    """Обьект, скользящий вместе с фоном."""

    def update(self):
        if self.game.intro:
            self.rect.x -= self.game.slide_speed

