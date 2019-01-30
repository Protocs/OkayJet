import pygame
from okayjet import util
from okayjet.objects.player import Player
from okayjet.settings import players, coins, SCREEN_WIDTH
from okayjet.objects.coin import Coin
import time

class Game:
    def __init__(self, fps, surface):
        self.game = True
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.surface = surface

        self.background = util.load_image("background.jpg")
        self.background_width = self.background.get_rect().width
        self.background_x = 0
        self.player = Player(players, 30, 355)
        self.coin = Coin(coins, 600, 100)
        self.start_time = time.time()

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
        x = self.background_x % self.background_width
        self.surface.blit(self.background, (x - self.background_width, 0))
        if x < SCREEN_WIDTH:
            self.surface.blit(self.background, (x, 0))
        if self.player.rect.x > SCREEN_WIDTH // 4:
            self.background_x -= 3 + ((time.time() - self.start_time) * 0.05)
        if self.player.rect.x > SCREEN_WIDTH // 4:
            coins.update()
        coins.draw(self.surface)
        players.update()
        players.draw(self.surface)
        pygame.display.flip()

    def keypress_handler(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.player.move(0, -4.5)
