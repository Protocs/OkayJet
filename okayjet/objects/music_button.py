from .gameobject import GameObject
from ..settings import SCREEN_WIDTH
from ..util import load_image

import pygame
from itertools import cycle


class MusicButton(GameObject):
    IMAGE_ON = "music_on.png"
    IMAGE_OFF = "music_off.png"

    def __init__(self, game):
        self.images = cycle([load_image(self.IMAGE_ON), load_image(self.IMAGE_OFF)])
        super().__init__(game, (0, 0))
        self.image = next(self.images)
        self.rect = self.image.get_rect()
        self.rect.topleft = (SCREEN_WIDTH - 50, 5)
        self.state = True

    def mouse_handler(self, pos):
        if self.rect.collidepoint(*pos):
            self.image = next(self.images)
            self.state = not self.state
            if self.state:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
