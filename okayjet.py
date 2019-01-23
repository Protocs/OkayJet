import pygame

from okayjet.game import Game
from okayjet.start_screen import Start
from okayjet.settings import GAME_NAME, SCREEN_SIZE, FPS

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(GAME_NAME)

start = Start(screen)
start.run()
game = Game(screen)
game.run()
