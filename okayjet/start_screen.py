import pygame
from okayjet import util


class Start:
    def __init__(self, fps, surface):
        self.start = True
        self.clock = pygame.time.Clock()
        self.background = util.load_image("start_background.png")
        self.fps = fps
        self.surface = surface
        self.start_button = util.load_image("press_somewhere_image.png")

    def run(self):
        while self.start:
            self.events()
            self.update()
            self.clock.tick(self.fps)

    def events(self):
        for event in pygame.event.get():
            if event.type in (pygame.MOUSEBUTTONUP, pygame.KEYUP):
                self.start = False
            elif event.type == pygame.QUIT:
                util.terminate()

    def update(self):
        self.surface.fill((0, 0, 0))
        self.background.blit(self.start_button, (150, 400))
        self.surface.blit(self.background, (0, 0))
        pygame.display.flip()
