import pygame
import sys
import util

class Start:
    def __init__(self, fps, surface):
        self.start = True
        self.clock = pygame.time.Clock()
        self.background = util.load_image("start_background.png")
        self.fps = fps
        self.surface = surface

    def run(self):
        while self.start:
            self.surface.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.surface.blit(self.background, (0, 0))
            pygame.display.flip()
            self.clock.tick(self.fps)