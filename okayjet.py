import pygame

from okayjet.game import Game
from okayjet.start_screen import Start
from okayjet.settings import GAME_NAME, SCREEN_SIZE

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(GAME_NAME)
pygame.display.set_icon(pygame.image.load("icon.png"))

while True:
    start = Start(screen)
    start.run()
    game = Game(screen, start.music_button.state)
    game.run()
