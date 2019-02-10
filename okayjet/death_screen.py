import pygame
from .util import load_image, terminate


class Death:
    def __init__(self, game):
        self.surface = game.surface
        self.death = True
        self.background = load_image("start_background.png")
        self.run()

    def run(self):
        while self.death:
            self.update()
            self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                terminate()

    def update(self):
        self.surface.blit(self.background, (0, 0))
        pygame.display.flip()
