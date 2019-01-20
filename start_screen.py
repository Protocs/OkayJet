import pygame
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
        self.surface.blit(self.background, (0, 0))
        buttons.update()
        buttons.draw(self.surface)
        pygame.display.flip()