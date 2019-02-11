import pygame

from .animated_sprite import AnimatedSprite
from ..settings import BOTTOM_BORDER
from ..death_screen import Death
from ..util import load_best_progress, save_progress


class Player(AnimatedSprite):
    IMAGE = "player.png"
    COLUMNS = 11
    FRAMES_CHANGING = 80

    def __init__(self, game, pos):
        super().__init__(game, pos)

        self.rect.y = BOTTOM_BORDER - self.rect.height

        # Ускорение свободного падения
        self.speedup = 0.1

    def kill(self):
        super().kill()
        self.game.game = False
        if self.game.metres > self.game.best_progress:
            save_progress(self.game.metres)
        Death(self.game)

    def update(self):
        if self.game.intro:
            self.rect = self.rect.move(3, 0)

        space_bar_pressed = pygame.key.get_pressed()[pygame.K_SPACE]

        if space_bar_pressed:
            self.change_frame(len(self.frames) - 1)
            self.speedup = 0.1
        else:
            if pygame.time.get_ticks() > self.next_frame:
                self.change_frame((self.current_frame + 1) % (len(self.frames) - 1))
                self.next_frame += self.FRAMES_CHANGING

            if self.rect.y < (BOTTOM_BORDER - self.rect.height):
                self.change_frame(0)
                self.rect.y = min((self.rect.y + (3 * self.speedup)),
                                  BOTTOM_BORDER - self.rect.height)
                self.speedup += 0.05

    def change_frame(self, frame):
        self.current_frame = frame
        self.image = self.frames[self.current_frame]
