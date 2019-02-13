import pygame

from .animated_sprite import AnimatedSprite
from ..settings import BOTTOM_BORDER, START_SPEED
from ..death_screen import Death
from ..util import save_progress


class Player(AnimatedSprite):
    IMAGE = "player.png"
    COLUMNS = 12
    FLASHING_TIME = 500

    @property
    def frames_changing(self):
        return 80 - (self.game.slide_speed - START_SPEED) * 8

    def __init__(self, game, pos):
        super().__init__(game, pos)
        self.flying_current_frame = 0

        self.rect.y = BOTTOM_BORDER - self.rect.height

        # Ускорение свободного падения
        self.speedup = 0.1
        # Дополнительные жизни
        self.extra_lives = 0
        self.flashing = False
        self.flashing_start = None

    def kill(self):
        super().kill()
        self.game.game = False
        if self.game.metres > self.game.best_progress:
            save_progress(self.game.metres)
        Death(self.game)

    def update(self):
        if self.game.intro:
            self.rect = self.rect.move(3, 0)

        if self.flashing:
            if pygame.time.get_ticks() - self.flashing_start >= self.FLASHING_TIME:
                self.rect.y = BOTTOM_BORDER - self.rect.height
                self.flashing = False
            else:
                self.rect.y = (1 - self.rect.y > 0) * BOTTOM_BORDER - self.rect.height

        space_bar_pressed = pygame.key.get_pressed()[pygame.K_SPACE]

        if space_bar_pressed:
            if pygame.time.get_ticks() > self.next_frame:
                self.change_frame(len(self.frames) - (self.flying_current_frame % 2 + 1))
                self.flying_current_frame += 1
                self.next_frame += self.frames_changing
            self.speedup = 0.1
        else:
            if pygame.time.get_ticks() > self.next_frame:
                self.change_frame((self.current_frame + 1) % (len(self.frames) - 2))
                self.next_frame += self.frames_changing

            if self.rect.y < (BOTTOM_BORDER - self.rect.height):
                self.change_frame(0)
                self.rect.y = min((self.rect.y + (3 * self.speedup)),
                                  BOTTOM_BORDER - self.rect.height)
                self.speedup += 0.05
        self.find_colliding()

    def change_frame(self, frame):
        self.current_frame = frame
        self.image = self.frames[self.current_frame]

    def find_colliding(self):
        for obstacle in self.game.sprite_groups["obstacles"]:
            if pygame.sprite.collide_mask(self, obstacle):
                self.kill_handler(obstacle)
        for coin in self.game.sprite_groups["coin_structure"]:
            if pygame.sprite.collide_mask(self, coin):
                coin.collide()
        for extra_life in self.game.sprite_groups["extra_lives"]:
            if pygame.sprite.collide_mask(self, extra_life):
                self.extra_lives += 1
                extra_life.kill()

    def kill_handler(self, obstacle):
        if not self.extra_lives:
            self.kill()
            return
        self.extra_lives -= 1
        self.rect.y = BOTTOM_BORDER - self.rect.height
        self.flashing = True
        self.flashing_start = pygame.time.get_ticks()
        obstacle.kill()
