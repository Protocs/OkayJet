from .gameobject import GameObject


class XSlideObject(GameObject):
    def update(self):
        if self.game.intro:
            self.rect.x -= self.game.slide_speed
