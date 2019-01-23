import pygame
from .util import terminate, load_image
from .settings import FPS


class Start:
    def __init__(self, surface):
        self.surface = surface

        # Была ли игра начата?
        self.start = True

        self.clock = pygame.time.Clock()

        self.background = load_image("start_background.png")
        self.start_button = load_image("press_somewhere_image.png")
        self.logo = load_image("logo.png")

    def run(self):
        while self.start:
            self.events()
            self.update()
            self.clock.tick(FPS)

    def events(self):
        for event in pygame.event.get():
            if event.type in (pygame.MOUSEBUTTONUP, pygame.KEYUP):
                self.start = False
            elif event.type == pygame.QUIT:
                terminate()

    def update(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.background, (0, 0))
        self.background.blit(self.start_button, (150, 400))
        self.background.blit(self.logo, (280, 75))
        pygame.display.flip()
