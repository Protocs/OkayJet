import pygame
from .collidable import Collidable
from ..settings import FRAMES_CHANGING


def cut_sheet(sheet, columns, rows, rect):
    frames = []
    for j in range(rows):
        for i in range(columns):
            frame_location = (rect.w * i, rect.h * j)
            frames.append(sheet.subsurface(pygame.Rect(frame_location, rect.size)))
    return frames


class AnimatedSprite(Collidable):
    def __init__(self, game, pos, columns, rows):
        super().__init__(game, pos)
        self.rect = pygame.Rect(*pos, self.image.get_width() // columns,
                                self.image.get_height() // rows)
        self.frames = cut_sheet(self.image, columns, rows, self.rect)
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.next_frame = pygame.time.get_ticks()

    def update(self):
        super().update()

        if pygame.time.get_ticks() > self.next_frame:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.next_frame += FRAMES_CHANGING
