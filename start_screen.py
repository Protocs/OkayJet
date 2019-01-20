import pygame
import sys

class Start:
    def __init__(self, fps, surface):
        self.start = True
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.surface = surface

    def run(self):
        while self.start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            ...
            pygame.display.flip()
            self.clock.tick(self.fps)