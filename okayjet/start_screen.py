import pygame

from .util import terminate, load_image
from .objects.animated_sprite import AnimatedSprite
from .settings import MUSIC_VOLUME


class AnimatedStartButton(AnimatedSprite):
    COLUMNS = 1
    ROWS = 15
    IMAGE = "press_somewhere_image.png"
    FRAMES_CHANGING = 85

    def update(self):
        if pygame.time.get_ticks() > self.next_frame:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.next_frame += self.FRAMES_CHANGING


class Start:
    """
    Начальная заставка с логотипом
    и приглашением к игре.
    """

    def __init__(self, surface):
        self.surface = surface

        # Была ли игра начата?
        self.start = True

        self.sprite_groups = {"all": pygame.sprite.Group()}

        self.background = load_image("start_background.png")
        self.start_button = AnimatedStartButton(self, (150, 400))
        self.logo = load_image("logo.png")

        pygame.mixer.music.load("data/music/start.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(MUSIC_VOLUME)

    def run(self):
        while self.start:
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                for i in range(int(MUSIC_VOLUME * 10), -1, -1):
                    pygame.mixer.music.set_volume(i / 10)
                    pygame.time.delay(20)
                self.start = False

            elif event.type == pygame.QUIT:
                terminate()

    def update(self):
        self.surface.blit(self.background, (0, 0))
        self.sprite_groups["all"].update()
        self.sprite_groups["all"].draw(self.surface)
        self.background.blit(self.logo, (280, 75))
        pygame.display.flip()
