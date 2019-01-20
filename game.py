import pygame
import util
from okayjet.objects.player import Player
from settings import players


class Game:
    def __init__(self, fps, surface):
        self.game = True
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.surface = surface

        self.background = util.load_image("background.jpg")
        self.player = Player(players, 30, 355)

    def run(self):
        while self.game:
            self.events()
            self.update()
            self.clock.tick(self.fps)

    def events(self):
        self.keypress_handler()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                util.terminate()

    def update(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.background, (0, 0))
        players.update()
        players.draw(self.surface)
        pygame.display.flip()

    def keypress_handler(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.player.move(0, -3)
