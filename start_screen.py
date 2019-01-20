import pygame
import sys
import util
from settings import buttons
from okayjet.objects.button import Button


class Start:
    def __init__(self, fps, surface):
        self.start = True
        self.clock = pygame.time.Clock()
        self.background = util.load_image("start_background.png")
        self.fps = fps
        self.surface = surface
        self.start_button = Button(buttons, 150, 400, util.load_image("press_somewhere_image.png"))

    def run(self):
        while self.start:
            self.surface.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.surface.blit(self.background, (0, 0))
            buttons.update()
            buttons.draw(self.surface)
            pygame.display.flip()
            self.clock.tick(self.fps)
